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

mod_name = 'BL2 Early Bloomer'
mod_version = '1.0.0'
input_filename = 'mod-input-file.txt'
output_filename = '{}.txt'.format(mod_name)

###
### Hotfix object to store all our hotfixes
###

hfs = Hotfixes(include_gearbox_patches=True)

# Early-game loot unlocks.  Except for this one specific case (Aquamarine Snipers),
# this can be done with `set` statements, so you'll see all those in mod-input-file.txt.
# This one has to be hotfixed to be fully cross-platform compatible, and predictable.
hfs.add_level_hotfix('part_early_game_fix_0',
        'PartEarlyGameFix',
        """,GD_Aster_Weapons.Snipers.SR_Maliwan_4_Aquamarine:WeaponPartListCollectionDefinition_306,
        ElementalPartData.WeightedParts,,
        (
            (
                Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Fire',
                Manufacturers=,
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=2
            ),
            (
                Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Shock',
                Manufacturers=,
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=2
            ),
            (
                Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Corrosive',
                Manufacturers=,
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=2
            ),
            (
                Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Slag',
                Manufacturers=,
                MinGameStageIndex=0,
                MaxGameStageIndex=1,
                DefaultWeightIndex=2
            )
        )""")

# Hotfixes for compatibility with my "Better Loot" mod.  No ill effects if applied
# without Better Loot installed!
hfs.add_level_hotfix('part_early_game_numerical_fix_0',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[0].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_1',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[1].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_2',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[2].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_3',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[3].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_4',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[4].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_5',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[5].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_6',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[6].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_7',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[7].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_8',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[8].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_9',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[9].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_10',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[10].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_11',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[11].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_12',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[12].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_13',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[13].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_14',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[14].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_15',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[15].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_16',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[16].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_17',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[17].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_18',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts[18].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_19',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[0].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_20',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[1].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_21',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[2].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_22',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[3].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_23',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[4].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_24',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[5].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_25',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[6].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_26',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[7].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_27',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[8].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_28',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[9].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_29',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[10].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_30',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[11].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_31',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[12].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_32',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[13].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_33',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[14].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_34',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[15].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_35',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[16].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_36',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[17].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_37',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts[18].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_38',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[0].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_39',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[1].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_40',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[2].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_41',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[3].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_42',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[4].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_43',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[5].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_44',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[6].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_45',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[7].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_46',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[8].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_47',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[9].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_48',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[10].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_49',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[11].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_50',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[12].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_51',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[13].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_52',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[14].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_53',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[15].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_54',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[16].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_55',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[17].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_56',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts[18].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_57',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[0].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_58',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[1].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_59',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[2].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_60',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[3].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_61',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[4].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_62',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[5].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_63',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[6].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_64',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[7].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_65',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[8].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_66',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[9].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_67',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[10].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_68',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[11].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_69',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[12].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_70',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[13].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_71',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[14].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_72',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[15].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_73',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[16].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_74',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[17].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_75',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts[18].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_76',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[0].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_77',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[1].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_78',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[2].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_79',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[3].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_80',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[4].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_81',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[5].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_82',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[6].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_83',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[7].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_84',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[8].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_85',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[9].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_86',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[10].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_87',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[11].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_88',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[12].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_89',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[13].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_90',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[14].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_91',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[15].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_92',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[16].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_93',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[17].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_94',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts[18].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_95',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[0].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_96',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[1].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_97',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[2].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_98',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[3].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_99',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[4].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_100',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[5].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_101',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[6].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_102',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[7].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_103',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[8].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_104',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[9].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_105',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[10].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_106',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[11].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_107',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[12].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_108',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[13].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_109',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[14].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_110',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[15].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_111',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[16].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_112',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[17].MinGameStageIndex,,0")
hfs.add_level_hotfix('part_early_game_numerical_fix_113',
    'PartEarlyGameNumericalFix',
    ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts[18].MinGameStageIndex,,0")

# Various grenade mod early unlocks.  These actually don't have to be
# hotfixes, but doing so lets us be much more concise.
for (gm_type, man_count) in [
            ('AreaEffect', 1),
            ('BouncingBetty', 2),
            ('Mirv', 2),
            ('Singularity', 1),
            ('Transfusion', 1),
        ]:
    for man_num in range(man_count):
        hfs.add_level_hotfix('grenade_{}_{}_0'.format(gm_type, man_num),
            'Grenade{}Man{}Rarity'.format(gm_type, man_num),
            ',GD_GrenadeMods.A_Item.GM_{},Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage,,0'.format(
                gm_type, man_num,
            ))
        hfs.add_level_hotfix('grenade_{}_{}_1'.format(gm_type, man_num),
            'Grenade{}Man{}Rarity'.format(gm_type, man_num),
            ',GD_GrenadeMods.A_Item.GM_{}_2_Uncommon,Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage,,0'.format(
                gm_type, man_num,
            ))
        hfs.add_level_hotfix('grenade_{}_{}_2'.format(gm_type, man_num),
            'Grenade{}Man{}Rarity'.format(gm_type, man_num),
            ',GD_GrenadeMods.A_Item.GM_{}_3_Rare,Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage,,0'.format(
                gm_type, man_num,
            ))
        hfs.add_level_hotfix('grenade_{}_{}_3'.format(gm_type, man_num),
            'Grenade{}Man{}Rarity'.format(gm_type, man_num),
            ',GD_GrenadeMods.A_Item.GM_{}_4_VeryRare,Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage,,0'.format(
                gm_type, man_num,
            ))

# Unlock rocket launcher ammo at level 1.  It's possible this can be done
# with `set`, but I like being able to cherry-pick what I'm changing

hfs.add_level_hotfix('rocket_vending', 'RocketVending',
    """,GD_ItemGrades.Ammo_Shop.ItemGrade_AmmoShop_RocketLauncher,
    Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage,,1""")

hfs.add_level_hotfix('rocket_drops', 'RocketDrops',
    """,GD_ItemGrades.Ammo.ItemGrade_Ammo_RocketLauncher,
    Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage,,1""")

hfs.add_level_hotfix('grenade_vending', 'GrenadeVending',
    """,GD_ItemGrades.Ammo_Shop.ItemGrade_AmmoShop_Grenade,
    Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage,,1""")

hfs.add_level_hotfix('grenade_drops', 'GrenadeDrops',
    """,GD_ItemGrades.Ammo.ItemGrade_Ammo_Grenade,
    Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage,,1""")

###
### Everything below this point is constructing the actual patch file
###

# Output the mod file
with open(input_filename, 'r') as df:
    with open(output_filename, 'w') as odf:
        odf.write(df.read().format(
            mod_name=mod_name,
            mod_version=mod_version,
            hotfixes=hfs,
            ))
print('Wrote mod file to {}'.format(output_filename))
