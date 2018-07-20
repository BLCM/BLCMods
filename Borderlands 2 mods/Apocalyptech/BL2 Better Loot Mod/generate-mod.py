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

# Python script to generate my BL2 Better Loot Mod.  All the drop
# weights and stuff can be controlled by all the variables at the
# top of the file.  Generates a human-readable multiline file which
# must be converted using conv_to_mod.py in order to be loaded by
# Borderlands / FilterTool.

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

mod_name = 'BL2 Better Loot Mod'
mod_version = '1.3.0-prerelease'
output_filename = '{}.blcm'.format(mod_name)

###
### Where we get our mod data from
###

input_filename = 'input-file-mod.txt'

###
### Variables which control drop rates and stuff like that
###

class Config(object):
    """
    Base class which allows us to use constants as format strings
    """

    def set_balanced_pct_reports(self, basename, weights, fixedlen=False):
        """
        Given a list of numerical `weights`, sets some attributes in our
        object based on `basename` which describe the percent chances
        of drops.  Var names will be `basename_pct_idx`, where `idx`
        relates to the position of the weight in question in `weights`.
        If `fixedlen` is true, the percentages will be stored as
        right-aligned strings, otherwise it should be numbers.
        """
        total = sum(weights)
        for (idx, weight) in enumerate(weights):
            varname = '{}_pct_{}'.format(basename, idx)
            pct = weight/total*100
            if pct >= 1:
                pct = round(pct)
            elif pct != 0:
                pct = round(pct, 2)
                if str(pct) == '1.0':
                    pct = 1
            if fixedlen:
                if pct == 0 or pct >= 1:
                    setattr(self, varname, '{:4d}'.format(round(pct)))
                else:
                    setattr(self, varname, '{:4.2f}'.format(pct))
            else:
                setattr(self, varname, pct)

    def set_badass_qty_reports(self, basename, quantities):
        """
        This is only really used when reporting likely numbers of drops from
        the various badass enemy definitions.  Will always set fixed-width
        strings.  Will set the vars `badass_basename_idx`.
        """
        for (idx, quantity) in enumerate(quantities):
            varname = 'badass_{}_{}'.format(basename, idx)
            if int(quantity) == quantity:
                setattr(self, varname, '{:4d}'.format(int(quantity)))
            elif round(quantity,1) == quantity:
                setattr(self, varname, '{:4.1f}'.format(quantity))
            else:
                setattr(self, varname, '{:4.2f}'.format(quantity))

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

class ConfigBase(Config):
    """
    Class to hold all our weights, and other vars which alter the probabilities of
    various things dropping.  Derive from this class to actually define the
    values.
    """

    # Gun Type drop weights.  Note that because these values are going into
    # our hotfix object, these variables *cannot* be successfully overridden
    # in an extending class.
    drop_prob_pistol = 100
    drop_prob_ar = 100
    drop_prob_smg = 100
    drop_prob_shotgun = 100
    drop_prob_sniper = 80
    drop_prob_launcher = 40

    # Drop rates within the "very high roll" pools of dice chests
    dice_vhigh_veryrare = 1
    dice_vhigh_alien = 1
    dice_vhigh_legendary = 0.5

    # 2.5x chance of both kinds of eridium
    eridium_bar_drop = 0.003750       # Stock: 0.001500
    eridium_stick_drop = 0.020000     # Stock: 0.008000

    def full_profile_name(self):
        if self.profile_name_orig:
            return '{} Quality (formerly "{}")'.format(self.profile_name, self.profile_name_orig)
        else:
            return '{} Quality'.format(self.profile_name)

    def relic_weight_string(self):
        """
        Forcing the "Reward" Relic pool to obey our custom weights.  There's
        22 of these definitions which are all identical (and one outlier), so
        we're going use a loop rather than a lot of copy+paste.  This is also
        happening inside our ConfigBase class so that our weights can get
        applied dynamically.
        """
        relic_weight_parts = []
        for relic_type in [
                'AggressionA',
                'AggressionB',
                'AggressionC',
                'AggressionD',
                'AggressionE',
                'AggressionF',
                'AllegianceA',
                'AllegianceB',
                'AllegianceC',
                'AllegianceD',
                'AllegianceE',
                'AllegianceF',
                'AllegianceG',
                'AllegianceH',
                'Elemental',
                'Proficiency',
                'Protection',
                'Resistance',
                'Stockpile',
                'Strength',
                'Tenacity',
                'Vitality',
                ]:
            relic_weight_parts.append("""
                set GD_Artifacts.PartLists.Parts_{relic_type}_Rare ConsolidatedAttributeInitData
                (
                    (
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    (
                        BaseValueConstant=100.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    (
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    (
                        BaseValueConstant={relic_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1
                    ),
                    (
                        BaseValueConstant={relic_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1
                    )
                )
""".format(
    relic_type=relic_type,
    relic_base_rare=self.relic_base_rare,
    relic_base_veryrare=self.relic_base_veryrare,
    ))
        # This one is the one that's slightly different
        relic_weight_parts.append("""
                set GD_Artifacts.PartLists.Parts_Elemental_Status_Rare ConsolidatedAttributeInitData
                (
                    (
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    (
                        BaseValueConstant=100.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    (
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    (
                        BaseValueConstant=100.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant=1.000000
                    ),
                    (
                        BaseValueConstant={relic_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1
                    ),
                    (
                        BaseValueConstant={relic_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1
                    )
                )
""".format(
    relic_type=relic_type,
    relic_base_rare=self.relic_base_rare,
    relic_base_veryrare=self.relic_base_veryrare,
    ))

        # Return the string
        return ''.join(relic_weight_parts).lstrip()

###
### Config classes which define the actual contstants that we use
### for things like drop weights, etc.
###

class ConfigLootsplosion(ConfigBase):
    """
    This is our default config, which I personally find quite pleasant.
    Many folks will consider this a bit too OP/Extreme.
    """

    profile_name = 'Excellent'
    profile_name_orig = 'Lootsplosion'

    # Custom weapon drop scaling
    weapon_base_common = 8
    weapon_base_uncommon = 85
    weapon_base_rare = 65
    weapon_base_veryrare = 50
    weapon_base_alien = 30
    weapon_base_legendary = 3
    weapon_base_iris_cobra = 1

    # Custom COM drop scaling (identical to weapons, apart from an additional Alignment COM pool)
    cm_base_common = weapon_base_common
    cm_base_uncommon = weapon_base_uncommon
    cm_base_rare = weapon_base_rare
    cm_base_veryrare = weapon_base_veryrare
    cm_base_alignment = 30
    cm_base_legendary = weapon_base_legendary

    # Custom grenade drop scaling (identical to weapons)
    grenade_base_common = weapon_base_common
    grenade_base_uncommon = weapon_base_uncommon
    grenade_base_rare = weapon_base_rare
    grenade_base_veryrare = weapon_base_veryrare
    grenade_base_legendary = weapon_base_legendary

    # Custom shield drop scaling (identical to weapons)
    shield_base_common = weapon_base_common
    shield_base_uncommon = weapon_base_uncommon
    shield_base_rare = weapon_base_rare
    shield_base_veryrare = weapon_base_veryrare
    shield_base_legendary = weapon_base_legendary

    # Relic drop weights
    relic_drop_scale_all = 0.2
    relic_drop_scale_reward = 1

    # Custom relic drop scaling, within "ArtifactsReward"
    relic_base_rare = 1.0
    relic_base_veryrare = 2.0

    # Drop rates for "regular" treasure chests
    treasure_base_common = 0
    treasure_base_uncommon = 0
    treasure_base_rare = 20
    treasure_base_veryrare = 60
    treasure_base_alien = 30
    treasure_base_legendary = 5

    # Drop rates for "epic" treasure chests
    epic_base_common = 0
    epic_base_uncommon = 0
    epic_base_rare = 0
    epic_base_veryrare = 1
    epic_base_alien = 1
    epic_base_legendary = 0.3

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.4
    badass_pool_alien = 0.4
    badass_pool_epicchest = 0.1

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 1
    super_badass_pool_veryrare = 1
    super_badass_pool_alien = 1
    super_badass_pool_legendary = 1
    super_badass_pool_epicchest = 1

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 1
    ultimate_badass_pool_veryrare_2 = 0.5
    ultimate_badass_pool_alien_1 = 1
    ultimate_badass_pool_alien_2 = 0.5
    ultimate_badass_pool_legendary_1 = 1
    ultimate_badass_pool_legendary_2 = 0.5
    ultimate_badass_pool_legendary_3 = 0.25
    ultimate_badass_pool_epicchest_1 = 1
    ultimate_badass_pool_epicchest_2 = 0.5
    ultimate_badass_pool_epicchest_3 = 0.5

class ConfigReasonable(ConfigLootsplosion):
    """
    Alternate config which has slightly-more-reasonable drop rates for stuff
    like legendaries.  Unsurprisingly, most folks find my default values a
    bit excessive.
    """

    profile_name = 'Very Good'
    profile_name_orig = 'Reasonable'

    # Weapon drops
    weapon_base_common = 32.75
    weapon_base_uncommon = 35
    weapon_base_rare = 25
    weapon_base_veryrare = 5
    weapon_base_alien = 2
    weapon_base_legendary = 0.25
    weapon_base_iris_cobra = 2

    # Class mods
    cm_base_common = weapon_base_common
    cm_base_uncommon = weapon_base_uncommon
    cm_base_rare = weapon_base_rare
    cm_base_veryrare = weapon_base_veryrare
    cm_base_alignment = 2
    cm_base_legendary = weapon_base_legendary

    # Custom grenade drop scaling (identical to weapons)
    grenade_base_common = weapon_base_common
    grenade_base_uncommon = weapon_base_uncommon
    grenade_base_rare = weapon_base_rare
    grenade_base_veryrare = weapon_base_veryrare
    grenade_base_legendary = weapon_base_legendary

    # Custom shield drop scaling (identical to weapons)
    shield_base_common = weapon_base_common
    shield_base_uncommon = weapon_base_uncommon
    shield_base_rare = weapon_base_rare
    shield_base_veryrare = weapon_base_veryrare
    shield_base_legendary = weapon_base_legendary

    # Relic drop weights
    relic_drop_scale_all = 0.6
    relic_drop_scale_reward = 0.6

    # Custom relic drop scaling, within "ArtifactsReward"
    relic_base_rare = 2.0
    relic_base_veryrare = 1.0

    # Drop rates for "regular" treasure chests
    treasure_base_common = 32.5
    treasure_base_uncommon = 40
    treasure_base_rare = 20
    treasure_base_veryrare = 5
    treasure_base_alien = 3
    treasure_base_legendary = 0.5

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = 25
    epic_base_rare = 49
    epic_base_veryrare = 15
    epic_base_alien = 10
    epic_base_legendary = 1

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.2
    badass_pool_alien = 0.15
    badass_pool_epicchest = 0.1

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 1
    super_badass_pool_veryrare = 0.4
    super_badass_pool_alien = 0.15
    super_badass_pool_legendary = 0.03
    super_badass_pool_epicchest = 1

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 1
    ultimate_badass_pool_veryrare_2 = 0
    ultimate_badass_pool_alien_1 = 0.4
    ultimate_badass_pool_alien_2 = 0
    ultimate_badass_pool_legendary_1 = 0.08
    ultimate_badass_pool_legendary_2 = 0
    ultimate_badass_pool_legendary_3 = 0
    ultimate_badass_pool_epicchest_1 = 1
    ultimate_badass_pool_epicchest_2 = 1
    ultimate_badass_pool_epicchest_3 = 1

# The profiles we'll generate
profiles = [
    ConfigLootsplosion(),
    ConfigReasonable(),
    ]

class QtyExcellent(Config):
    """
    Excellent drop quantities - bosses will drop as many items as they
    have unique items in their pools.  Formerly this was the "Lootsplosion"
    defaults.
    """

    qty_index = 'excellent'
    qty_label = 'Excellent Drop Quantities (formerly "Lootsplosion")'

    quantity_default_two = '2'
    quantity_default_three = '3'

    quantity_chubby = '4'
    quantity_terra = '7'
    quantity_vermivorous = '5'
    quantity_warrior = '8'
    quantity_hyperius_legendary = '7'
    quantity_hyperius_seraph = '4'
    quantity_gee_seraph = '4'
    quantity_gee_legendary = '6'
    quantity_sorcerers_daughter = '4'

    # Voracidous quantities have to be done slightly differently, because both
    # Dexiduous and Voracidous use the same Seraph and Legendary pools for their
    # unique drops, but Dexi calls it multiple times, whereas Vorac just calls
    # it the once (by default).  So upping the quantity for Vorac makes Dexi's
    # drops totally ludicrous.  So instead, we're just gonna specify the pool
    # multiple times in Vorac's ItemPool.  This is lame, but should let both
    # of them coexist.
    voracidous_drop_seraph_1 = 1
    voracidous_drop_seraph_2 = 1
    voracidous_drop_seraph_3 = 1
    voracidous_drop_seraph_4 = 1
    voracidous_drop_legendary_1 = 1
    voracidous_drop_legendary_2 = 1
    voracidous_drop_legendary_3 = 1
    voracidous_drop_legendary_4 = 1

class QtyImproved(Config):
    """
    Improved drop quantities - bosses with more than one unique item will
    spawn more than one, though not necessarily as many as there are items
    in the pool.  Formerly the "Reasonable" preset.
    """

    qty_index = 'improved'
    qty_label = 'Improved Drop Quantities (formerly "Reasonable")'

    quantity_default_two = '2'
    quantity_default_three = '2'

    quantity_chubby = '2'
    quantity_terra = '4'
    quantity_vermivorous = '3'
    quantity_warrior = '4'
    quantity_hyperius_legendary = '2'
    quantity_hyperius_seraph = '2'
    quantity_gee_seraph = '2'
    quantity_gee_legendary = '2'
    quantity_sorcerers_daughter = '2'

    # Voracidous quantities have to be done slightly differently, because both
    # Dexiduous and Voracidous use the same Seraph and Legendary pools for their
    # unique drops, but Dexi calls it multiple times, whereas Vorac just calls
    # it the once (by default).  So upping the quantity for Vorac makes Dexi's
    # drops totally ludicrous.  So instead, we're just gonna specify the pool
    # multiple times in Vorac's ItemPool.  This is lame, but should let both
    # of them coexist.
    voracidous_drop_seraph_1 = 1
    voracidous_drop_seraph_2 = 1
    voracidous_drop_seraph_3 = 0
    voracidous_drop_seraph_4 = 0
    voracidous_drop_legendary_1 = 1
    voracidous_drop_legendary_2 = 1
    voracidous_drop_legendary_3 = 0
    voracidous_drop_legendary_4 = 0

class QtyStock(Config):
    """
    Stock drop quantities - bosses will only ever drop a single item from
    their unique drop pools.  (This is the same as the game's stock drop
    quantities.
    """

    qty_index = 'stock'
    qty_label = 'Stock Drop Quantities (just one per boss)'

    quantity_default_two = '1'
    quantity_default_three = '1'

    quantity_chubby = '1'
    quantity_terra = '1'
    quantity_vermivorous = '1'
    quantity_warrior = '1'
    quantity_hyperius_legendary = '1'
    quantity_hyperius_seraph = '1'
    quantity_gee_seraph = '1'
    quantity_gee_legendary = '1'
    quantity_sorcerers_daughter = '1'

    # Voracidous quantities have to be done slightly differently, because both
    # Dexiduous and Voracidous use the same Seraph and Legendary pools for their
    # unique drops, but Dexi calls it multiple times, whereas Vorac just calls
    # it the once (by default).  So upping the quantity for Vorac makes Dexi's
    # drops totally ludicrous.  So instead, we're just gonna specify the pool
    # multiple times in Vorac's ItemPool.  This is lame, but should let both
    # of them coexist.
    voracidous_drop_seraph_1 = 1
    voracidous_drop_seraph_2 = 0
    voracidous_drop_seraph_3 = 0
    voracidous_drop_seraph_4 = 0
    voracidous_drop_legendary_1 = 1
    voracidous_drop_legendary_2 = 0
    voracidous_drop_legendary_3 = 0
    voracidous_drop_legendary_4 = 0

# Remove bias for dropping Pistols in the main game.  Also buffs drop rates
# for snipers and launchers, though it does not bring them up to the level
# of pistols/ARs/SMGs/shotguns.  This could be done with a `set` statement, but
# this is more concise.
for (number, rarity) in [
        ('01', 'Common'),
        ('02', 'Uncommon'),
        ('04', 'Rare'),
        ('05', 'VeryRare'),
        ('05', 'VeryRare_Alien'),
        ('06', 'Legendary'),
        ]:
    for (idx, (guntype, gunprob)) in enumerate([
            ('Pistol', ConfigBase.drop_prob_pistol),
            ('AR', ConfigBase.drop_prob_ar),
            ('SMG', ConfigBase.drop_prob_smg),
            ('Shotgun', ConfigBase.drop_prob_shotgun),
            ('Sniper', ConfigBase.drop_prob_sniper),
            ('Launcher', ConfigBase.drop_prob_launcher),
            ]):
        mp.register_str('normalize_weapon_types_{}_{}'.format(rarity, guntype),
            'level None set GD_Itempools.WeaponPools.Pool_Weapons_All_{}_{} BalancedItems[{}].Probability.BaseValueConstant {}'.format(
                number,
                rarity,
                idx,
                gunprob))

# Bandit Cooler nerf ("needed" in v1.2.0 'cause of our weighted pool fixes)
for idx, objname in enumerate([
        'GD_Balance_Treasure.LootableGrades.ObjectGrade_Bandit_Cooler',
        'GD_Balance_Treasure.LootableGradesTrap.MidgetBandit.ObjectGrade_BanditCooler_MidgetBandit',
        ]):
    mp.register_str('bandit_cooler_nerf_{}'.format(idx),
        """level None set {} DefaultLoot[4].ItemAttachments[0].ItemPool ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common'""".format(
            objname
            ))

# Make Laney's Dwarves drop crystals, and be likely to drop a gemstone between 'em
for num in range(1, 8):
    mp.register_str('laney_dwarf_drop_{}'.format(num),
        """level Fridge_P set GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf{} DefaultItemPoolList
        (
            (
                ItemPool=ItemPoolDefinition'GD_ItempoolsEnemyUse.WeaponPools.Pool_Weapons_SMG_EnemyUse',
                PoolProbability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                )
            ),
            (
                ItemPool=ItemPoolDefinition'GD_ItempoolsEnemyUse.Shields.Pool_Shields_Standard_EnemyUse',
                PoolProbability=(
                    BaseValueConstant=0.250000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                )
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Crystal',
                PoolProbability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                )
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_04_Gemstone',
                PoolProbability=(
                    BaseValueConstant=0.200000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                )
            )
        )
        """.format(num))

# Improve The Warrior drops
for (num, pool) in [
        (12, 'GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_LongGuns'),
        (15, 'GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_Pistols'),
        (17, 'GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_Launchers'),
        ]:
    mp.register_str('warrior_drop_{}'.format(num),
        "level Boss_Volcano_P set GD_FinalBoss.Character.AIDef_FinalBoss:AIBehaviorProviderDefinition_1.Behavior_SpawnItems_{} ItemPoolList[0].ItemPool ItemPoolDefinition'{}'".format(num, pool))

# Make Witch Doctors drop some slightly-more-interesting loot
witch_extra_pools = """(
        ItemPool=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_ArtifactsReward',
        PoolProbability=(
            BaseValueConstant=1.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=0.400000
        )
    ),
    (
        ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
        PoolProbability=(
            BaseValueConstant=1.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )
    )"""
for doctor in ['Fire', 'Shock', 'Slag', 'Slow', 'Vampire']:
    mp.register_str('witchdoctor_{}'.format(doctor),
        """level None set GD_Sage_Pop_Natives.Balance.PawnBalance_WitchDoctor{} DefaultItemPoolList
        (
            (
                ItemPool=ItemPoolDefinition'GD_CustomItemPools_Sage.Fanboat.Pool_Customs_Fanboat_All',
                PoolProbability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_VehicleSkins',
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                )
            ),
            {}
        )""".format(doctor, witch_extra_pools))

# And do the same for the Witch Doctors in the Son of Crawmerax Headhunter Pack
for (label, classname) in [
        ('Slow', 'GD_Nast_Native_WitchDoctorSlow.Population.PawnBalance_Nast_WitchDoctorSlow'),
        ('Slag', 'GD_Nast_WitchDoctorSlag.Population.PawnBalance_Nast_WitchDoctorSlag'),
        ]:
    mp.register_str('crawmerax_witch_{}'.format(label),
        'level Easter_P set {} DefaultItemPoolList ({})'.format(classname, witch_extra_pools))

# Badass Borok Fixes
for borok in ['Corrosive', 'Fire', 'Shock', 'Slag']:
    mp.register_str('badass_borok_{}'.format(borok),
        "level None set GD_Sage_Pop_Rhino.Balance.PawnBalance_Sage_RhinoBadass{} DefaultItemPoolIncludedLists[0] ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'".format(borok))

# Voracidous drop pool seraph crystal fix
for idx in range(3):
    mp.register_str('vorac_seraph_{}'.format(idx),
        "level Sage_Cliffs_P set GD_Sage_ItemPools.Raid.PoolList_Sage_Raid_Items ItemPools[{}].ItemPool ItemPoolDefinition'GD_Sage_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7_Drop'".format(idx))

# Normalize the probabilities for the Sorcerer's Daughter legendary pool
for num in range(4):
    mp.register_str('dragonkeep_sorcerersdaughter_normalize_{}'.format(num),
        'level Dungeon_P set GD_AngelBoss.LootPools.Pool_AngelBossRunnable BalancedItems[{}].Probability.BaseValueScaleConstant 1.0'.format(num))

# Make the individual Jack battles at the end of Dragon Keep drop from a badass pool
for suffix in ['', '_Demon', '_DemonFall', '_Phase2']:
    mp.register_str('dragonkeep_jack{}_drop1'.format(suffix),
        "level CastleKeep_P set GD_Aster_Pop_Wizards.Balance.PawnBalance_JackWarlock{} DefaultItemPoolIncludedLists[0] ItemPoolListDefinition'GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear'".format(suffix))

# Three tributes from the Wattle Gobbler Headhunter pack don't actually drop
# anything, whereas the others drop from the badass pool.  Fix that.
for (name, classname) in [
        ('cynder', 'GD_IncineratorFemale.Balance.PawnBalance_IncineratorFemale'),
        ('strip', 'GD_FleshripperFemale.Balance.PawnBalance_FleshripperFemale'),
        ('flay', 'GD_FleshripperMale.Balance.PawnBalance_FleshripperMale'),
        ]:
    mp.register_str('wattle_tribute_{}'.format(name),
        "level Hunger_P set {} DefaultItemPoolIncludedLists (ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear')".format(classname))

# Make the BLNG Loader drop from the Badass pool, and add a lot of money drops
money_pool_list=["""
    (
        ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',
        PoolProbability=(
            BaseValueConstant=1.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )
    )"""]*30
mp.register_str('wedding_blng_drop',
    "level Distillery_P set GD_BlingLoader.Population.PawnBalance_BlingLoader DefaultItemPoolList ({})".format(','.join(money_pool_list)))

# Fix some container drop pools which reference an item (Pool_BuffDrinks_Euphoria)
# which doesn't actually exist, causing that loot possibility to never actually
# get chosen.  We'll replace with Pool_BuffDrinks_HealingRegen.  Most of these could
# happen via a regular `set` statement, but this lets us be much more concise.
for (idx, (classname, propname, loot_idx, attachment_idx)) in enumerate([
        ('GD_Itempools.ListDefs.EpicChestRedLoot', 'LootData', 4, 11),
        ('GD_Itempools.ListDefs.EpicChestBanditLoot', 'LootData', 3, 11),
        ('GD_Balance_Treasure.ChestGrades.ObjectGrade_DahlEpic', 'DefaultLoot', 4, 11),
        ('GD_Balance_Treasure.ChestGrades.ObjectGrade_DahlEpic_BearerBadNews', 'DefaultLoot', 4, 11),
        ('GD_Itempools.ListDefs.EpicChestHyperionLoot', 'LootData', 3, 11),
        ('GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic', 'DefaultLoot', 4, 11),
        ('GD_Lobelia_DahlDigi.LootableGradesUnique.ObjectGrade_DalhEpicCrate_Digi', 'DefaultLoot', 4, 11),
        ]):
    mp.register_str('euphoria_fix_{}'.format(idx),
        'level None set {} {}[{}].ItemAttachments[{}].ItemPool GD_Itempools.BuffDrinkPools.Pool_BuffDrinks_HealingRegen'.format(
            classname,
            propname,
            loot_idx,
            attachment_idx,
            ))

# Legendary Pool management
unique_hotfixes = []
pearl_hotfixes = []
seraph_hotfixes = []
for (guntype, legendaries, uniques, pearls, seraphs) in [
        (
            'AssaultRifles',
            [
                # Regular Legendaries
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Bandit_5_Madhouse',
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Dahl_5_Veruc',
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBuster',
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Torgue_5_KerBlaster',
                'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Vladof_5_Sherdifier',
            ],
            [
                # Uniques
                'GD_Aster_Weapons.AssaultRifles.AR_Bandit_3_Ogre',
                'GD_Iris_Weapons.AssaultRifles.AR_Torgue_3_BoomPuppy',
                'GD_Iris_Weapons.AssaultRifles.AR_Vladof_3_Kitten',
                'GD_Orchid_BossWeapons.AssaultRifle.AR_Jakobs_3_Stinkpot',
                'GD_Orchid_BossWeapons.AssaultRifle.AR_Vladof_3_Rapier',
                'GD_Sage_Weapons.AssaultRifle.AR_Bandit_3_Chopper',
                'GD_Sage_Weapons.AssaultRifle.AR_Jakobs_3_DamnedCowboy',
                'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Dahl_3_Scorpio',
                'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Jakobs_3_Stomper',
                'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Torgue_3_EvilSmasher',
                'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Vladof_3_Hail',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.AssaultRifle.AR_Bandit_6_Sawbar',
                'GD_Gladiolus_Weapons.AssaultRifle.AR_Dahl_6_Bearcat',
                'GD_Lobelia_Weapons.AssaultRifles.AR_Jakobs_6_Bekah',
            ],
            [
                # Seraphs
                'GD_Aster_RaidWeapons.AssaultRifles.Aster_Seraph_Seeker_Balance',
                'GD_Orchid_RaidWeapons.AssaultRifle.Seraphim.Orchid_Seraph_Seraphim_Balance',
                'GD_Sage_RaidWeapons.AssaultRifle.Sage_Seraph_LeadStorm_Balance',
            ],
        ),
        (
            'Launchers',
            [
                # Regular Legendaries
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom',
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Pyrophobia',
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Tediore_5_Bunny',
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem',
                'GD_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol',
                'GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet',
            ],
            [
                # Uniques
                'GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_3_TheHive',
                'GD_Orchid_BossWeapons.Launcher.RL_Torgue_3_12Pounder',
                'GD_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer',
                'GD_Weap_Launchers.A_Weapons_Unique.RL_Bandit_3_Roaster',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.Launchers.RL_Torgue_6_Tunguska',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.RPG.Ahab.Orchid_Seraph_Ahab_Balance',
            ],
        ),
        (
            'Pistols',
            [
                # Regular Legendaries
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Gub',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Gunerang',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Hornet',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Vladof_5_Infinity',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Maliwan_5_ThunderballFists',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun',
            ],
            [
                # Uniques
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Judge',
                'GD_Aster_Weapons.Pistols.Pistol_Maliwan_3_GrogNozzle',
                'GD_Orchid_BossWeapons.Pistol.Pistol_Jakobs_ScarletsGreed',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensHead',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Dahlminator',
                'GD_Iris_Weapons.Pistols.Pistol_Torgue_3_PocketRocket',
                'GD_Sage_Weapons.Pistols.Pistol_Jakobs_3_Rex',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Law',
                'GD_Orchid_BossWeapons.Pistol.Pistol_Maliwan_3_LittleEvie',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Teapot',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Vladof_3_Veritas',
                'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Bandit_3_Tenderbox',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.Pistol.Pistol_Jakobs_6_Unforgiven',
                'GD_Gladiolus_Weapons.Pistol.Pistol_Vladof_6_Stalker',
                'GD_Lobelia_Weapons.Pistol.Pistol_Maliwan_6_Wanderlust',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.Pistol.Devastator.Orchid_Seraph_Devastator_Balance',
                'GD_Sage_RaidWeapons.Pistol.Sage_Seraph_Infection_Balance',
                'GD_Aster_RaidWeapons.Pistols.Aster_Seraph_Stinger_Balance',
            ],
        ),
        (
            'Shotguns',
            [
                # Regular Legendaries
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun',
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Tediore_5_Deliverance',
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker',
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker',
                'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall',
            ],
            [
                # Uniques
                'GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Hydra',
                'GD_Orchid_BossWeapons.Shotgun.SG_Bandit_3_JollyRoger',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_HeartBreaker',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Dog',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Blockhead',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo',
                'GD_Orchid_BossWeapons.Shotgun.SG_Jakobs_3_OrphanMaker',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Landscaper',
                'GD_Iris_Weapons.Shotguns.SG_Hyperion_3_SlowHand',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_Shotgun1340',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_RokSalt',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_TidalWave',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Teeth',
                'GD_Aster_Weapons.Shotguns.SG_Torgue_3_SwordSplosion',
                'GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Twister',
                'GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Triquetra',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.Shotgun.SG_Hyperion_6_Butcher',
                'GD_Lobelia_Weapons.Shotguns.SG_Torgue_6_Carnage',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.Shotgun.Spitter.Orchid_Seraph_Spitter_Balance',
                'GD_Sage_RaidWeapons.Shotgun.Sage_Seraph_Interfacer_Balance',
                'GD_Aster_RaidWeapons.Shotguns.Aster_Seraph_Omen_Balance',
            ],
        ),
        (
            'SMG',
            [
                # Regular Legendaries
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Bandit_5_Slagga',
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_BabyMaker',
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Emperor',
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire',
                'GD_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch',
            ],
            [
                # Uniques
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_BoneShredder',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Bane',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Commerce',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Chulainn',
                'GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Lascaux',
                'GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk',
                'GD_Sage_Weapons.SMG.SMG_Hyperion_3_YellowJacket',
                'GD_Aster_Weapons.SMGs.SMG_Bandit_3_Orc',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.SMG.SMG_Tediore_6_Avenger',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.SMG.Tattler.Orchid_Seraph_Tattler_Balance',
                'GD_Orchid_RaidWeapons.SMG.Actualizer.Orchid_Seraph_Actualizer_Balance',
                'GD_Aster_RaidWeapons.SMGs.Aster_Seraph_Florentine_Balance',
            ],
        ),
        (
            'SniperRifles',
            [
                # Regular Legendaries
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork',
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Lyudmila',
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Volcano',
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher',
                'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader',
            ],
            [
                # Uniques
                'GD_Sage_Weapons.SniperRifles.Sniper_Jakobs_3_ElephantGun',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Buffalo',
                'GD_Iris_Weapons.SniperRifles.Sniper_Jakobs_3_Cobra',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie',
                'GD_Orchid_BossWeapons.SniperRifles.Sniper_Maliwan_3_Pimpernel',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Morningstar',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_Sloth',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Tresspasser',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Longbow',
            ],
            [
                # Pearls
                'GD_Gladiolus_Weapons.sniper.Sniper_Maliwan_6_Storm',
                'GD_Lobelia_Weapons.sniper.Sniper_Jakobs_6_Godfinger',
            ],
            [
                # Seraphs
                'GD_Orchid_RaidWeapons.sniper.Patriot.Orchid_Seraph_Patriot_Balance',
                'GD_Sage_RaidWeapons.sniper.Sage_Seraph_HawkEye_Balance',
            ],
        ),
        ]:

    # First set up a hotfix for the base pool initialization
    initial_pool = []
    for legendary in legendaries:
        initial_pool.append((legendary, 1, 'WeaponBalanceDefinition'))
    for i in range(len(uniques) + len(pearls) + len(seraphs)):
        initial_pool.append((None, 0))
    mp.register_str('weapon_pool_clear_{}'.format(guntype.lower()),
        'level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems {}'.format(
            guntype,
            mp.get_balanced_items(initial_pool),
            ))

    # Hotfixes to add uniques
    for (idx, unique) in enumerate(uniques):
        unique_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + idx,
                unique
                ))

    # Hotfixes to add pearls
    for (idx, pearl) in enumerate(pearls):
        pearl_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + len(uniques) + idx,
                pearl
                ))

    # Hotfixes to add seraphs
    for (idx, seraph) in enumerate(seraphs):
        seraph_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + len(uniques) + len(pearls) + idx,
                seraph
                ))

mp.register_str('legendary_unique_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in unique_hotfixes]
    ))

mp.register_str('legendary_pearl_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in pearl_hotfixes]
    ))

mp.register_str('legendary_seraph_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in seraph_hotfixes]
    ))

# Legendary shield/grenade pool configuration.  Doing this a bit differently since there's
# not nearly as many shields/grenades to handle as weapons.

items = {
    'shield': {
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
        },
    'grenade': {
        'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary': [
            ('breath_of_terra', 12, 'GD_GrenadeMods.A_Item_Legendary.GM_FlameSpurt'),
            ('fireball', 13, 'GD_Aster_GrenadeMods.A_Item.GM_Fireball'),
            ('fuster_cluck', 14, 'GD_GrenadeMods.A_Item_Custom.GM_FusterCluck'),
            ('kiss_of_death', 15, 'GD_GrenadeMods.A_Item_Custom.GM_KissOfDeath'),
            ('lightning_bolt', 16, 'GD_Aster_GrenadeMods.A_Item.GM_LightningBolt'),
            ('magic_missile', 17, 'GD_Aster_GrenadeMods.A_Item.GM_MagicMissileRare'),
            ('crossfire', 18, 'GD_Iris_SeraphItems.Crossfire.Iris_Seraph_GrenadeMod_Crossfire_Balance'),
            ('meteor_shower', 19, 'GD_Iris_SeraphItems.MeteorShower.Iris_Seraph_GrenadeMod_MeteorShower_Balance'),
            ('o_negative', 20, 'GD_Iris_SeraphItems.ONegative.Iris_Seraph_GrenadeMod_ONegative_Balance'),
            ],
        },
    }
for (itemtype, itemdict) in items.items():
    for (pool, itemlist) in itemdict.items():
        for (label, index, itemname) in itemlist:
            mp.set_bi_item_pool('{}_{}'.format(itemtype, label),
                pool,
                index,
                itemname,
                invbalance='InventoryBalanceDefinition')

# Relics are a bit weirder since they don't *really* have rarity-level pools
# like everything else.  There *is* technically a "Legendary" pool for them,
# but it's not really used the way any other legendary pool is (the only "true"
# legendary relic isn't meant to be world-droppable anyway).  So, these are
# handled a bit separately
for (label, index, relic, weight) in [
        # Leg:
        ('blood_terra', 10, 'GD_Artifacts.A_Item_Unique.A_Terramorphous', 0.5),
        # Uniques:
        ('midnight_star', 11, 'GD_Orchid_Artifacts.A_Item_Unique.A_Blade', 0.5),
        ('deputys_badge', 12, 'GD_Artifacts.A_Item_Unique.A_Deputy', 0.5),
        ('opportunity', 13, 'GD_Artifacts.A_Item_Unique.A_Opportunity', 0.5),
        ('endowment', 14, 'GD_Artifacts.A_Item_Unique.A_Endowment', 0.5),
        ('amulet', 15, 'GD_Aster_Artifacts.A_Item_Unique.A_MysteryAmulet', 0.25),
        ('sheriffs_badge', 16, 'GD_Artifacts.A_Item_Unique.A_Sheriff', 0.5),
        ('afterburner', 17, 'GD_Artifacts.A_Item_Unique.A_Afterburner', 0.5),
        # E-Tech:
        ('ancients_blood', 18, 'GD_Gladiolus_Artifacts.A_Item.A_VitalityStockpile_VeryRare', 0.5),
        ('ancients_bone', 19, 'GD_Gladiolus_Artifacts.A_Item.A_ElementalProficiency_VeryRare', 0.5),
        ('ancients_heart_1', 20, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityAssault_VeryRare', 0.25),
        ('ancients_heart_2', 21, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityLauncher_VeryRare', 0.25),
        ('ancients_heart_3', 22, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityPistol_VeryRare', 0.25),
        ('ancients_heart_4', 23, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityShotgun_VeryRare', 0.25),
        ('ancients_heart_5', 24, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacitySMG_VeryRare', 0.25),
        ('ancients_heart_6', 25, 'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacitySniper_VeryRare', 0.25),
        ('ancients_skin', 26, 'GD_Gladiolus_Artifacts.A_Item.A_ResistanceProtection_VeryRare', 0.5),
        # Seraph:
        ('seraphs_blood', 27, 'GD_Orchid_Artifacts.A_Item_Unique.A_SeraphBloodRelic', 0.5),
        ('seraphs_breath', 28, 'GD_Sage_Artifacts.A_Item.A_SeraphBreath', 0.5),
        ('seraphs_might', 29, 'GD_Iris_SeraphItems.Might.Iris_Seraph_Artifact_Might_Balance', 0.5),
        ('seraphs_shadow', 30, 'GD_Aster_Artifacts.A_Item_Unique.A_SeraphShadow', 0.5),
        ]:
    mp.set_bi_item_pool('relic_{}'.format(label),
        'GD_Itempools.ArtifactPools.Pool_ArtifactsReward',
        index,
        relic,
        invbalance='InventoryBalanceDefinition',
        scale=weight,
        )

###
### Generate our quality category strings
###

qualities = {}
for profile in profiles:

    profile.set_balanced_pct_reports('drop_weapon', [
            profile.weapon_base_common,
            profile.weapon_base_uncommon,
            profile.weapon_base_rare,
            profile.weapon_base_veryrare,
            profile.weapon_base_alien,
            profile.weapon_base_legendary,
            ], fixedlen=True)
    # We're assuming that all items have the same percentages, which at the
    # moment is true.  It's possible that at some point in the future that'll
    # become Not True, and we'll have more work to do.
    profile.set_balanced_pct_reports('drop_items', [
            profile.cm_base_common,
            profile.cm_base_uncommon,
            profile.cm_base_rare,
            profile.cm_base_veryrare,
            profile.cm_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('treasure_weapon', [
            profile.treasure_base_common,
            profile.treasure_base_uncommon,
            profile.treasure_base_rare,
            profile.treasure_base_veryrare,
            profile.treasure_base_alien,
            profile.treasure_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('treasure_items', [
            profile.treasure_base_common,
            profile.treasure_base_uncommon,
            profile.treasure_base_rare,
            profile.treasure_base_veryrare,
            profile.treasure_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('epic_weapon', [
            profile.epic_base_uncommon,
            profile.epic_base_rare,
            profile.epic_base_veryrare,
            profile.epic_base_alien,
            profile.epic_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('epic_items', [
            profile.epic_base_uncommon,
            profile.epic_base_rare,
            profile.epic_base_veryrare,
            profile.epic_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('relic_reward', [
            profile.relic_base_rare,
            profile.relic_base_veryrare,
            ])
    profile.set_badass_qty_reports('regular', [
            profile.badass_pool_veryrare,
            profile.badass_pool_alien,
            profile.badass_pool_epicchest,
            ])
    profile.set_badass_qty_reports('super', [
            profile.super_badass_pool_rare,
            profile.super_badass_pool_veryrare,
            profile.super_badass_pool_alien,
            profile.super_badass_pool_legendary,
            profile.super_badass_pool_epicchest,
            ])
    profile.set_badass_qty_reports('ultimate', [
            profile.ultimate_badass_pool_veryrare_1 + profile.ultimate_badass_pool_veryrare_2,
            profile.ultimate_badass_pool_alien_1 + profile.ultimate_badass_pool_alien_2,
            profile.ultimate_badass_pool_legendary_1 + profile.ultimate_badass_pool_legendary_2 + profile.ultimate_badass_pool_legendary_3,
            profile.ultimate_badass_pool_epicchest_1 + profile.ultimate_badass_pool_epicchest_2 + profile.ultimate_badass_pool_epicchest_3,
            ])

    with open('input-file-quality.txt') as df:
        qualities[profile.profile_name] = df.read().format(
                config=profile,
                mp=mp,
                relic_pct=round(profile.relic_drop_scale_reward/(profile.relic_drop_scale_all+profile.relic_drop_scale_reward)*100),
                )

###
### Generate our drop quantity category strings
###

boss_quantities = {}
for qty in [QtyExcellent(), QtyImproved(), QtyStock()]:
    vorac_legendary_qty = qty.voracidous_drop_legendary_1 + \
            qty.voracidous_drop_legendary_2 + \
            qty.voracidous_drop_legendary_3 + \
            qty.voracidous_drop_legendary_4
    vorac_seraph_qty = qty.voracidous_drop_seraph_1 + \
            qty.voracidous_drop_seraph_2 + \
            qty.voracidous_drop_seraph_3 + \
            qty.voracidous_drop_seraph_4
    with open('input-file-quantity.txt') as df:
        boss_quantities[qty.qty_index] = df.read().format(
                config=qty,
                mp=mp,
                vorac_legendary_qty=vorac_legendary_qty,
                vorac_seraph_qty=vorac_seraph_qty,
                )

###
### Generate our boss unique drop strings
###

boss_drops = {}
for (label, key, unique_pct, rare_pct) in [
        ('Guaranteed', 'guaranteed', 1, 1),
        ('Very Improved', 'veryimproved', .5, .75),
        ('Improved', 'improved', .33, .60),
        ('Slightly Improved', 'slight', .22, .45),
        ('Stock', 'stock', .1, .33),
        ]:

    with open('input-file-droprate.txt', 'r') as df:
        boss_drops[key] = df.read().format(
                section_label='{} ({}% Uniques, {}% Rares)'.format(
                    label, round(unique_pct*100), round(rare_pct*100)),
                unique_pct=unique_pct,
                rare_pct=rare_pct,
                )

###
### Read in our early game unlocks
###

with open('input-file-earlyunlock.txt') as df:
    early_game_unlocks = df.read()

###
### Everything below this point is constructing the actual patch file
###

# Now read in our main input file
with open(input_filename, 'r') as df:
    mod_str = df.read().format(
        mod_name=mod_name,
        mod_version=mod_version,
        mod_type='BL2',
        mp=mp,
        base=ConfigBase(),
        drop_quality_excellent=qualities['Excellent'],
        drop_quality_verygood=qualities['Very Good'],
        boss_drops_guaranteed=boss_drops['guaranteed'],
        boss_drops_veryimproved=boss_drops['veryimproved'],
        boss_drops_improved=boss_drops['improved'],
        boss_drops_slightimproved=boss_drops['slight'],
        boss_drops_stock=boss_drops['stock'],
        boss_quantity_excellent=boss_quantities['excellent'],
        boss_quantity_improved=boss_quantities['improved'],
        boss_quantity_stock=boss_quantities['stock'],
        early_game_unlocks=early_game_unlocks,
        )
mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod to: {}'.format(output_filename))
