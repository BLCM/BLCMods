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

# Python script to generate my Speedier Stingrays mod

import sys

try:
    from hotfixes import Hotfixes
except ModuleNotFoundError:
    print('')
    print('****************************************************************')
    print('To run this script, you will need to copy or symlink hotfixes.py')
    print('from the parent directory, so it exists here as well.  Sorry for')
    print('the bother!')
    print('****************************************************************')
    print('')
    sys.exit(1)

###
### Output variables
###

mod_name = 'Speedier Stingrays'
mod_version = '1.0.0'
output_filename = '{}.txt'.format(mod_name)

###
### Generate hotfixes!
###

hotfix_strings = {}

demand_name = 'GD_Co_StingRay_Streaming'
handling_name = 'GD_Co_StingRay_Streaming.Handling.Handling_StingRay'
afterburner_name = 'GD_Co_StingRay_Streaming.ResourcePools.AfterburnerPool_StingRay'
prefix_label = ' '*(4*1)
prefix = ' '*(4*2)
for (label, vehicle_name, class_name) in [
        ('Flak Cannon',
            'GD_Co_StingRay_Streaming.Archetype.Vehicle_StingRay_FlakBurst',
            'GD_Co_StingRay_Streaming.Archetype.Class_StingRay_FlakBurst',
            ),
        ('Cryo Rocket',
            'GD_Co_StingRay_Streaming.Archetype.Vehicle_StingRay_CryoRocket',
            'GD_Co_StingRay_Streaming.Archetype.Class_StingRay_CryoRocket',
            ),
        ]:

    hfs = Hotfixes(nameprefix=label)

    # Default: 2400
    hfs.add_demand_hotfix('max_speed', 'Stingray',
        '{},{},MaxSpeed,,3400'.format(demand_name, vehicle_name))

    # Default: 3000
    hfs.add_demand_hotfix('full_air_speed', 'Stingray',
        '{},{},FullAirSpeed,,4000'.format(demand_name, vehicle_name))

    # Default: 10000
    hfs.add_demand_hotfix('afterburner_speed', 'Stingray',
        '{},{},AfterburnerSpeed,,14000'.format(demand_name, class_name))

    # Default: 150
    hfs.add_demand_hotfix('afterburner_force', 'Stingray',
        '{},{},AfterburnerForceMagnitude,,200'.format(demand_name, class_name))

    # Default: 2
    hfs.add_demand_hotfix('afterburner_boost_time', 'Stingray',
        '{},{},AfterburnerBoostTime,,3.5'.format(demand_name, class_name))

    # Default: 27500
    hfs.add_demand_hotfix('afterburner_impulse_z', 'Stingray',
        '{},{},AfterburnerImpulse.Z,,32500'.format(demand_name, class_name))

    hotfix_strings[label] = """{prefix_label}#<{label} Stingray>

{prefix}{hotfixes:max_speed}

{prefix}{hotfixes:full_air_speed}

{prefix}{hotfixes:afterburner_speed}

{prefix}{hotfixes:afterburner_force}

{prefix}{hotfixes:afterburner_boost_time}

{prefix}{hotfixes:afterburner_impulse_z}

{prefix_label}#</{label} Stingray>""".format(
        prefix_label=prefix_label,
        prefix=prefix,
        label=label,
        hotfixes=hfs,
        )

###
### Common Hotfixes
###

hfs = Hotfixes(nameprefix=label)

# Default: 30
hfs.add_demand_hotfix('afterburner_total', 'Stingray',
    '{},{},BaseMaxValue.BaseValueConstant,,45'.format(demand_name, afterburner_name))

# Default: 20
hfs.add_demand_hotfix('afterburner_regen_rate', 'Stingray',
    '{},{},BaseOnIdleRegenerationRate,,25'.format(demand_name, afterburner_name))

# Default: 1.5
hfs.add_demand_hotfix('afterburner_regen_delay', 'Stingray',
    '{},{},BaseOnIdleRegenerationDelay,,1.2'.format(demand_name, afterburner_name))

# Default: 800
hfs.add_demand_hotfix('thrust_forward', 'Stingray',
    '{},{},MaxThrustForce,,1600'.format(demand_name, handling_name))

# Default: 800
hfs.add_demand_hotfix('thrust_reverse', 'Stingray',
    '{},{},MaxReverseForce,,1600'.format(demand_name, handling_name))

# Default: 1050
hfs.add_demand_hotfix('thrust_side', 'Stingray',
    '{},{},MaxStrafeForce,,2000'.format(demand_name, handling_name))

# Default: 2000
hfs.add_demand_hotfix('turn_torque', 'Stingray',
    '{},{},TurnTorqueMax,,4000'.format(demand_name, handling_name))

###
### Generate the mod string
###

mod_str = """#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Improves the speed of both varieties of stingrays.  They were already
    # quite good, but this makes them even better.

{flak}

{cryo}

    #<Common Attributes>

        {hotfixes:afterburner_total}

        {hotfixes:afterburner_regen_rate}

        {hotfixes:afterburner_regen_delay}

        {hotfixes:thrust_forward}

        {hotfixes:thrust_reverse}

        {hotfixes:thrust_side}

        {hotfixes:turn_torque}

    #</Common Attributes>

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        flak=hotfix_strings['Flak Cannon'],
        cryo=hotfix_strings['Cryo Rocket'],
        hotfixes=hfs,
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
