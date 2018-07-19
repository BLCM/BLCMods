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

class ConfigBase(object):
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
    dice_vhigh_veryrare = '1'
    dice_vhigh_alien = '1'
    dice_vhigh_legendary = '0.5'

    # 2.5x chance of both kinds of eridium
    eridium_bar_drop = '0.003750'       # Stock: 0.001500
    eridium_stick_drop = '0.020000'     # Stock: 0.008000

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

    def __format__(self, formatstr):
        """
        A bit of magic so that we can use our values in format strings
        """
        attr = getattr(self, formatstr)
        if type(attr) == str:
            return attr
        else:
            return attr()

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
    weapon_base_common = '8'
    weapon_base_uncommon = '85'
    weapon_base_rare = '65'
    weapon_base_veryrare = '50'
    weapon_base_alien = '30'
    weapon_base_legendary = '3'
    weapon_base_iris_cobra = '1'

    # Custom COM drop scaling (identical to weapons, apart from an additional Alignment COM pool)
    cm_base_common = weapon_base_common
    cm_base_uncommon = weapon_base_uncommon
    cm_base_rare = weapon_base_rare
    cm_base_veryrare = weapon_base_veryrare
    cm_base_alignment = '30'
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
    relic_drop_scale_all = '0.2'
    relic_drop_scale_reward = '1'

    # Custom relic drop scaling, within "ArtifactsReward"
    relic_base_rare = '1.0'
    relic_base_veryrare = '2.0'

    # Drop rates for "regular" treasure chests
    treasure_base_common = '0'
    treasure_base_uncommon = '0'
    treasure_base_rare = '20'
    treasure_base_veryrare = '60'
    treasure_base_alien = '30'
    treasure_base_legendary = '5'

    # Drop rates for "epic" treasure chests
    epic_base_common = '0'
    epic_base_uncommon = '0'
    epic_base_rare = '0'
    epic_base_veryrare = '1'
    epic_base_alien = '1'
    epic_base_legendary = '0.3'

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = '0.4'
    badass_pool_alien = '0.4'
    badass_pool_epicchest = '0.1'

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = '1'
    super_badass_pool_veryrare = '1'
    super_badass_pool_alien = '1'
    super_badass_pool_legendary = '1'
    super_badass_pool_epicchest = '1'

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = '1'
    ultimate_badass_pool_veryrare_2 = '0.5'
    ultimate_badass_pool_alien_1 = '1'
    ultimate_badass_pool_alien_2 = '0.5'
    ultimate_badass_pool_legendary_1 = '1'
    ultimate_badass_pool_legendary_2 = '0.5'
    ultimate_badass_pool_legendary_3 = '0.25'
    ultimate_badass_pool_epicchest_1 = '1'
    ultimate_badass_pool_epicchest_2 = '0.5'
    ultimate_badass_pool_epicchest_3 = '0.5'

    # Unique drop quantities.  Some of these are pretty high in my "default"
    # configuration, so putting them here lets me override them in the other
    # configs, easily.
    quantity_chubby = '4'
    quantity_terra = '7'
    quantity_vermivorous = '5'
    quantity_warrior = '8'
    quantity_hyperius_legendary = '7'
    quantity_hyperius_seraph = '4'
    quantity_gee_seraph = '4'
    quantity_gee_legendary = '6'

    # Voracidous quantities have to be done slightly differently, because both
    # Dexiduous and Voracidous use the same Seraph and Legendary pools for their
    # unique drops, but Dexi calls it multiple times, whereas Vorac just calls
    # it the once (by default).  So upping the quantity for Vorac makes Dexi's
    # drops totally ludicrous.  So instead, we're just gonna specify the pool
    # multiple times in Vorac's ItemPool.  This is lame, but should let both
    # of them coexist.
    voracidous_drop_seraph_1 = '1'
    voracidous_drop_seraph_2 = '1'
    voracidous_drop_seraph_3 = '1'
    voracidous_drop_seraph_4 = '1'
    voracidous_drop_legendary_1 = '1'
    voracidous_drop_legendary_2 = '1'
    voracidous_drop_legendary_3 = '1'
    voracidous_drop_legendary_4 = '1'

class ConfigReasonable(ConfigLootsplosion):
    """
    Alternate config which has slightly-more-reasonable drop rates for stuff
    like legendaries.  Unsurprisingly, most folks find my default values a
    bit excessive.
    """

    profile_name = 'Very Good'
    profile_name_orig = 'Reasonable'

    # Weapon drops
    weapon_base_common = '32.75'
    weapon_base_uncommon = '35'
    weapon_base_rare = '25'
    weapon_base_veryrare = '5'
    weapon_base_alien = '2'
    weapon_base_legendary = '0.25'
    weapon_base_iris_cobra = '2'

    # Class mods
    cm_base_common = weapon_base_common
    cm_base_uncommon = weapon_base_uncommon
    cm_base_rare = weapon_base_rare
    cm_base_veryrare = weapon_base_veryrare
    cm_base_alignment = '2'
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
    relic_drop_scale_all = '0.6'
    relic_drop_scale_reward = '0.6'

    # Custom relic drop scaling, within "ArtifactsReward"
    relic_base_rare = '2.0'
    relic_base_veryrare = '1.0'

    # Drop rates for "regular" treasure chests
    treasure_base_common = '32.5'
    treasure_base_uncommon = '40'
    treasure_base_rare = '20'
    treasure_base_veryrare = '5'
    treasure_base_alien = '3'
    treasure_base_legendary = '0.5'

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = '25'
    epic_base_rare = '49'
    epic_base_veryrare = '15'
    epic_base_alien = '10'
    epic_base_legendary = '1'

    # Unique drop quantities -- overridden from the base class to make
    # them a bit more reasonable.
    quantity_chubby = '2'
    quantity_terra = '4'
    quantity_vermivorous = '3'
    quantity_warrior = '4'
    quantity_hyperius_legendary = '2'
    quantity_hyperius_seraph = '2'
    quantity_gee_seraph = '2'
    quantity_gee_legendary = '2'

    # Voracidous quantities have to be done slightly differently, because both
    # Dexiduous and Voracidous use the same Seraph and Legendary pools for their
    # unique drops, but Dexi calls it multiple times, whereas Vorac just calls
    # it the once (by default).  So upping the quantity for Vorac makes Dexi's
    # drops totally ludicrous.  So instead, we're just gonna specify the pool
    # multiple times in Vorac's ItemPool.  This is lame, but should let both
    # of them coexist.
    voracidous_drop_seraph_1 = '1'
    voracidous_drop_seraph_2 = '1'
    voracidous_drop_seraph_3 = '0'
    voracidous_drop_seraph_4 = '0'
    voracidous_drop_legendary_1 = '1'
    voracidous_drop_legendary_2 = '1'
    voracidous_drop_legendary_3 = '0'
    voracidous_drop_legendary_4 = '0'

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = '0.2'
    badass_pool_alien = '0.15'
    badass_pool_epicchest = '0.1'

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = '1'
    super_badass_pool_veryrare = '0.4'
    super_badass_pool_alien = '0.15'
    super_badass_pool_legendary = '.03'
    super_badass_pool_epicchest = '1'

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = '1'
    ultimate_badass_pool_veryrare_2 = '0'
    ultimate_badass_pool_alien_1 = '0.4'
    ultimate_badass_pool_alien_2 = '0'
    ultimate_badass_pool_legendary_1 = '0.08'
    ultimate_badass_pool_legendary_2 = '0'
    ultimate_badass_pool_legendary_3 = '0'
    ultimate_badass_pool_epicchest_1 = '1'
    ultimate_badass_pool_epicchest_2 = '1'
    ultimate_badass_pool_epicchest_3 = '1'

# The profiles we'll generate
profiles = [
    ConfigLootsplosion(),
    ConfigReasonable(),
    ]

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
        mp.register_str('grenade_{}_{}_0'.format(gm_type, man_num),
            'level None set GD_GrenadeMods.A_Item.GM_{} Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
                gm_type, man_num,
            ))
        mp.register_str('grenade_{}_{}_1'.format(gm_type, man_num),
            'level None set GD_GrenadeMods.A_Item.GM_{}_2_Uncommon Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
                gm_type, man_num,
            ))
        mp.register_str('grenade_{}_{}_2'.format(gm_type, man_num),
            'level None set GD_GrenadeMods.A_Item.GM_{}_3_Rare Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
                gm_type, man_num,
            ))
        mp.register_str('grenade_{}_{}_3'.format(gm_type, man_num),
            'level None set GD_GrenadeMods.A_Item.GM_{}_4_VeryRare Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
                gm_type, man_num,
            ))

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

###
### Generate our quality category strings
###

qualities = {}
for profile in profiles:

    with open('input-file-quality.txt') as df:
        qualities[profile.profile_name] = df.read().format(
                config=profile,
                mp=mp,
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
        ('Stock Equip', 'stock', .1, .33),
        ]:

    with open('input-file-droprate.txt', 'r') as df:
        boss_drops[key] = df.read().format(
                section_label='{} ({}% Uniques, {}% Rares)'.format(
                    label, round(unique_pct*100), round(rare_pct*100)),
                unique_pct=unique_pct,
                rare_pct=rare_pct,
                )

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
        )
mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod to: {}'.format(output_filename))
