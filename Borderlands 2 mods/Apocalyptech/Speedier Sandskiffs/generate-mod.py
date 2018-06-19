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

# Python script to generate my Speedier Sandskiffs

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

mod_name = 'Speedier Sandskiffs'
mod_version = '1.0.0'
output_filename = '{}.txt'.format(mod_name)

###
### Generate hotfixes!
###

hotfix_strings = {}

handling_name = 'GD_Orchid_Hovercraft.Handling.HandlingDef_Hovercraft'
afterburner_name = 'GD_Orchid_Hovercraft.ResourcePools.AfterburnerPool_Hovercraft'
prefix_label = ' '*(4*1)
prefix = ' '*(4*2)
for (label, demand_name, vehicle_name, class_name) in [
        ('Harpoon',
            'GD_Orchid_HarpoonHovercraft',
            'GD_Orchid_HarpoonHovercraft.Archetype.Vehicle_HarpoonHovercraft',
            'GD_Orchid_HarpoonHovercraft.ClassDefinition.Class_HarpoonHovercraft',
            ),
        ('Rocket',
            'GD_Orchid_RocketHovercraft',
            'GD_Orchid_RocketHovercraft.Archetype.Vehicle_RocketHovercraft',
            'GD_Orchid_RocketHovercraft.ClassDefinition.Class_RocketHovercraft',
            ),
        ('Sawblade',
            'GD_Orchid_SawHovercraft',
            'GD_Orchid_SawHovercraft.Archetype.Vehicle_SawBladeHovercraft',
            'GD_Orchid_SawHovercraft.ClassDefinition.Class_SawBladeHovercraft',
            ),
        ]:

    hfs = Hotfixes(nameprefix=label)

    hfs.add_demand_hotfix('max_speed', 'Skiff',
        '{},{},MaxSpeed,,7000'.format(demand_name, vehicle_name))

    hfs.add_demand_hotfix('flying_speed', 'Skiff',
        '{},{},FlyingSpeed,,4000'.format(demand_name, vehicle_name))

    hfs.add_demand_hotfix('afterburner_speed', 'Skiff',
        '{},{},AfterburnerSpeed,,7000'.format(demand_name, class_name))

    hfs.add_demand_hotfix('afterburner_activation_speed', 'Skiff',
        '{},{},AfterburnerActivationSpeed,,250'.format(demand_name, class_name))

    hfs.add_demand_hotfix('afterburner_boost_time', 'Skiff',
        '{},{},AfterburnerBoostTime,,25'.format(demand_name, class_name))

    hfs.add_demand_hotfix('throttle_speed', 'Skiff',
        '{},{},ThrottleSpeed,,100'.format(demand_name, handling_name))

    hfs.add_demand_hotfix('afterburner_total', 'Skiff',
        '{},{},BaseMaxValue.BaseValueConstant,,200'.format(demand_name, afterburner_name))

    hfs.add_demand_hotfix('afterburner_regen_rate', 'Skiff',
        '{},{},BaseOnIdleRegenerationRate,,50'.format(demand_name, afterburner_name))

    hfs.add_demand_hotfix('afterburner_regen_delay', 'Skiff',
        '{},{},BaseOnIdleRegenerationDelay,,2'.format(demand_name, afterburner_name))

    hotfix_strings[label] = """{prefix_label}#<{label} Skiff>

{prefix}{hotfixes:max_speed}

{prefix}{hotfixes:flying_speed}

{prefix}{hotfixes:afterburner_speed}

{prefix}{hotfixes:afterburner_activation_speed}

{prefix}{hotfixes:afterburner_boost_time}

{prefix}{hotfixes:throttle_speed}

{prefix}{hotfixes:afterburner_total}

{prefix}{hotfixes:afterburner_regen_rate}

{prefix}{hotfixes:afterburner_regen_delay}

{prefix_label}#</{label} Skiff>""".format(
        prefix_label=prefix_label,
        prefix=prefix,
        label=label,
        hotfixes=hfs,
        )

###
### Generate the mod string
###

mod_str = """#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Improves the speed of all varieties of sandskiffs.  They were already
    # pretty good, honestly, but this makes them better.

{harpoon}

{rocket}

{saw}

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        harpoon=hotfix_strings['Harpoon'],
        rocket=hotfix_strings['Rocket'],
        saw=hotfix_strings['Sawblade'],
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
