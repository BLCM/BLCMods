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

# NOTE: Some more data for this came from invbalstage.py, but we're not automating
# that since it required a bunch of manual pruning.  The various
# Manufacturers[x].Grades[x].GameStageRequirement.MinGameStage hotfixes can be
# found that way, though.  (Mostly grenades, but also a few relics)

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

try:
    from ftexplorer.data import Data
except ModuleNotFoundError:
    print('')
    print('****************************************************************')
    print('To run this script, you will need to copy or symlink the')
    print('"ftexplorer" and "resources" dirs from my ft-explorer project so')
    print('they exist here as well.  Sorry for the bother!')
    print('****************************************************************')
    print('')
    sys.exit(1)

###
### Output variables
###

mod_name = 'BL2 Early Bloomer'
mod_version = '1.1.0'
input_filename = 'mod-input-file.txt'
output_filename = '{}.blcm'.format(mod_name)

# Hotfixes for compatibility with my "Better Loot" mod.  No ill effects if applied
# without Better Loot installed!
better_loot_compat_list = []
for (classname) in [
        'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28',
        'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29',
        'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30',
        'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31',
        'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32',
        'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33',
        ]:
    for i in range(19):
        better_loot_compat_list.append('level None set {} AlphaPartData.WeightedParts[{}].MinGameStageIndex 0'.format(
            classname,
            i,
            ))
prefix = ' '*(4*2)
better_loot_compat = "\n\n".join(['{}{}'.format(prefix, s) for s in better_loot_compat_list])

# Various grenade mod early unlocks.  These actually don't have to be
# hotfixes, but doing so lets us be much more concise.
grenade_unlock_list = []
for (gm_type, man_count) in [
            ('AreaEffect', 1),
            ('BouncingBetty', 2),
            ('Mirv', 2),
            ('Singularity', 1),
            ('Transfusion', 1),
        ]:
    for man_num in range(man_count):
        grenade_unlock_list.append('level None set GD_GrenadeMods.A_Item.GM_{} Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
            gm_type, man_num
            ))
        grenade_unlock_list.append('level None set GD_GrenadeMods.A_Item.GM_{}_2_Uncommon Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
            gm_type, man_num
            ))
        grenade_unlock_list.append('level None set GD_GrenadeMods.A_Item.GM_{}_3_Rare Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
            gm_type, man_num,
            ))
        grenade_unlock_list.append('level None set GD_GrenadeMods.A_Item.GM_{}_4_VeryRare Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
            gm_type, man_num,
            ))
prefix = ' '*(4*2)
grenade_unlock = "\n\n".join(['{}{}'.format(prefix, s) for s in grenade_unlock_list])

# Generate an exhaustive list of part unlocks, using my ft-explorer
# data introspection routines.
exhaustive_unlocks_list = []
data = Data('BL2')
classnames = sorted(data.get_all_by_type('WeaponPartListCollectionDefinition') +
        data.get_all_by_type('ItemPartListCollectionDefinition'))
for classname in classnames:
    obj_struct = data.get_struct_by_full_object(classname)

    if 'ConsolidatedAttributeInitData' not in obj_struct:
        # Should maybe keep track of which of these doesn't have it...
        continue

    # Figure out our caid values
    caid = obj_struct['ConsolidatedAttributeInitData']
    caid_values = []
    for caid_val in caid:
        caid_values.append(float(caid_val['BaseValueConstant']))

    # Now loop through all our items.
    caid_updates = set()
    for key, val in obj_struct.items():
        if key[-8:] == 'PartData':
            for part in val['WeightedParts']:
                min_stage_idx = int(part['MinGameStageIndex'])
                if caid_values[min_stage_idx] > 1:
                    caid_updates.add(min_stage_idx)

    # Update, if need be!
    if len(caid_updates) > 0:
        #print('Updating the following in {}:'.format(obj_name))
        for idx in caid_updates:
            #print(' * {}: {}'.format(idx, caid_values[idx]))
            exhaustive_unlocks_list.append('level None set {} ConsolidatedAttributeInitData[{}].BaseValueConstant 1'.format(
                classname, idx
                ))

prefix = ' '*(4*2)
exhaustive_unlocks = "\n\n".join(['{}{}'.format(prefix, s) for s in exhaustive_unlocks_list])

###
### Everything below this point is constructing the actual patch file
###

# Output the mod file
with open(input_filename, 'r') as df:
    mod_str = df.read().format(
        mod_name=mod_name,
        mod_version=mod_version,
        grenade_unlock=grenade_unlock,
        better_loot_compat=better_loot_compat,
        exhaustive_unlocks=exhaustive_unlocks,
        )
mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to {}'.format(output_filename))
