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

# Python script to generate my No Wasted COMs mod

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

mod_name = 'BL2 No Wasted COMs'
mod_version = '1.0.0'
output_filename = '{}-source.txt'.format(mod_name)

###
### Generate hotfixes!
###

hfs = Hotfixes()
pools = [
        ('01_Common',
            'GD_Itempools.ClassModPools.Pool_ClassMod_01_Common',
            '01_Common'),
        ('02_Uncommon',
            'GD_Itempools.ClassModPools.Pool_ClassMod_02_Uncommon',
            '02_Uncommon'),
        ('04_Rare',
            'GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare',
            '03_Rare'),
        ('05_VeryRare',
            'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
            '04_VeryRare'),
        ('06_Legendary',
            'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary',
            '05_Legendary'),
        ('06_SlayerOfTerramorphous',
            'GD_Itempools.ClassModPools.Pool_ClassMod_06_SlayerOfTerramorphous',
            '01_Common'),
        ('00_Aster',
            'GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_00_Aster',
            None),
        ('Lobelia',
            'GD_Lobelia_Itempools.ClassModPools.Pool_ClassMod_Lobelia_All',
            None),
    ]
characters = [
        ('GD_Assassin_Streaming',
            'GD_Itempools.ClassModPools.Pool_ClassMod_Assassin',
            'GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_Assassin_Aster',
            'GD_Lobelia_Itempools.ClassModPools.Pool_ClassMod_Lobelia_Assassin',
            ),
        ('GD_Mercenary_Streaming',
            'GD_Itempools.ClassModPools.Pool_ClassMod_Merc',
            'GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_Merc_Aster',
            'GD_Lobelia_Itempools.ClassModPools.Pool_ClassMod_Lobelia_Merc',
            ),
        ('GD_Siren_Streaming',
            'GD_Itempools.ClassModPools.Pool_ClassMod_Siren',
            'GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_Siren_Aster',
            'GD_Lobelia_Itempools.ClassModPools.Pool_ClassMod_Lobelia_Siren',
            ),
        ('GD_Soldier_Streaming',
            'GD_Itempools.ClassModPools.Pool_ClassMod_Soldier',
            'GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_Soldier_Aster',
            'GD_Lobelia_Itempools.ClassModPools.Pool_ClassMod_Lobelia_Soldier',
            ),
        ('GD_Lilac_Psycho_Streaming',
            'GD_Lilac_Itempools.ClassModPools.Pool_ClassMod_LilacPlayerClass',
            'GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_Psycho_Aster',
            'GD_Lobelia_Itempools.ClassModPools.Pool_ClassMod_Lobelia_Psycho',
            ),
        ('GD_Tulip_Mechro_Streaming',
            'GD_Tulip_Itempools.ClassModPools.Pool_ClassMod_Mechromancer',
            'GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_Mechromancer_Aster',
            'GD_Lobelia_Itempools.ClassModPools.Pool_ClassMod_Lobelia_Mechromancer',
            ),
    ]

# First, a `set` statement to do an initial clear of the pools.  This is
# actually only here so that it's possible to "reset" the drop pools by
# re-executing the patch from the main menu; otherwise you'd have to quit
# the game entirely.
def generate_balanced_items(items):
    stanzas = []
    for item in items:
        stanzas.append("""
            ( 
                ItmPoolDefinition=ItemPoolDefinition'{}', 
                InvBalanceDefinition=None, 
                Probability=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000 
                ), 
                bDropOnDeath=True 
            )
            """.format(item))
    return '({})'.format(','.join(stanzas))
initial_sets = {}
for (weight, pool, individual_weight) in pools:
    if weight == '00_Aster':
        initial_sets[weight] = "set GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_00_Aster BalancedItems\n{}".format(
            generate_balanced_items([char[2] for char in characters]))
    elif weight == 'Lobelia':
        initial_sets[weight] = "set GD_Lobelia_Itempools.ClassModPools.Pool_ClassMod_Lobelia_All BalancedItems\n{}".format(
            generate_balanced_items([char[3] for char in characters]))
    else:
        initial_sets[weight] = "set GD_Itempools.ClassModPools.Pool_ClassMod_{} BalancedItems\n{}".format(
            weight,
            generate_balanced_items(['{}_{}'.format(char[1], individual_weight) for char in characters]))

# Now, a general level hotfix to clear out the InitializationDefinition
# values in the main loot pools.  This is necessary because something that's
# not a hotfix but acts like a hotfix will reset InitializationDefinition on
# each level load, regardless of what we've done to it beforehand, so we have
# to override that.
for (weight, pool, individual_weight) in pools:
    for idx in range(6):
        hfs.add_level_hotfix('com_id_clear_{}_{}'.format(weight, idx),
            'COMIDClear',
            """,{pool},
            BalancedItems[{idx}].Probability.InitializationDefinition,,
            None
            """.format(
                pool=pool,
                idx=idx))

# OnDemand hotfixes for each player class
for idx, (streaming, pool_reg, pool_aster, pool_lobelia) in enumerate(characters):

    short = streaming.split('_')[-2]

    for (weight, pool, individual_weight) in pools:
        hfs.add_demand_hotfix('com_{}_set_{}'.format(short, weight),
            'COM{}Set'.format(short),
            """
            {streaming},
            {pool},
            BalancedItems[{idx}].Probability.BaseValueConstant,,
            1
            """.format(
                    streaming=streaming,
                    pool=pool,
                    idx=idx,
                    ))

###
### Generate the mod string
###

mod_str = """#<{mod_name}>

    # {mod_name} v{mod_version}
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Sets the game to only drop COMs for the player classes who are actually
    # in the game at the time.  Once a player class has joined the game, the
    # only way to remove that character's COMs from the drop pools is to exit
    # to the main menu and re-execute the patch.

    #<Initial Clear>

        # Do an initial set to clear out the COM item pools.  This is actually
        # only required if you're looking to "clear out" a pool after a character's
        # left the game, and must be done by exiting out to the main menu and re-
        # executing the mod/patch.

        {set_01_Common}

        {set_02_Uncommon}

        {set_04_Rare}

        {set_05_VeryRare}

        {set_06_Legendary}

        {set_06_SlayerOfTerramorphous}

        {set_00_Aster}

        {set_Lobelia}

    #</Initial Clear>

    #<Level Clear>

        # Something hotfix-like modifies the InitializationDefinition of these pools
        # on level load, so we need a level-load hotfix to clear it out.

        {hotfixes:com_id_clear_01_Common_0}
        
        {hotfixes:com_id_clear_01_Common_1}
        
        {hotfixes:com_id_clear_01_Common_2}
        
        {hotfixes:com_id_clear_01_Common_3}
        
        {hotfixes:com_id_clear_01_Common_4}
        
        {hotfixes:com_id_clear_01_Common_5}

        {hotfixes:com_id_clear_02_Uncommon_0}
        
        {hotfixes:com_id_clear_02_Uncommon_1}
        
        {hotfixes:com_id_clear_02_Uncommon_2}
        
        {hotfixes:com_id_clear_02_Uncommon_3}
        
        {hotfixes:com_id_clear_02_Uncommon_4}
        
        {hotfixes:com_id_clear_02_Uncommon_5}

        {hotfixes:com_id_clear_04_Rare_0}
        
        {hotfixes:com_id_clear_04_Rare_1}
        
        {hotfixes:com_id_clear_04_Rare_2}
        
        {hotfixes:com_id_clear_04_Rare_3}
        
        {hotfixes:com_id_clear_04_Rare_4}
        
        {hotfixes:com_id_clear_04_Rare_5}

        {hotfixes:com_id_clear_05_VeryRare_0}
        
        {hotfixes:com_id_clear_05_VeryRare_1}
        
        {hotfixes:com_id_clear_05_VeryRare_2}
        
        {hotfixes:com_id_clear_05_VeryRare_3}
        
        {hotfixes:com_id_clear_05_VeryRare_4}
        
        {hotfixes:com_id_clear_05_VeryRare_5}

        {hotfixes:com_id_clear_06_Legendary_0}
        
        {hotfixes:com_id_clear_06_Legendary_1}
        
        {hotfixes:com_id_clear_06_Legendary_2}
        
        {hotfixes:com_id_clear_06_Legendary_3}
        
        {hotfixes:com_id_clear_06_Legendary_4}
        
        {hotfixes:com_id_clear_06_Legendary_5}

        {hotfixes:com_id_clear_06_SlayerOfTerramorphous_0}
        
        {hotfixes:com_id_clear_06_SlayerOfTerramorphous_1}
        
        {hotfixes:com_id_clear_06_SlayerOfTerramorphous_2}
        
        {hotfixes:com_id_clear_06_SlayerOfTerramorphous_3}
        
        {hotfixes:com_id_clear_06_SlayerOfTerramorphous_4}

        {hotfixes:com_id_clear_06_SlayerOfTerramorphous_5}

        {hotfixes:com_id_clear_00_Aster_0}
        
        {hotfixes:com_id_clear_00_Aster_1}
        
        {hotfixes:com_id_clear_00_Aster_2}
        
        {hotfixes:com_id_clear_00_Aster_3}
        
        {hotfixes:com_id_clear_00_Aster_4}

        {hotfixes:com_id_clear_00_Aster_5}

        {hotfixes:com_id_clear_Lobelia_0}
        
        {hotfixes:com_id_clear_Lobelia_1}
        
        {hotfixes:com_id_clear_Lobelia_2}
        
        {hotfixes:com_id_clear_Lobelia_3}
        
        {hotfixes:com_id_clear_Lobelia_4}

        {hotfixes:com_id_clear_Lobelia_5}

    #</Level Clear>

    #<Assassin>

        # Allows Assassin COM drops when that class joins

        {hotfixes:com_Assassin_set_01_Common}
        
        {hotfixes:com_Assassin_set_02_Uncommon}
        
        {hotfixes:com_Assassin_set_04_Rare}
        
        {hotfixes:com_Assassin_set_05_VeryRare}
        
        {hotfixes:com_Assassin_set_06_Legendary}
        
        {hotfixes:com_Assassin_set_06_SlayerOfTerramorphous}

        {hotfixes:com_Assassin_set_00_Aster}

        {hotfixes:com_Assassin_set_Lobelia}

    #</Assassin>

    #<Mercenary>

        # Allows Mercenary COM drops when that class joins

        {hotfixes:com_Mercenary_set_01_Common}
        
        {hotfixes:com_Mercenary_set_02_Uncommon}
        
        {hotfixes:com_Mercenary_set_04_Rare}
        
        {hotfixes:com_Mercenary_set_05_VeryRare}
        
        {hotfixes:com_Mercenary_set_06_Legendary}
        
        {hotfixes:com_Mercenary_set_06_SlayerOfTerramorphous}

        {hotfixes:com_Mercenary_set_00_Aster}

        {hotfixes:com_Mercenary_set_Lobelia}

    #</Mercenary>

    #<Siren>

        # Allows Siren COM drops when that class joins

        {hotfixes:com_Siren_set_01_Common}
        
        {hotfixes:com_Siren_set_02_Uncommon}
        
        {hotfixes:com_Siren_set_04_Rare}
        
        {hotfixes:com_Siren_set_05_VeryRare}
        
        {hotfixes:com_Siren_set_06_Legendary}
        
        {hotfixes:com_Siren_set_06_SlayerOfTerramorphous}

        {hotfixes:com_Siren_set_00_Aster}

        {hotfixes:com_Siren_set_Lobelia}

    #</Siren>

    #<Soldier>

        # Allows Soldier COM drops when that class joins

        {hotfixes:com_Soldier_set_01_Common}
        
        {hotfixes:com_Soldier_set_02_Uncommon}
        
        {hotfixes:com_Soldier_set_04_Rare}
        
        {hotfixes:com_Soldier_set_05_VeryRare}
        
        {hotfixes:com_Soldier_set_06_Legendary}
        
        {hotfixes:com_Soldier_set_06_SlayerOfTerramorphous}

        {hotfixes:com_Soldier_set_00_Aster}

        {hotfixes:com_Soldier_set_Lobelia}

    #</Soldier>

    #<Psycho>

        # Allows Psycho COM drops when that class joins

        {hotfixes:com_Psycho_set_01_Common}
        
        {hotfixes:com_Psycho_set_02_Uncommon}
        
        {hotfixes:com_Psycho_set_04_Rare}
        
        {hotfixes:com_Psycho_set_05_VeryRare}
        
        {hotfixes:com_Psycho_set_06_Legendary}
        
        {hotfixes:com_Psycho_set_06_SlayerOfTerramorphous}

        {hotfixes:com_Psycho_set_00_Aster}

        {hotfixes:com_Psycho_set_Lobelia}

    #</Psycho>

    #<Mechromancer>

        # Allows Mechromancer COM drops when that class joins

        {hotfixes:com_Mechro_set_01_Common}
        
        {hotfixes:com_Mechro_set_02_Uncommon}
        
        {hotfixes:com_Mechro_set_04_Rare}
        
        {hotfixes:com_Mechro_set_05_VeryRare}
        
        {hotfixes:com_Mechro_set_06_Legendary}
        
        {hotfixes:com_Mechro_set_06_SlayerOfTerramorphous}

        {hotfixes:com_Mechro_set_00_Aster}

        {hotfixes:com_Mechro_set_Lobelia}

    #</Mechromancer>

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        hotfixes=hfs,
        set_01_Common=initial_sets['01_Common'],
        set_02_Uncommon=initial_sets['02_Uncommon'],
        set_04_Rare=initial_sets['04_Rare'],
        set_05_VeryRare=initial_sets['05_VeryRare'],
        set_06_Legendary=initial_sets['06_Legendary'],
        set_06_SlayerOfTerramorphous=initial_sets['06_SlayerOfTerramorphous'],
        set_00_Aster=initial_sets['00_Aster'],
        set_Lobelia=initial_sets['Lobelia'],
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
