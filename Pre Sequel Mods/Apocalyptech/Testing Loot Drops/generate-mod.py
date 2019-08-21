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

mod_name = 'Testing Loot Drops'
input_filename = 'input-file-mod.txt'
output_filename = '{}.blcm'.format(mod_name)

###
### Control variables
###

# Set `loot_drop_quantity` to the number of items each enemy will drop.
loot_drop_quantity = 5

# Force Pool_GunsAndGear to always drop the specified pool, if `force_gunsandgear_drop`
# is True.  Useful for testing out how individual pools are behaving.
force_gunsandgear_drop = True
force_gunsandgear_drop_type = 'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary'

# Force Pool_GunsAndGear to always drop the specified item, if
# `force_gunsandgear_specific` is True.  Useful for seeing what exactly an
# item is.  `force_gunsandgear_specific` will override `force_gunsandgear_drop`,
# if both are set to True.
force_gunsandgear_specific = False
# Types:
#   'WeaponBalanceDefinition'
#   'InventoryBalanceDefinition'
force_gunsandgear_specific_items = [
    ('GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol', 1, 'WeaponBalanceDefinition'),
    #('GD_Petunia_Weapons.Snipers.Sniper_Jakobs_3_Plunkett', 1, 'InventoryBalanceDefinition'),
    ]


###
### Now generate the mod
###

# Process our forced GunsAndGear drop
gunsandgear_drop_str = ''
if force_gunsandgear_specific:
    drop_specific = force_gunsandgear_specific_items[0][0]
    if len(force_gunsandgear_specific_items) > 1:
        drop_specific = '{} (and others)'.format(drop_specific)
    gunsandgear_drop_str = """
    #<Force GunsAndGearDrop to {drop_specific}>

        # Forces the GunsAndGear drop pool to always drop {drop_specific}

        level None set GD_Itempools.GeneralItemPools.Pool_GunsAndGear BalancedItems
        {balanced}

    #</Force GunsAndGearDrop to {drop_specific}>
    """.format(
        drop_specific=drop_specific,
        balanced=mp.get_balanced_items(force_gunsandgear_specific_items),
        )
elif force_gunsandgear_drop:
    gunsandgear_drop_str = """
    #<Force GunsAndGearDrop to {force_gunsandgear_drop_type}>

        # Forces the GunsAndGear drop pool to always drop {force_gunsandgear_drop_type}

        level None set GD_Itempools.GeneralItemPools.Pool_GunsAndGear BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'{force_gunsandgear_drop_type}',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

    #</Force GunsAndGearDrop to {force_gunsandgear_drop_type}>
    """.format(force_gunsandgear_drop_type=force_gunsandgear_drop_type)

# Read in our main input file
with open(input_filename, 'r') as df:
    if loot_drop_quantity == 1:
        plural = ''
    else:
        plural = 's'
    loot_str = df.read().format(
            mod_name=mod_name,
            loot_drop_quantity=loot_drop_quantity,
            plural=plural,
            gunsandgear_drop_str=gunsandgear_drop_str,
            )

mp.human_str_to_blcm_filename(loot_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
