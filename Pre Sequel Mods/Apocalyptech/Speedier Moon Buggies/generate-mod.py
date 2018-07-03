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

# Python script to generate my Speedier Moon Buggies mod

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

mod_name = 'Speedier Moon Buggies'
mod_version = '1.0.0'
output_filename = '{}.txt'.format(mod_name)

###
### Generate hotfixes!
###

hotfix_strings = {}

demand_name = 'GD_MoonBuggy_Streaming'
handling_name = 'GD_MoonBuggy_Streaming.Handling.HandlingDef_MoonBuggy'
afterburner_name = 'GD_MoonBuggy_Streaming.ResourcePools.AfterburnerPool_MoonBuggy'
prefix_label = ' '*(4*1)
prefix = ' '*(4*2)
for (label, vehicle_name, class_name) in [
        ('Laser',
            'GD_MoonBuggy_Streaming.Archetype.Vehicle_MoonBuggy_Laser',
            'GD_MoonBuggy_Streaming.Archetype.Class_MoonBuggy_Laser',
            ),
        ('Missile Pod',
            'GD_MoonBuggy_Streaming.Archetype.Vehicle_MoonBuggy_MissilePod',
            'GD_MoonBuggy_Streaming.Archetype.Class_MoonBuggy_MissilePod',
            ),
        ]:

    hfs = Hotfixes(nameprefix=label)

    # Default: 4500
    hfs.add_demand_hotfix('max_speed', 'MoonBuggy',
        '{},{},MaxSpeed,,8000'.format(demand_name, vehicle_name))

    # Default: 5000
    hfs.add_demand_hotfix('ground_speed', 'MoonBuggy',
        '{},{},GroundSpeed,,6000'.format(demand_name, vehicle_name))

    # Default: 5000
    hfs.add_demand_hotfix('ground_speed_base', 'MoonBuggy',
        '{},{},GroundSpeedBaseValue,,6000'.format(demand_name, vehicle_name))

    # Default: 2000
    hfs.add_demand_hotfix('afterburner_speed', 'MoonBuggy',
        '{},{},AfterburnerSpeed,,4000'.format(demand_name, class_name))

    # Default: 900
    hfs.add_demand_hotfix('afterburner_activation_speed', 'MoonBuggy',
        '{},{},AfterburnerActivationSpeed,,400'.format(demand_name, class_name))

    # Default: 700
    hfs.add_demand_hotfix('afterburner_force', 'MoonBuggy',
        '{},{},AfterburnerForceMagnitude,,1800'.format(demand_name, class_name))

    # Default: 4
    # (actually, y'know what?  Let's just leave that.  4 already feels generous enough.
    # We're improving the regen rate below.  That'll do.)
    #hfs.add_demand_hotfix('afterburner_boost_time', 'MoonBuggy',
    #    '{},{},AfterburnerBoostTime,,4'.format(demand_name, class_name))

    hotfix_strings[label] = """{prefix_label}#<{label} Moon Buggy>

{prefix}{hotfixes:max_speed}

{prefix}{hotfixes:ground_speed}

{prefix}{hotfixes:ground_speed_base}

{prefix}{hotfixes:afterburner_speed}

{prefix}{hotfixes:afterburner_activation_speed}

{prefix}{hotfixes:afterburner_force}

{prefix_label}#</{label} Moon Buggy>""".format(
        prefix_label=prefix_label,
        prefix=prefix,
        label=label,
        hotfixes=hfs,
        )

###
### Common Hotfixes
###

hfs = Hotfixes(nameprefix=label)

# Default: 100
hfs.add_demand_hotfix('afterburner_total', 'MoonBuggy',
    '{},{},BaseMaxValue.BaseValueConstant,,150'.format(demand_name, afterburner_name))

# Default: 20
hfs.add_demand_hotfix('afterburner_regen_rate', 'MoonBuggy',
    '{},{},BaseOnIdleRegenerationRate,,30'.format(demand_name, afterburner_name))

# Default: 5
hfs.add_demand_hotfix('afterburner_regen_delay', 'MoonBuggy',
    '{},{},BaseOnIdleRegenerationDelay,,2.5'.format(demand_name, afterburner_name))

# Default: 0.75
hfs.add_demand_hotfix('throttle_speed', 'MoonBuggy',
    '{},{},ThrottleSpeed,,10'.format(demand_name, handling_name))

# Default: -0.2
hfs.add_demand_hotfix('reverse_throttle', 'MoonBuggy',
    '{},{},ReverseThrottle,,-10'.format(demand_name, handling_name))

# Default: 10
hfs.add_demand_hotfix('brake_torque', 'MoonBuggy',
    '{},{},MaxBrakeTorque,,15'.format(demand_name, handling_name))

###
### Generate the mod string
###

mod_str = """#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Improves the speed of both varieties of moon buggies, mostly just so they
    # have an easier time making the couple of jumps in the early game.

{laser}

{missile}

    #<Common Attributes>

        {hotfixes:afterburner_total}

        {hotfixes:afterburner_regen_rate}

        {hotfixes:afterburner_regen_delay}

        {hotfixes:throttle_speed}

        {hotfixes:reverse_throttle}

        {hotfixes:brake_torque}

    #</Common Attributes>

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        laser=hotfix_strings['Laser'],
        missile=hotfix_strings['Missile Pod'],
        hotfixes=hfs,
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
