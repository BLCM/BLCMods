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

mod_name = 'Stalkers Use Shields'
mod_version = '1.1.0'
output_filename = '{}.blcm'.format(mod_name)

###
### Some constants
###

class BaseConfig(object):
    """
    Basic class to hold config info
    """

    def __format__(self, formatstr):
        """
        A bit of magic so that we can use our values in format strings
        """
        attr = getattr(self, formatstr)
        if type(attr) == str:
            return attr
        elif type(attr) == int or type(attr) == float:
            return str(attr)
        else:
            return attr()

class DropConfig(BaseConfig):
    """
    Class to hold basic config for drops
    """

    # Shield pool sets
    set_regular_shields = None
    set_maylay_shields = None

    # Rarity weight presets that we'll generate
    weight_common = None
    weight_uncommon = None
    weight_rare = None
    weight_veryrare = None
    weight_legendary = None
    rarity_presets = [
            ('excellent', 'Stalkers Have Excellent Shields'),
            ('better', 'Stalkers Have Better Shields'),
            ('stock', 'Stalkers Have Common Shields'),
        ]

    # Computed percent drop rates, for reporting to the user in mod comments
    pct_common = None
    pct_uncommon = None
    pct_rare = None
    pct_veryrare = None
    pct_legendary = None

    # Stalker shield equips
    stalker_dipl = []
    
    ###
    ### ... FUNCTIONS??!?
    ###

    def _get_pct_chance(self, weight, total):
        chance = weight/total*100
        if chance == 0:
            return '0'
        elif chance > 1:
            return round(chance)
        else:
            return round(chance, 2)


    def set_rarity_weights(self, rarity_key):
        rarity = self.rarities[rarity_key]
        self.weight_common = rarity['common']
        self.weight_uncommon = rarity['uncommon']
        self.weight_rare = rarity['rare']
        self.weight_veryrare = rarity['veryrare']
        self.weight_legendary = rarity['legendary']

        total_weight = (self.weight_common + self.weight_uncommon +
                self.weight_rare + self.weight_veryrare +
                self.weight_legendary)

        self.pct_common = self._get_pct_chance(self.weight_common, total_weight)
        self.pct_uncommon = self._get_pct_chance(self.weight_uncommon, total_weight)
        self.pct_rare = self._get_pct_chance(self.weight_rare, total_weight)
        self.pct_veryrare = self._get_pct_chance(self.weight_veryrare, total_weight)
        self.pct_legendary = self._get_pct_chance(self.weight_legendary, total_weight)

class Regular(DropConfig):
    """
    Config info for regular enemies
    """

    # Hotfix prefix
    hotfix_prefix = 'reg'

    # Equip weights
    rarities = {
        'excellent': {
            'common': 20,
            'uncommon': 85,
            'rare': 65,
            'veryrare': 40,
            'legendary': 3,
            },
        'better': {
            'common': 32.75,
            'uncommon': 35,
            'rare': 25,
            'veryrare': 5,
            'legendary': 0.25,
            },
        'stock': {
            'common': 80,
            'uncommon': 10,
            'rare': 1,
            'veryrare': 0.1,
            'legendary': 0.03,
            },
        }

    # Shield pools
    regular_shields = 'GD_CustomItemPools_allium.Mechro.AlliumTGSkins'
    maylay_shields = 'GD_CustomItemPools_allium.Soldier.AlliumXmasHeads'

    # Stalker shield equips
    stalker_dipl = [
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerAmbush'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerCyclone'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerNeedle'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerSlagged'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerSpring'),
            (0, 'GD_Orchid_Pop_Stalker.Balance.PawnBalance_Orchid_StalkerOrchid'),
            (0, 'GD_Orchid_Pop_Stalker.Balance.PawnBalance_Orchid_StalkerRabid'),
        ]

class Badass(DropConfig):
    """
    Config info for badass enemies
    """

    # Hotfix prefix
    hotfix_prefix = 'badass'

    # Equip weights
    rarities = {
        'excellent': {
            'common': 0,
            'uncommon': 0,
            'rare': 35,
            'veryrare': 60,
            'legendary': 10,
            },
        'better': {
            'common': 0,
            'uncommon': 25,
            'rare': 49,
            'veryrare': 15,
            'legendary': 1,
            },
        # There's really not such a thing as a "stock" badass pool we could
        # base these weights on, so we're sort of just making it up.
        'stock': {
            'common': 0,
            'uncommon': 40,
            'rare': 30,
            'veryrare': 10,
            'legendary': 0.25,
            },
        }


    # Shield pools
    regular_shields = 'GD_CustomItemPools_allium.Mercenary.AlliumTGSkins'
    maylay_shields = 'GD_CustomItemPools_allium.Psycho.AlliumTGSkins'

    # Stalker shield equips
    stalker_dipl = [
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerBadass'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerChubby'),
            (0, 'GD_Population_Stalker.Balance.Unique.PawnBalance_Henry'),
            (0, 'GD_Population_Stalker.Balance.Unique.PawnBalance_Stalker_Simon'),
            (0, 'GD_Population_Stalker.Balance.Unique.PawnBalance_Stalker_SwallowedWhole'),
            (0, 'GD_Population_Stalker.Balance.Unique.PawnBalance_StalkerFreeWilly'),
            (0, 'GD_Population_Stalker.Balance.Unique.PawnBalance_StalkerRabid'),
            (0, 'GD_Orchid_Pop_Stalker.Balance.PawnBalance_Orchid_StalkerBadass'),
            (0, 'GD_Orchid_Pop_Stalker.Balance.PawnBalance_Orchid_StalkerChubby'),
            (0, 'GD_Orchid_Pop_StalkerPet.PawnBalance_Orchid_StalkerPet'),
            (0, 'GD_Sage_SM_NowYouSeeItData.Creature.PawnBalance_Sage_NowYouSeeIt_Creature'),
        ]

###
### Convenience functions
###

def get_balanced_items(items):
    """
    Returns a string containing a BalancedItems array with the given `items`.
    Each element of the list `items` should be a tuple, the first element
    being the itempool class name, the second being the weight of that
    item, and the third (optional) being an `invbalance` (or None).  If `None`,
    the item will be put into the ItmPoolDefinition attribute - otherwise it
    will be put into the InvBalanceDefinition attribute, with the given
    `invbalance` string as the type of object being linked to (most commonly
    either WeaponBalanceDefinition or InventoryBalanceDefinition)
    """
    bal_items = []
    new_items = []
    for item in items:
        if len(item) == 2:
            new_items.append((item[0], item[1], None))
        else:
            new_items.append((item[0], item[1], item[2]))
    for (classname, weight, invbalance) in new_items:
        if classname:
            if invbalance:
                itmpool = 'None'
                invbal = "{}'{}'".format(invbalance, classname)
            else:
                itmpool = "ItemPoolDefinition'{}'".format(classname)
                invbal = 'None'
        else:
            itmpool = 'None'
            invbal = 'None'
        bal_items.append("""
            (
                ItmPoolDefinition={},
                InvBalanceDefinition={},
                Probability=(
                    BaseValueConstant={},
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=False
            )
            """.format(itmpool, invbal, weight))
    return '({})'.format(','.join(bal_items))

def get_balanced_set(objectname, items):
    """
    Returns a regular "set" command to set `objectname`'s BalancedItems
    attribute to an array with the specified `items`.  The bulk of the
    work here is done in `get_balanced_items()`.
    """
    return "set {} BalancedItems\n{}".format(objectname,
            get_balanced_items(items))

def set_bi_item_pool(hotfix_name, classname, index, item,
        level=None, prob=None, invbalance=None):
    """
    Sets an entire BalancedItem structure
    """
    global mp
    if level is None:
        level = 'None'
    if prob is None:
        prob = 1
    if invbalance:
        itmpool = 'None'
        invbal = "{}'{}'".format(invbalance, item)
    else:
        itmpool = "ItemPoolDefinition'{}'".format(item)
        invbal = 'None'
    mp.register_str(hotfix_name,
        """level {} set {} BalancedItems[{}]
        (
            ItmPoolDefinition={},
            InvBalanceDefinition={},
            Probability=(
                BaseValueConstant={},
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1
            ),
            bDropOnDeath=True
        )""".format(level, classname, index, itmpool, invbal, prob))

###
### Code to generate the mod
###

regular = Regular()
badass = Badass()

# Configure rarity pools
rarity_sections = {}
for (rarity_key, rarity_label) in DropConfig.rarity_presets:

    for config in [regular, badass]:

        config.set_rarity_weights(rarity_key)

        # Regular shield pool
        config.set_regular_shields = get_balanced_set(
            config.regular_shields,
            [
                ('GD_Itempools.ShieldPools.Pool_Shields_All_01_Common', config.weight_common),
                ('GD_Itempools.ShieldPools.Pool_Shields_All_02_Uncommon', config.weight_uncommon),
                ('GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare', config.weight_rare),
                ('GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare', config.weight_veryrare),
                ('GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary', config.weight_legendary),
            ])

        # Maylay shield pool
        config.set_maylay_shields = get_balanced_set(
            config.maylay_shields,
            [
                ('GD_Itempools.ShieldPools.Pool_Shields_Roid_01_Common', config.weight_common),
                ('GD_Itempools.ShieldPools.Pool_Shields_Roid_02_Uncommon', config.weight_uncommon),
                ('GD_Itempools.ShieldPools.Pool_Shields_Roid_04_Rare', config.weight_rare),
                ('GD_Itempools.ShieldPools.Pool_Shields_Roid_05_VeryRare', config.weight_veryrare),
                ('GD_Itempools.ShieldPools.Pool_Shields_Roid_06_Legendary', config.weight_legendary),
            ])

    with open('input-file-rarity.txt', 'r') as df:
        rarity_sections[rarity_key] = df.read().format(
                section_label=rarity_label,
                regular=regular,
                badass=badass,
                )

# Legendary shield pool configuration.
shields = {
    'GD_Itempools.ShieldPools.Pool_Shields_Absorption_06_Legendary': [
        ('1340', 2, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_1340'),
        ('equitas', 3, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_Equitas'),
        ('sponge', 4, 'GD_Iris_SeraphItems.Sponge.Iris_Seraph_Shield_Sponge_Balance'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_Booster_06_Legendary': [
        ('potogold', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_PotOGold'),
        ('bigboomblaster', 2, 'GD_Iris_SeraphItems.BigBoomBlaster.Iris_Seraph_Shield_Booster_Balance'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_Chimera_06_Legendary': [
        ('evolution', 1, 'GD_Orchid_RaidWeapons.Shield.Anshin.Orchid_Seraph_Anshin_Shield_Balance')
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_Juggernaut_06_Legendary': [
        ('hoplite', 1, 'GD_Iris_SeraphItems.Hoplite.Iris_Seraph_Shield_Juggernaut_Balance'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_NovaShields_Explosive_06_Legendary': [
        ('deadlybloom', 0, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_DeadlyBloom'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_Roid_06_Legendary': [
        ('order', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_Order'),
        ('lovethumper', 2, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_04_LoveThumper'),
        ('punchee', 3, 'GD_Iris_SeraphItems.Pun-chee.Iris_Seraph_Shield_Pun-chee_Balance'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_Standard_06_Legendary': [
        ('manlyman', 1, 'GD_Orchid_Shields.A_Item_Custom.S_BladeShield'),
        ('roughrider', 2, 'GD_Sage_Shields.A_Item_Custom.S_BucklerShield'),
        ('antagonist', 3, 'GD_Aster_ItemGrades.Shields.Aster_Seraph_Antagonist_Shield_Balance'),
        ('blockade', 4, 'GD_Aster_ItemGrades.Shields.Aster_Seraph_Blockade_Shield_Balance'),
        ],
    }
for (pool, shieldlist) in shields.items():
    for (label, index, shieldname) in shieldlist:
        set_bi_item_pool('shield_{}'.format(label),
            pool,
            index,
            shieldname,
            invbalance='InventoryBalanceDefinition')

# Regular Stalker shield hotfixes
stalker_shields_real_list = []
prefix = ' '*(4*3)
for config in [regular, badass]:
    for (idx, (dipl_idx, popdef)) in enumerate(config.stalker_dipl):
        stalker_shields_real_list.append("{}level None set {} DefaultItemPoolList[{}].ItemPool ItemPoolDefinition'{}'".format(
            prefix, popdef, dipl_idx, config.regular_shields
            ))

# Only-Maylay Stalker shield hotfixes
stalker_shields_maylay_list = []
prefix = ' '*(4*3)
for config in [regular, badass]:
    for (idx, (dipl_idx, popdef)) in enumerate(config.stalker_dipl):
        stalker_shields_maylay_list.append("{}level None set {} DefaultItemPoolList[{}].ItemPool ItemPoolDefinition'{}'".format(
            prefix, popdef, dipl_idx, config.maylay_shields,
            ))

###
### Generate the mod string
###

with open('input-file-mod.txt') as df:
    mod_str = df.read().format(
        mod_name=mod_name,
        mod_version=mod_version,
        mp=mp,
        regular=regular,
        badass=badass,
        rarity_excellent=rarity_sections['excellent'],
        rarity_better=rarity_sections['better'],
        rarity_stock=rarity_sections['stock'],
        stalker_shields_real="\n\n".join(stalker_shields_real_list),
        stalker_shields_maylay="\n\n".join(stalker_shields_maylay_list),
        )

###
### Output to a file.
###

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
