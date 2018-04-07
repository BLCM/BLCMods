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

mod_name = 'TPS No Wasted COMs'
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
        ('06_EridianVanquisher',
            'GD_Itempools.ClassModPools.Pool_ClassMod_06_EridianVanquisher',
            '06_EridianVanquisher'),
        ('07_Chronicler',
            'GD_Pet_ItemPools.ClassModPools.Pool_Chronicler_ClassMod_All',
            None),
        ('Petunia',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_All',
            None),
        # This one's used as part of an early-game specific COM drop
        ('01_Common_1st',
            'GD_Itempools.ClassModPools.Pool_ClassMods_01_Common_1st',
            '01_Common'),
        # This one's only actually used for X-STLK-23's drops
        ('06_Celestial',
            'GD_Itempools.ClassModPools.Pool_ClassMods_06_Celestial',
            '06_EridianVanquisher'),
    ]
characters = [
        ('GD_Lawbringer_Streaming',
            'GD_Cork_Itempools.ClassModPools.Pool_ClassMod_Lawbringer',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Lawbringer_07_Chronicler',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Lawbringer_All_Petunia',
            ),
        ('GD_Prototype_Streaming',
            'GD_Cork_Itempools.ClassModPools.Pool_ClassMod_Prototype',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Prototype_07_Chronicler',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Prototype_All_Petunia',
            ),
        ('GD_Enforcer_Streaming',
            'GD_Cork_Itempools.ClassModPools.Pool_ClassMod_Enforcer',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Enforcer_07_Chronicler',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Enforcer_All_Petunia',
            ),
        ('GD_Gladiator_Streaming',
            'GD_Cork_Itempools.ClassModPools.Pool_ClassMod_Gladiator',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Gladiator_07_Chronicler',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Gladiator_All_Petunia',
            ),
        ('Crocus_Baroness_Streaming',
            'GD_Crocus_Itempools.ClassModPools.Pool_ClassMod_Baroness',
            'GD_Crocus_Itempools.ClassModPools.Pool_ClassMod_Baroness_07_ChroniclerOfElpis',
            'GD_Crocus_Itempools.ClassModPools.Pool_Pet_ClassMod_Baroness_All_Petunia',
            ),
        ('Quince_Doppel_Streaming',
            'GD_Quince_Itempools.ClassModPools.Pool_ClassMod_Doppelganger',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Doppel_07_Chronicler',
            'GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_Doppel_All_Petunia',
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
    if weight == '07_Chronicler':
        initial_sets[weight] = "set GD_Pet_ItemPools.ClassModPools.Pool_Chronicler_ClassMod_All BalancedItems\n{}".format(
            generate_balanced_items([char[2] for char in characters]))
    elif weight == 'Petunia':
        initial_sets[weight] = "set GD_Pet_ItemPools.ClassModPools.Pool_Pet_ClassMod_All BalancedItems\n{}".format(
            generate_balanced_items([char[3] for char in characters]))
    else:
        initial_sets[weight] = "set {} BalancedItems\n{}".format(
            pool,
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
for idx, (streaming, pool_reg, pool_chronicler, pool_petunia) in enumerate(characters):

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

        {set_01_Common_1st}

        {set_02_Uncommon}

        {set_04_Rare}

        {set_05_VeryRare}

        {set_06_Legendary}

        {set_06_Celestial}

        {set_06_EridianVanquisher}

        {set_07_Chronicler}

        {set_Petunia}

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

        {hotfixes:com_id_clear_01_Common_1st_0}
        
        {hotfixes:com_id_clear_01_Common_1st_1}
        
        {hotfixes:com_id_clear_01_Common_1st_2}
        
        {hotfixes:com_id_clear_01_Common_1st_3}
        
        {hotfixes:com_id_clear_01_Common_1st_4}
        
        {hotfixes:com_id_clear_01_Common_1st_5}

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

        {hotfixes:com_id_clear_06_Celestial_0}
        
        {hotfixes:com_id_clear_06_Celestial_1}
        
        {hotfixes:com_id_clear_06_Celestial_2}
        
        {hotfixes:com_id_clear_06_Celestial_3}
        
        {hotfixes:com_id_clear_06_Celestial_4}
        
        {hotfixes:com_id_clear_06_Celestial_5}

        {hotfixes:com_id_clear_06_EridianVanquisher_0}
        
        {hotfixes:com_id_clear_06_EridianVanquisher_1}
        
        {hotfixes:com_id_clear_06_EridianVanquisher_2}
        
        {hotfixes:com_id_clear_06_EridianVanquisher_3}
        
        {hotfixes:com_id_clear_06_EridianVanquisher_4}

        {hotfixes:com_id_clear_06_EridianVanquisher_5}

        {hotfixes:com_id_clear_07_Chronicler_0}
        
        {hotfixes:com_id_clear_07_Chronicler_1}
        
        {hotfixes:com_id_clear_07_Chronicler_2}
        
        {hotfixes:com_id_clear_07_Chronicler_3}
        
        {hotfixes:com_id_clear_07_Chronicler_4}

        {hotfixes:com_id_clear_07_Chronicler_5}

        {hotfixes:com_id_clear_Petunia_0}
        
        {hotfixes:com_id_clear_Petunia_1}
        
        {hotfixes:com_id_clear_Petunia_2}
        
        {hotfixes:com_id_clear_Petunia_3}
        
        {hotfixes:com_id_clear_Petunia_4}

        {hotfixes:com_id_clear_Petunia_5}

    #</Level Clear>

    #<Lawbringer>

        # Allows Lawbringer COM drops when that class joins

        {hotfixes:com_Lawbringer_set_01_Common}

        {hotfixes:com_Lawbringer_set_01_Common_1st}
        
        {hotfixes:com_Lawbringer_set_02_Uncommon}
        
        {hotfixes:com_Lawbringer_set_04_Rare}
        
        {hotfixes:com_Lawbringer_set_05_VeryRare}
        
        {hotfixes:com_Lawbringer_set_06_Legendary}
        
        {hotfixes:com_Lawbringer_set_06_Celestial}
        
        {hotfixes:com_Lawbringer_set_06_EridianVanquisher}

        {hotfixes:com_Lawbringer_set_07_Chronicler}

        {hotfixes:com_Lawbringer_set_Petunia}

    #</Lawbringer>

    #<Prototype>

        # Allows Prototype COM drops when that class joins

        {hotfixes:com_Prototype_set_01_Common}

        {hotfixes:com_Prototype_set_01_Common_1st}
        
        {hotfixes:com_Prototype_set_02_Uncommon}
        
        {hotfixes:com_Prototype_set_04_Rare}
        
        {hotfixes:com_Prototype_set_05_VeryRare}
        
        {hotfixes:com_Prototype_set_06_Legendary}
        
        {hotfixes:com_Prototype_set_06_Celestial}
        
        {hotfixes:com_Prototype_set_06_EridianVanquisher}

        {hotfixes:com_Prototype_set_07_Chronicler}

        {hotfixes:com_Prototype_set_Petunia}

    #</Prototype>

    #<Enforcer>

        # Allows Enforcer COM drops when that class joins

        {hotfixes:com_Enforcer_set_01_Common}

        {hotfixes:com_Enforcer_set_01_Common_1st}
        
        {hotfixes:com_Enforcer_set_02_Uncommon}
        
        {hotfixes:com_Enforcer_set_04_Rare}
        
        {hotfixes:com_Enforcer_set_05_VeryRare}
        
        {hotfixes:com_Enforcer_set_06_Legendary}
        
        {hotfixes:com_Enforcer_set_06_Celestial}
        
        {hotfixes:com_Enforcer_set_06_EridianVanquisher}

        {hotfixes:com_Enforcer_set_07_Chronicler}

        {hotfixes:com_Enforcer_set_Petunia}

    #</Enforcer>

    #<Gladiator>

        # Allows Gladiator COM drops when that class joins

        {hotfixes:com_Gladiator_set_01_Common}

        {hotfixes:com_Gladiator_set_01_Common_1st}
        
        {hotfixes:com_Gladiator_set_02_Uncommon}
        
        {hotfixes:com_Gladiator_set_04_Rare}
        
        {hotfixes:com_Gladiator_set_05_VeryRare}
        
        {hotfixes:com_Gladiator_set_06_Legendary}
        
        {hotfixes:com_Gladiator_set_06_Celestial}
        
        {hotfixes:com_Gladiator_set_06_EridianVanquisher}

        {hotfixes:com_Gladiator_set_07_Chronicler}

        {hotfixes:com_Gladiator_set_Petunia}

    #</Gladiator>

    #<Baroness>

        # Allows Baroness COM drops when that class joins

        {hotfixes:com_Baroness_set_01_Common}

        {hotfixes:com_Baroness_set_01_Common_1st}
        
        {hotfixes:com_Baroness_set_02_Uncommon}
        
        {hotfixes:com_Baroness_set_04_Rare}
        
        {hotfixes:com_Baroness_set_05_VeryRare}
        
        {hotfixes:com_Baroness_set_06_Legendary}
        
        {hotfixes:com_Baroness_set_06_Celestial}
        
        {hotfixes:com_Baroness_set_06_EridianVanquisher}

        {hotfixes:com_Baroness_set_07_Chronicler}

        {hotfixes:com_Baroness_set_Petunia}

    #</Baroness>

    #<Doppelganger>

        # Allows Doppelganer COM drops when that class joins

        {hotfixes:com_Doppel_set_01_Common}

        {hotfixes:com_Doppel_set_01_Common_1st}
        
        {hotfixes:com_Doppel_set_02_Uncommon}
        
        {hotfixes:com_Doppel_set_04_Rare}
        
        {hotfixes:com_Doppel_set_05_VeryRare}
        
        {hotfixes:com_Doppel_set_06_Legendary}
        
        {hotfixes:com_Doppel_set_06_Celestial}
        
        {hotfixes:com_Doppel_set_06_EridianVanquisher}

        {hotfixes:com_Doppel_set_07_Chronicler}

        {hotfixes:com_Doppel_set_Petunia}

    #</Doppelganger>

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        hotfixes=hfs,
        set_01_Common=initial_sets['01_Common'],
        set_01_Common_1st=initial_sets['01_Common_1st'],
        set_02_Uncommon=initial_sets['02_Uncommon'],
        set_04_Rare=initial_sets['04_Rare'],
        set_05_VeryRare=initial_sets['05_VeryRare'],
        set_06_Legendary=initial_sets['06_Legendary'],
        set_06_Celestial=initial_sets['06_Celestial'],
        set_06_EridianVanquisher=initial_sets['06_EridianVanquisher'],
        set_07_Chronicler=initial_sets['07_Chronicler'],
        set_Petunia=initial_sets['Petunia'],
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
