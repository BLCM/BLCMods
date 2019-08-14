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
mod_name = 'BL2 Invulnerable Escortees'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

# Variables that we'll set for each char
vars_to_set = []
for element in ['Ignite', 'Shock', 'Corrosive', 'Amp']:
    for var_type in ['Chance', 'Duration']:
        vars_to_set.append('Base{}{}ResistanceModifier.BaseValueConstant'.format(element, var_type))
for element in ['Normal', 'Explosive', 'Shock', 'Corrosive', 'Incendiary', 'Amp']:
    for var_type in ['Impact', 'StatusEffect']:
        vars_to_set.append('Base{}DamageModifiers.ResistanceTo{}.BaseValueConstant'.format(element, var_type))

# The characters to operate on
chars = [
        ('Der Monstrositat',
            'The Borok Dietmar wants you to trap in the Hammerlock DLC mission "Still Just a Borok in a Cage"',
            None,
            'GD_Sage_SM_BorokCageData.Population.PawnBalance_Sage_BorokCage_Creature',
            'Sage_Underground_P',
            [],
            [
                [],
            ],
            [],
            ),
        ('Enrique',
            'Tina\'s pet in the Torgue DLC, during the mission "Walking the Dog"',
            'GD_IrisTinaSkag.Character.CharClass_Iris_SkagBadassFire',
            None,
            'Iris_Hub_P',
            [
                #('GD_Balance_HealthAndDamage.AIParameters.Attribute_HealthMultiplier', 7, 'None', 'None', 1),
                ('GD_Balance_HealthAndDamage.AIParameters.Attribute_EnemyNonWeaponDamageMultiplier', 9, 'None', 'None', 1),
                ('GD_Balance_Experience.Attributes.Attribute_ExperienceMultiplier', 0, 'None', "AttributeInitializationDefinition'GD_AI_Balance.XP.XPMultiplier_06_Badass'", 1),
                ('GD_Balance_HealthAndDamage.AIParameters.Attribute_DamageToVehiclesOnCollisionMultiplier', 5, 'None', 'None', 1),
            ],
            [],
            [],
            ),
        ('Flesh-Stick',
            'Tina\'s nemesis during the "You Are Cordially Invited" quest line in Tundra Express',
            'GD_FleshStick.Character.CharClass_FleshStick',
            None,
            'TundraExpress_P',
            [],
            [],
            [],
            ),
        ('Hacked Overseer',
            'The hacked constructor from the mission "Statuesque" in Opportunity',
            'GD_ConstructorLaserStatue.Character.CharClass_ConstructorLaserStatue',
            None,
            'HyperionCity_P',
            [
                #('GD_Balance_HealthAndDamage.AIParameters.Attribute_HealthMultiplier', 36, 'None', 'None', 1),
                ('GD_Balance_HealthAndDamage.AIParameters.Attribute_EnemyNonWeaponDamageMultiplier', 1, 'None', 'None', 1),
                ('GD_Balance_Experience.Attributes.Attribute_ExperienceMultiplier', 0, 'None', "AttributeInitializationDefinition'GD_AI_Balance.XP.XPMultiplier_06_Badass'", 1),
                ('GD_Balance_HealthAndDamage.AIParameters.Attribute_DamageToVehiclesOnCollisionMultiplier', 10, 'None', 'None', 1),
            ],
            [],
            [],
            ),
        ('Mosstache',
            'Aubrey\'s instrument of vengeance in the Dragon Keep DLC mission "Tree Hugger"',
            'GD_Treant_TreeHugger.Character.CharClass_Treant_TreeHugger',
            None,
            'Dark_Forest_P',
            [
                #('GD_Balance_HealthAndDamage.AIParameters.Attribute_HealthMultiplier', 25, 'None', 'None', 1),
                ('GD_Balance_HealthAndDamage.AIParameters.Attribute_EnemyNonWeaponDamageMultiplier', 6, 'None', 'None', 1),
                ('GD_Balance_Experience.Attributes.Attribute_ExperienceMultiplier', 0, 'None', "AttributeInitializationDefinition'GD_AI_Balance.XP.XPMultiplier_02_Normal'", 1),
                ('GD_Balance_HealthAndDamage.AIParameters.Attribute_DamageToVehiclesOnCollisionMultiplier', 2, 'None', 'None', 1),
            ],
            [],
            [
                'set GD_Aster_TreeHuggerData.IO_TreeHugger_SaplingPlanted bCanTakeDirectDamage False',
                'set GD_Aster_TreeHuggerData.IO_TreeHugger_SaplingPlanted bCanTakeRadiusDamage False',
            ],
            ),

    ]

def get_asv_full(asvs):
    asvs.extend([
        ('GD_Balance_HealthAndDamage.AIParameters.Attribute_HealthMultiplier', 99999999, 'None', 'None', 1),
        ('D_Attributes.DamageSourceModifiers.ReceivedGrenadeDamageModifier', 0, 'None', 'None', 1),
        ('D_Attributes.DamageSourceModifiers.ReceivedMeleeDamageModifier', 0, 'None', 'None', 1),
        ])
    asv_elements = []
    for (attr, bvc, bva, idef, bvsc) in asvs:
        asv_elements.append("""
        (
            Attribute=AttributeDefinition'{}',
            BaseValue=(
                BaseValueConstant={},
                BaseValueAttribute={},
                InitializationDefinition={},
                BaseValueScaleConstant={}
            )
        )""".format(
            attr, bvc, bva, idef, bvsc,
            ))
    return "({})".format(','.join(asv_elements))

# Construct the mod
lines = []
lines.append('BL2')
lines.append('#<{}>'.format(mod_name))
lines.append('')
lines.append('    # {} v{}'.format(mod_name, mod_version))
lines.append('    # by Apocalyptech')
lines.append('    # Licensed under Public Domain / CC0 1.0 Universal')
lines.append('    #')
lines.append('    # Makes any NPC you are required to "escort" be effectively invulnerable')
lines.append('    # to damage, so there\'s no chance of them accidentally being killed and')
lines.append('    # causing you to have to restart the mission.')
lines.append('')

for (char_name, comment, char_class, pawn_class, level_name, asvs, pt_asvs, extras) in chars:

    lines.append('#<{}>'.format(char_name))
    lines.append('')
    lines.append('# {}'.format(comment))
    lines.append('')
    if char_class:
        for var_name in vars_to_set:
            lines.append('level {} set {} {} 0'.format(level_name, char_class, var_name))
            lines.append('')
        lines.append('level {} set {} AttributeStartingValues {}'.format(level_name, char_class, get_asv_full(asvs)))
        lines.append('')
    for extra in extras:
        lines.append('level {} {}'.format(level_name, extra))
        lines.append('')
    if pawn_class:
        for (pt_idx, ind_pt_asvs) in enumerate(pt_asvs):
            lines.append('level {} set {} PlayThroughs[{}].AttributeStartingValues {}'.format(
                level_name, pawn_class, pt_idx, get_asv_full(ind_pt_asvs),
                ))
            lines.append('')

    lines.append('#</{}>'.format(char_name))
    lines.append('')

lines.append("""#<Murderlin's Son (disabled by default)><mut>

#<Let Murderlin's Son's Tower Get Damaged>

    # Unlike the other "escort" quests, preventing the tower from
    # being damaged here seems pretty ridiculous, so by default
    # we keep it damageable.

    level TempleSlaughter_P set GD_Aster_TempleTowerData.InteractiveObjects.IO_MO_TempleObjective bCanTakeDirectDamage True

    level TempleSlaughter_P set GD_Aster_TempleTowerData.InteractiveObjects.IO_MO_TempleObjective bCanTakeRadiusDamage True

#</Let Murderlin's Son's Tower Get Damaged>

#<Disable Damage to Murderlin's Son's Tower>

    # If you really want "The Magic of Childhood" to be utterly
    # trivial, this option will let you finish the level literally
    # without ever having to fire a shot.

    level TempleSlaughter_P set GD_Aster_TempleTowerData.InteractiveObjects.IO_MO_TempleObjective bCanTakeDirectDamage False

    level TempleSlaughter_P set GD_Aster_TempleTowerData.InteractiveObjects.IO_MO_TempleObjective bCanTakeRadiusDamage False

#</Disable Damage to Murderlin's Son's Tower>

#</Murderlin's Son (disabled by default)>
""")

lines.append('')
lines.append('#</{}>'.format(mod_name))

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))
