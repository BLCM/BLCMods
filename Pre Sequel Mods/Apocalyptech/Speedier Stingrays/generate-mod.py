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

mod_name = 'Speedier Stingrays'
mod_version = '1.1.0'
output_filename = '{}.blcm'.format(mod_name)

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

    hotfix_strings[label] = """{prefix_label}#<{label} Stingray>

{prefix}demand {demand_name} set {vehicle_name} MaxSpeed 3400

{prefix}demand {demand_name} set {vehicle_name} FullAirSpeed 4000

{prefix}demand {demand_name} set {class_name} AfterburnerSpeed 14000

{prefix}demand {demand_name} set {class_name} AfterburnerForceMagnitude 200

{prefix}demand {demand_name} set {class_name} AfterburnerBoostTime 3.5

{prefix}demand {demand_name} set {class_name} AfterburnerImpulse.Z 32500

{prefix_label}#</{label} Stingray>""".format(
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
    # Improves the speed of both varieties of stingrays.  They were already
    # quite good, but this makes them even better.

{flak}

{cryo}

    #<Common Attributes>

        demand {demand_name} set {afterburner_name} BaseMaxValue.BaseValueConstant 45

        demand {demand_name} set {afterburner_name} BaseOnIdleRegenerationRate 25

        demand {demand_name} set {afterburner_name} BaseOnIdleRegenerationDelay 1.2

        demand {demand_name} set {handling_name} MaxThrustForce 1600

        demand {demand_name} set {handling_name} MaxReverseForce 1600

        demand {demand_name} set {handling_name} MaxStrafeForce 2000

        demand {demand_name} set {handling_name} TurnTorqueMax 4000

    #</Common Attributes>

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        flak=hotfix_strings['Flak Cannon'],
        cryo=hotfix_strings['Cryo Rocket'],
        demand_name=demand_name,
        afterburner_name=afterburner_name,
        handling_name=handling_name,
        )

###
### Output to a file.
###

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
