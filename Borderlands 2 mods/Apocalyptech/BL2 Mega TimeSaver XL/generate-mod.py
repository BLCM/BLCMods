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
mod_name = 'BL2 Mega TimeSaver XL'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)
speed_scale = 5
vehicle_anim_speed_scale = 2
slots_scale = 5

data = Data('BL2')

class Changes(object):
    """
    Changes that we'll be keeping track of
    """

    def __init__(self, interps=[], interpdata=[], others=[], raw=[]):
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

        Start any "object name" with a hash sign (`#`) to put in a comment
        rather than a `set` statement.
        """
        self.interps = interps
        self.interpdata = interpdata
        self.others = others
        self.raw = raw

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
        return len(self.interps) > 0 or len(self.interpdata) > 0 or len(self.others) > 0 or len(self.raw) > 0

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

def delay_bpd(bpd_name, scale, delay_overrides={}, skip_cold=set()):

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

# Data!  Interps were largely found via my ft-explorer 'level_interps.py' sandbox script
dlcs = [
    ('Base Game', [
        Level('Arid Nexus - Badlands', 'Stockade_P',
            doors=Changes(
                interps=[
                    'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqAct_Interp_2',
                    'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Uncle_Teddy.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Uncle Teddy\'s Vending Machine',
                    'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Uncle_Teddy.SeqAct_Interp_2',
                    ],
                ),
            ),
        Level('Arid Nexus - Boneyard', 'Fyrestone_P',
            doors=Changes(
                interps=[
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.YouDontKnowJack.SeqAct_Interp_0',
                    'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThisJustIn.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThisJustIn.SeqAct_Interp_1',
                    'Fyrestone_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Bloodshot Ramparts', 'DamTop_P'),
        Level('Bloodshot Stronghold', 'Dam_P',
            doors=Changes(
                interps=[
                    '# I suspect nearly all of these are enemy-use doors',
                    'Dam_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Dam_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Dam_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Dam_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'Dam_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PrisonCells.SeqAct_Interp_0',
                    'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PrisonCells.SeqAct_Interp_1',
                    'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PrisonCells.SeqAct_Interp_2',
                    'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PrisonCells.SeqAct_Interp_3',
                    'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PrisonCells.SeqAct_Interp_4',
                    'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqAct_Interp_0',
                    'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqAct_Interp_1',
                    'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqAct_Interp_3',
                    ],
                ),
            ),
        Level('Bunker', 'Boss_Cliffs_P',
            doors=Changes(
                interps=[
                    'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    ('Boss_Cliffs_VOGAntechamber.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1', 0.5),
                    ],
                ),
            ),
        Level('Caustic Caverns', 'Caverns_P',
            doors=Changes(
                interps=[
                    '# Minecart Mischief doors',
                    'Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.SeqAct_Interp_5',
                    'Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.SeqAct_Interp_6',
                    'Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.SeqAct_Interp_9',
                    ],
                interpdata=[
                    '# Regular doors',
                    'caverns_p.TheWorld:PersistentLevel.Main_Sequence.InterpData_11',
                    'caverns_p.TheWorld:PersistentLevel.Main_Sequence.InterpData_16',
                    'caverns_p.TheWorld:PersistentLevel.Main_Sequence.InterpData_4',
                    'caverns_p.TheWorld:PersistentLevel.Main_Sequence.InterpData_6',
                    ],
                ),
            lifts=Changes(
                interps=[
                    '# Lost Treasure lift',
                    'Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LostTreasure.SeqAct_Interp_1',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Lost Treasure coming out of the ground',
                    'Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LostTreasure.SeqAct_Interp_0',
                    ],
                interpdata=[
                    '# Minecart Speed',
                    ('Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.InterpData_1', 2.5),
                    ('Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.InterpData_10', 2.5),
                    ('Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.InterpData_11', 2.5),
                    ('Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.InterpData_2', 2.5),
                    ('Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.InterpData_4', 2.5),
                    ('Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.InterpData_8', 2.5),
                    ],
                ),
            ),
        Level('Control Core Angel', 'VOGChamber_P',
            doors=Changes(
                interps=[
                    '# I am almost positive that these don\'t do anything.',
                    'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqAct_Interp_0',
                    'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqAct_Interp_1',
                    'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqAct_Interp_3',
                    'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqAct_Interp_4',
                    'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_10',
                    'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_16',
                    ],
                ),
            ),
        Level('Dust', 'Interlude_P'),
        Level('End of the Line', 'TundraTrain_P'),
        Level('Eridium Blight', 'Ash_P',
            doors=Changes(
                interps=[
                    'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Grandmother_House.SeqAct_Interp_0',
                    'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ],
                interpdata=[
                    '# Gates blocking the way to Hero\'s Pass',
                    ('Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.InterpData_3', 0.5),
                    'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.InterpData_2',
                    ],
                others=[
                    # These are the delays between opening the three bars and opening the doors themselves,
                    # though there's still a six-second gap that I haven't gotten rid of yet.
                    ('Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqAct_Delay_4', 'Duration', 4),
                    ('Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqVar_Float_2', 'FloatValue', 5.5),
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Fink\'s Slaughterhouse', 'BanditSlaughter_P',
            lifts=Changes(
                interps=[
                    'BanditSlaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    ]
                ),
            ),
        Level('Fridge', 'Fridge_P',
            doors=Changes(
                interps=[
                    '# Almost certainly a bunch of these are enemy-use only',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    #'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1', # omitting this one, also has red lights
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_10',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_13',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_14',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_15',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_16',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_17',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_18',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_19',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_20',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    #'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7', # another red light
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    'Fridge_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ColdShoulder.SeqAct_Interp_10',
                    'Fridge_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ColdShoulder.SeqAct_Interp_12',
                    'Fridge_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ColdShoulder.SeqAct_Interp_9',
                    'Fridge_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_0',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_1',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_10',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_2',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_3',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_4',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_5',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_6',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_7',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_8',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_9',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    ],
                ),
            ),
        Level('Friendship Gulag', 'HypInterlude_P'),
        Level('Frostburn Canyon', 'IceCanyon_P'),
        Level('Hero\'s Pass', 'FinalBossAscent_P',
            doors=Changes(
                interps=[
                    '# Little Forcefield',
                    'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqAct_Interp_3',
                    '# Big Forcefield',
                    'FinalBossAscent_FX.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            ),
        Level('Highlands', 'Grass_P',
            doors=Changes(
                interps=[
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HiddenJournals.SeqAct_Interp_2',
                    ],
                interpdata=[
                    '# Container with third medicine shipment - buffing this far more than our usual scaling',
                    ('Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked.InterpData_2', 0.25),
                    ],
                ),
            others=Changes(
                interps=[
                    '# Mortar aiming',
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqAct_Interp_0',
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqAct_Interp_10',
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqAct_Interp_11',
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqAct_Interp_12',
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqAct_Interp_7',
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqAct_Interp_9',
                    ],
                interpdata=[
                    '# Overlook Grinder',
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked2.InterpData_0',
                    'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked2.InterpData_7',
                    ],
                others=[
                    ('GD_Z2_Overlooked2Data.InteractiveObjects.IO_Overlooked2_ShieldEssenceSpawn:BehaviorProviderDefinition_0', 'BehaviorSequences[0].ConsolidatedOutputLinkData[1].ActivateDelay', 4),
                    ('GD_Z2_Overlooked2Data.InteractiveObjects.IO_Overlooked2_ShieldEssenceSpawn:BehaviorProviderDefinition_0', 'BehaviorSequences[0].ConsolidatedOutputLinkData[2].ActivateDelay', 4),
                    ],
                ),
            ),
        Level('Highlands Outwash', 'Outwash_P',
            doors=Changes(
                interps=[
                    'Outwash_Dam.TheWorld:PersistentLevel.Main_Sequence.Combat.SeqAct_Interp_2',
                    'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HiddenJournals.SeqAct_Interp_2',
                    ],
                ),
            lifts=Changes(
                interps=[
                    '# Tram System - This is only receiving half the usual boost, because it looks too weird otherwise',
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_4', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_8', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_6', 0.5),

                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_0', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_1', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_2', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_3', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_5', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_7', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_9', 0.5),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Interp_11', 0.5),
                    ],
                interpdata=[
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_0', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_1', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_2', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_3', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_4', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_6', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_7', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_8', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_10', 2),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.InterpData_19', 2),
                    ],
                others=[
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Delay_0', 'Duration', 1),
                    ('Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqAct_Delay_1', 'Duration', 1),
                    ],
                ),
            ),
        Level('Holy Spirits', 'Luckys_P',
            drawbridges=Changes(
                interps=[
                    'Luckys_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EndOfRainbow.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Lynchwood', 'Grass_Lynchwood_P',
            lifts=Changes(
                interps=[
                    'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.SeqAct_Interp_7',
                    'Grass_Lynchwood_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    'Grass_Lynchwood_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Grass_Lynchwood_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'Grass_Lynchwood_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    ],
                ),
            ),
        Level('Natural Selection Annex', 'CreatureSlaughter_P',
            lifts=Changes(
                interps=[
                    'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    ],
                ),
            ),
        Level('Opportunity', 'HyperionCity_P',
            doors=Changes(
                interps=[
                    'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HellHathNoFury.SeqAct_Interp_1',
                    'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HomeMovies.SeqAct_Interp_0',
                    'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqAct_Interp_0',
                    'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Combat.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Elevator.SeqAct_Interp_0',
                    'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Elevators.SeqAct_Interp_0',
                    'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqAct_Interp_0',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Laser-cutting times (only improving a bit)',
                    ('HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqAct_Interp_1', 0.33/(speed_scale/1.4)),
                    ('HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqAct_Interp_2', 0.66/(speed_scale/1.4)),
                    ('HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqAct_Interp_3', 0.5/(speed_scale/1.4)),
                    ('HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqAct_Interp_4', 0.5/(speed_scale/1.4)),
                    ],
                ),
            ),
        Level('Ore Chasm', 'RobotSlaughter_P',
            doors=Changes(
                interps=[
                    'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ],
                ),
            ),
        Level('Sanctuary (after liftoff)', 'SanctuaryAir_P',
            doors=Changes(
                interps=[
                    'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BearerOfBadNews.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Sanctuary (before liftoff)', 'Sanctuary_P',
            doors=Changes(
                interps=[
                    'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqAct_Interp_5',
                    'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqAct_Interp_8',
                    '# Scooter\'s Garage door, I believe (though it gets cutscene\'d almost immediately, difficult to tell)',
                    'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Scooters_Garage.SeqAct_Interp_52',
                    'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Scooters_Garage.SeqAct_Interp_53',
                    ],
                others=[
                    ('# Main Sanctuary Gate', None, None),
                    ('GD_SanctuaryObjects.InteractiveObjects.SanctuaryGate', 'BodyComposition.Attachments[0].Data.Float', 7),
                    ('GD_SanctuaryObjects.InteractiveObjects.SanctuaryGate', 'BodyComposition.Attachments[3].Data.Float', 1.75),
                    ('GD_SanctuaryObjects.InteractiveObjects.SanctuaryGate:BehaviorProviderDefinition_0', 'BehaviorSequences[1].ConsolidatedOutputLinkData[1].ActivateDelay', 4.5),
                    ],
                ),
            ),
        Level('Sanctuary Hole', 'Sanctuary_Hole_P',
            doors=Changes(
                interps=[
                    'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.SeqAct_Interp_6',
                    ],
                interpdata=[
                    'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.InterpData_2',
                    ],
                ),
            lifts=Changes(
                interpdata=[
                    'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.InterpData_1',
                    'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.InterpData_12',
                    'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.InterpData_13',
                    'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.InterpData_14',
                    'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.InterpData_3',
                    'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.InterpData_7',
                    ],
                ),
            ),
        Level('Sawtooth Cauldron', 'CraterLake_P',
            lifts=Changes(
                interps=[
                    '# The elevator looks a little jerky when sped up -- we\'re not buffing it quite',
                    '# as much as other objects, to minimize that a bit, though it still happens',
                    ('CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0', 0.5),
                    'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Boombringer Silo',
                    'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode16.SeqAct_Interp_1',
                    ],
                interpdata=[
                    '# Capture the Flags flag-raising speed',
                    'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.InterpData_0',
                    'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.InterpData_1',
                    'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.InterpData_2',
                    ],
                ),
            ),
        Level('Southern Shelf', 'SouthernShelf_P',
            doors=Changes(
                interps=[
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Symbiosis.SeqAct_Interp_0',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HandsomeJackHere.SeqAct_Interp_0',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HandsomeJackHere.SeqAct_Interp_2',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_17',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    '# Gates',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.GATE_SEQUENCE.SeqAct_Interp_14',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6', # also some "Claptrap" vars...
                    'SouthernShelf_P.TheWorld:PersistentLevel.Main_Sequence.Freighter.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BrewstersElevator.SeqAct_Interp_3',
                    ],
                ),
            ),
        Level('Southern Shelf - Bay', 'Cove_P',
            # A lot of stuff from SouthernShelf_P in here, I bet it was originally one map.
            # I think this is probably about all that's actually needed in here...
            lifts=Changes(
                interps=[
                    '# Raft thing',
                    ('Cove_P.TheWorld:PersistentLevel.Main_Sequence.PirateCove.SeqAct_Interp_1', 1.5),
                    ],
                ),
            drawbridges=Changes(
                interps=[
                    'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ('Cove_P.TheWorld:PersistentLevel.Main_Sequence.PirateCove.SeqAct_Interp_0', 2),
                    ],
                ),
            ),
        Level('Southpaw Steam and Power', 'SouthpawFactory_P',
            doors=Changes(
                interps=[
                    '# Exit Doors (after last assassin)',
                    'SouthpawFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'SouthpawFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ],
                ),
            ),
        Level('Terramorphous Peak', 'ThresherRaid_P'), # we could technically speed up some doors, but why bother?
        Level('Thousand Cuts', 'Grass_Cliffs_P',
            lifts=Changes(
                interps=[
                    'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Grass_Cliffs_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                others=[
                    ('Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.WillowSeqEvent_ElevatorUsed_0', 'ReTriggerDelay', 6),
                    ],
                ),
            ),
        Level('Three Horns Divide', 'Ice_P',
            doors=Changes(
                interps=[
                    'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HiddenJournals.SeqAct_Interp_0',
                    'Ice_P.TheWorld:PersistentLevel.Main_Sequence.SpawnStyleFun.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Three Horns Valley', 'Frost_P',
            doors=Changes(
                interps=[
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode03.SeqAct_Interp_5',
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HiddenJournals.SeqAct_Interp_0',
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NoVacancy.SeqAct_Interp_3',
                    'Frost_P.TheWorld:PersistentLevel.Main_Sequence.SpawnStyleFun.SeqAct_Interp_0',
                    '# Bloodshot Front Gate',
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqAct_Interp_3',
                    ],
                interpdata=[
                    '# The front Bloodshot gate has a lot of "hardcoded" timing which needs tweaking',
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.InterpData_3',
                    '# Angel opening the way to the Fridge',
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.InterpData_0',
                    ],
                others=[
                    ('# Since we speed up the Bloodshot gate opening, we also need to speed up the "slam" when', None, None),
                    ('# you honk the first time (without a Technical)', None, None),
                    ('Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqAct_Delay_3', 'Duration', 4),
                    ('Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqAct_Delay_4', 'Duration', 2),
                    ('Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqAct_Delay_5', 'Duration', 0.5),
                    ('Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqAct_Delay_6', 'Duration', 2),
                    ('Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqAct_Delay_7', 'Duration', 1),
                    ('Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqAct_Delay_8', 'Duration', 2.5),
                    ('Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqAct_Delay_9', 'Duration', 2),
                    ],
                ),
            drawbridges=Changes(
                interps=[
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodshotSlums.SeqAct_Interp_1',
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodshotSlums.SeqAct_Interp_2',
                    'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodshotSlums.SeqAct_Interp_3',
                    ],
                ),
            ),
        Level('Tundra Express', 'TundraExpress_P',
            doors=Changes(
                interpdata=[
                    '# The gate to Tina\'s place',
                    'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gates.script_TinyTinaGate.InterpData_1',
                    ],
                ),
            others=Changes(
                interps=[
                    '# The chest in No Hard Feelings',
                    'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NoHardFeelings.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Vault of the Warrior', 'Boss_Volcano_P',
            lifts=Changes(
                interps=[
                    'Boss_Volcano_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Wildlife Exploitation Preserve', 'PandoraPark_P',
            doors=Changes(
                interps=[
                    'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_18',
                    'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.ConstructorSpot.SeqAct_Interp_0',
                    'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.ConstructorSpot.SeqAct_Interp_1',
                    'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.ConstructorSpot.SeqAct_Interp_2',
                    'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.ConstructorSpot.SeqAct_Interp_4',
                    'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqAct_Interp_0',
                    'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqAct_Interp_1',
                    'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqAct_Interp_5',
                    '# Bloodwing-related doors',
                    'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    ],
                ),
            lifts=Changes(
                interpdata=[
                    'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.InterpData_0',
                    'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.InterpData_1',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Wall+Safe hiding a Doctor\'s Orders Objective',
                    'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DoctorsOrders.Safe.SeqAct_Interp_2',
                    'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DoctorsOrders.Safe.SeqAct_Interp_3',
                    ],
                interpdata=[
                    '# Crane which can get the player up to a vault symbol.  Only speeding up slightly',
                    ('PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.InterpData_2', speed_scale*.6),
                    ],
                )
            ),
        Level('Windshear Waste', 'Glacial_P',
            doors=Changes(
                interps=[
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_16',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_17',
                    '# Barge door',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    ],
                ),
            ),
        ]),
    ('DLC 1 - Captain Scarlett and her Pirate\'s Booty', [
        Level('Hayter\'s Folly', 'Orchid_Caves_P',
            doors=Changes(
                interps=[
                    'ORCHID_CAVES_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Orchid_Caves_Raid_C.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'ORCHID_CAVES_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Leviathan\'s Lair', 'Orchid_WormBelly_P'), # Nothing!  The one gate already opens fast enough
        Level('Magnys Lighthouse', 'Orchid_Spire_P',
            lifts=Changes(
                interps=[
                    'Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    # Speeds for these two are set via SeqVar_Floats, below
                    #('Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3', 2),
                    #('Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4', 2),
                    ],
                others=[
                    # So I think that Float_0 is used during the main mission, and Float_4 is used on the replay
                    ('Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_0', 'FloatValue', 0.25*1.5, True),
                    # I think that *this* value gets copied over to Float_0 when the elevator is going up...
                    ('Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_2', 'FloatValue', 0.25*2, True),

                    ('Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_4', 'FloatValue', 0.25*1.5, True),
                    # Likewise, I think this value overwrites Float_4 when going up...
                    ('Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_6', 'FloatValue', 0.25*2, True),
                    ],
                ),
            others=Changes(
                interps=[
                    '# Turret on crane',
                    'Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Oasis', 'Orchid_OasisTown_P',
            doors=Changes(
                interps=[
                    'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Rustyards', 'Orchid_ShipGraveyard_P',
            doors=Changes(
                interps=[
                    'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    ],
                ),
            ),
        Level('Washburne Refinery', 'Orchid_Refinery_P',
            doors=Changes(
                interps=[
                    'Orchid_Refinery_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Orchid_Refinery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Orchid_Refinery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LevelChallenges.SeqAct_Interp_0',
                    'Orchid_Refinery_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Orchid_Refinery_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Wurmwater', 'Orchid_SaltFlats_P',
            doors=Changes(
                interps=[
                    #'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    #'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    ],
                ),
            ),
        ]),
    ('DLC 2 - Mr. Torgue\'s Campaign of Carnage', [
        Level('Badass Crater Bar', 'Iris_Moxxi_P'), # Nothing!
        Level('Badass Crater of Badassitude', 'Iris_Hub_P'), # Nothing?  Hm.
        Level('Beatdown', 'Iris_DL2_P',
            doors=Changes(
                interps=[
                    # I think this one's an enemy-use only garage door, leaving it.
                    # Iris_DL2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1
                    'Iris_DL2_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            ),
        Level('Forge', 'Iris_DL3_P',
            doors=Changes(
                interps=[
                    'Iris_DL3_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Iris_DL3_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'Iris_DL3_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Iris_DL3_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    ],
                ),
            ),
        Level('Pyro Pete\'s Bar', 'Iris_DL2_Interior_P',
            doors=Changes(
                interps=[
                    '# These don\'t actually seem to have any effect, alas.',
                    'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    ],
                others=[
                    ('# Door between bar and staging area', None, None),
                    ('GD_IrisEpisode03_BattleData.InteractiveObjects.MO_Iris_Bardoors', 'BodyComposition.Attachments[0].Data.Float', 1.5),
                    ('GD_IrisEpisode03_BattleData.InteractiveObjects.MO_Iris_Bardoors', 'BodyComposition.Attachments[5].Data.Float', 1.5),
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    ],
                ),
            ),
        Level('Southern Raceway', 'Iris_Hub2_P',
            doors=Changes(
                others=[
                    ('# Chainlink fences guarding Motor Momma area', None, None),
                    ('GD_IrisEpisode04Data.InteractiveObjects.MO_Iris_Mama_Doors', 'BodyComposition.Attachments[0].Data.Float', 3),
                    ('GD_IrisEpisode04Data.InteractiveObjects.MO_Iris_Mama_Doors', 'BodyComposition.Attachments[3].Data.Float', 3),
                    ('GD_IrisEpisode04Data.InteractiveObjects.MO_Iris_Mama_Doors', 'BodyComposition.Attachments[6].Data.Float', 3),
                    ('GD_IrisEpisode04Data.InteractiveObjects.MO_Iris_Mama_Doors', 'BodyComposition.Attachments[9].Data.Float', 3),
                    ],
                ),
            ),
        Level('Torgue Arena (final boss)', 'Iris_DL1_TAS_P',
            doors=Changes(
                interps=[
                    '# Trapdoor (you can\'t actually get to it, but whatever.)',
                    'Iris_DL1_TAS_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Iris_DL1_TAS_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                others=[
                    ('# Main arena door', None, None),
                    ('GD_IrisEpisode06Data.InteractiveObjects.MO_Iris_TASMission_Doors', 'BodyComposition.Attachments[1].Data.Float', 2),
                    ('GD_IrisEpisode06Data.InteractiveObjects.MO_Iris_TASMission_Doors', 'BodyComposition.Attachments[5].Data.Float', 8),
                    ('GD_IrisEpisode06Data.InteractiveObjects.MO_Iris_TASMission_Doors', 'BodyComposition.Attachments[8].Data.Float', 8),
                    ],
                ),
            ),
        Level('Torgue Arena (normal)', 'Iris_DL1_P',
            doors=Changes(
                interps=[
                    '# Trapdoor',
                    'Iris_DL1_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Iris_DL1_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                others=[
                    ('# Main arena door', None, None),
                    ('GD_IrisEpisode02Data.InteractiveObjects.MO_Iris_ArenaBattle1_Doors', 'BodyComposition.Attachments[0].Data.Float', 1.5),
                    ],
                ),
            ),
        ]),
    ('DLC 3 - Sir Hammerlock\'s Big Game Hunt', [
        Level('Ardorton Station', 'Sage_PowerStation_P',
            doors=Changes(
                interps=[
                    'Sage_PowerStation_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    # These require a bit more than our usual boost
                    ('Sage_PowerStation_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2', 2),
                    ('Sage_PowerStation_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3', 2),
                    ('Sage_PowerStation_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4', 2),
                    'Sage_PowerStation_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    ],
                ),
            ),
        Level('Candlerakk\'s Crag', 'Sage_Cliffs_P',
            doors=Changes(
                interps=[
                    'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            drawbridges=Changes(
                interps=[
                    'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            others=Changes(
                others=[
                    ('# Code entry wheels to H.S.S. Terminus', None, None),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel1', 'BodyComposition.Attachments[4].Data.Float', 0.5),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel1', 'BodyComposition.Attachments[10].Data.Float', 0.5),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel1:BehaviorProviderDefinition_0', 'BehaviorSequences[1].ConsolidatedOutputLinkData[8].ActivateDelay', 0.5),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel2', 'BodyComposition.Attachments[4].Data.Float', 0.5),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel2', 'BodyComposition.Attachments[10].Data.Float', 0.5),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel2:BehaviorProviderDefinition_0', 'BehaviorSequences[1].ConsolidatedOutputLinkData[4].ActivateDelay', 0.5),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel3', 'BodyComposition.Attachments[4].Data.Float', 0.5),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel3', 'BodyComposition.Attachments[10].Data.Float', 0.5),
                    ('GD_Sage_Ep5_Data.IO_Sage_Ep5_DoorWheel3:BehaviorProviderDefinition_0', 'BehaviorSequences[1].ConsolidatedOutputLinkData[10].ActivateDelay', 0.5),
                    ],
                ),
            ),
        Level('H.S.S. Terminus', 'Sage_HyperionShip_P',
            doors=Changes(
                interps=[
                    # This one controls some doors but also a *lot* of other stuff; going to leave it out for now.
                    #'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            ),
        Level('Hunter\'s Grotto', 'Sage_Underground_P',
            doors=Changes(
                interps=[
                    # Probably enemy-spawn-only
                    #'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    # I think this one might be the gate which leads to that elevator...
                    'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            others=Changes(
                raw=[
                    '# Hammerlock walking speed',
                    'GD_Sage_Hammerlock.Character.CharClass_Sage_Hammerlock GroundSpeed 440',
                    ],
                ),
            ),
        Level('Scylla\'s Grove', 'Sage_RockForest_P',
            lifts=Changes(
                interps=[
                    'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        ]),
    ('DLC 4 - Tiny Tina\'s Assault on Dragon Keep', [
        Level('Dark Forest', 'Dark_Forest_P',
            others=Changes(
                interps=[
                    '# Crumpets',
                    'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Crumpets.Cage_Crumpet.SeqAct_Interp_0',
                    'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Crumpets.Well_Crumpet.SeqAct_Interp_0',
                    'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Crumpets.Well_Crumpet.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Dragon Keep', 'CastleKeep_P',
            doors=Changes(
                interps=[
                    'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.FakeGateIO.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'CastleKeep_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Flamerock Refuge', 'Village_P',
            others=Changes(
                interps=[
                    '# Third question in Fake Geek Guy',
                    'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqAct_Interp_5',
                    'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqAct_Interp_8',
                    ],
                ),
            ),
        Level('Immortal Woods', 'Dead_Forest_P'),
        Level('Lair of Infinite Agony', 'Dungeon_P',
            doors=Changes(
                interps=[
                    '# Entrance to Winged Storm',
                    'Dungeon_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    ],
                ),
            ),
        Level('Mines of Avarice', 'Mines_P',
            others=Changes(
                interps=[
                    '# Crumpet cages',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Crumpets.Cages_0.SeqAct_Interp_2',
                    # I was concerned that speeding up the cube puzzle would make it more difficult, if you
                    # wanted to solve it the "proper" way, but it's actually nicer IMO.
                    '# Rubik\'s Cube Puzzle',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqAct_Interp_1',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqAct_Interp_15',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqAct_Interp_2',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqAct_Interp_3',
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqAct_Interp_9', 2),
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX1_Right.SeqAct_Interp_0',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX1_Right.SeqAct_Interp_2',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX1_Right.SeqAct_Interp_8',
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX1_Right.SeqAct_Interp_9', 2),
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX3_Left.SeqAct_Interp_0',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX3_Left.SeqAct_Interp_2',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX3_Left.SeqAct_Interp_8',
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX3_Left.SeqAct_Interp_9', 2),
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY1_Right.SeqAct_Interp_0',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY1_Right.SeqAct_Interp_2',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY1_Right.SeqAct_Interp_8',
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY1_Right.SeqAct_Interp_9', 2),
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY3_Left.SeqAct_Interp_0',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY3_Left.SeqAct_Interp_2',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY3_Left.SeqAct_Interp_8',
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY3_Left.SeqAct_Interp_9', 2),
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ1_Right.SeqAct_Interp_0',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ1_Right.SeqAct_Interp_2',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ1_Right.SeqAct_Interp_8',
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ1_Right.SeqAct_Interp_9', 2),
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ3_Left.SeqAct_Interp_0',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ3_Left.SeqAct_Interp_2',
                    'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ3_Left.SeqAct_Interp_8',
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ3_Left.SeqAct_Interp_9', 2),
                    ],
                others=[
                    # Play Rate for some animations in the cube puzzle, not sure exactly which.
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqVar_Float_1', 'FloatValue', 2, True),
                    # And *these* vars, I think, get copied over to that var, presumably for differences between showing the
                    # initial state and then solving it yourself.
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqVar_Float_2', 'FloatValue', 2, True),
                    # This second one is the faster value, presumably when solving it yourself.  The vanilla value is actually 4, not
                    # 2, but I think that'd be *too* fast otherwise.
                    ('Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqVar_Float_3', 'FloatValue', 2, True),
                    ],
                ),
            ),
        Level('Murderlin\'s Temple', 'TempleSlaughter_P',
            doors=Changes(
                interps=[
                    '# Only receiving half the usual boost because the associated rock bridge looks weird otherwise',
                    ('TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0', 0.5),
                    ],
                ),
            lifts=Changes(
                interps=[
                    'TempleSlaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            drawbridges=Changes(
                interps=[
                    '# Only receiving half the usual boost because it looks weird otherwise',
                    ('TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12', 0.5),
                    ],
                ),
            ),
        Level('Hatred\'s Shadow', 'CastleExterior_P',
            lifts=Changes(
                interps=[
                    'CastleExterior_P.TheWorld:PersistentLevel.Main_Sequence.Environment.SeqAct_Interp_3',
                    ],
                ),
            ),
        Level('Unassuming Docks', 'Docks_P'),
        Level('Winged Storm', 'DungeonRaid_P',
            doors=Changes(
                interps=[
                    '# Doors + Drawbridge immediately after fight',
                    'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    '# Exit door',
                    'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_13',
                    ],
                raw=[
                    # There's actually still a bit of a delay in here that I'd love to get rid of, but
                    # this is good enough.  Basically we're moving the ActivateRemoteEvent_0 call from
                    # SeqAct_Interp_12 to SeqEvent_RemoteEvent_13, so it doesn't wait for the initial
                    # lootsplosion stuff before firing.  Not that this really matters anyway, since this
                    # is one of the nicer lootsplosions to stick around for.  Even with auto-Eridium-pickup
                    # you wouldn't be able to finish collecting all of it before the vanilla drawbridge+gate
                    # timing happened.
                    '# Door and Drawbridge timing',
                    """DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13 OutputLinks
                    (
                        ( 
                            Links=( 
                                ( 
                                    LinkedOp=SeqAct_Interp'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12', 
                                    InputLinkIdx=0 
                                ) 
                            ), 
                            LinkDesc="Out", 
                            bHasImpulse=False, 
                            bDisabled=False, 
                            bDisabledPIE=False, 
                            bClampedMax=False, 
                            bClampedMin=False, 
                            bHidden=False, 
                            bIsActivated=False, 
                            bMoving=False, 
                            LinkedOp=None, 
                            ActivateDelay=3.500000 
                        ),
                        ( 
                            Links=( 
                                ( 
                                    LinkedOp=SeqAct_ActivateRemoteEvent'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_ActivateRemoteEvent_0', 
                                    InputLinkIdx=0 
                                ) 
                            ), 
                            LinkDesc="Completed", 
                            bHasImpulse=False, 
                            bDisabled=False, 
                            bDisabledPIE=False, 
                            bClampedMax=False, 
                            bClampedMin=False, 
                            bHidden=False, 
                            bIsActivated=False, 
                            bMoving=False, 
                            LinkedOp=None, 
                            ActivateDelay=0.000000 
                        )
                    )""",
                    # Presumably only one of `Links` or `bDisabled` would be Actually Needed here.
                    'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12 OutputLinks[0].Links ()',
                    'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12 OutputLinks[0].bDisabled True',
                    'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12 OutputLinks[0].bDisabledPIE True',
                    ],
                ),
            ),
        ]),
    ('DLC 5 - Commander Lilith and the Fight for Sanctuary', [
        Level('Backburner', 'Backburner_P',
            doors=Changes(
                interps=[
                    # These two gates are super-slow; buff 'em up more than usual
                    ('BackBUrner_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.Mission_000.SeqAct_Interp_1', 1.5),
                    ('BackBUrner_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.Mission_000.SeqAct_Interp_4', 1.5),
                    'BackBurner_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.HypocriticalOathPart1.SeqAct_Interp_1',
                    'BackBurner_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.HypocriticalOathPart2.SeqAct_Interp_2',
                    ],
                ),
            ),
        Level('Burrows', 'Sandworm_P',
            others=Changes(
                interps=[
                    '# The pipe Brick knocks over',
                    'Sandworm_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Dahl Abandon', 'OldDust_P',
            doors=Changes(
                interps=[
                    'OldDust_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.Mission_025.SeqAct_Interp_0',
                    'OldDust_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.Mission_050.SeqAct_Interp_0',
                    'OldDust_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SpaceCowboy.SeqAct_Interp_0',
                    'OldDust_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.Vaughnguard.SeqAct_Interp_1',
                    'OldDust_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.Vaughnguard.SeqAct_Interp_3',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'OldDust_Interactive.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            drawbridges=Changes(
                interps=[
                    'OldDust_LD.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            others=Changes(
                interps=[
                    # Only speeding this up by 60% of our usual buff, I think it'll look too weird otherwise.
                    '# Claptocurrency mining drill',
                    ('OldDust_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.Claptocurrency.SeqAct_Interp_1', 0.6),
                    ],
                ),
            ),
        Level('Fallen Helios', 'Helios_P',
            doors=Changes(
                interps=[
                    'Helios_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Helios_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    'Helios_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Helios_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    # This one is related to loading the small bomb into the big one
                    #'Helios_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Helios_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    'Helios_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.MyBrittlePony.SeqAct_Interp_0',
                    'Helios_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.MyBrittlePony.SeqAct_Interp_1',
                    'Helios_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.Sirentology.SeqAct_Interp_0',
                    'Helios_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.Sirentology.SeqAct_Interp_1',
                    'Helios_UranusArena.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Helios_LD.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Helios_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Helios_Mission_Main.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'Helios_UranusArena.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            ),
        Level('Fight for Sanctuary (intro map)', 'SanctIntro_P'),
        Level('Mt. Scarab Research Center', 'ResearchCenter_P',
            doors=Changes(
                interps=[
                    'ResearchCenter_Entrance.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'ResearchCenter_Interactive.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'ResearchCenter_Interactive.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'ResearchCenter_MissionMain.TheWorld:PersistentLevel.Main_Sequence.PlotMission050.SeqAct_Interp_0',
                    'ResearchCenter_MissionMain.TheWorld:PersistentLevel.Main_Sequence.PlotMission050.SeqAct_Interp_1',
                    'ResearchCenter_MissionMain.TheWorld:PersistentLevel.Main_Sequence.PlotMission050.SeqAct_Interp_2',
                    'ResearchCenter_MissionMain.TheWorld:PersistentLevel.Main_Sequence.PlotMission050.SeqAct_Interp_3',
                    'ResearchCenter_MissionMain.TheWorld:PersistentLevel.Main_Sequence.PlotMission050.SeqAct_Interp_4',
                    'ResearchCenter_MissionMain.TheWorld:PersistentLevel.Main_Sequence.PlotMission050.SeqAct_Interp_9',
                    'ResearchCenter_MissionSide.TheWorld:PersistentLevel.Main_Sequence.BFFFs.SeqAct_Interp_0',
                    ],
                ),
            ),
        Level('Paradise Sanctum', 'GaiusSanctuary_P',
            doors=Changes(
                interps=[
                    'GaiusSanctuary_MissionMain.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    ],
                ),
            ),
        Level('Writhing Deep', 'SandwormLair_P',
            lifts=Changes(
                interps=[
                    # Lift up to the summoning area.  The first one is going up, the second one is
                    # the trapdoor once the beat's been dropped.  We can't make the second one too
                    # fast or you don't have time to fall down to the arena, but it seems that if
                    # we don't buff *both* then you tend to fall through the elevator floor as soon
                    # as you get to the top, which is... weird.  Anyway, whatever.  This seems to
                    # work fine.
                    ('SandwormLair_Terrain.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1', 0.6),
                    ('SandwormLair_Terrain.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2', 0.6),
                    ],
                ),
            ),
        ]),
    ('Headhunter Packs', [
        Level('Gluttony Gulch (Headhunter Pack 2 - The Horrible Hunger of the Ravenous Wattle Gobbler)', 'Hunger_P',
            doors=Changes(
                interps=[
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_1',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_0',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_2',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_3',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_9',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.TorgueLockpickDoor.SeqAct_Interp_8',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.FirstTributeFight.SeqAct_Interp_0',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.GrabMeat.SeqAct_Interp_1',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.GrabMeat.SeqAct_Interp_6',
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.GrabMeat.SeqAct_Interp_7',
                    'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SecondTributeFight.SeqAct_Interp_5',
                    'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SecondTributeFight.SeqAct_Interp_7',
                    'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqAct_Interp_1',
                    'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqAct_Interp_4',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Matinees.SeqAct_Interp_2',
                    ],
                interpdata=[
                    '# Lifts to the arena (and arena forcefields)',
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.RunnableBoss.InterpData_4',
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.RunnableBoss.InterpData_2',
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.InterpData_0',
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.InterpData_5',
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.InterpData_6',
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.InterpData_7',
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.InterpData_8',
                    'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.InterpData_9',
                    ],
                ),
            others=Changes(
                others=[
                    ('# Speed up cooking process', None, None),
                    ('GD_Allium_TG_Plot_M01Data.IO_AlliumTG_CookTarget:BehaviorProviderDefinition_2.Behavior_Metronome_59', 'TickInterval', 0.9*(speed_scale/2)),
                    ],
                raw=[
                    'GD_Allium_TG_Plot_M01Data.IO_AlliumTG_CookTarget:BehaviorProviderDefinition_2 BehaviorSequences[1].BehaviorData2[14].LinkedVariables.ArrayIndexAndLength 0',
                    ],
                ),
            ),
        Level('Hallowed Hollow (Headhunter Pack 1 - T.K. Baha\'s Bloody Harvest)', 'Pumpkin_Patch_P',
            doors=Changes(
                interps=[
                    'PUMPKIN_PATCH_COMBAT.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'PUMPKIN_PATCH_COMBAT.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Blacksmith.SeqAct_Interp_3',
                    'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ChurchFires.SeqAct_Interp_2',
                    'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ChurchFires.SeqAct_Interp_8',
                    'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gate.SeqAct_Interp_0',
                    'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gate.SeqAct_Interp_1',
                    'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gate.SeqAct_Interp_2',
                    'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gate.SeqAct_Interp_3',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    ],
                )
            ),
        Level('Marcus\'s Mercenary Shop (Headhunter Pack 3 - How Marcus Saved Mercenary Day)', 'Xmas_P',
            doors=Changes(
                interps=[
                    'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_13',
                    'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_14',
                    'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    'Xmas_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_3',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Unloading coal from the train',
                    'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    '# Bells to summon Tinder Snowflake',
                    'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ],
                ),
            ),
        Level('Rotgut Distillery (Headhunter Pack 4 - Mad Moxxi and the Wedding Day Massacre)', 'Distillery_P',
            doors=Changes(
                interps=[
                    'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqAct_Interp_1',
                    'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqAct_Interp_6',
                    'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqAct_Interp_0',
                    'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqAct_Interp_1',
                    'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqAct_Interp_5',
                    'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqAct_Interp_7',
                    'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqAct_Interp_8',
                    'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.DespawnCouple.SeqAct_Interp_0',
                    'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.VanDoorInteraction.SeqAct_Interp_2',
                    'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.DistilleryCombat_LoaderChase.SeqAct_Interp_0',
                    'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.DistilleryCombat_LoaderChase.SeqAct_Interp_1',
                    'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.GoldenLoader.SeqAct_Interp_2',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    ],
                ),
            others=Changes(
                interps=[
                    '# Thresher fishing',
                    'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqAct_Interp_5',
                    ],
                others=[
                    ('# More Thresher fishing', None, None),
                    ('Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqVar_RandomFloat_1', 'Min', 0.5),
                    ('Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqVar_RandomFloat_1', 'Max', 2),
                    ('Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqVar_RandomFloat_2', 'Min', 0.5/2),
                    ('Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqVar_RandomFloat_2', 'Max', 5/2),
                    ('# Drinking animation', None, None),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot', 'AnimLength', 2.360302*2),
                    # These should really be handled by a split-off bit of `get_interpdata_tuples` but whatever...
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'PosTrack.Points[1].InVal', 0.524849*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'PosTrack.Points[2].InVal', 1.174849*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'PosTrack.Points[3].InVal', 1.852806*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'PosTrack.Points[4].InVal', 2.352806*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'EulerTrack.Points[1].InVal', 0.524849*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'EulerTrack.Points[2].InVal', 1.174849*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'EulerTrack.Points[3].InVal', 1.852806*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'EulerTrack.Points[4].InVal', 2.352806*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'LookupTrack.Time[1].InVal', 0.524849*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'LookupTrack.Time[2].InVal', 1.174849*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'LookupTrack.Time[3].InVal', 1.852806*2),
                    ('GD_Nast_VDay_Mission_Data.CamAnims.CamAnim_DrinkFromSpigot:InterpGroup_0.InterpTrackMove_0', 'LookupTrack.Time[4].InVal', 2.352806*2),
                    ],
                raw=[
                    '# More thresher fishing speedups',
                    'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqAct_RandomSwitch_0 LinkCount 1',
                    'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqAct_RandomSwitch_0 Indices (3)',
                    '# Speed up Ed, and remove proximity requirement',
                    'GD_Nast_BadassJunkLoader.Character.CharClass_Nast_BadassJunkLoader GroundSpeed 440',
                    'GD_Nast_BadassJunkLoader.Character.CharClass_Nast_BadassJunkLoader WalkingPct 1',
                    'GD_Nast_BadassJunkLoader.Character.AIDef_Nast_BadassJunkLoader:AIBehaviorProviderDefinition_0 BehaviorSequences[1].BehaviorData2[3].LinkedVariables.ArrayIndexAndLength 0',
                    'GD_Nast_BadassJunkLoader.Character.AIDef_Nast_BadassJunkLoader:AIBehaviorProviderDefinition_0.Behavior_CompareFloat_0 ValueA 0',
                    'GD_Nast_BadassJunkLoader.Character.AIDef_Nast_BadassJunkLoader:AIBehaviorProviderDefinition_0.Behavior_CompareFloat_0 ValueB 1',
                    ],
                ),
            ),
        Level('Wam Bam Island (Headhunter Pack 5 - Sir Hammerlock vs. the Son of Crawmerax)', 'Easter_P',
            doors=Changes(
                interps=[
                    'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_6',
                    # This one is Hammerlock opening the big ol' door - looks a bit silly if it gets any faster than this.
                    ('Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0', 0.5),
                    'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_18',
                    'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    ],
                others=[
                    # Not actually sure if this is doing anything here.  Whatever.
                    ('Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_0', 'FloatValue', 1/2, True)
                    ],
                ),
            lifts=Changes(
                interps=[
                    'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_7',
                    'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_8',
                    'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_9',
                    # The speed for these two is actually controlled by the SeqVar_Float, below.
                    #'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_11',
                    #'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_12',
                    'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_4',
                    ],
                others=[
                    ('Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqVar_Float_9', 'FloatValue', 0.5, True),
                    ],
                ),
            others=Changes(
                interps=[
                    '# Treasure injectors',
                    'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_0',
                    'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_1',
                    'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_2',
                    'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqAct_Interp_5',
                    ],
                ),
            ),
        ]),
    ('Others', [
        Level('Raid on Digistruct Peak', 'TestingZone_P',
            doors=Changes(
                interps=[
                    'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.Unlock_Door.SeqAct_Interp_1',
                    ],
                ),
            lifts=Changes(
                interps=[
                    'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.TestingZone.SeqAct_Interp_2',
                    'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.TestingZone.SeqAct_Interp_3',
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
lines.append("""BL2
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Speeds up nearly all objects that the player interacts with, by {speed_scale}x (mostly).
    # No more waiting for doors to open, elevators to ascend, overengineered Hyperion 
    # containers to unpack, or other such annoyances!
    #
    # Includes a mod graciously donated by Gronp, specifically "Faster Vehicle
    # Animations."  The original version of this mod has options for how much to
    # speed up the animations, so if you want to tweak those values, use Gronp's
    # version and make sure it appears after this one in your mod list:
    # https://www.nexusmods.com/borderlands2/mods/175

""".format(
    mod_name=mod_name,
    mod_version=mod_version,
    speed_scale=speed_scale,
    ))

# Containers
lines.append("""#<Containers>

        # Previously the standalone "BL2 Container TimeSaver XL" mod

        #<Improved Opening Speed>

            #<Most Containers>

                level None set Anim_Lootables.Animations.AnimTree_Lootables_Willow:WillowAnimNode_Simple_339 PlayRate {speed_scale}

                level None set Anim_Lootables.Animations.AnimTree_Lootables_Willow:WillowAnimNode_Simple_340 PlayRate {speed_scale}

                level None set Anim_Lootables.Animations.AnimTree_Lootables_Willow:WillowAnimNode_Simple_0 PlayRate {speed_scale}

            #</Most Containers>

            #<Golden Chest>

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_66 PlayRate {speed_scale}

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_339 PlayRate {speed_scale}

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_340 PlayRate {speed_scale}

                level None set GD_Balance_Treasure.Animations.AnimTree_Lootables_GoldenChest:WillowAnimNode_Simple_0 PlayRate {speed_scale}

            #</Golden Chest>

            #<Non-Mimic Mimic Chests>

                level None set GD_Aster_Lootables.AnimTrees.AnimTree_Lootables_Willow_LoopingOpenedIdle_Mimic:WillowAnimNode_Simple_8532 PlayRate {speed_scale}

                level None set GD_Aster_Lootables.AnimTrees.AnimTree_Lootables_Willow_LoopingOpenedIdle_Mimic:WillowAnimNode_Simple_339 PlayRate {speed_scale}

                level None set GD_Aster_Lootables.AnimTrees.AnimTree_Lootables_Willow_LoopingOpenedIdle_Mimic:WillowAnimNode_Simple_340 PlayRate {speed_scale}

                level None set GD_Aster_Lootables.AnimTrees.AnimTree_Lootables_Willow_LoopingOpenedIdle_Mimic:WillowAnimNode_Simple_0 PlayRate {speed_scale}

            #</Non-Mimic Mimic Chests>

            #<Dice Chests>

                #<Base PlayRate Tweaks>

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_239 PlayRate {speed_scale_1_25}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_239 PlayRate {speed_scale_1_25}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_720 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_721 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_722 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_723 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_724 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_725 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_726 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_727 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_728 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_729 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_730 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_731 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_732 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_733 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_734 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_735 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_736 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_737 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_738 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_D21:WillowAnimNode_Simple_739 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_720 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_721 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_722 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_723 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_724 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_725 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_726 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_727 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_728 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_729 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_730 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_731 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_732 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_733 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_734 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_735 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_736 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_737 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_738 PlayRate {speed_scale}

                    level None set Aster_Prop_Dice.AnimTree.AnimTree_DTwenty:WillowAnimNode_Simple_739 PlayRate {speed_scale}

                #</Base PlayRate Tweaks>

                #<Other Delay Tweaks>

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[70].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1.Behavior_Delay_251 Delay 0.4

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[45].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1.Behavior_Delay_250 Delay 0.4

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[101].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1.Behavior_Delay_255 Delay 0.8

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[93].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1.Behavior_Delay_252 Delay 0.8

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[96].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1.Behavior_Delay_253 Delay 0.2

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[99].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1.Behavior_Delay_254 Delay 0.1

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1 BehaviorSequences[3].BehaviorData2[36].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1.Behavior_Delay_77 Delay 0.2

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1 BehaviorSequences[3].BehaviorData2[0].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_DiceChest:BehaviorProviderDefinition_1.Behavior_Delay_76 Delay 0.27

                #</Other Delay Tweaks>

            #</Dice Chests>

            #<Digistruct Chests>

                #<Chest Digistruct Speed (only affects ammo chests)>

                    level None set GD_CoordinatedEffects.Digistruct_Chest EffectDuration 0.8

                #</Chest Digistruct Speed (only affects ammo chests)>

                #<Ammo Chests>

                    level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_HyperionAmmo_Digi:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[1].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_HyperionAmmo_Digi:BehaviorProviderDefinition_1.Behavior_Delay_1119 Delay 0.8

                    level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_HyperionAmmo_Digi:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[9].LinkedVariables.ArrayIndexAndLength 0

                    level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_HyperionAmmo_Digi:BehaviorProviderDefinition_1.Behavior_Delay_1120 Delay 0

                #</Ammo Chests>

                #<Weapon Chests (Digistruct Peak)>

                    # First: update the item spawn delay

                    level TestingZone_P set GD_Lobelia_DahlDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[0].LinkedVariables.ArrayIndexAndLength 0

                    level TestingZone_P set GD_Lobelia_DahlDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1.Behavior_Delay_278 Delay 0.0651264

                    # Next: switch the initial digistruct effect to TopDown (from Standard) and speed up TopDown.
                    # We do this because otherwise it shares the same effect as the enemies in the level, which
                    # will cause unwanted interactions

                    level TestingZone_P set GD_Lobelia_DahlDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1.Behavior_CoordinatedEffect_196 Effect CoordinatedEffectDefinition'GD_CoordinatedEffects.Digistruct_TopDown'

                    level TestingZone_P set GD_CoordinatedEffects.Digistruct_TopDown EffectDuration 1.333333

                    # Finally: trigger the opening anim stuff more quickly after the digistructing

                    level TestingZone_P set GD_Lobelia_DahlDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[14].LinkedVariables.ArrayIndexAndLength 0

                    level TestingZone_P set GD_Lobelia_DahlDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1.Behavior_Delay_279 Delay 1.333333

                #</Weapon Chests (Digistruct Peak)>

                #<Weapon Chests (Writhing Deep)>

                    level SandwormLair_P set GD_Anemone_Lobelia_DahDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[3].ActivateDelay 0.05

                #</Weapon Chests (Writhing Deep)>

                #<Chest Spawner Tweaks>

                    # This is what makes sure that the ammo spawners start their countdowns when appropriate.
                    # Note that the ammo spawners seem to basically all use the base game "Episode 17" spawner
                    # rather than create their own.

                    level None set GD_Episode17Data.InteractiveObjects.MO_Ep17_AmmoMachine:BehaviorProviderDefinition_0 BehaviorSequences[1].ConsolidatedOutputLinkData[5].ActivateDelay 0.8

                #</Chest Spawner Tweaks>

            #</Digistruct Chests>

        #</Improved Opening Speed>

        #<Items Available At Spawn>

            # These statements set chests to immediately allow attached items to be picked up
            # by the user.  Without these, many containers would result in un-pick-uppable
            # loot.

            level None set GD_Allium_Lootables.IOs.IO_Stove:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Allium_Lootables.IOs.IO_Xmas_Present:BehaviorProviderDefinition_1.Behavior_AttachItems_111 bDisablePickups False

            level None set GD_Aster_LootNinjaData.InteractiveObjects.InteractiveObj_StewChest:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_AmmoChest:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_CashChest:BehaviorProviderDefinition_1.Behavior_AttachItems_2 bDisablePickups False

            level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_MimicChest_NoMimic:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_BanditChest:BehaviorProviderDefinition_1.Behavior_AttachItems_2 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_BanditWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_172 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Ammo:BehaviorProviderDefinition_1.Behavior_AttachItems_39 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Cooler:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_CardboardBox:BehaviorProviderDefinition_1.Behavior_AttachItems_9 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Cashbox:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlAmmo:BehaviorProviderDefinition_1.Behavior_AttachItems_44 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlCooler:BehaviorProviderDefinition_1.Behavior_AttachItems_105 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlSmallBox:BehaviorProviderDefinition_1.Behavior_AttachItems_119 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_6 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Dumpster:BehaviorProviderDefinition_4.Behavior_AttachItems_134 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_216 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionAmmo:BehaviorProviderDefinition_1.Behavior_AttachItems_123 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionChest:BehaviorProviderDefinition_0.Behavior_AttachItems_78 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionMinibox:BehaviorProviderDefinition_1.Behavior_AttachItems_101 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionSmallbox:BehaviorProviderDefinition_1.Behavior_AttachItems_122 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_LaundryMachine:BehaviorProviderDefinition_10.Behavior_AttachItems_155 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Mailbox:BehaviorProviderDefinition_12.Behavior_AttachItems_161 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MailboxBandit:BehaviorProviderDefinition_12.Behavior_AttachItems_164 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MetalCrate:BehaviorProviderDefinition_1.Behavior_AttachItems_237 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MilitaryCrate:BehaviorProviderDefinition_1.Behavior_AttachItems_28 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MiniFridge:BehaviorProviderDefinition_11.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Safe:BehaviorProviderDefinition_1.Behavior_AttachItems_182 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StorageLocker:BehaviorProviderDefinition_0.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StrongBox:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Toilet:BehaviorProviderDefinition_0.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest:BehaviorProviderDefinition_1.Behavior_AttachItems_24 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Golden:BehaviorProviderDefinition_1.Behavior_AttachItems_4 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.BugMorph.InteractiveObj_Dumpster_BugMorph:BehaviorProviderDefinition_4.Behavior_AttachItems_136 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditCooler_MidgetBandit:BehaviorProviderDefinition_1.Behavior_AttachItems_56 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditWeaponChest_MidgetBandit:BehaviorProviderDefinition_1.Behavior_AttachItems_233 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_CardboardBox_MidgetBandit:BehaviorProviderDefinition_1.Behavior_AttachItems_67 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_Dumpster_MidgetBandit:BehaviorProviderDefinition_4.Behavior_AttachItems_140 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_LaundryMachine_MidgetBandit:BehaviorProviderDefinition_10.Behavior_AttachItems_139 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_MetalCrate_MidgetBandit:BehaviorProviderDefinition_1.Behavior_AttachItems_241 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_MilitaryCrate_MidgetBandit:BehaviorProviderDefinition_1.Behavior_AttachItems_61 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_StorageLocker_MidgetBandit:BehaviorProviderDefinition_0.Behavior_AttachItems_196 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_Toilet_MidgetBandit:BehaviorProviderDefinition_0.Behavior_AttachItems_226 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1.Behavior_AttachItems_32 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_CardboardBox_MidgetHyperion:BehaviorProviderDefinition_1.Behavior_AttachItems_4 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_Dumpster_MidgetHyperion:BehaviorProviderDefinition_4.Behavior_AttachItems_144 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_HyperionAmmo_MidgetHyperion:BehaviorProviderDefinition_1.Behavior_AttachItems_75 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_LaundryMachine_MidgetHyperion:BehaviorProviderDefinition_10.Behavior_AttachItems_143 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_MetalCrate_MidgetHyperion:BehaviorProviderDefinition_1.Behavior_AttachItems_245 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_MilitaryCrate_MidgetHyperion:BehaviorProviderDefinition_1.Behavior_AttachItems_65 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_StorageLocker_MidgetHyperion:BehaviorProviderDefinition_0.Behavior_AttachItems_202 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_Toilet_MidgetHyperion:BehaviorProviderDefinition_0.Behavior_AttachItems_230 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObj_EpicChest_Dahl_BigBoy:BehaviorProviderDefinition_1.Behavior_AttachItems_23 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObj_HypWeaponChestBot:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObject_HyperionAmmo_Digi:BehaviorProviderDefinition_1.Behavior_AttachItems_9 bDisablePickups False

            level None set GD_EasterEggs.InteractiveObjects.InteractiveObj_WhatsInTheBox:BehaviorProviderDefinition_1.Behavior_AttachItems_34 bDisablePickups False

            level None set GD_Iris_Balance_Treasure.InteractiveObjects.InteractiveObj_Iris_HyperionChest:BehaviorProviderDefinition_0.Behavior_AttachItems_6 bDisablePickups False

            level None set GD_Iris_ChallengeData.InteractiveObjects.IO_ChallengeChest:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Lobelia_DahlDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1.Behavior_AttachItems_8 bDisablePickups False

            level None set GD_Nasturtium_Lootables.InteractiveObjects.InteractiveObj_NastChest_Ammo:BehaviorProviderDefinition_1.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Nasturtium_Lootables.InteractiveObjects.InteractiveObj_NastChest_Epic:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Orchid_LevelChallenges.InteractiveObjects.IO_OasisChallenge_DahlWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_2 bDisablePickups False

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1.Behavior_AttachItems_49 bDisablePickups False

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1.Behavior_AttachItems_51 bDisablePickups False

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1.Behavior_AttachItems_2 bDisablePickups False

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Orchid_Flatbed_EpicChestRed:BehaviorProviderDefinition_1.Behavior_AttachItems_6 bDisablePickups False

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_Ammo:BehaviorProviderDefinition_1.Behavior_AttachItems_4 bDisablePickups False

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_EndGame:BehaviorProviderDefinition_1.Behavior_AttachItems_10 bDisablePickups False

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_Epic:BehaviorProviderDefinition_1.Behavior_AttachItems_13 bDisablePickups False

            level None set GD_Sage_Lootables.InteractiveObjects.InteractiveObj_HyperionChest_EndGame:BehaviorProviderDefinition_1.Behavior_AttachItems_8 bDisablePickups False

            level None set GD_Sage_Lootables.InteractiveObjects.InteractiveObj_TribalChest:BehaviorProviderDefinition_1.Behavior_AttachItems_32 bDisablePickups False

            level None set GD_Sage_Lootables.InteractiveObjects.InteractiveObj_TribalHyperionBox:BehaviorProviderDefinition_1.Behavior_AttachItems_11 bDisablePickups False

            level None set GD_Z3_CustomerServiceData.InteractiveObjects.CustomerService_Mailbox:BehaviorProviderDefinition_12.Behavior_AttachItems_3 bDisablePickups False

            level None set GD_Z3_LostTreasureData.InteractiveObjects.InteractiveObj_CardboardBox_LTstart:BehaviorProviderDefinition_1.Behavior_AttachItems_19 bDisablePickups False

            level None set GD_Z3_UncleTeddyData.InteractiveObjects.InteractiveObj_StorageLocker_UncleTeddy:BehaviorProviderDefinition_0.Behavior_AttachItems_0 bDisablePickups False

            level None set gd_z2_notetoselfdata.InteractiveObjects.IO_NoteToSelf_Chest:BehaviorProviderDefinition_1.Behavior_AttachItems_27 bDisablePickups False

            level None set GD_Anemone_Lobelia_DahDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1.Behavior_AttachItems_26 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_DahlAmmo_MidgetBandit:BehaviorProviderDefinition_1.Behavior_AttachItems_91 bDisablePickups False

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_DahlAmmo_MidgetHyperion:BehaviorProviderDefinition_1.Behavior_AttachItems_93 bDisablePickups False

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditChest:BehaviorProviderDefinition_1.Behavior_AttachItems_4 bDisablePickups False

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_8 bDisablePickups False

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1.Behavior_AttachItems_0 bDisablePickups False

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest:BehaviorProviderDefinition_1.Behavior_AttachItems_7 bDisablePickups False

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_HyperionChest:BehaviorProviderDefinition_0.Behavior_AttachItems_1 bDisablePickups False

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_MetalCrate:BehaviorProviderDefinition_1.Behavior_AttachItems_6 bDisablePickups False

        #</Items Available At Spawn>

        #<Item Spawn Delay>

            # This changes the containers to immediately spawn loot instead of, as is usual, waiting
            # for a small delay (which is typically to wait for animations to be in the "proper" state.

            level None set GD_Allium_Lootables.IOs.IO_Stove:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[3].ActivateDelay 0

            level None set GD_Allium_Lootables.IOs.IO_Xmas_Present:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[4].ActivateDelay 0

            level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_AmmoChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_CashChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_MimicChest_NoMimic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[4].ActivateDelay 0

            level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_MimicChest_NoMimic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[5].ActivateDelay 0

            level None set GD_Aster_Lootables.InteractiveObjects.InteractiveObj_MimicChest_NoMimic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[7].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Ammo:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Bandit_Cooler:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_CardboardBox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Cashbox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlAmmo:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlCooler:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlSmallBox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_DahlWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Dumpster:BehaviorProviderDefinition_4 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionMinibox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_HyperionSmallbox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_LaundryMachine:BehaviorProviderDefinition_10 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Mailbox:BehaviorProviderDefinition_12 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MetalCrate:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MilitaryCrate:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_MiniFridge:BehaviorProviderDefinition_11 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StorageLocker:BehaviorProviderDefinition_0 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_StrongBox:BehaviorProviderDefinition_1 BehaviorSequences[5].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_Toilet:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Golden:BehaviorProviderDefinition_1 BehaviorSequences[5].ConsolidatedOutputLinkData[1].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.BugMorph.InteractiveObj_Dumpster_BugMorph:BehaviorProviderDefinition_4 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.04

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditCooler_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[3].ActivateDelay 0.144

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditCooler_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[4].ActivateDelay 0.2

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditCooler_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[6].ActivateDelay 0.16

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditWeaponChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[3].ActivateDelay 0.1

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditWeaponChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[7].ActivateDelay 0.34

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditWeaponChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[0].ActivateDelay 0.2

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_BanditWeaponChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.2

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_CardboardBox_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[3].ActivateDelay 0.094

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_CardboardBox_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_Dumpster_MidgetBandit:BehaviorProviderDefinition_4 BehaviorSequences[2].ConsolidatedOutputLinkData[5].ActivateDelay 0.07

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_Dumpster_MidgetBandit:BehaviorProviderDefinition_4 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.04

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_LaundryMachine_MidgetBandit:BehaviorProviderDefinition_10 BehaviorSequences[2].ConsolidatedOutputLinkData[7].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_LaundryMachine_MidgetBandit:BehaviorProviderDefinition_10 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_MetalCrate_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[3].ActivateDelay 0.27

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_MetalCrate_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.26

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_MilitaryCrate_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[5].ActivateDelay 0.1

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_MilitaryCrate_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[6].ActivateDelay 0.07

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_MilitaryCrate_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_StorageLocker_MidgetBandit:BehaviorProviderDefinition_0 BehaviorSequences[2].ConsolidatedOutputLinkData[4].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_StorageLocker_MidgetBandit:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.035

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_Toilet_MidgetBandit:BehaviorProviderDefinition_0 BehaviorSequences[0].ConsolidatedOutputLinkData[6].ActivateDelay 0.06

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_Toilet_MidgetBandit:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.035

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[1].ActivateDelay 0.04

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[2].ActivateDelay 0.02

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[3].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[4].ActivateDelay 0.07

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[8].ActivateDelay 0.23

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[10].ActivateDelay 0.24

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[11].ActivateDelay 0.4

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_TreasureChest_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.27

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_CardboardBox_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[4].ActivateDelay 0.094

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_CardboardBox_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[4].ActivateDelay 0.1

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_CardboardBox_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_Dumpster_MidgetHyperion:BehaviorProviderDefinition_4 BehaviorSequences[2].ConsolidatedOutputLinkData[5].ActivateDelay 0.07

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_Dumpster_MidgetHyperion:BehaviorProviderDefinition_4 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.04

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_HyperionAmmo_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[7].ActivateDelay 0.1

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_LaundryMachine_MidgetHyperion:BehaviorProviderDefinition_10 BehaviorSequences[2].ConsolidatedOutputLinkData[7].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_LaundryMachine_MidgetHyperion:BehaviorProviderDefinition_10 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_MetalCrate_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[5].ActivateDelay 0.3

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_MetalCrate_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.26

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_MilitaryCrate_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[5].ActivateDelay 0.1

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_MilitaryCrate_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[6].ActivateDelay 0.07

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_MilitaryCrate_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.05

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_StorageLocker_MidgetHyperion:BehaviorProviderDefinition_0 BehaviorSequences[2].ConsolidatedOutputLinkData[3].ActivateDelay 0.06

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_StorageLocker_MidgetHyperion:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.035

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_Toilet_MidgetHyperion:BehaviorProviderDefinition_0 BehaviorSequences[0].ConsolidatedOutputLinkData[6].ActivateDelay 0.06

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_Toilet_MidgetHyperion:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.035

            level None set GD_Balance_Treasure.InteractiveObjectsUnique.InteractiveObj_EpicChest_Dahl_BigBoy:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Iris_ChallengeData.InteractiveObjects.IO_ChallengeChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Nasturtium_Lootables.InteractiveObjects.InteractiveObj_NastChest_Ammo:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Nasturtium_Lootables.InteractiveObjects.InteractiveObj_NastChest_Epic:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[1].ActivateDelay 0.156

            level None set GD_Nasturtium_Lootables.InteractiveObjects.InteractiveObj_NastChest_Epic:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[2].ActivateDelay 0.24

            level None set GD_Nasturtium_Lootables.InteractiveObjects.InteractiveObj_NastChest_Epic:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[7].ActivateDelay 0.23

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[2].ActivateDelay 0.156

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[3].ActivateDelay 0.24

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[6].ActivateDelay 0.23

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[7].ActivateDelay 0.04

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[8].ActivateDelay 0.02

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[9].ActivateDelay 0.05

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[10].ActivateDelay 0.07

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[3].ActivateDelay 0.23

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[6].ActivateDelay 0.04

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[7].ActivateDelay 0.02

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[8].ActivateDelay 0.05

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[9].ActivateDelay 0.07

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[11].ActivateDelay 0.156

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[12].ActivateDelay 0.24

            level None set GD_Orchid_PlotDataMission04.Mission04.IO_Orchid_CompassPiece2:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[18].ActivateDelay 0.4

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[1].ActivateDelay 0.04

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[2].ActivateDelay 0.02

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[3].ActivateDelay 0.05

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[4].ActivateDelay 0.07

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[8].ActivateDelay 0.23

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[11].ActivateDelay 0.156

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[12].ActivateDelay 0.24

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[3].ActivateDelay 0.23

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[8].ActivateDelay 0.156

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[9].ActivateDelay 0.24

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[13].ActivateDelay 0.04

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[14].ActivateDelay 0.02

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[15].ActivateDelay 0.05

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Flatbed_PirateChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[16].ActivateDelay 0.07

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_Orchid_Flatbed_EpicChestRed:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[9].ActivateDelay 0

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_Ammo:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_EndGame:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[9].ActivateDelay 0

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_EndGame:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[11].ActivateDelay 0

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_EndGame:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[12].ActivateDelay 0

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_Epic:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[3].ActivateDelay 0

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_Epic:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[4].ActivateDelay 0

            level None set GD_Orchid_TreasureChests.InteractiveObjects.InteractiveObj_PirateChest_Epic:BehaviorProviderDefinition_1 BehaviorSequences[0].ConsolidatedOutputLinkData[5].ActivateDelay 0

            level None set GD_Sage_Lootables.InteractiveObjects.InteractiveObj_TribalHyperionBox:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Z3_UncleTeddyData.InteractiveObjects.InteractiveObj_StorageLocker_UncleTeddy:BehaviorProviderDefinition_0 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Allium_Lootables.IOs.IO_LootCar:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBoth.InteractiveObj_BanditWeaponChest_MidgetBoth:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[4].ActivateDelay 0.1

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBoth.InteractiveObj_BanditWeaponChest_MidgetBoth:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[9].ActivateDelay 0.34

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBoth.InteractiveObj_BanditWeaponChest_MidgetBoth:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[0].ActivateDelay 0.2

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_DahlAmmo_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[6].ActivateDelay 0.06

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetBandit.InteractiveObj_DahlAmmo_MidgetBandit:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.08

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_DahlAmmo_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[6].ActivateDelay 0.06

            level None set GD_Balance_Treasure.InteractiveObjectsTrap.MidgetHyperion.InteractiveObj_DahlAmmo_MidgetHyperion:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.08

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[1].ActivateDelay 0.04

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[2].ActivateDelay 0.02

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[3].ActivateDelay 0.05

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[4].ActivateDelay 0.07

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[8].ActivateDelay 0.7

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[5].ActivateDelay 0.34

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[0].ActivateDelay 0.2

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_BanditWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.2

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[0].ActivateDelay 0.04

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[1].ActivateDelay 0.02

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[2].ActivateDelay 0.05

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[3].ActivateDelay 0.07

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[8].ActivateDelay 0.116

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[2].ConsolidatedOutputLinkData[10].ActivateDelay 0.6

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_DahlEpic:BehaviorProviderDefinition_1 BehaviorSequences[4].ConsolidatedOutputLinkData[2].ActivateDelay 0.14

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_HypWeaponChest:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.05

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_HyperionChest:BehaviorProviderDefinition_0 BehaviorSequences[3].ConsolidatedOutputLinkData[3].ActivateDelay 0.3

            level None set GD_Anemone_Treasure.InteractiveObjects.InteractiveObj_MetalCrate:BehaviorProviderDefinition_1 BehaviorSequences[3].ConsolidatedOutputLinkData[2].ActivateDelay 0.26

        #</Item Spawn Delay>

        #<Faster Mimic Speed>

            # Since we're buffing the Non-Mimic Mimic chests, we may as well speed up
            # the Chest->Mimic transition as well, just so it matches.  As it is, I'm
            # not *actually* sure if any of this really does much.  There's still a
            # tiny delay before the Mimic actually starts attacking you.  Ah well!

            level None set GD_MimicShared.Anims.Anim_Mimic_Chest_To_Mimic PlayRate 3.75

            level None set GD_MimicShared.Anims.Anim_Mimic_Chest_To_Mimic TimedBehaviorEvents[0].Time 0.096

            level None set GD_Mimic.Character.AIDef_Mimic:AIBehaviorProviderDefinition_0 BehaviorSequences[0].ConsolidatedOutputLinkData[8].ActivateDelay 0.04

            level None set GD_Mimic.Character.AIDef_Mimic:AIBehaviorProviderDefinition_0 BehaviorSequences[0].ConsolidatedOutputLinkData[11].ActivateDelay 0.1

        #</Faster Mimic Speed>

    #</Containers>
""".format(
    speed_scale=speed_scale,
    speed_scale_1_25=speed_scale*1.25,
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

# Drawbridges
lines.append('#<Drawbridges>')
lines.append('')
for (dlc_name, levels) in dlcs:
    if any([l.has_drawbridges_data() for l in levels]):
        lines.append('#<{}>'.format(dlc_name))
        lines.append('')
        for level in levels:
            level.process_drawbridges(speed_scale, lines)
        lines.append('#</{}>'.format(dlc_name))
        lines.append('')
lines.append('#</Drawbridges>')
lines.append('')

# Fast Travel
lines.append("""#<Fast Travel Stations>

    # Speeds up opening of Fast Travel stations.  Mostly so that if you start
    # your game at the Highlands (Overlook), Three Horns Valley, or Hunter's
    # Grotto (Lodge) stations, you don't have to wait for the opening
    # animation to use the FT network.
    #
    # Formerly the standalone "BL2 Fast Travel TimeSaver XL" mod

    level None set GD_GameSystemMachines.SpecialMoves.SpecialMove_FastTravelClosedToOpen PlayRate {speed_scale}

    level None set GD_GameSystemMachines.SpecialMoves.SpecialMove_FastTravelClosedToOpenBroken PlayRate {speed_scale}

    level None set GD_GameSystemMachines.InteractiveObjects.FastTravelMachine:BehaviorProviderDefinition_4 BehaviorSequences[2].ConsolidatedOutputLinkData[4].ActivateDelay 0

    level None set GD_GameSystemMachines.InteractiveObjects.FastTravelMachine:BehaviorProviderDefinition_4 BehaviorSequences[2].ConsolidatedOutputLinkData[7].ActivateDelay 0

    level None set GD_GameSystemMachines.InteractiveObjects.FastTravelMachine:BehaviorProviderDefinition_4 BehaviorSequences[2].ConsolidatedOutputLinkData[6].ActivateDelay 0.2

    level None set GD_GameSystemMachines.InteractiveObjects.FastTravelMachine:BehaviorProviderDefinition_4 BehaviorSequences[2].ConsolidatedOutputLinkData[2].ActivateDelay 0.2

    level None set GD_GameSystemMachines.InteractiveObjects.FastTravelMachine:BehaviorProviderDefinition_4 BehaviorSequences[2].ConsolidatedOutputLinkData[3].ActivateDelay 0.2

#</Fast Travel Stations>
""".format(speed_scale=speed_scale))

# Lifts
lines.append('#<Lifts / Elevators / Transporters>')
lines.append('')
lines.append('    # This includes things like the horizontal raft thing in Southern Shelf - Bay,')
lines.append('    # and the tram system in Highlands Outwash.')
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

# Slot Machines
bpd_slots_scale = slots_scale/2
lines.append("""#<Slot Machines>

    # There are a lot of variables at play with these -- the speedup for all slot
    # machines should be about {bpd_slots_scale}x overall.

    #<Shared Animations>

        level None set gd_slotmachine.Animation.Anim_PullHandle PlayRate {slots_scale}

        level None set gd_slotmachine.Animation.Anim_SpinEnd PlayRate {slots_scale}

        level None set gd_slotmachine.Animation.Anim_SpinLoop PlayRate {slots_scale}

        level None set gd_slotmachine.Animation.AnimTree_SlotMachine:WillowAnimNode_Simple_75 PlayRate {slots_scale}

        level None set gd_slotmachine.Animation.AnimTree_SlotMachine:WillowAnimNode_Simple_89 PlayRate {slots_scale}

    #</Shared Animations>

    #<Base Game Slot Machines>
""".format(
    slots_scale=slots_scale,
    bpd_slots_scale=bpd_slots_scale,
    ))

for cmd in delay_bpd('gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0', bpd_slots_scale, delay_overrides={
        # These are vars are usually set dynamically by the engine -- we can't trust the in-data values
        # to do the math with.
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_83': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_84': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_85': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_87': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_88': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_89': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_90': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_91': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_95': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_96': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_97': 5/bpd_slots_scale,
        'gd_slotmachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_99': 5/bpd_slots_scale,
        },
        # We need this full delay between the door opening and spawning the grenade
        skip_cold={(1, 86)}):
    lines.append('level None {}'.format(cmd))
    lines.append('')

lines.append('#</Base Game Slot Machines>')
lines.append('')
lines.append('#<Torgue Token Slot Machines>')
lines.append('')

for cmd in delay_bpd('GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0', bpd_slots_scale, delay_overrides={
        # These are vars are usually set dynamically by the engine -- we can't trust the in-data values
        # to do the math with.
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4407': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4408': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4409': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4410': (5/bpd_slots_scale)*1.2,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4411': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4412': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4413': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4418': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4419': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4420': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4421': 5/bpd_slots_scale,
        'GD_Iris_SlotMachine.Iris_SlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_4422': 5/bpd_slots_scale,
        },
        # We need this full delay between the door opening and spawning the grenade
        skip_cold={(1, 36)}):
    lines.append('level Iris_Moxxi_P {}'.format(cmd))
    lines.append('')

lines.append('#</Torgue Token Slot Machines>')
lines.append('')
lines.append('#<Tiny Tina Slot Machines>')
lines.append('')

for cmd in delay_bpd('GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0', bpd_slots_scale, delay_overrides={
        # These are vars are usually set dynamically by the engine -- we can't trust the in-data values
        # to do the math with.
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1540': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1537': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1534': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1546': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1558': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1543': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1571': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1544': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1572': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1545': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1568': 5/bpd_slots_scale,
        'GD_Aster_EridiumSlotMachine.EridiumSlotMachine:BehaviorProviderDefinition_0.Behavior_Delay_1569': 5/bpd_slots_scale,
        }):
    lines.append('level Village_P {}'.format(cmd))
    lines.append('')

lines.append('#</Tiny Tina Slot Machines>')
lines.append('')
lines.append('#</Slot Machines>')
lines.append('')

# Vehicle Animations
vehicles = [
        ('Bandit Technical',
            ['GD_BTech_Streaming'],
            [
                'GD_BanditTechnical.Animations.CrewAnim_DriverEnterFront',
                'GD_BanditTechnical.Animations.CrewAnim_DriverEnterLeft',
                'GD_BanditTechnical.Animations.CrewAnim_DriverExitLeft',
                'GD_BanditTechnical.Animations.CrewAnim_TurretEnterRight',
                'GD_BanditTechnical.Animations.CrewAnim_TurretExitRight',
                'GD_BanditTechnical.Animations.CrewAnim_BackseatEnterLeft',
                'GD_BanditTechnical.Animations.CrewAnim_BackseatExitLeft',
                'GD_BanditTechnical.Animations.CrewAnim_BackseatEnterRight',
                'GD_BanditTechnical.Animations.CrewAnim_BackseatExitRight',
                'GD_BanditTechnical.Animations.CrewAnim_SwitchToDriver',
                'GD_BanditTechnical.Animations.CrewAnim_SwitchToTurret',
                'GD_BanditTechnical.Animations.CrewAnim_BackseatSwitchToLeft',
                'GD_BanditTechnical.Animations.CrewAnim_BackseatSwitchToRight',
            ]),
        ('Fan Boat',
            ['GD_Sage_ShockFanBoat', 'GD_Sage_CorrosiveFanBoat', 'GD_Sage_IncendiaryFanBoat'],
            [
                'GD_Sage_FanBoat.Animations.CrewAnim_DriverEnterLeft',
                'GD_Sage_FanBoat.Animations.CrewAnim_DriverEnterRight',
                'GD_Sage_FanBoat.Animations.CrewAnim_DriverExitRight',
                'GD_Sage_FanBoat.Animations.CrewAnim_DriverExitLeft',
                'GD_Sage_FanBoat.Animations.CrewAnim_TurretEnterLeft',
                'GD_Sage_FanBoat.Animations.CrewAnim_TurretEnterRight',
                'GD_Sage_FanBoat.Animations.CrewAnim_TurretExitLeft',
                'GD_Sage_FanBoat.Animations.CrewAnim_TurretExitRight',
                'GD_Sage_FanBoat.Animations.CrewAnim_SwitchToDriver',
                'GD_Sage_FanBoat.Animations.CrewAnim_SwitchToTurret',
            ]),
        ('Hovercraft / Skiff',
            ['GD_Orchid_HarpoonHovercraft', 'GD_Orchid_RocketHovercraft', 'GD_Orchid_SawHovercraft'],
            [
                'GD_Orchid_Hovercraft.Animations.CrewAnim_DriverEnterLeft',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_DriverEnterRight',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_DriverExitLeft',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_DriverExitRight',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_TurretEnterLeft',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_TurretEnterRight',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_TurretExitLeft',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_TurretExitRight',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_SwitchToDriver',
                'GD_Orchid_Hovercraft.Animations.CrewAnim_SwitchToTurret',
            ]),
        ('Runner',
            ['GD_Runner_Streaming'],
            [
                'GD_Runner_Streaming.Animations.CrewAnim_DriverEnter_Front',
                'GD_Runner_Streaming.Animations.CrewAnim_DriverEnter_Left',
                'GD_Runner_Streaming.Animations.CrewAnim_DriverEnter_Right',
                'GD_Runner_Streaming.Animations.CrewAnim_DriverExit_Right',
                'GD_Runner_Streaming.Animations.CrewAnim_DriverExit_Left',
                'GD_Runner_Streaming.Animations.CrewAnim_TurretEnter_Left',
                'GD_Runner_Streaming.Animations.CrewAnim_TurretEnter_Right',
                'GD_Runner_Streaming.Animations.CrewAnim_TurretExit_Left',
                'GD_Runner_Streaming.Animations.CrewAnim_TurretExit_Right',
                'GD_Runner_Streaming.Animations.CrewAnim_Turret_From_Driver',
                'GD_Runner_Streaming.Animations.CrewAnim_Driver_From_Turret',
            ]),
        ]
lines.append("""#<Vehicle Animations>

    # Vehicle Animations (such as characters entering, leaving, or changing seats)
    # are only getting a {vehicle_anim_speed_scale}x boost, since they look pretty weird if faster.
    #
    # This is a direct copy from Gronp\'s "Faster Vehicle Animations," used with permission.
    # https://www.nexusmods.com/borderlands2/mods/175
    # Many thanks!

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
