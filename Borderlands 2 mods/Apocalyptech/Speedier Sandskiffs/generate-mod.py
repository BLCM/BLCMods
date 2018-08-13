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

###
### Output variables
###

mod_name = 'Speedier Sandskiffs'
mod_version = '1.1.0'
output_filename = '{}.blcm'.format(mod_name)

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

    hotfix_strings[label] = """{prefix_label}#<{label} Skiff>

{prefix}demand {demand_name} set {vehicle_name} MaxSpeed 7000

{prefix}demand {demand_name} set {vehicle_name} FlyingSpeed 4000

{prefix}demand {demand_name} set {class_name} AfterburnerSpeed 7000

{prefix}demand {demand_name} set {class_name} AfterburnerActivationSpeed 250

{prefix}demand {demand_name} set {class_name} AfterburnerBoostTime 25

{prefix}demand {demand_name} set {handling_name} ThrottleSpeed 100

{prefix}demand {demand_name} set {afterburner_name} BaseMaxValue.BaseValueConstant 200

{prefix}demand {demand_name} set {afterburner_name} BaseOnIdleRegenerationRate 50

{prefix}demand {demand_name} set {afterburner_name} BaseOnIdleRegenerationDelay 2

{prefix_label}#</{label} Skiff>""".format(
        prefix_label=prefix_label,
        prefix=prefix,
        label=label,
        demand_name=demand_name,
        vehicle_name=vehicle_name,
        class_name=class_name,
        handling_name=handling_name,
        afterburner_name=afterburner_name,
        )

###
### Generate the mod string
###

mod_str = """BL2
#<{mod_name}>

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

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
