#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2018, CJ Kucera
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

# Python script to generate my Configurable Catch-A-Ride mod

import sys

try:
    from modprocessor import ModProcessor
except ModuleNotFoundError:
    print('')
    print('********************************************************************')
    print('To run this script, you will need to copy or symlink modprocessor.py')
    print('from the parent directory, so it exists here as well.  Sorry for')
    print('the bother!')
    print('********************************************************************')
    print('')
    sys.exit(1)

###
### Output variables
###

mod_name = 'Configurable Catch-A-Ride'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

###
### Support classes
###

class Vehicle(object):

    def __init__(self, vehicle_id, label, ingame_label,
            station_class, vehicle_class):
        self.vehicle_id = vehicle_id
        self.label = label
        self.ingame_label = ingame_label
        self.station_class = station_class
        self.vehicle_class = vehicle_class

    def get_set(self, prefix, on_station):
        retlist = []
        p = ' '*4

        if self.label[0].lower() in 'aeiou':
            article = 'an'
        else:
            article = 'a'
        
        retlist.append('#<Spawn {} {}>'.format(article, self.label))
        retlist.append('{}set {} VehicleName {}'.format(
            p, on_station.station_class, self.ingame_label,
            ))
        retlist.append('{}level None set {} PathToVSSDefinition {}'.format(
            p, on_station.station_class, self.vehicle_class,
            ))
        retlist.append('#</Spawn {} {}>'.format(article, self.label))

        # Return
        return ['{}{}'.format(prefix, s) for s in retlist]

class Vehicles(object):

    def __init__(self, prefix):
        self.prefix = prefix
        self.vehicle_dict = {}
        self.vehicle_list = []

    def add_vehicle(self, vehicle):
        self.vehicle_dict[vehicle.vehicle_id] = vehicle
        self.vehicle_list.append(vehicle)

    def __getitem__(self, key):
        return self.vehicle_dict[key]

    def __format__(self, formatstr):
        vehicle = self.vehicle_dict[formatstr]
        p = ' '*4
        retlist = []
        retlist.append('#<{}><MUT>'.format(vehicle.label))
        retlist.extend(vehicle.get_set(p, vehicle))
        for v2 in self.vehicle_list:
            if v2 != vehicle:
                retlist.extend(v2.get_set(p, vehicle))
        retlist.append('#</{}>'.format(vehicle.label))
        return "\n\n".join(['{}{}'.format(self.prefix, s) for s in retlist])

###
### Vehicles
###

vehicles = Vehicles(prefix=' '*(4))
vehicles.add_vehicle(Vehicle('runnermg',
        'Runner (Machine Gun)', 'Light Runner MG',
        'GD_Globals.VehicleSpawnStation.VSSUI_MGRunner',
        'GD_Runner_Streaming.VSS.VSS_MGLightRunner'
        ))
vehicles.add_vehicle(Vehicle('runnerrocket',
        'Runner (Rocket)', 'Light Runner Rocket Launcher',
        'GD_Globals.VehicleSpawnStation.VSSUI_RocketRunner',
        'GD_Runner_Streaming.VSS.VSS_RocketRunner'
        ))
vehicles.add_vehicle(Vehicle('technicalsaw',
        'Technical (Sawblade)', 'Sawblade Technical',
        'GD_Globals.VehicleSpawnStation.VSSUI_SawBladeTechnical',
        'GD_BTech_Streaming.VSS.VSS_SawBladeTechnical'
        ))
vehicles.add_vehicle(Vehicle('technicalcat',
        'Technical (Catapult)', 'Catapult Technical',
        'GD_Globals.VehicleSpawnStation.VSSUI_CatapultTechnical',
        'GD_BTech_Streaming.VSS.VSS_CatapultTechnical'
        ))
vehicles.add_vehicle(Vehicle('skiffrocket',
        'Sandskiff (Rocket)', 'Rocket Hovercraft',
        'GD_OrchidPackageDef.Vehicles.VSSUI_RocketHovercraft',
        'GD_Orchid_RocketHovercraft.VSS.VSS_RocketHovercraft'
        ))
vehicles.add_vehicle(Vehicle('skiffharpoon',
        'Sandskiff (Harpoon)', 'Harpoon Hovercraft',
        'GD_OrchidPackageDef.Vehicles.VSSUI_HarpoonHovercraft',
        'GD_Orchid_HarpoonHovercraft.VSS.VSS_HarpoonHovercraft'
        ))
vehicles.add_vehicle(Vehicle('skiffsaw',
        'Sandskiff (Sawblade)', 'Saw Blade Hovercraft',
        'GD_OrchidPackageDef.Vehicles.VSSUI_SawBladeHovercraft',
        'GD_Orchid_SawHovercraft.VSS.VSS_SawBladeHovercraft'
        ))
vehicles.add_vehicle(Vehicle('boatcorrosive',
        'Fan Boat (Corrosive)', 'Corrosive Fan Boat',
        'GD_SagePackageDef.Vehicles.VSSUI_CorrosiveFanBoat',
        'GD_Sage_CorrosiveFanBoat.VSS.VSS_CorrosiveFanBoat'
        ))
vehicles.add_vehicle(Vehicle('boatfire',
        'Fan Boat (Incendiary)', 'Flamethrower Fan Boat',
        'GD_SagePackageDef.Vehicles.VSSUI_IncendiaryFanBoat',
        'GD_Sage_IncendiaryFanBoat.VSS.VSS_IncendiaryFanBoat'
        ))
vehicles.add_vehicle(Vehicle('boatshock',
        'Fan Boat (Shock)', 'Shock Fan Boat',
        'GD_SagePackageDef.Vehicles.VSSUI_ShockFanBoat',
        'GD_Sage_ShockFanBoat.VSS.VSS_ShockFanBoat'
        ))

###
### Generate the mod string
###

mod_str = """BL2
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by FromDarkHell + Apocalyptech
    #
    # Configure catch-a-ride spawns.  Any of the vehicle-spawn slots can be changed
    # to spawn any vehicle.  The default configuration is exactly the same as the
    # game's stock Catch-A-Ride presets.
    #
    # Note that skins for spawned vehicles won't work if they're changed from their
    # default settings.

{vehicles:runnermg}

{vehicles:runnerrocket}

{vehicles:technicalsaw}

{vehicles:technicalcat}

{vehicles:skiffrocket}

{vehicles:skiffharpoon}

{vehicles:skiffsaw}

{vehicles:boatcorrosive}

{vehicles:boatfire}

{vehicles:boatshock}

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        vehicles=vehicles,
        )

###
### Output to a file.
###

mp = ModProcessor()
mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
