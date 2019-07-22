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
mod_name = 'TPS Improved Hyperion Stabilizers'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

# TPS Max Accuracy starts at 9, rather than BL2's 12, so we have to account for that
weapon_info = [
        # Doing Lasers isn't worth it -- they really don't behave much differently
        # from all other lasers.  Plus they already had a -6 to AccuracyMax.
        #('Lasers', -6, -7, [
        #    'GD_Cork_Weap_Lasers.Body.Laser_Body_Hyperion',
        #    'GD_Cork_Weap_Lasers.Body.Laser_Body_Hyperion_2',
        #    [
        #        'GD_Cork_Weap_Lasers.Body.Laser_Body_Hyperion_3',
        #        'GD_Cork_Weap_Lasers.Body.Laser_Body_Hyperion_3_Mining',
        #    ],
        #    'GD_Cork_Weap_Lasers.Body.Laser_Body_Hyperion_4',
        #    ],
        #    (0, 0), (1, 1), [
        #    ]),
        ('Pistols', 0, -5, [
            'GD_Weap_Pistol.Body.Pistol_Body_Hyperion',
            'GD_Weap_Pistol.Body.Pistol_Body_Hyperion_2',
            'GD_Weap_Pistol.Body.Pistol_Body_Hyperion_3',
            'GD_Weap_Pistol.Body.Pistol_Body_Hyperion_4',
            ],
            (0.4, 0), (1.7, 1.4), [
                'GD_Weap_Pistol.ManufacturerMaterials.Mat_Old_Hyperion_1',
                'GD_Weap_Pistol.ManufacturerMaterials.Mat_Old_Hyperion_2',
                'GD_Weap_Pistol.ManufacturerMaterials.Mat_Old_Hyperion_3',
                'GD_Weap_Pistol.ManufacturerMaterials.Mat_Old_Hyperion_4',
            ],
            ),
        ('Shotguns', 0, -1, [
            'GD_Weap_Shotgun.Body.SG_Body_Hyperion',
            'GD_Weap_Shotgun.Body.SG_Body_Hyperion_2',
            'GD_Weap_Shotgun.Body.SG_Body_Hyperion_3',
            'GD_Weap_Shotgun.Body.SG_Body_Hyperion_4',
            ],
            (0.4, 0), (1.7, 1.4), [
                'GD_Weap_Shotgun.ManufacturerMaterials.Mat_Old_Hyperion_1',
                'GD_Weap_Shotgun.ManufacturerMaterials.Mat_Old_Hyperion_2',
                'GD_Weap_Shotgun.ManufacturerMaterials.Mat_Old_Hyperion_3',
                'GD_Weap_Shotgun.ManufacturerMaterials.Mat_Old_Hyperion_4',
            ]),
        ('SMGs', 0, -6, [
            [
                'GD_Weap_SMG.Body.SMG_Body_Hyperion',
                'GD_Weap_SMG.Body.SMG_Body_Gearbox_1',
            ],
            'GD_Weap_SMG.Body.SMG_Body_Hyperion_VarA',
            [
                'GD_Weap_SMG.Body.SMG_Body_Hyperion_VarB',
                'GD_Cork_Weap_SMG.Body.SMG_Body_Hyperion_BlackSnake',
            ],
            'GD_Weap_SMG.Body.SMG_Body_Hyperion_VarC',
            ],
            (0.4, 0), (1.7, 1.4), [
                'GD_Weap_SMG.ManufacturerMaterials.Mat_Old_Hyperion_1',
                'GD_Weap_SMG.ManufacturerMaterials.Mat_Old_Hyperion_2',
                [
                    'GD_Weap_SMG.ManufacturerMaterials.Mat_Old_Hyperion_3',
                    'GD_Cork_Weap_SMG.ManufacturerMaterials.Mat_Old_Hyperion_3_BlackSnake',
                ],
                'GD_Weap_SMG.ManufacturerMaterials.Mat_Old_Hyperion_4',
            ]),
        ('Sniper Rifles', -2, -7, [
            'GD_Weap_SniperRifles.Body.SR_Body_Hyperion',
            'GD_Weap_SniperRifles.Body.SR_Body_Hyperion_2',
            'GD_Weap_SniperRifles.Body.SR_Body_Hyperion_3',
            'GD_Weap_SniperRifles.Body.SR_Body_Hyperion_4',
            ],
            (0.2, 0), (None, None), [
                'GD_Weap_SniperRifles.ManufacturerMaterials.Material_Old_Hyperion_1',
                'GD_Weap_SniperRifles.ManufacturerMaterials.Material_Old_Hyperion_2',
                'GD_Weap_SniperRifles.ManufacturerMaterials.Material_Old_Hyperion_3',
                'GD_Weap_SniperRifles.ManufacturerMaterials.Material_Old_Hyperion_4',
            ]),
        ]

# Construct the mod
lines = []
lines.append("""TPS
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Vastly improves the starting accuracy of Hyperion weapons, and
    # the time it takes for them to achieve peak accuracy.

    #<Global Changes>

       #<Sniper Rifles>

            # This just lets Hyperion sniper rifles achieve even better accuracy once
            # they've reached the end of their reverse-recoil chain"

            level None set GD_Weap_SniperRifles.A_Weapons.WeaponType_Hyperion_Sniper ExternalAttributeEffects[0].BaseModifierValue.BaseValueConstant -1

        #</Sniper Rifles>

    #</Global Changes>

    #<Choose Improvement Level><mut>

""".format(mod_name=mod_name, mod_version=mod_version))

lines.append('        #<All Rarities Receive Maximum Improvement>')
lines.append('')
for (gun_name,
        start_preadd, target_preadd,
        bodies,
        (old_max_worst, old_max_best),
        (old_min_worst, old_min_best),
        materials,
        ) in weapon_info:
    lines.append('    #<{}>'.format(gun_name))
    lines.append('')

    # Main buffs
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

    # Material changes for Old Hyperion (nerfs, technically, but less than stock)
    for mat in materials:
        if isinstance(mat, list):
            to_process = mat
        else:
            to_process = [mat]
        for mat in to_process:
            lines.append('            level None set {} ExternalAttributeEffects[0].BaseModifierValue.BaseValueConstant {}'.format(
                mat,
                old_max_best,
                ))
            lines.append('')
            lines.append('            level None set {} ExternalAttributeEffects[0].ModifierType MT_PreAdd'.format(
                mat,
                ))
            lines.append('')
            if old_min_worst is not None:
                lines.append('            level None set {} ExternalAttributeEffects[1].BaseModifierValue.BaseValueConstant {}'.format(
                    mat,
                    old_min_best,
                    ))
                lines.append('')

    lines.append('    #</{}>'.format(gun_name))
    lines.append('')

lines.append('        #</All Rarities Receive Maximum Improvement>')
lines.append('')
lines.append('        #<Lower Rarities Receive Less Improvement>')
lines.append('')
for (gun_name,
        start_preadd, target_preadd,
        bodies,
        (old_max_worst, old_max_best),
        (old_min_worst, old_min_best),
        materials,
        ) in weapon_info:
    lines.append('    #<{}>'.format(gun_name))
    lines.append('')

    # Main buffs
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

    # Material changes for Old Hyperion (nerfs, technically, but less than stock)
    if len(materials) > 1:
        diff_max = (old_max_best - old_max_worst)/(len(materials)-1)
        if old_min_worst is None:
            diff_min = None
        else:
            diff_min = (old_min_best - old_min_worst)/(len(materials)-1)
        for (idx, mat) in enumerate(materials):
            if isinstance(mat, list):
                to_process = mat
            else:
                to_process = [mat]
            for mat in to_process:
                lines.append('            level None set {} ExternalAttributeEffects[0].BaseModifierValue.BaseValueConstant {:0.6f}'.format(
                    mat,
                    old_max_worst + (idx*diff_max),
                    ))
                lines.append('')
                lines.append('            level None set {} ExternalAttributeEffects[0].ModifierType MT_PreAdd'.format(
                    mat,
                    ))
                lines.append('')
                if diff_min is not None:
                    lines.append('            level None set {} ExternalAttributeEffects[1].BaseModifierValue.BaseValueConstant {:0.6f}'.format(
                        mat,
                        old_min_worst + (idx*diff_min),
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
