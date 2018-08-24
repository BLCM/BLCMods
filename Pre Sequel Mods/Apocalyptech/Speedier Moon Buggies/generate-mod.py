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

mod_name = 'Speedier Moon Buggies'
mod_version = '1.1.0'
output_filename = '{}.blcm'.format(mod_name)

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

    hotfix_strings[label] = """{prefix_label}#<{label} Moon Buggy>

{prefix}demand {demand_name} set {vehicle_name} MaxSpeed 8000

{prefix}demand {demand_name} set {vehicle_name} GroundSpeed 6000

{prefix}demand {demand_name} set {vehicle_name} GroundSpeedBaseValue 6000

{prefix}demand {demand_name} set {class_name} AfterburnerSpeed 4000

{prefix}demand {demand_name} set {class_name} AfterburnerActivationSpeed 400

{prefix}demand {demand_name} set {class_name} AfterburnerForceMagnitude 1800

{prefix_label}#</{label} Moon Buggy>""".format(
        prefix_label=prefix_label,
        prefix=prefix,
        label=label,
        demand_name=demand_name,
        vehicle_name=vehicle_name,
        class_name=class_name,
        )

###
### Generate the mod string
###

mod_str = """TPS
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Improves the speed of both varieties of moon buggies, mostly just so they
    # have an easier time making the couple of jumps in the early game.

{laser}

{missile}

    #<Common Attributes>

        demand {demand_name} set {afterburner_name} BaseMaxValue.BaseValueConstant 150

        demand {demand_name} set {afterburner_name} BaseOnIdleRegenerationRate 30

        demand {demand_name} set {afterburner_name} BaseOnIdleRegenerationDelay 2.5

        demand {demand_name} set {handling_name} ThrottleSpeed 10

        demand {demand_name} set {handling_name} ReverseThrottle -10

        demand {demand_name} set {handling_name} MaxBrakeTorque 15

    #</Common Attributes>

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        laser=hotfix_strings['Laser'],
        missile=hotfix_strings['Missile Pod'],
        demand_name=demand_name,
        afterburner_name=afterburner_name,
        handling_name=handling_name,
        )

###
### Output to a file.
###

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
