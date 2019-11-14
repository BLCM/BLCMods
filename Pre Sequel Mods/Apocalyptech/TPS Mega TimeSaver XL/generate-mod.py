#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2019, CJ Kucera
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

try:
    from modprocessor import ModProcessor
    mp = ModProcessor()
except ModuleNotFoundError:
    print('')
    print('********************************************************************')
    print('To run this script, you will need to copy or symlink modprocessor.py')
    print('from the parent directory, so it exists here as well.  Sorry for')
    print('the bother!')
    print('********************************************************************')
    print('')
    sys.exit(1)

try:
    from ftexplorer.data import Data
except ModuleNotFoundError:
    print('')
    print('****************************************************************')
    print('To run this script, you will need to copy or symlink the')
    print('"ftexplorer" and "resources" dirs from my ft-explorer project so')
    print('they exist here as well.  Sorry for the bother!')
    print('****************************************************************')
    print('')
    sys.exit(1)

# Control Vars
mod_name = 'TPS Mega TimeSaver XL'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)
speed_scale = 5
vehicle_anim_speed_scale = 2
slots_scale = 5
grinder_scale = 5

data = Data('TPS')

class Changes(object):
    """
    Changes that we'll be keeping track of
    """

    def __init__(self, interps=[], interpdata=[], others=[], raw=[], bpds=[]):
        """
        Three different types of data that we work with.

        `interps`: Is ordinarily just a string which is an object name, and
        we'll set the `PlayRate` attribute on that object.  Can be a tuple
        instead, consisting of an object name and a scaling factor for
        the `PlayRate` -- a scale <1 means to slow things down a bit,
        >1 means to speed them up more.

        `interpdata`: Is ordinarily just a string which is an `InterpData`
        object, and the timestamps found in the structure will be scaled
        appropriately.  Can be a tuple instead, consisting of the object
        name and a scaling factors -- a scale <1 means to speed things up,
        >1 means to slow them down (this is the *opposite* of `interps`,
        since `interps` sets a rate, whereas these specify timestamps,
        basically.

        `others`: Used for more freeform setting of data.  This must be
        a tuple, consisting of an object name, attribute, and "vanilla"
        value, which will be scaled appropriately.

        `raw`: Set statements (minus the original `set`) which will just
        be passed through untouched (apart from being hotfixed to the
        specified level)

        `bpds`: BPDs to scale

        Start any "object name" with a hash sign (`#`) to put in a comment
        rather than a `set` statement.
        """
        self.interps = interps
        self.interpdata = interpdata
        self.others = others
        self.raw = raw
        self.bpds = bpds

    def get_division_tuples(self):
        level_divides = []
        for data in self.interpdata:
            if isinstance(data, tuple):
                interpdata_name = data[0]
                scale = data[1]
            else:
                interpdata_name = data
                scale = 1
            if interpdata_name[0] == '#':
                level_divides.append((interpdata_name, None, None))
            else:
                level_divides.extend(Changes.get_interpdata_tuples(interpdata_name, scale))
        level_divides.extend(self.others)
        return level_divides

    def has_data(self):
        return len(self.interps) > 0 or len(self.interpdata) > 0 or len(self.others) > 0 or len(self.raw) > 0 or len(self.bpds) > 0

    def process(self, level_package, scale, lines):
        """
        Adds our information to the given lines array
        """

        for interp in self.interps:
            if interp[0] == '#':
                lines.append(interp)
            else:
                if isinstance(interp, tuple):
                    interp_name = interp[0]
                    interp_scale = round(scale * interp[1], 1)
                else:
                    interp_name = interp
                    interp_scale = scale
                lines.append('level {} set {} PlayRate {}'.format(
                    level_package, interp_name, interp_scale,
                    ))
            lines.append('')

        for div_tuple in self.get_division_tuples():
            if len(div_tuple) == 3:
                (obj_name, attr_name, stock_val) = div_tuple
                do_multiply = False
            else:
                (obj_name, attr_name, stock_val, do_multiply) = div_tuple
            if obj_name[0] == '#':
                lines.append(obj_name)
            else:
                if do_multiply:
                    new_val = stock_val*scale
                else:
                    new_val = stock_val/scale
                lines.append('level {} set {} {} {:0.6f}'.format(
                    level_package,
                    obj_name,
                    attr_name,
                    new_val,
                    ))
            lines.append('')

        for statement in self.raw:
            if statement[0] == '#':
                lines.append(statement)
            else:
                lines.append('level {} set {}'.format(level_package, statement))
            lines.append('')

        for bpd_name in self.bpds:
            if bpd_name[0] == '#':
                lines.append(bpd_name)
                lines.append('')
            else:
                for cmd in delay_bpd(bpd_name, scale):
                    lines.append('level {} {}'.format(level_package, cmd))
                    lines.append('')

    @staticmethod
    def get_interpdata_tuples(interpdata_name, scale=1):
        """
        Function to generate a list of tuples describing the vanilla state, timingwise,
        of an `InterpData` structure, which is used for a lot of gate-like animations
        in the game.  Optionally scale the value by `scale`
        """

        global data

        to_report = []
        interpdata = data.get_struct_by_full_object(interpdata_name)
        for varname in ['InterpLength', 'EdSectionStart', 'EdSectionEnd']:
            if float(interpdata[varname]) > 0:
                to_report.append((interpdata_name, varname, float(interpdata[varname])*scale))
            
        for group_name in [Data.get_attr_obj(n) for n in sorted(interpdata['InterpGroups'])]:
            group = data.get_struct_by_full_object(group_name)
            if 'InterpTracks' in group and group['InterpTracks'] != '' and group['InterpTracks'] != 'None':
                for track_name in [Data.get_attr_obj(n) for n in group['InterpTracks']]:
                    track = data.get_struct_by_full_object(track_name)
                    if 'InterpTrackToggle_' in track_name:
                        if 'ToggleTrack' in track:
                            for idx, toggle in enumerate(track['ToggleTrack']):
                                if float(toggle['Time']) > 0:
                                    to_report.append((track_name, 'ToggleTrack[{}].Time'.format(idx), float(toggle['Time'])*scale))
                    elif 'InterpTrackMove_' in track_name:
                        for (varname, timename) in [
                                ('PosTrack', 'InVal'),
                                ('EulerTrack', 'InVal'),
                                ('LookupTrack', 'Time'),
                                ]:
                            if varname in track:
                                for idx, move in enumerate(track[varname]['Points']):
                                    if float(move[timename]) > 0:
                                        to_report.append((track_name, '{}.Points[{}].{}'.format(varname, idx, timename), float(move[timename])*scale))
                    elif 'InterpTrackVectorProp_' in track_name or 'InterpTrackVectorMaterialParam_' in track_name:
                        if 'VectorTrack' in track:
                            for idx, point in enumerate(track['VectorTrack']['Points']):
                                if float(point['InVal']) > 0:
                                    to_report.append((track_name, 'VectorTrack.Points[{}].InVal'.format(idx), float(point['InVal'])*scale))
                    elif 'InterpTrackFloatProp_' in track_name or 'InterpTrackFloatMaterialParam_' in track_name:
                        if 'FloatTrack' in track:
                            for idx, prop in enumerate(track['FloatTrack']['Points']):
                                if float(prop['InVal']) > 0:
                                    to_report.append((track_name, 'VectorTrack.Points[{}].InVal'.format(idx), float(prop['InVal'])*scale))
                    elif 'InterpTrackVisibility_' in track_name:
                        if 'VisibilityTrack' in track:
                            for idx, visibility in enumerate(track['VisibilityTrack']):
                                if float(visibility['Time']) > 0:
                                    to_report.append((track_name, 'VisibilityTrack[{}].Time'.format(idx), float(visibility['Time'])*scale))
                    elif 'InterpTrackAkEvent_' in track_name: 
                        if 'AkEvents' in track:
                            for idx, akevent in enumerate(track['AkEvents']):
                                if float(akevent['Time']) > 0:
                                    to_report.append((track_name, 'AkEvents[{}].Time'.format(idx), float(akevent['Time'])*scale))
                    elif 'InterpTrackEvent_' in track_name:
                        if 'EventTrack' in track:
                            for idx, event in enumerate(track['EventTrack']):
                                if float(event['Time']) > 0:
                                    to_report.append((track_name, 'EventTrack[{}].Time'.format(idx), float(event['Time'])*scale))
                    elif 'InterpTrackAnimControl_' in track_name:
                        if 'FloatTrack' in track:
                            for idx, prop in enumerate(track['FloatTrack']['Points']):
                                if float(prop['InVal']) > 0:
                                    to_report.append((track_name, 'VectorTrack.Points[{}].InVal'.format(idx), float(prop['InVal'])*scale))
                        if 'AnimSeqs' in track:
                            for idx, prop in enumerate(track['AnimSeqs']):
                                for prop_name in ['StartTime', 'AnimStartOffset', 'AnimEndOffset']:
                                    if float(prop[prop_name]) > 0:
                                        to_report.append((track_name, 'AnimSeqs[{}].{}'.format(idx, prop_name), float(prop[prop_name])*scale))
                    else:
                        raise Exception('Unsupported type for: {}'.format(track_name))

        return to_report

class Level(object):
    """
    Simple little class to hold info about what we're changing in a level
    """

    def __init__(self, level_name, level_package, doors=None, lifts=None, drawbridges=None, others=None):
        self.level_name = level_name
        self.level_package = level_package
        self.doors = doors
        self.lifts = lifts
        self.drawbridges = drawbridges
        self.others = others

    def process_changes(self, change, scale, lines):
        """
        Adds change information to the given lines
        """
        if change and change.has_data():
            lines.append('#<{}>'.format(self.level_name))
            lines.append('')
            change.process(self.level_package, scale, lines)
            lines.append('#</{}>'.format(self.level_name))
            lines.append('')

    def has_doors_data(self):
        return self.doors and self.doors.has_data()

    def has_lifts_data(self):
        return self.lifts and self.lifts.has_data()

    def has_drawbridges_data(self):
        return self.drawbridges and self.drawbridges.has_data()

    def has_others_data(self):
        return self.others and self.others.has_data()

    def process_doors(self, scale, lines):
        """
        Adds door information to the given lines
        """
        self.process_changes(self.doors, scale, lines)

    def process_lifts(self, scale, lines):
        """
        Adds lift information to the given lines
        """
        self.process_changes(self.lifts, scale, lines)

    def process_drawbridges(self, scale, lines):
        """
        Adds drawbridges information to the given lines
        """
        self.process_changes(self.drawbridges, scale, lines)

    def process_others(self, scale, lines):
        """
        Adds other information to the given lines
        """
        self.process_changes(self.others, scale, lines)

    def __lt__(self, other):
        return self.level_name.lower() < other.level_name.lower()

def delay_bpd(bpd_name, scale, delay_overrides={}, metronome_overrides={}, skip_cold=set()):

    global data

    bpd_struct = data.get_struct_by_full_object(bpd_name)
    for seq_idx, sequence in enumerate(bpd_struct['BehaviorSequences']):
        for ev_idx, event in enumerate(sequence['EventData2']):
            if float(event['UserData']['ReTriggerDelay']) > 0:
                yield 'set {} BehaviorSequences[{}].EventData2[{}].UserData.ReTriggerDelay {}'.format(
                        bpd_name,
                        seq_idx,
                        ev_idx,
                        round(float(event['UserData']['ReTriggerDelay'])/scale, 6),
                        )
        for cold_idx, cold in enumerate(sequence['ConsolidatedOutputLinkData']):
            if (seq_idx, cold_idx) not in skip_cold:
                if float(cold['ActivateDelay']) > 0:
                    yield 'set {} BehaviorSequences[{}].ConsolidatedOutputLinkData[{}].ActivateDelay {}'.format(
                            bpd_name,
                            seq_idx,
                            cold_idx,
                            round(float(cold['ActivateDelay'])/scale, 6),
                            )
        for data_idx, bdata in enumerate(sequence['BehaviorData2']):
            if bdata['Behavior'].startswith("Behavior_Delay'"):
                if int(bdata['LinkedVariables']['ArrayIndexAndLength']) != 0:
                    yield 'set {} BehaviorSequences[{}].BehaviorData2[{}].LinkedVariables.ArrayIndexAndLength 0'.format(
                            bpd_name,
                            seq_idx,
                            data_idx,
                            )
                delay_name = Data.get_attr_obj(bdata['Behavior'])
                delay = data.get_struct_by_full_object(delay_name)
                if float(delay['Delay']) > 0:
                    if delay_name in delay_overrides:
                        new_value = delay_overrides[delay_name]
                    else:
                        new_value = float(delay['Delay'])/scale
                    yield 'set {} Delay {}'.format(
                            delay_name,
                            round(new_value, 6),
                            )

            elif bdata['Behavior'].startswith("Behavior_Metronome'"):
                if int(bdata['LinkedVariables']['ArrayIndexAndLength']) != 0:
                    yield 'set {} BehaviorSequences[{}].BehaviorData2[{}].LinkedVariables.ArrayIndexAndLength 0'.format(
                            bpd_name,
                            seq_idx,
                            data_idx,
                            )
                metronome_name = Data.get_attr_obj(bdata['Behavior'])
                metronome = data.get_struct_by_full_object(metronome_name)
                if float(metronome['Duration']) > 0:
                    if metronome_name in metronome_overrides:
                        new_value = metronome_overrides[metronome_name]
                    else:
                        new_value = float(metronome['Duration'])/scale
                    yield 'set {} Duration {}'.format(
                            metronome_name,
                            round(new_value, 6),
                            )


# Data!  Interps were largely found via my ft-explorer 'level_interps.py' sandbox script
dlcs = [
    ('Base Game', [
        Level('Concordia', 'Spaceport_P',
            doors=Changes(
                interps=[
                    'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_13',
                    'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_14',
                    'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SlidingDoorWithSound.SeqAct_Interp_1',
                    'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SlidingDoorWithSound_0.SeqAct_Interp_1',
                    'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SlidingDoorWithSound_1.SeqAct_Interp_1',
                    'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SlidingDoorWithSound_2.SeqAct_Interp_1',
                    'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SlidingDoorWithSound_3.SeqAct_Interp_1',
                    'Spaceport_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_10',
                    'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    ],
                ),
            ),
        Level('Crisis Scar', 'ComFacility_P',
            doors=Changes(
                interps=[
                    'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqAct_Interp_0',
                    'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqAct_Interp_6',
                    'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqAct_Interp_2',
                    'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_UpperFloorGply.SeqAct_Interp_7',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ActivateRelay.SeqAct_Interp_17',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ActivateRelay_0.SeqAct_Interp_17',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ActivateRelay_1.SeqAct_Interp_17',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Dynamic.SeqAct_Interp_4',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Dynamic.SeqAct_Interp_7',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_13',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_17',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Turret covers',
                    'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Eleseer', 'InnerCore_P'), # Nothing, perhaps?
        Level('Eye of Helios', 'LaserBoss_P',
            doors=Changes(
                interps=[
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqAct_Interp_10',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqAct_Interp_11',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqAct_Interp_3',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqAct_Interp_5',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqAct_Interp_6',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqAct_Interp_9',
                    # Not sure about this one, has some lighting vars attached too...
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.CoreIntro.SeqAct_Interp_0',
                    ],
                others=[
                    ('LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqVar_Float_0', 'FloatValue', 0.4, True),
                    ('LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqVar_Float_2', 'FloatValue', 1, True),
                    ],
                ),
            lifts=Changes(
                interps=[
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Elevator_Breadcrumbing.SeqAct_Interp_2',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Elevator_Breadcrumbing.SeqAct_Interp_21',

                    # Testing these:
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Elevator_Breadcrumbing.SeqAct_Interp_1',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Elevator_Breadcrumbing.SeqAct_Interp_7',
                    ],
                others=[
                    ('LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Elevator_Breadcrumbing.SeqVar_Float_1', 'FloatValue', 1.5, True),
                    ],
                ),
            others=Changes(
                interps=[
                    '# Digistruct chests after Zarpedon fight',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_12',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_13',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_14',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_15',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_16',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_17',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_18',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_19',
                    'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.LootChest_Room.SeqAct_Interp_20',
                    ],
                others=[
                    ('# Injection cores', None, None),
                    ('GD_Co_LaserRebootMissionData.IO_HyperionInjectionNode', 'BodyComposition.Attachments[5].Data.Float', 1),
                    ('GD_Co_LaserRebootMissionData.IO_HyperionInjectionNode', 'BodyComposition.Attachments[11].Data.Float', 1),
                    ],
                ),
            ),
        Level('Helios Station', 'MoonShotIntro_P',
            lifts=Changes(
                interps=[
                    'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Moonshot Bullet',
                    'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_19',
                    'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    '# Moonshot Container',
                    'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    ],
                ),
            ),
        Level('Hyperion Hub of Heroism', 'CentralTerminal_P',
            doors=Changes(
                interps=[
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqAct_Interp_8',
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqAct_Interp_9',
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RandDAccess.SeqAct_Interp_0',
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RandD_Door_Sequence.SeqAct_Interp_0',
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqAct_Interp_1',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqAct_Interp_3',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqAct_Interp_0',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqAct_Interp_2',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqAct_Interp_3',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqAct_Interp_0',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Inner_Hull.SeqAct_Interp_0',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqAct_Interp_2',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqAct_Interp_6',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqAct_Interp_2',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RandD_Door_Sequence.SeqAct_Interp_1',
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RandD_Door_Sequence.SeqAct_Interp_2',
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqAct_Interp_8',
                    ],
                ),
            ),
        Level('Jack\'s Office', 'JacksOffice_P',
            doors=Changes(
                interps=[
                    'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jack_Door.SeqAct_Interp_1',
                    'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Initial library transformation (triggered by Jack)',
                    ('JacksOffice_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9', 0.7),
                    '# Library Transformation',
                    ('JacksOffice_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_10', 0.7),
                    ],
                ),
            ),
        Level('Lunar Launching Station', 'Laser_P',
            doors=Changes(
                interps=[
                    # I strongly suspect that nearly all of these are enemy-use doors, and probably
                    # shouldn't really be buffed
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_0',
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_1',
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_10',
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_2',
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_3',
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_4',
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_5',
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_8',
                    # These are maybe a bit more likely to be "real"
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LoadingStationCombat.SeqAct_Interp_1',
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LoadingStationCombat.SeqAct_Interp_3',
                    ],
                ),
            lifts=Changes(
                interps=[
                    # I think the lifts in here are probably already plenty fast enough, will have
                    # to check on that.
                    'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_7',
                    ],
                ),
            others=Changes(
                interps=[
                    '# To The Moon cargo container',
                    'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqAct_Interp_0',
                    'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqAct_Interp_2',
                    '# Lock and Load Loader rack',
                    'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.LoaderRackMatinees.SeqAct_Interp_4',
                    'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.LoaderRackMatinees.SeqAct_Interp_5',
                    'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.LoaderRackMatinees.SeqAct_Interp_6',
                    ],
                others=[
                    # If these go *too* fast it breaks the mission flow
                    ('# To The Moon / Lock and Load conveyor', None, None),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqVar_Float_0', 'FloatValue', 0.1/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqVar_Float_1', 'FloatValue', 0.35/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqVar_Float_2', 'FloatValue', 1.5/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqVar_Float_5', 'FloatValue', 0.8/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqVar_Float_6', 'FloatValue', 0.35/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqVar_Float_8', 'FloatValue', 0.6/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqVar_Float_9', 'FloatValue', 0.45/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_2', 'FloatValue', 0.8/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_11', 'FloatValue', 0.8/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqVar_Float_1', 'FloatValue', 1/2, True),
                    ('Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqVar_Float_9', 'FloatValue', 3/2, True),
                    ('# Things That Go Boom AI Download speed', None, None),
                    ('GD_Co_Side_ExplodersData.Population.IO_AIUploadBar:BehaviorProviderDefinition_0.Behavior_Metronome_215', 'TickInterval', 0.25),
                    ('GD_Co_Side_ExplodersData.Population.IO_AIUploadBar:BehaviorProviderDefinition_0.Behavior_SimpleMath_856', 'A', 1.5),
                    ('GD_Co_Side_ExplodersData.Population.IO_AIUploadBar:BehaviorProviderDefinition_0.Behavior_SimpleMath_855', 'A', 0.25),
                    ('GD_Co_Side_ExplodersData.Population.IO_AIUploadBar:BehaviorProviderDefinition_0.Behavior_SimpleMath_858', 'A', 0.1),
                    ],
                raw=[
                    '# Speed up Things That Go Boom AI Download speed (continued)',
                    'GD_Co_Side_ExplodersData.Population.IO_AIUploadBar:BehaviorProviderDefinition_0 BehaviorSequences[0].BehaviorData2[1].LinkedVariables.ArrayIndexAndLength 0',
                    'GD_Co_Side_ExplodersData.Population.IO_AIUploadBar:BehaviorProviderDefinition_0 BehaviorSequences[0].BehaviorData2[18].LinkedVariables.ArrayIndexAndLength 786433',
                    'GD_Co_Side_ExplodersData.Population.IO_AIUploadBar:BehaviorProviderDefinition_0 BehaviorSequences[0].BehaviorData2[0].LinkedVariables.ArrayIndexAndLength 65537',
                    'GD_Co_Side_ExplodersData.Population.IO_AIUploadBar:BehaviorProviderDefinition_0 BehaviorSequences[0].BehaviorData2[41].LinkedVariables.ArrayIndexAndLength 3538945',
                    ],
                ),
            ),
        Level('Meriff\'s Office', 'Meriff_P',
            doors=Changes(
                interps=[
                    'Meriff_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Hidden ECHO number one',
                    'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    '# Hidden ECHO number two',
                    'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    '# Hidden ECHO number three',
                    'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    ],
                bpds=[
                    'GD_Co_WipingSlateData.IO_WipingSlate_SlotMachine:BehaviorProviderDefinition_0',
                    ],
                ),
            ),
        Level('Outfall Pumping Station', 'Digsite_Rk5arena_P',
            # Not really sure about any of this, we'll see how it goes
            doors=Changes(
                interps=[
                    'Digsite_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Digsite_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Digsite_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Outlands Canyon', 'Outlands_P2',
            doors=Changes(
                interps=[
                    'Outlands_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Outlands_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'Outlands_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.TreasuresOfECHOMadre.SeqAct_Interp_4',
                    # Labelled as 'SpawnDoor', leaving it alone for now...
                    #'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.Boomshakalaka.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Outlands Spur', 'Outlands_P',
            doors=Changes(
                interps=[
                    # These are labelled "SpawnGate", leaving for now...
                    #'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    #'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    #'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_14',
                    'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_16',
                    'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_18',
                    'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_23',
                    'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_24',
                    'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_25',
                    'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            others=Changes(
                interps=[
                    # Gonna give this a bit less of a boost than everything else, looks a bit
                    # too silly otherwise
                    '# Rotating the methane pipes during storyline mission',
                    ('Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4', .5),
                    ],
                ),
            ),
        Level('Pity\'s Fall', 'Wreck_P',
            doors=Changes(
                interps=[
                    # I wouldn't be suprised if all the "Combat" ones here are enemy-use
                    'Wreck_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Wreck_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Wreck_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Wreck_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_17',
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_19',
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    # These, I believe, are the doors that Felicity opens for you
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_15',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    # This one's actually an "ElevatorDoor," I figure it makes more sense here though
                    'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    # This one is the elevator which drops on you while collecting Zarpedon ECHOs.
                    # Already plenty fast, and looks weird if sped up even more.
                    #'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Exposing the power core (have to wait for dialogue to be able to shoot it anyway)',
                    ('Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2', 0.3),
                    ('Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_21', 0.3),
                    '# Jettisoned engine',
                    ('Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6', 0.5),
                    ],
                ),
            ),
        Level('Regolith Range', 'Deadsurface_P',
            doors=Changes(
                interps=[
                    'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqAct_Interp_1',
                    'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqAct_Interp_3',
                    'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqAct_Interp_1',
                    'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqAct_Interp_2',
                    'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqAct_Interp_3',
                    'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqAct_Interp_1',
                    'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TalesfromElips.SeqAct_Interp_1',
                    'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Last_Requests.SeqAct_Interp_0',
                    ],
                ),
            others=Changes(
                others=[
                    ('# ECHO Terminal in "Last Requests"', None, None),
                    ('gd_co_lastrequestsdata.IO_EchoTransmitter', 'BodyComposition.Attachments[4].Data.Float', 3),
                    ],
                bpds=[
                    'gd_co_lastrequestsdata.IO_EchoTransmitter:BehaviorProviderDefinition_1',
                    ],
                ),
            ),
        Level('Research and Development', 'RandDFacility_P',
            doors=Changes(
                interps=[
                    # This one is "Bars", presumably Stalker bars
                    'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqAct_Interp_0',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqAct_Interp_2',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqAct_Interp_14',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_10',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_13',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_14',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_15',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_16',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_17',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_18',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_19',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_20',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    '# Door to aquarium area (I think this might not work, but eh)',
                    ('RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7', 0.5),
                    ],
                others=[
                    # Actual vanilla value is 0.5, but that's too slow for me even after scaling
                    ('# The door Dr. Langois opens to the next section', None, None),
                    ('RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_10', 'FloatValue', 1, True),
                    ],
                ),
            lifts=Changes(
                interps=[
                    'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    # This one's labelled "Plate" - could be a moving platform or something?  Haven't been
                    # in here in too long, check later.
                    #'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqAct_Interp_1',
                    ],
                others=[
                    ('# Hidden challenge elevator', None, None),
                    ('RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_0', 'FloatValue', 0.5, True),
                    ],
                ),
            others=Changes(
                interps=[
                    '# Scanner to get into hidden observation lab',
                    'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    '# Water draining to get Dr. Torres\' teddy bear',
                    ('RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11', 0.1),
                    #'# Lab 19 Activation Console',
                    #'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqAct_Interp_1',
                    ],
                others=[
                    ("# It Ain't Rocket Surgery blood tanks", None, None),
                    ('GD_Co_Side_RocketSurgeryData.InteractiveObjects.WheelBarrel', 'BodyComposition.Attachments[2].Data.Float', 0.3),
                    ('GD_Co_Side_RocketSurgeryData.InteractiveObjects.WheelBarrel', 'BodyComposition.Attachments[7].Data.Float', 0.1),
                    ('GD_Co_Side_RocketSurgeryData.InteractiveObjects.WheelBarrel', 'BodyComposition.Attachments[11].Data.Float', 0.3),
                    ('GD_Co_Side_RocketSurgeryData.InteractiveObjects.WheelBarrel', 'BodyComposition.Attachments[16].Data.Float', 0.1),
                    ('# Lab 19 Activation Console', None, None),
                    ('GD_Co_Side_Lab19Data.IOs.IO_Puzzle', 'BodyComposition.Attachments[2].Data.Float', 2),
                    ],
                bpds=[
                    "# It Ain't Rocket Surgery blood tanks (continued)",
                    'GD_Co_Side_RocketSurgeryData.InteractiveObjects.WheelBarrel:BehaviorProviderDefinition_0',
                    '# Lab 19 Activation Console (continued)',
                    'GD_Co_Side_Lab19Data.IOs.IO_Puzzle:BehaviorProviderDefinition_0',
                    ],
                raw=[
                    '# Dr. Langois walking speed',
                    'GD_Co_DrLangoisNPC.Character.Pawn_DrLangoisNPC GroundSpeed 700',
                    ],
                ),
            ),
        Level('Serenity\'s Waste', 'Moonsurface_P',
            doors=Changes(
                interps=[
                    'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqAct_Interp_2',
                    'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqAct_Interp_3',
                    'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqAct_Interp_0',
                    'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqAct_Interp_1',
                    'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TalesfromElips.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Stanton\'s Liver', 'StantonsLiver_P',
            doors=Changes(
                interps=[
                    'StantonsLiver_SideMissions.TheWorld:PersistentLevel.Main_Sequence.Grinders.SeqAct_Interp_26',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'StantonsLiver_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            others=Changes(
                others=[
                    ('# All The Little Creatures control wheels', None, None),
                    ('GD_Cork_AllthelittleData.InteractiveObjects.IO_AllTheLittle_Wheel01', 'BodyComposition.Attachments[1].Data.Float', 1),
                    ('GD_Cork_AllthelittleData.InteractiveObjects.IO_AllTheLittle_Wheel02', 'BodyComposition.Attachments[1].Data.Float', 1),
                    ('GD_Cork_AllthelittleData.InteractiveObjects.IO_AllTheLittle_Wheel03', 'BodyComposition.Attachments[1].Data.Float', 1),
                    ('GD_Cork_AllthelittleData.InteractiveObjects.IO_AllTheLittle_Wheel04', 'BodyComposition.Attachments[1].Data.Float', 1),
                    ('GD_Cork_AllthelittleData.InteractiveObjects.IO_AllTheLittle_Wheel05', 'BodyComposition.Attachments[1].Data.Float', 1),
                    ],
                ),
            ),
        Level('Sub-Level 13', 'Sublevel13_P',
            doors=Changes(
                interps=[
                    'Sublevel13_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Sublevel13_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ],
                ),
            ),
        Level('Titan Industrial Facility', 'DahlFactory_P',
            doors=Changes(
                interps=[
                    # This one has a "Suit" attached, wonder if this is when Felicity Power Suit comes out
                    # (Oh wait, though, that comes out in Robot Production Plant, yeah?  Hrm.)
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqAct_Interp_0',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqAct_Interp_12',
                    # "Trash" door on this one
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeStingRay.SeqAct_Interp_0',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeStingRay.SeqAct_Interp_1',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeStingRay.SeqAct_Interp_10',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_Atrium.SeqAct_Interp_3',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqAct_Interp_0',
                    # This one also has a "Sign" attached...
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqAct_Interp_1',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqAct_Interp_8',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Stingray_Factory.SeqAct_Interp_3',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Train_Station.SeqAct_Interp_0',
                    # Various Tork objects in here too, might affect some of those animations
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Train_Station.SeqAct_Interp_10',
                    'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Train_Station.SeqAct_Interp_5',
                    ],
                ),
            ),
        Level('Titan Robot Production Plant', 'DahlFactory_Boss',
            # Lots of suit-related stuff in here, obvs.  Will have to see how that is when I test.
            doors=Changes(
                interps=[
                    'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.FinalRoomCombat.SeqAct_Interp_12',
                    'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqAct_Interp_1',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqAct_Interp_5',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqAct_Interp_1',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqAct_Interp_10',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqAct_Interp_5',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqAct_Interp_0',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqAct_Interp_2',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqAct_Interp_4',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqAct_Interp_5',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqAct_Interp_6',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqAct_Interp_1',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqAct_Interp_17',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqAct_Interp_4',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_FinalArea.SeqAct_Interp_1',
                    # "Suit Door"...
                    #'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SpawnMats.SeqAct_Interp_5',
                    # Another "Suit Door"
                    #'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SpawnMats.SeqAct_Interp_8',
                    ],
                ),
            lifts=Changes(
                interps=[
                    # Labelled with "Plate", definitely check this one out.
                    #'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SpawnMats.SeqAct_Interp_4',
                    '# Lift which brings eye bots up',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqAct_Interp_1',
                    '# Lift which brings torso up',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqAct_Interp_3',
                    '# Lift which brings the mech suit (legs) down',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqAct_Interp_1',
                    # I'm pretty sure one of these contains the elevator which brings Felicity down to ground level, but I can't
                    # seem to actually change the speed.  And regardless, it's only that initial lowering which would really
                    # make sense to change anyway; the rest of it is pretty locked into dialogue+cutscene.
                    #'# Elevator which lowers Felicity into position',
                    #'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqAct_Interp_0',
                    #'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqAct_Interp_1',
                    #'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqAct_Interp_7',
                    ],
                ),
            others=Changes(
                interps=[
                    # Timings on these often have to be a little bit slower than our global scaling
                    '# Eye creation sequence',
                    ('DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Eye_Creation_Area.SeqAct_Interp_5', 0.5),
                    '# Picking up the torso',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Prototype_Moving.SeqAct_Interp_0',
                    '# Welding turrets to the torso',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqAct_Interp_11',
                    # Turns out we can hardly buff these two at all without losing dialogue
                    '# Welding torso to the legs',
                    ('DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqAct_Interp_8', 0.35),
                    '# Moving completed Constructor to final area',
                    ('DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Prototype_Moving.SeqAct_Interp_1', 0.3),
                    '# Rotating rails',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_FinalArea.SeqAct_Interp_0',
                    '# Continuing moving after rail rotation',
                    'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Prototype_Moving.SeqAct_Interp_13',
                    # Speeding this up cuts of dialogue.
                    #'# Felicity installation terminal',
                    #('DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqAct_Interp_0', 0.5),
                    ],
                ),
            ),
        Level('Triton Flats', 'Moon_P',
            doors=Changes(
                interps=[
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqAct_Interp_1',
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqAct_Interp_17',
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqAct_Interp_4',
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_5_AI_Core.SeqAct_Interp_1',
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_5_AI_Core.SeqAct_Interp_6',
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.NoSuchTHingAsAFreeLaunch.SeqAct_Interp_17',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqAct_Interp_0',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqAct_Interp_1',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqAct_Interp_21',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.RecruitmentDrive.SeqAct_Interp_1',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqAct_Interp_0',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqAct_Interp_1',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WhereforeArtThou?.SeqAct_Interp_1',
                    ],
                ),
            lifts=Changes(
                interps=[
                    # Panels?
                    #'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            others=Changes(
                interps=[
                    '# No Such Thing as a Free Launch gyroscope',
                    'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.NoSuchTHingAsAFreeLaunch.SeqAct_Interp_3',
                    ],
                others=[
                    # Just speed this up by maybe 2x, so we do some finagling with the scale here.
                    ('# Bunch of Ice Holes mission timing (just a 2x speedup)', None, None),
                    ('Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqAct_Delay_0', 'Duration', 20*speed_scale/2),
                    ('Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqAct_Delay_1', 'Duration', 15*speed_scale/2),
                    ('Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqAct_Delay_2', 'Duration', 15*speed_scale/2),
                    ('Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqAct_Delay_3', 'Duration', 20*speed_scale/2),
                    ('Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqAct_Delay_4', 'Duration', 45*speed_scale/2),
                    ('Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqAct_Delay_5', 'Duration', 45*speed_scale/2),
                    ('Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqAct_Delay_6', 'Duration', 20*speed_scale/2),
                    ('Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqAct_Delay_7', 'Duration', 10*speed_scale/2),
                    ],
                ),
            ),
        Level('Tycho\'s Ribs', 'Access_P',
            # Nothing super obvious, will need to give it an eyeball to see if the big ol'
            # elevators could use speeding-up
            ),
        Level('Veins of Helios', 'InnerHull_P',
            doors=Changes(
                interps=[
                    # As usual, I suspect none of these 'Combat' ones are player-related
                    'InnerHull_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'InnerHull_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'InnerHull_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_39',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    # This one's a bit slow even with a 5x speedup
                    ('InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_40', 1.5),
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_65',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_67',
                    'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqAct_Interp_4',
                    'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqAct_Interp_25',
                    'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqAct_Interp_26',
                    'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.TroubleWithSpaceHurps.SeqAct_Interp_8',
                    # Huh, lots more objects than usual; "Blast Shields" but door props
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    '# Airlocks',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_15',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_16',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_19',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_20',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_21',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_22',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_24',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_37',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    '# Airlock Meters',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_41',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_45',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_46',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_47',
                    '# Airlock 1 bioscan',
                    'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_63',
                    ],
                others=[
                    ('# Other Airlock Timing', None, None),
                    ('InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Delay_2', 'Delay', 0),
                    ('InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Delay_4', 'Delay', 0),
                    ('InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Delay_5', 'Delay', 0),
                    ('InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Delay_25', 'Delay', 0),
                    ],
                ),
            lifts=Changes(
                interps=[
                    # I wonder if any of these are moving platforms actually...  I bet they
                    # almost certainly are, 'cause I don't remember any outright elevators
                    # in there.
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_30',
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_31',
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_32',
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_34',
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_35',
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_38',
                    # Floating Platforms -- I suspect these should, in general, NOT be sped up.
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_14',
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_64',
                    ],
                ),
            others=Changes(
                interps=[
                    # This *does* speed up the animation of the drone and the garbage pile, but
                    # there's some kind of hardcoded 13.8-second delay somewhere which I can *not*
                    # figure out.  It's definitely not tied to the animation itself though.
                    # Annoying!
                    #'# Trash-cleaning robot during Quarantine: Infestation',
                    #'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_36',
                    ],
                bpds=[
                    '# Eradicate! digistruct console',
                    'GD_Cork_Eradicate_Data.InteractiveObjects.IO_BotScanner:BehaviorProviderDefinition_0',
                    ],
                ),
            ),
        Level('Vorago Solitude', 'Digsite_P',
            doors=Changes(
                interps=[
                    'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            others=Changes(
                raw=[
                    '# ICU-P and RT-FC walking speed (I suspect this doesn\'t actually work)',
                    'GD_Co_NPC_TheseAreTheBots.Character.CharClass_L3PO GroundSpeed 800',
                    'GD_Co_NPC_TheseAreTheBots.Character.CharacterClass_C2T2 GroundSpeed 800',
                    ],
                ),
            ),
        ]),
    ('Claptastic Voyage', [
        Level('Cluster 00773 P4ND0R4', 'Ma_LeftCluster_P',
            doors=Changes(
                interps=[
                    'Ma_LeftCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    ],
                ),
            others=Changes(
                interps=[
                    '# MINAC Cannon Aiming',
                    'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_10',
                    'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    ('Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_18', 0.5),
                    '# MINAC Paint Barrel',
                    'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_13',
                    'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_14',
                    '# Printers (in Chip\'s Data Mining Adventure)',
                    'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_22',
                    'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_23',
                    'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_24',
                    ],
                ),
            ),
        Level('Cluster 99002 0V3RL00K', 'Ma_RightCluster_P',
            doors=Changes(
                interps=[
                    # Eh, "Memory door," I suspect this is just related to the opening anim
                    #'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Challenge_Claptrap_Memory.SeqAct_Interp_0',
                    # Church door
                    'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    ],
                ),
            ),
        Level('Cortex', 'Ma_SubBoss_P',
            doors=Changes(
                interps=[
                    'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            others=Changes(
                others=[
                    ('# Mutator key insertion', None, None),
                    ('GD_Ma_Mutator.Mutator.IO_MutatorQuestComputer', 'BodyComposition.Attachments[10].Data.Float', 2),
                    ],
                ),
            ),
        Level('Deck 13 1/2', 'Ma_Deck13_P',
            # Will have to see
            ),
        Level('Deck 13.5', 'Ma_FinalBoss_P',
            # Will have to see
            ),
        Level('Motherlessboard', 'Ma_Motherboard_P',
            doors=Changes(
                interps=[
                    'Ma_Motherboard_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqAct_Interp_10',
                    'Ma_Motherboard_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqAct_Interp_2',
                    ],
                ),
            ),
        Level('Nexus', 'Ma_Nexus_P',
            # Various "Plinth"s in here, presumably the characters which pop up.  Didn't speed any of those up yet, though
            doors=Changes(
                interps=[
                    'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqAct_Interp_12',
                    # Has a PlayRate, will probably have to change that for this one to *actually* work:
                    'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqAct_Interp_1',
                    'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqAct_Interp_15',
                    'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqAct_Interp_9',
                    'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.SecretDoor.SeqAct_Interp_5',
                    ],
                ),
            ),
        Level('Subconscious', 'Ma_Subconscious_P',
            doors=Changes(
                interps=[
                    'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Sub-Subconscious.SeqAct_Interp_3',
                    # Various other vars in here too, will have to see how it looks.
                    'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqAct_Interp_16',
                    'Ma_Subconscious_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_10',
                    ],
                ),
            ),
        ]),
    ('Other DLC', [
        Level('Abandoned Training Facility', 'MoonSlaughter_P',
            doors=Changes(
                interps=[
                    'MoonSlaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'MoonSlaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Hologram Projection',
                    'MoonSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'MoonSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Holodome', 'Eridian_Slaughter_P',
            # Lots of objects in here in general, will have to test to see if any are worth speeding up.
            lifts=Changes(
                interps=[
                    'Eridian_slaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            ),
        ]),
    ]

# Theoretically already sorted, but this'll take care of any errors
for (_, levels) in dlcs:
    levels.sort()

# Construct the mod.  There's quite a bit in the "Container" section that we should
# really programmatically construct, but that's historically been a non-code-driven
# mod, just built in BLCMM itself, so that'll have to wait for a possible eventual
# overhaul.
lines = []
lines.append("""TPS
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Speeds up nearly all objects that the player interacts with, by {speed_scale}x (mostly).
    # No more waiting for doors to open, elevators to ascend, overengineered Hyperion 
    # containers to unpack, or other such annoyances!

""".format(
    mod_name=mod_name,
    mod_version=mod_version,
    speed_scale=speed_scale,
    ))

# Computers / Switches
lines.append("""#<Computers / Switches>

    # This likely isn't a comprehensive list of all interactable computers/switches
    # in the game, but it does make a few interactions a bit quicker.
""")
for (label, base_name, bpd_suffix) in [
        ('Computer Console (generic)', 'GD_GenericSwitches.InteractiveObjects.IO_ComputerConsole', 'BehaviorProviderDefinition_1'),
        ('Computer Console A', 'GD_GenericSwitches.InteractiveObjects.IO_ComputerConsole_A', 'BehaviorProviderDefinition_1'),
        ('Computer Console A (with lever)', 'GD_GenericSwitches.InteractiveObjects.IO_ComputerConsole_A_Lever', 'BehaviorProviderDefinition_1'),
        ('Computer Console B', 'GD_GenericSwitches.InteractiveObjects.IO_ComputerConsole_B', 'BehaviorProviderDefinition_1'),
        ('Computer Console C', 'GD_GenericSwitches.InteractiveObjects.IO_ComputerConsole_C', 'BehaviorProviderDefinition_1'),
        ('Generic Button', 'GD_GenericSwitches.InteractiveObjects.GenericButton', 'BehaviorProviderDefinition_0'),
        ('Hyperion Button', 'GD_GenericSwitches.InteractiveObjects.GenericButtonHyperion', 'BehaviorProviderDefinition_0'),
        ('Floor Lever', 'GD_GenericSwitches.InteractiveObjects.GenericFloorLever', 'BehaviorProviderDefinition_0'),
        ('Keypad', 'GD_GenericSwitches.InteractiveObjects.GenericKeypad', 'BehaviorProviderDefinition_0'),
        ('Generic Switch', 'GD_GenericSwitches.InteractiveObjects.GenericSwitch', 'BehaviorProviderDefinition_0'),
        ('Generic Wheel', 'GD_GenericSwitches.InteractiveObjects.GenericWheel', 'BehaviorProviderDefinition_0'),
        ('Claptastic Voyage Console (generic)', 'GD_Ma_GenericSwitches.InteractiveObjects.IO_ComputerConsole', 'BehaviorProviderDefinition_1'),
        ('Claptastic Voyage Console A (with lever)', 'GD_Ma_GenericSwitches.InteractiveObjects.IO_ComputerConsole_A_Lever', 'BehaviorProviderDefinition_1'),
        ]:
    lines.append('#<{}>'.format(label))
    lines.append('')

    # First get any Floats we see in the base IO
    io_struct = data.get_struct_by_full_object(base_name)
    for (attach_idx, attach) in enumerate(io_struct['BodyComposition']['Attachments']):
        floatval = float(attach['Data']['Float'])
        if floatval != 0:
            lines.append('level None set {} BodyComposition.Attachments[{}].Data.Float {:0.6f}'.format(base_name, attach_idx, floatval/speed_scale))
            lines.append('')

    # Now the BPD
    bpd_name = '{}:{}'.format(base_name, bpd_suffix)
    for cmd in delay_bpd(bpd_name, speed_scale):
        lines.append('level None {}'.format(cmd))
        lines.append('')

    lines.append('#</{}>'.format(label))
    lines.append('')
lines.append('#</Computers / Switches>')
lines.append('')

# Containers
lines.append("""#<Containers>

        # Previously the standalone "TPS Container TimeSaver XL" mod

        #<Improved Opening Speed>

            #<Most Containers>

                level None set Anim_Lootables.Animations.AnimTree_Lootables_Willow:WillowAnimNode_Simple_0 PlayRate {speed_scale}

                level None set Anim_Lootables.Animations.AnimTree_Lootables_Willow:WillowAnimNode_Simple_340 PlayRate {speed_scale}

                level None set Anim_Lootables.Animations.AnimTree_Lootables_Willow:WillowAnimNode_Simple_684 PlayRate {speed_scale_3}

                level None set Anim_Lootables.Animations.AnimTree_Lootables_Willow:WillowAnimNode_Simple_754 PlayRate {speed_scale}

                level None set Prop_Co_Lootables.Animations.AnimTree_Lootables_Cork:WillowAnimNode_Simple_0 PlayRate {speed_scale}

                level None set Prop_Co_Lootables.Animations.AnimTree_Lootables_Cork:WillowAnimNode_Simple_340 PlayRate {speed_scale}

                level None set Prop_Co_Lootables.Animations.AnimTree_Lootables_Cork:WillowAnimNode_Simple_684 PlayRate {speed_scale_3}

                level None set Prop_Co_Lootables.Animations.AnimTree_Lootables_Cork:WillowAnimNode_Simple_754 PlayRate {speed_scale}

            #</Most Containers>

            #<Golden Chest>

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_0 PlayRate {speed_scale}

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_66 PlayRate {speed_scale}

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_86 PlayRate {speed_scale}

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_339 PlayRate {speed_scale}

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_340 PlayRate {speed_scale}

            #</Golden Chest>

            #<Digistruct Chests>

                #<Digistruct Speed>

                    level None set GD_CoordinatedEffects.Digistruct_Chest EffectDuration {duration_4}

                    level None set GD_CoordinatedEffects.Digistruct_Chest_Despawn EffectDuration {duration_3}

                #</Digistruct Speed>

                #<Chest Tweaks>

                    level None set GD_Ma_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_Ma_HyperionAmmo_Digi:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[11].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Ma_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_Ma_HyperionAmmo_Digi:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[9].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Ma_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_Ma_HyperionAmmo_Digi:BehaviorProviderDefinition_1.Behavior_Delay_66 Delay {duration_4}

                    level None set GD_Ma_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_Ma_HyperionAmmo_Digi:BehaviorProviderDefinition_1.Behavior_Delay_65 Delay 0

                #</Chest Tweaks>

                #<Spawner Tweaks>

                    # This is what makes sure that the ammo spawners start their countdowns when appropriate.

                    level None set GD_Ma_AmmoMachine.IO_Ma_AmmoMachine:BehaviorProviderDefinition_0 BehaviorSequences[1].ConsolidatedOutputLinkData[6].ActivateDelay {duration_4}

                #</Spawner Tweaks>

            #</Digistruct Chests>

        #</Improved Opening Speed>

        #<Items Available At Spawn>

            # These statements set chests to immediately allow attached items to be picked up
            # by the user.  Without these, many containers would result in un-pick-uppable
            # loot.

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_8BitDahlAmmo:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_8BitDahlAmmo:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_8bitDahlWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_8bitTreasureChest:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_BanditWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Ammo:BehaviorProviderDefinition_1.Behavior_AttachItems_10 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Cooler:BehaviorProviderDefinition_1.Behavior_AttachItems_8 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_CardboardBox:BehaviorProviderDefinition_1.Behavior_AttachItems_9 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Cashbox:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlAmmo:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlAmmo:BehaviorProviderDefinition_1.Behavior_AttachItems_2 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlCooler:BehaviorProviderDefinition_1.Behavior_AttachItems_15 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlCooler:BehaviorProviderDefinition_1.Behavior_AttachItems_40 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlCoolerO2:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlCoolerO2:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlSmallBox:BehaviorProviderDefinition_1.Behavior_AttachItems_119 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_14 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Dumpster:BehaviorProviderDefinition_4.Behavior_AttachItems_134 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionAmmo:BehaviorProviderDefinition_1.Behavior_AttachItems_34 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionChest:BehaviorProviderDefinition_0.Behavior_AttachItems_7 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionMinibox:BehaviorProviderDefinition_1.Behavior_AttachItems_101 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionSmallbox:BehaviorProviderDefinition_1.Behavior_AttachItems_122 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_LaundryMachine:BehaviorProviderDefinition_10.Behavior_AttachItems_155 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Mailbox:BehaviorProviderDefinition_12.Behavior_AttachItems_161 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MetalCrate:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MilitaryCrate:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MiniFridge:BehaviorProviderDefinition_11.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Safe:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StorageLocker:BehaviorProviderDefinition_0.Behavior_AttachItems_11 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StrongBox:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StrongBox_Isaiah:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Toilet:BehaviorProviderDefinition_0.Behavior_AttachItems_5 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Golden:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Moonstone:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_HyperionAmmo_Digi:BehaviorProviderDefinition_1.Behavior_AttachItems_9 bDisablePickups False

            level None set GD_Co_Chapter03_Data.InteractiveObjects.InteractiveObj_MoxxiDahlEpic:BehaviorProviderDefinition_1.Behavior_AttachItems_5 bDisablePickups False

            level None set GD_Co_LaserRebootMissionDataJJ.EpicChest.IO_HyperionEpicChest_Digi:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Co_LaserRebootMissionDataJJ.GunRack.IO_HypGunRack_Digi:BehaviorProviderDefinition_1.Behavior_AttachItems_6 bDisablePickups False

            level None set GD_Co_Paint_Job_Data.InteractiveObjects.Paint_Loot_Chest:BehaviorProviderDefinition_0.Behavior_AttachItems_7 bDisablePickups False

            level None set GD_Co_VoiceOver_Data.InteractiveObjects.Book_Loot_Chest:BehaviorProviderDefinition_0.Behavior_AttachItems_6 bDisablePickups False

            level None set GD_Co_WipingSlateData.InteractiveObjects.InteractiveObj_Safe_WipingSlate:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_EridianSlaughterData.InteractiveObjects.InteractiveObj_DahlAmmoPet:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_EridianSlaughterData.InteractiveObjects.InteractiveObj_DahlAmmoPet:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Ammo_Marigold:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlWeaponChest_Glitched:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlWeaponChest_Marigold:BehaviorProviderDefinition_1.Behavior_AttachItems_7 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest_Glitched:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest_Marigold:BehaviorProviderDefinition_1.Behavior_AttachItems_2 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionAmmo_Marigold:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionChest_Glitched:BehaviorProviderDefinition_0.Behavior_AttachItems_14 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionMinibox_Marigold:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionSmallbox_Marigold:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_MetalCrate_Glitched:BehaviorProviderDefinition_1.Behavior_AttachItems_2 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_MetalCrate_Marigold:BehaviorProviderDefinition_1.Behavior_AttachItems_6 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_StrongBox_Marigold:BehaviorProviderDefinition_1.Behavior_AttachItems_11 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Glitched:BehaviorProviderDefinition_1.Behavior_AttachItems_5 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_Ma_HyperionAmmo_Digi:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Ma_Balance_Treasure.Lootables.InteractiveObj_Dumpster_Marigold:BehaviorProviderDefinition_4.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Ma_Chapter02_Data.InteractiveObjects.InteractiveObj_HypWeaponChest_FileSearch_Glitched:BehaviorProviderDefinition_1.Behavior_AttachItems_6 bDisablePickups False

            level None set GD_Ma_Mutator.Mutator.IO_CommonChest_Mut:BehaviorProviderDefinition_1.Behavior_AttachItems_10 bDisablePickups False

            level None set GD_Ma_Mutator.Mutator.IO_GlitchChest_Mut:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Ma_Mutator.Mutator.IO_RedChest_Mut:BehaviorProviderDefinition_1.Behavior_AttachItems_12 bDisablePickups False

            level None set GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_01:BehaviorProviderDefinition_0.Behavior_AttachItems_17 bDisablePickups False

            level None set GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_02:BehaviorProviderDefinition_0.Behavior_AttachItems_18 bDisablePickups False

            level None set GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_03:BehaviorProviderDefinition_0.Behavior_AttachItems_24 bDisablePickups False

            level None set gd_co_hot_head_data.InteractiveObjects.InteractiveObj_HypWeaponChest_Custom:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set gd_co_lastrequestsdata.InteractiveObjects.InteractiveObj_DahlEpic_LastRequests:BehaviorProviderDefinition_1.Behavior_AttachItems_5 bDisablePickups False

            level None set gd_co_novanoproblemdata.IO_ElectronicObjectThree:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set gd_co_novanoproblemdata.InteractiveObjects.InteractiveObj_ShockChest:BehaviorProviderDefinition_1.Behavior_AttachItems_10 bDisablePickups False

            level None set gd_co_voyageofcaptainchefdata.InteractiveObjects.IO_Co_FlagBox:BehaviorProviderDefinition_1.Behavior_AttachItems_2 bDisablePickups False

            level None set GD_Ma_Grinder.InteractiveObjects.IO_Grinder:BehaviorProviderDefinition_0.Behavior_AttachItems_1 bDisablePickups False

        #</Items Available At Spawn>

        #<Item Spawn Delay>

            # This changes the containers to immediately spawn loot instead of, as is usual, waiting
            # for a small delay (which is typically to wait for animations to be in the "proper" state.

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_8BitDahlAmmo:BehaviorProviderDefinition_1 BehaviorSequences[6].ConsolidatedOutputLinkData[2].ActivateDelay 0.080000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_8bitDahlWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.120000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_8bitTreasureChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.270000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Ammo:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Cooler:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.144000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_CardboardBox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Cashbox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlAmmo:BehaviorProviderDefinition_1 BehaviorSequences[6].ConsolidatedOutputLinkData[2].ActivateDelay 0.080000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlCooler:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.035000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlCoolerO2:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.035000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.140000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlSmallBox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.035000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.120000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Dumpster:BehaviorProviderDefinition_4 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.040000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionMinibox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.020000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionSmallbox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.040000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_LaundryMachine:BehaviorProviderDefinition_10 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Mailbox:BehaviorProviderDefinition_12 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MetalCrate:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.260000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MilitaryCrate:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MiniFridge:BehaviorProviderDefinition_11 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.040000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StorageLocker:BehaviorProviderDefinition_0 BehaviorSequences[5].ConsolidatedOutputLinkData[2].ActivateDelay 0.035000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StrongBox:BehaviorProviderDefinition_1 BehaviorSequences[5].ConsolidatedOutputLinkData[2].ActivateDelay 0.035000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StrongBox_Isaiah:BehaviorProviderDefinition_1 BehaviorSequences[5].ConsolidatedOutputLinkData[2].ActivateDelay 0.035000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Toilet:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.035000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.270000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Golden:BehaviorProviderDefinition_1 BehaviorSequences[5].ConsolidatedOutputLinkData[1].ActivateDelay 0.270000

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Moonstone:BehaviorProviderDefinition_1 BehaviorSequences[5].ConsolidatedOutputLinkData[1].ActivateDelay 0.270000

            level None set GD_Co_Chapter03_Data.InteractiveObjects.InteractiveObj_MoxxiDahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.140000

            level None set GD_EridianSlaughterData.InteractiveObjects.InteractiveObj_DahlAmmoPet:BehaviorProviderDefinition_1 BehaviorSequences[6].ConsolidatedOutputLinkData[2].ActivateDelay 0.080000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Ammo_Marigold:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlWeaponChest_Glitched:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.120000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlWeaponChest_Marigold:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.120000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest_Glitched:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest_Marigold:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionChest_Glitched:BehaviorProviderDefinition_0 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.100000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionMinibox_Marigold:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.020000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionSmallbox_Marigold:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.040000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_MetalCrate_Glitched:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.260000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_MetalCrate_Marigold:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.260000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_StrongBox_Marigold:BehaviorProviderDefinition_1 BehaviorSequences[5].ConsolidatedOutputLinkData[2].ActivateDelay 0.035000

            level None set GD_Ma_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Glitched:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.270000

            level None set GD_Ma_Balance_Treasure.Lootables.InteractiveObj_Dumpster_Marigold:BehaviorProviderDefinition_4 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.040000

            level None set GD_Ma_Chapter02_Data.InteractiveObjects.InteractiveObj_HypWeaponChest_FileSearch_Glitched:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set GD_Ma_Mutator.Mutator.IO_CommonChest_Mut:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.270000

            level None set GD_Ma_Mutator.Mutator.IO_GlitchChest_Mut:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.270000

            level None set GD_Ma_Mutator.Mutator.IO_RedChest_Mut:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.270000

            level None set GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_01:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.400000

            level None set GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_02:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.400000

            level None set GD_Ma_Population_Treasure.InteractiveObjects.InteractiveObj_HiddenStash_03:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.400000

            level None set gd_co_hot_head_data.InteractiveObjects.InteractiveObj_HypWeaponChest_Custom:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.050000

            level None set gd_co_lastrequestsdata.InteractiveObjects.InteractiveObj_DahlEpic_LastRequests:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.140000

            level None set gd_co_novanoproblemdata.InteractiveObjects.InteractiveObj_ShockChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.120000

            level None set gd_co_voyageofcaptainchefdata.InteractiveObjects.IO_Co_FlagBox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[6].ActivateDelay 0.100000

        #</Item Spawn Delay>

    #</Containers>
""".format(
    speed_scale=speed_scale,
    speed_scale_1_25=speed_scale*1.25,
    speed_scale_3=speed_scale*3,
    duration_3=round(3/speed_scale, 6),
    duration_4=round(4/speed_scale, 6),
    ))

# Doors/Gates
lines.append("""#<Doors / Gates>

        #<Regular Doors>

            # These variables take care of basically any "regular" player-interactable door (ie: something
            # without a separate button)

            level None set Anim_Doors.Animations.Anim_DoorSlider:AnimSequence_0 RateScale {speed_scale}

            level None set Anim_Doors.Animations.Anim_DoorSlider:AnimSequence_1 RateScale {speed_scale}

            level None set Anim_Doors.Animations.Anim_DoorSlider:AnimSequence_2 RateScale {speed_scale}

            level None set Anim_Doors.Animations.Anim_DoorSlider:AnimSequence_3 RateScale {speed_scale}

            level None set Anim_Doors.Animations.Anim_GenericDoor:AnimSequence_3 RateScale {speed_scale}

            level None set Anim_Doors.Animations.Anim_GenericDoor:AnimSequence_5 RateScale {speed_scale}

            level None set Anim_Doors.Animations.Anim_GenericDoor:AnimSequence_6 RateScale {speed_scale}

        #</Regular Doors>

        #<Level-Specific Doors and Gates>

            # It's worth noting that many of the statements here probably aren't really
            # necessary, and possibly some don't even do anything useful.  When constructing
            # the mod, rather than look for slow doors+things in-game and *then* try to
            # find the relevant objects, I'd just run some queries and alter any object
            # which seemed apropos.  So almost certainly I'm buffing at least a few things
            # which don't actually do anything, or things like doors which let new enemies
            # through, etc.

""".format(
    speed_scale=speed_scale,
    ))

for (dlc_name, levels) in dlcs:
    if any([l.has_doors_data() for l in levels]):
        lines.append('#<{}>'.format(dlc_name))
        lines.append('')
        for level in levels:
            level.process_doors(speed_scale, lines)
        lines.append('#</{}>'.format(dlc_name))
        lines.append('')

lines.append('#</Level-Specific Doors and Gates>')
lines.append('')
lines.append('#</Doors / Gates>')
lines.append('')

# Fast Travel
lines.append("""#<Fast Travel Machines>

    # Speeds up opening of Fast Travel stations.  Useful in the rare instances
    # where a station has to activate before you can use it -- in TPS the first
    # real noticeable instance of this is after the battle with Felicity Rampant.

    level None set GD_GameSystemMachines.SpecialMoves.SpecialMove_FastTravelClosedToOpen PlayRate {speed_scale}

    level None set GD_GameSystemMachines.SpecialMoves.SpecialMove_FastTravelClosedToOpenBroken PlayRate {speed_scale}

    level None set GD_GameSystemMachines.InteractiveObjects.IO_FastTravelMachine_Dahl BodyComposition.Attachments[46].Data.Float {button_time}

    level None set GD_GameSystemMachines.InteractiveObjects.IO_FastTravelMachine_Dahl BodyComposition.Attachments[49].Data.Float {button_time}

    level None set GD_GameSystemMachines.InteractiveObjects.IO_FastTravelMachine_Dahl BodyComposition.Attachments[52].Data.Float {button_time}

""".format(
    speed_scale=speed_scale,
    button_time=0.5/speed_scale,
    ))

for bpd_name in [
        'GD_GameSystemMachines.InteractiveObjects.LevelTravelMachine:BehaviorProviderDefinition_4',
        'GD_GameSystemMachines.Behaviors.Be_FastTravelMachine',
        ]:
    for cmd in delay_bpd(bpd_name, speed_scale):
        lines.append('level None {}'.format(cmd))
        lines.append('')

lines.append('#</Fast Travel Machines>')
lines.append('')

# Grinder
lines.append("""#<Grinder>

    level Spaceport_P set GD_Grinder.Misc.AnimTree_Grinder:WillowAnimNode_Simple_0 PlayRate {scale}

    level Spaceport_P set GD_Grinder.Misc.AnimTree_Grinder:WillowAnimNode_Simple_339 PlayRate {scale}

    level Spaceport_P set GD_Grinder.Misc.AnimTree_Grinder:WillowAnimNode_Simple_609 PlayRate {scale}

    level Spaceport_P set GD_Grinder.Misc.AnimTree_Grinder:WillowAnimNode_Simple_931 PlayRate {scale}

    level Spaceport_P set GD_Grinder.Misc.AnimTree_Grinder:WillowAnimNode_Simple_933 PlayRate {scale}

    level Spaceport_P set GD_Grinder.Misc.AnimTree_Grinder:WillowAnimNode_Simple_934 PlayRate {scale}

    level Spaceport_P set GD_Grinder.Misc.AnimTree_Grinder:WillowAnimNode_Simple_931 BlendInTime {blend_time}

    level Spaceport_P set GD_Grinder.Misc.AnimTree_Grinder:WillowAnimNode_Simple_931 BlendOutTime {blend_time}

""".format(scale=grinder_scale, blend_time=1/grinder_scale))
for cmd in delay_bpd('GD_Grinder.InteractiveObjects.IO_Grinder:BehaviorProviderDefinition_0', grinder_scale):
    lines.append('level Spaceport_P {}'.format(cmd))
    lines.append('')
lines.append('#</Grinder>')
lines.append('')

# Drawbridges
#lines.append('#<Drawbridges>')
#lines.append('')
#for (dlc_name, levels) in dlcs:
#    if any([l.has_drawbridges_data() for l in levels]):
#        lines.append('#<{}>'.format(dlc_name))
#        lines.append('')
#        for level in levels:
#            level.process_drawbridges(speed_scale, lines)
#        lines.append('#</{}>'.format(dlc_name))
#        lines.append('')
#lines.append('#</Drawbridges>')
#lines.append('')

# Lifts
lines.append('#<Lifts / Elevators / Transporters>')
lines.append('')
for (dlc_name, levels) in dlcs:
    if any([l.has_lifts_data() for l in levels]):
        lines.append('#<{}>'.format(dlc_name))
        lines.append('')
        for level in levels:
            level.process_lifts(speed_scale, lines)
        lines.append('#</{}>'.format(dlc_name))
        lines.append('')
lines.append('#</Lifts / Elevators / Transporters>')
lines.append('')

# Other
lines.append('#<Other Level-Specific Objects>')
lines.append('')
for (dlc_name, levels) in dlcs:
    if any([l.has_others_data() for l in levels]):
        lines.append('#<{}>'.format(dlc_name))
        lines.append('')
        for level in levels:
            level.process_others(speed_scale, lines)
        lines.append('#</{}>'.format(dlc_name))
        lines.append('')
lines.append('#</Other Level-Specific Objects>')
lines.append('')

# Oxygen Generators
lines.append("""#<Oxygen Generators>

    level None set Anim_Co_OxygenGenerator.Anim_OxygenGenerator:OxyGen_Closing RateScale {speed_scale}

    level None set Anim_Co_OxygenGenerator.Anim_OxygenGenerator:OxyGen_Opening RateScale {speed_scale}
""".format(speed_scale=speed_scale))
for bpd in [
        'GD_Co_AirDome.Behaviors.BP_OxygenGenerator_Shared',
        'GD_Co_AirDome.Behaviors.BP_OxygenDome_Shared',
        ]:
    for cmd in delay_bpd(bpd, speed_scale):
        lines.append('level None {}'.format(cmd))
        lines.append('')
lines.append('#</Oxygen Generators>')
lines.append('')

# Slot Machines
bpd_slots_scale = slots_scale/2
lines.append("""#<Slot Machines>

    # There are a lot of variables at play with these -- the speedup should be about {bpd_slots_scale}x overall.

    level None set GD_SlotMachine.Animation.Anim_PullHandle PlayRate {slots_scale}

    level None set GD_SlotMachine.Animation.Anim_SpinEnd PlayRate {slots_scale}

    level None set GD_SlotMachine.Animation.Anim_SpinLoop PlayRate {slots_scale}

    level None set GD_SlotMachine.Animation.AnimTree_SlotMachine:WillowAnimNode_Simple_75 PlayRate {slots_scale}

    level None set GD_SlotMachine.Animation.AnimTree_SlotMachine:WillowAnimNode_Simple_89 PlayRate {slots_scale}
""".format(
    slots_scale=slots_scale,
    bpd_slots_scale=bpd_slots_scale,
    ))

for cmd in delay_bpd('GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0', bpd_slots_scale, delay_overrides={
        # These are vars are usually set dynamically by the engine -- we can't trust the in-data values
        # to do the math with.
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_584': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_585': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_586': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_587': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_588': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_592': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_593': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_595': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_596': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_597': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_598': 5/bpd_slots_scale,
        'GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_599': 5/bpd_slots_scale,
        },
        # We need this full delay between the door opening and spawning the grenade
        skip_cold={(1, 61)}):
    lines.append('level None {}'.format(cmd))
    lines.append('')

lines.append('#</Slot Machines>')
lines.append('')

# Vehicle Animations
vehicles = [
        ('Moon Buggy',
            ['GD_MoonBuggy_Streaming'],
            [
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_Driver_From_Turret',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_DriverEnter_Front',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_DriverEnter_Left',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_DriverEnter_Right',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_DriverExit_Left',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_DriverExit_Right',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_Turret_From_Driver',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_TurretEnter_Left',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_TurretEnter_Rear',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_TurretEnter_Right',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_TurretExit_Left',
                'GD_MoonBuggy_Streaming.Animations.CrewAnim_TurretExit_Right',
            ]),
        ('Stingray',
            ['GD_Co_Stingray_Streaming'],
            [
                'GD_Co_StingRay_Streaming.Animations.CrewAnim_DriverEnter_Front',
                'GD_Co_StingRay_Streaming.Animations.CrewAnim_DriverEnter_Left',
                'GD_Co_StingRay_Streaming.Animations.CrewAnim_DriverEnter_Rear',
                'GD_Co_StingRay_Streaming.Animations.CrewAnim_DriverEnter_Right',
                'GD_Co_StingRay_Streaming.Animations.CrewAnim_DriverExit_Left',
                'GD_Co_StingRay_Streaming.Animations.CrewAnim_DriverExit_Right',
            ]),
        ]
lines.append("""#<Vehicle Animations>

    # Vehicle Animations (such as characters entering, leaving, or changing seats)
    # are only getting a {vehicle_anim_speed_scale}x boost, since they look pretty weird if faster.
    # Thanks to Gronp for this technique!

""".format(vehicle_anim_speed_scale=vehicle_anim_speed_scale))

for (vehicle_name, packages, animations) in vehicles:
    lines.append('#<{}>'.format(vehicle_name))
    lines.append('')
    for package in packages:
        for animation in animations:
            lines.append('demand {} set {} PlayRate {}'.format(package, animation, vehicle_anim_speed_scale))
            lines.append('')
    lines.append('#</{}>'.format(vehicle_name))
    lines.append('')

lines.append('#</Vehicle Animations>')
lines.append('')

# Close!
lines.append('#</{}>'.format(mod_name))

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))
