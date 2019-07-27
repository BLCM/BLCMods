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

# Control Vars
mod_name = 'BL2 Improved Hyperion Stabilizers'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

weapon_info = [
        ('Pistols', 0, -7, [
            'GD_Weap_Pistol.Body.Pistol_Body_Hyperion',
            'GD_Weap_Pistol.Body.Pistol_Body_Hyperion_2',
            'GD_Weap_Pistol.Body.Pistol_Body_Hyperion_3',
            'GD_Weap_Pistol.Body.Pistol_Body_Hyperion_4',
            ]),
        ('Shotguns', 0, -3, [
            'GD_Weap_Shotgun.Body.SG_Body_Hyperion',
            'GD_Weap_Shotgun.Body.SG_Body_Hyperion_2',
            'GD_Weap_Shotgun.Body.SG_Body_Hyperion_3',
            [
                'GD_Weap_Shotgun.Body.SG_Body_Hyperion_4',
                'GD_Gladiolus_Weapons.Shotgun.SG_Body_Hyperion_6',
                'GD_Anemone_Weapons.Shotgun.Overcompensator.SG_Body_Hyperion_Overcompensator',
            ]]),
        ('SMGs', 0, -9, [
            [
                'GD_Weap_SMG.Body.SMG_Body_Hyperion',
                'GD_Weap_SMG.Body.SMG_Body_Gearbox_1',
            ],
            'GD_Weap_SMG.Body.SMG_Body_Hyperion_VarA',
            'GD_Weap_SMG.Body.SMG_Body_Hyperion_VarB',
            'GD_Weap_SMG.Body.SMG_Body_Hyperion_VarC',
            ]),
        ('Sniper Rifles', -2, -10, [
            'GD_Weap_SniperRifles.Body.SR_Body_Hyperion',
            'GD_Weap_SniperRifles.Body.SR_Body_Hyperion_2',
            'GD_Weap_SniperRifles.Body.SR_Body_Hyperion_3',
            'GD_Weap_SniperRifles.Body.SR_Body_Hyperion_4',
            ]),
        ]

# Construct the mod
lines = []
lines.append('BL2')
lines.append('#<{}>'.format(mod_name))
lines.append('')
lines.append('    # {} v{}'.format(mod_name, mod_version))
lines.append('    # by Apocalyptech')
lines.append('    # Licensed under Public Domain / CC0 1.0 Universal')
lines.append('    #')
lines.append('    # Vastly improves the starting accuracy of Hyperion weapons, and')
lines.append('    # the time it takes for them to achieve peak accuracy.')
lines.append('')
lines.append('    #<Global Changes>')
lines.append('')
lines.append('        # This just lets Hyperion sniper rifles achieve even better accuracy once')
lines.append("        # they've reached the end of their reverse-recoil chain")
lines.append('')
lines.append('        level None set GD_Weap_SniperRifles.A_Weapons.WeaponType_Hyperion_Sniper ExternalAttributeEffects[0].BaseModifierValue.BaseValueConstant -1')
lines.append('')
lines.append('    #</Global Changes>')
lines.append('')
lines.append('    #<Choose Improvement Level><mut>')
lines.append('')
lines.append('        #<All Rarities Receive Maximum Improvement>')
lines.append('')
for (gun_name, start_preadd, target_preadd, bodies) in weapon_info:
    lines.append('    #<{}>'.format(gun_name))
    lines.append('')
    to_set = target_preadd - start_preadd
    for body in bodies:
        if isinstance(body, list):
            to_process = body
        else:
            to_process = [body]
        for body in to_process:
            lines.append("""        set {} ExternalAttributeEffects
            (
                (
                    AttributeToModify = ResourcePoolAttributeDefinition'D_Attributes.AccuracyResourcePool.AccuracyMaxValue',
                    ModifierType = MT_PreAdd,
                    BaseModifierValue =
                    (
                        BaseValueConstant = {:0.6f},
                        BaseValueAttribute = None,
                        InitializationDefinition = None,
                        BaseValueScaleConstant = 1.000000
                    )
                )
            )""".format(
                body,
                to_set,
                ))
            lines.append('')
    lines.append('    #</{}>'.format(gun_name))
    lines.append('')
lines.append('        #</All Rarities Receive Maximum Improvement>')
lines.append('')
lines.append('        #<Lower Rarities Receive Less Improvement>')
lines.append('')
for (gun_name, start_preadd, target_preadd, bodies) in weapon_info:
    lines.append('    #<{}>'.format(gun_name))
    lines.append('')
    real_target = target_preadd - start_preadd
    interval = real_target / len(bodies)
    for (idx, body) in enumerate(bodies):
        if isinstance(body, list):
            to_process = body
        else:
            to_process = [body]
        for body in to_process:
            lines.append("""        set {} ExternalAttributeEffects
            (
                (
                    AttributeToModify = ResourcePoolAttributeDefinition'D_Attributes.AccuracyResourcePool.AccuracyMaxValue',
                    ModifierType = MT_PreAdd,
                    BaseModifierValue =
                    (
                        BaseValueConstant = {:0.6f},
                        BaseValueAttribute = None,
                        InitializationDefinition = None,
                        BaseValueScaleConstant = 1.000000
                    )
                )
            )""".format(
                body,
                (idx+1)*interval,
                ))
            lines.append('')
    lines.append('    #</{}>'.format(gun_name))
    lines.append('')
lines.append('        #</Lower Rarities Receive Less Improvement>')
lines.append('')
lines.append('    #</Choose Improvement Level>')
lines.append('')
lines.append('')
lines.append('#</{}>'.format(mod_name))

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))
