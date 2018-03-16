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

mod_name = 'BL2 Better Loot Mod'
mod_version = '1.2.0 (prerelease)'
variant_ucp = 'UCP Compat'
variant_standalone = 'Standalone'
variant_offline = 'Standalone Offline'

###
### Where we get our mod data from
###

input_filename = 'mod-input-file.txt'

###
### Hotfix object to store all our hotfixes
###

hfs = Hotfixes(include_gearbox_patches=True)

###
### Variables which control drop rates and stuff like that
###

class ConfigBase(object):
    """
    Class to hold all our weights, and other vars which alter the probabilities of
    various things dropping.  Derive from this class to actually define the
    values.
    """

    def filename(self, mod_name, variant_name):
        """
        Constructs our filename
        """
        return '{} ({}) - {}-source.txt'.format(
                mod_name,
                self.profile_name,
                variant_name,
            )

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

    profile_name = 'Lootsplosion'

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

    # Boss drop rates
    boss_drop_uniques = '1.0'
    boss_drop_rares = '1.0'

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

    # Drop rates within the "very high roll" pools of dice chests
    dice_vhigh_veryrare = '1'
    dice_vhigh_alien = '1'
    dice_vhigh_legendary = '0.5'

    # 2.5x chance of both kinds of eridium
    eridium_bar_drop = '0.003750'       # Stock: 0.001500
    eridium_stick_drop = '0.020000'     # Stock: 0.008000

    # Gun Type drop weights.  Note that because these values are going into
    # our hotfix object, these variables *cannot* be successfully overridden
    # in an extending class.
    drop_prob_pistol = 100
    drop_prob_ar = 100
    drop_prob_smg = 100
    drop_prob_shotgun = 100
    drop_prob_sniper = 80
    drop_prob_launcher = 40

class ConfigReasonable(ConfigLootsplosion):
    """
    Alternate config which has slightly-more-reasonable drop rates for stuff
    like legendaries.  Unsurprisingly, most folks find my default values a
    bit excessive.
    """

    profile_name = 'Reasonable Drops'

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

    # Boss drop rates
    boss_drop_uniques = '0.5'
    boss_drop_rares = '0.25'

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

###
### Vars used primarily during testing of loot pools - these aren't
### intended to be "live" in the mod by default.
###

# Vars to control testing our drop pools.  Set `test_drop_pools` to True and
# every enemy will drop a bunch of loot.
test_drop_pools = False
loot_drop_chance_1p = '1.000000'    # Stock: 0.085000
loot_drop_chance_2p = '1.000000'    # Stock: 0.070000
loot_drop_chance_3p = '1.000000'    # Stock: 0.060000
loot_drop_chance_4p = '1.000000'    # Stock: 0.050000
loot_drop_quantity = '5'            # Stock: 1.000000

# Some alternate vars from a mutually-exclusive area - merely improve
# the drop rate, rather than making it 100%
loot_drop_chance_1p_alt = '0.170000'    # Stock: 0.085000
loot_drop_chance_2p_alt = '0.140000'    # Stock: 0.070000
loot_drop_chance_3p_alt = '0.120000'    # Stock: 0.060000
loot_drop_chance_4p_alt = '0.100000'    # Stock: 0.050000

# Force Pool_GunsAndGear to always drop the specified pool, if `force_gunsandgear_drop`
# is True.  Useful for testing out how individual pools are behaving.
force_gunsandgear_drop = False
force_gunsandgear_drop_type = 'GD_Itempools.ArtifactPools.Pool_ArtifactsReward'

# Force Pool_GunsAndGear to always drop the specified item, if
# `force_gunsandgear_specific` is True.  Useful for seeing what exactly an
# item is.  `force_gunsandgear_specific` will override `force_gunsandgear_drop`,
# if both are set to True.
force_gunsandgear_specific = False
force_gunsandgear_specific_name = 'GD_Orchid_BossWeapons.RPG.Ahab.Orchid_Boss_Ahab_Balance_NODROP'

###
### Hotfixes; these are handled a little differently than everything
### else.
###

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
            ('Pistol', ConfigLootsplosion.drop_prob_pistol),
            ('AR', ConfigLootsplosion.drop_prob_ar),
            ('SMG', ConfigLootsplosion.drop_prob_smg),
            ('Shotgun', ConfigLootsplosion.drop_prob_shotgun),
            ('Sniper', ConfigLootsplosion.drop_prob_sniper),
            ('Launcher', ConfigLootsplosion.drop_prob_launcher),
            ]):
        hfs.add_level_hotfix('normalize_weapon_types_{}_{}'.format(rarity, guntype),
            'NormWeap{}{}'.format(rarity, guntype),
            ',GD_Itempools.WeaponPools.Pool_Weapons_All_{}_{},BalancedItems[{}].Probability.BaseValueConstant,,{}'.format(
                number,
                rarity,
                idx,
                gunprob))

# Some tweaks to Locker drops -- enforce Blue-rarity as much as possible.
# This is in addition to the main `set` in mod-input-file.txt
hfs.add_level_hotfix('locker_shield', 'LockerDrops',
    """,GD_Itempools.ListDefs.StorageLockerLoot,
    LootData[4].ItemAttachments[0].ItemPool,,
    ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare'""")
hfs.add_level_hotfix('locker_grenade', 'LockerDrops',
    """,GD_Itempools.ListDefs.StorageLockerLoot,
    LootData[5].ItemAttachments[0].ItemPool,,
    ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare'""")
hfs.add_level_hotfix('locker_gungrenade', 'LockerDrops',
    """,GD_Itempools.ListDefs.StorageLockerLoot,
    LootData[6].ItemAttachments[1].ItemPool,,
    ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare'""")

# Cardboard Box nerf ("needed" in v1.2.0 'cause of our weighted pool fixes)
hfs.add_level_hotfix('cardboard_box_nerf', 'CardboardBoxNerf',
    """,GD_Balance_Treasure.LootableGrades.ObjectGrade_Cardboard_Box,
    DefaultLoot[1].ItemAttachments[0].ItemPool,,
    ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common'""")

# Bandit Cooler nerf ("needed" in v1.2.0 'cause of our weighted pool fixes)
for idx, objname in enumerate([
        'GD_Balance_Treasure.LootableGrades.ObjectGrade_Bandit_Cooler',
        'GD_Balance_Treasure.LootableGradesTrap.MidgetBandit.ObjectGrade_BanditCooler_MidgetBandit',
        ]):
    hfs.add_level_hotfix('bandit_cooler_nerf_{}'.format(idx),
        'BanditCoolerNerf',
        """,{},DefaultLoot[4].ItemAttachments[0].ItemPool,,
        ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common'""".format(
            objname
            ))

# Make Knuckledragger drop from the badass loot pool
hfs.add_level_hotfix('knuckledragger_badass', 'KnuckledraggerDrop',
    """Glacial_P,GD_Population_PrimalBeast.Balance.Unique.PawnBalance_PrimalBeast_KnuckleDragger,
    DefaultItemPoolIncludedLists,,
    (ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear')""")

# Make Shirtless Men drop from the badass loot pool
hfs.add_level_hotfix('shirtless_man_badass', 'ShirtlessManDrop',
    "Interlude_P,GD_Population_Marauder.Balance.Unique.PawnBalance_ShirtlessMan,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Gluttonous Thresher drop from the super badass loot pool
hfs.add_level_hotfix('gluttonous_badass', 'GluttonousDrop',
    "Outwash_P,GD_Population_Thresher.Balance.PawnBalance_ThresherGluttonous,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear'")

# Make Sinkhole drop from the badass loot pool
hfs.add_level_hotfix('sinkhole_badass', 'SinkholeDrop',
    "Fridge_P,GD_Population_Stalker.Balance.Unique.PawnBalance_Stalker_SwallowedWhole,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Laney's Dwarves drop crystals, and be likely to drop a gemstone between 'em
for num in range(1, 8):
	hfs.add_level_hotfix('laney_dwarf_drop_{}'.format(num),
        'LaneyDwarfDrop{}'.format(num),
		"""Fridge_P,GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf{},DefaultItemPoolList,,
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

# Make Rakkman drop from the badass pool
hfs.add_level_hotfix('rakkman_badass', 'RakkmanDrop',
    "Fridge_P,GD_Population_Psycho.Balance.Unique.PawnBalance_RakkMan,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Improve Mordecai's Stash end-mission drops.  All snipers, and much better
# quality.
hfs.add_level_hotfix('mordecai_stash_0', 'MordecaiStash',
    "Interlude_P,GD_Z3_GoodBadMordecaiData.IO_GoodBadMordecai_GraveStash:BehaviorProviderDefinition_2.Behavior_SpawnItems_48,ItemPoolList[19].ItemPool,,ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare'")
hfs.add_level_hotfix('mordecai_stash_1', 'MordecaiStash',
    "Interlude_P,GD_Z3_GoodBadMordecaiData.IO_GoodBadMordecai_GraveStash:BehaviorProviderDefinition_2.Behavior_SpawnItems_48,ItemPoolList[20].ItemPool,,ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare_Alien'")
hfs.add_level_hotfix('mordecai_stash_2', 'MordecaiStash',
    "Interlude_P,GD_Z3_GoodBadMordecaiData.IO_GoodBadMordecai_GraveStash:BehaviorProviderDefinition_2.Behavior_SpawnItems_48,ItemPoolList[21].ItemPool,,ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Snipers_04_Gemstone'")
hfs.add_level_hotfix('mordecai_stash_3', 'MordecaiStash',
    "Interlude_P,GD_Z3_GoodBadMordecaiData.IO_GoodBadMordecai_GraveStash:BehaviorProviderDefinition_2.Behavior_SpawnItems_48,ItemPoolList[22].ItemPool,,ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary'")

# Make Mick Zaford and Papa/Jimbo Hodunk drop from the badass pool
hfs.add_level_hotfix('mickzaford_badass', 'MickZafordDrop',
    "Interlude_P,GD_Population_Marauder.Balance.Unique.PawnBalance_MickZaford_Combat,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")
hfs.add_level_hotfix('papa_hodunk_badass', 'PapaHodunkDrop',
    "Interlude_P,GD_Population_Marauder.Balance.Unique.PawnBalance_JimboRiding,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Jack's Body Double drop from the badass pool
hfs.add_level_hotfix('bodydouble_badass', 'BodyDoubleDrop',
    "HyperionCity_P,GD_Population_Jack.Balance.PawnBalance_JacksBodyDouble,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Deputy Winger drop from the badass pool
hfs.add_level_hotfix('deputy_badass', 'DeputyDrop',
    "Grass_Lynchwood_P,GD_Population_Sheriff.Balance.PawnBalance_Deputy,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Vastly improve Roland's chest in Sanctuary (all legendaries)
hfs.add_level_hotfix('roland_chest', 'BetterRolandChest',
    """SanctuaryAir_P,GD_Balance_Treasure.ChestGrades.ObjectGrade_DahlEpic_BearerBadNews,DefaultLoot,,
    (
        (
            ConfigurationName="TreasureChest_2guns2Pistols",
            LootGameStageVarianceFormula=None,
            Weight=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=2.000000
            ),
            ItemAttachments=(
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Gun1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Gun2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Pistol5"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Pistol6"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo3"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo4"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade3"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_GrenadeAmmo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade4"
                )
            )
        ),
        (
            ConfigurationName="TreasureChest_4Pistols1Long",
            LootGameStageVarianceFormula=None,
            Weight=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            ),
            ItemAttachments=(
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Pistol1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Pistol2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Pistol3"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Pistol4"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Gun3"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo3"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo4"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade3"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_Chest_Ammo',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade4"
                )
            )
        ),
        (
            ConfigurationName="TreasureChest_Launcher",
            LootGameStageVarianceFormula=None,
            Weight=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            ),
            ItemAttachments=(
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Launcher1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Launcher2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_RocketLauncher',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Grenades',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Grenades',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo3"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_RocketLauncher',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Ammo4"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_RocketLauncher',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade1"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Grenades',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade2"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Grenades',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade3"
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_RocketLauncher',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    AttachmentPointName="Grenade4"
                )
            )
        )
    )
    """)

# Make Badass Bedrock Bullymongs drop from the badass pool
hfs.add_level_hotfix('bedrock_bullymong_badass', 'BedrockBullymongBadass',
    ",GD_Population_PrimalBeast.Balance.PawnBalance_PrimalBeast_BedrockBadass,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Mortar drop from the badass pool
hfs.add_level_hotfix('mortar_badass', 'MortarDrop',
    "CraterLake_P,GD_Population_Rat.Balance.Unique.PawnBalance_Mortar,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Bonehead 2.0 drop from the badass pool
hfs.add_level_hotfix('bonehead2_badass', 'Bonehead2Drop',
    "Stockade_P,GD_Population_Loader.Balance.Unique.PawnBalance_BoneHead2,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Improve Talon of God gifts
hfs.add_level_hotfix('talon_gifts_zed', 'TalonGiftsZed',
    "SanctuaryAir_P,GD_Zed.Character.AIDef_Zed:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_11,ItemPoolList[0].ItemPool,,ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare'")
hfs.add_level_hotfix('talon_gifts_scooter', 'TalonGiftsScooter',
    "SanctuaryAir_P,GD_Scooter.Character.AIDef_Scooter:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_25,ItemPoolList[0].ItemPool,,ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare'")
hfs.add_level_hotfix('talon_gifts_tannis', 'TalonGiftsTannis',
    "SanctuaryAir_P,GD_TannisNPC.Character.AIDef_TannisNPC:AIBehaviorProviderDefinition_1.Behavior_SpawnItems_6,ItemPoolList[0].ItemPool,,ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_04_VeryRare'")
hfs.add_level_hotfix('talon_gifts_moxxi', 'TalonGiftsMoxxi',
    "SanctuaryAir_P,GD_Moxxi.Character.AIDef_Moxxi:AIBehaviorProviderDefinition_1.Behavior_SpawnItems_1,ItemPoolList[0].ItemPool,,ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_SMGs_04_Gemstone'")
hfs.add_level_hotfix('talon_gifts_hammerlock', 'TalonGiftsHammerlock',
    "SanctuaryAir_P,GD_Hammerlock.Character.AIDef_Hammerlock:AIBehaviorProviderDefinition_1.Behavior_SpawnItems_20,ItemPoolList[0].ItemPool,,ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Snipers_04_Gemstone'")
hfs.add_level_hotfix('talon_gifts_marcus_0', 'TalonGiftsMarcus',
    "SanctuaryAir_P,GD_Marcus.Character.AIDef_Marcus:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_14,ItemPoolList[0].ItemPool,,ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_ARs_04_Gemstone'")
hfs.add_level_hotfix('talon_gifts_marcus_1', 'TalonGiftsMarcus',
    "SanctuaryAir_P,GD_Marcus.Character.AIDef_Marcus:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_14,ItemPoolList[1].ItemPool,,ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare'")
hfs.add_level_hotfix('talon_gifts_marcus_2', 'TalonGiftsMarcus',
    "SanctuaryAir_P,GD_Marcus.Character.AIDef_Marcus:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_14,ItemPoolList[2].ItemPool,,ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Shotguns_04_Gemstone'")

# Improve The Warrior drops
for (num, pool) in [
        (12, 'GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_LongGuns'),
        (15, 'GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_Pistols'),
        (17, 'GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_Launchers'),
        ]:
    hfs.add_level_hotfix('warrior_drop_{}'.format(num),
        'WarriorDrop',
        "Boss_Volcano_P,GD_FinalBoss.Character.AIDef_FinalBoss:AIBehaviorProviderDefinition_1.Behavior_SpawnItems_{},ItemPoolList[0].ItemPool,,ItemPoolDefinition'{}'".format(num, pool))

# Make No-Beard always drop his unique
hfs.add_level_hotfix('scarlett_nobeard', 'NoBeardDrop',
    'Orchid_OasisTown_P,GD_Orchid_Pop_NoBeard.PawnBalance_Orchid_NoBeard,DefaultItemPoolList[1].PoolProbability.BaseValueConstant,,1.0')

# Make Big Sleep always drop his unique
hfs.add_level_hotfix('scarlett_bigsleep', 'BigSleepDrop',
    'Orchid_Caves_P,GD_Orchid_Pop_Sandman.Balance.PawnBalance_Orchid_BigSleep,DefaultItemPoolList[1].PoolProbability.BaseValueConstant,,1.0')

# UCP Compatibility fixes: We need to add in a hotfix to set Hyperius and
# Master Gee to always drop from their Legendary pool.  We hardcode that
# with a regular "set" command, but a UCP hotfix (to improve the Legendary
# drop rate) would overwrite our 100% chance.  So, in addition to the "set"
# command, we'll overwrite the probability again.
hfs.add_level_hotfix('scarlett_hyperius_ucp_fix', 'HyperiusUCPFix',
    'Orchid_Refinery_P,GD_Orchid_ItemPools.Raid.PoolList_Orchid_Raid1_Items,Itempools[0].PoolProbability.BaseValueConstant,,1.0')
hfs.add_level_hotfix('scarlett_mastergee_ucp_fix', 'MasterGeeUCPFix',
    'Orchid_Caves_P,GD_Orchid_ItemPools.Raid.PoolList_Orchid_Raid3_Items,Itempools[0].PoolProbability.BaseValueConstant,,1.0')

# Make the Chubby drop pool better.
hfs.add_level_hotfix('chubby_drop', 'ChubbyDrop',
    """,GD_Itempools.ListDefs.ChubbyEnemyGunsAndGear,ItemPools,,
    (
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.Runnables.Pool_ChubbieUniques',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGear',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGear',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.VehicleSkins.Pool_VehicleSkins_All',
            PoolProbability=(
                BaseValueConstant=0.000000,
                BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_VehicleSkins',
                InitializationDefinition=None,
                BaseValueScaleConstant=10.000000
            )
        ),
        (
            ItemPool=CrossDLCItemPoolDefinition'GD_Lobelia_Itempools.WeaponPools.Pool_Lobelia_Pearlescent_Weapons_All',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
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
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
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
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.BuffDrinkPools.Pool_BuffDrinks_HealingInstant',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_NeedOnly',
            PoolProbability=(
                BaseValueConstant=0.000000,
                BaseValueAttribute=None,
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                BaseValueScaleConstant=0.250000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_Emergency',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        )
    )""")

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

# We want to make Piston always drop the Slow Hand, which is index 2 in its
# DefaultItemPoolList, but if a user has UCP installed and with the default
# selections, index 0 and 2 get swapped.  So, rather than just alter index
# 2's probability, we'll have to set indexes 0 and 2 explicitly.  So, do that.
hfs.add_level_hotfix('torgue_piston_0', 'PistonDropSlowHand',
    """,GD_Iris_Population_PistonBoss.Balance.Iris_PawnBalance_PistonBoss,DefaultItemPoolList[0],,
    (
        ItemPool=ItemPoolDefinition'GD_ItempoolsEnemyUse.Shields.Pool_Shields_Standard_EnemyUse',
        PoolProbability=(
            BaseValueConstant=1.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )
    )""")
hfs.add_level_hotfix('torgue_piston_2', 'PistonDropSlowHand',
    """,GD_Iris_Population_PistonBoss.Balance.Iris_PawnBalance_PistonBoss,DefaultItemPoolList[2],,
    (
        ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.EnemyDropPools.Pool_Weapons_Piston',
        PoolProbability=(
            BaseValueConstant=1.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )
    )""")

# Make Witch Doctors drop some slightly-more-interesting loot
witch_extra_pools = """
    (
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
    hfs.add_level_hotfix('witchdoctor_{}'.format(doctor),
        'WitchDoctor{}Drops'.format(doctor),
        """,GD_Sage_Pop_Natives.Balance.PawnBalance_WitchDoctor{},DefaultItemPoolList,,
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
    hfs.add_level_hotfix('crawmerax_witch_{}'.format(label),
        'CrawmeraxWitch{}Drops'.format(label),
        'Easter_P,{},DefaultItemPoolList,,({})'.format(classname, witch_extra_pools))

# Badass Borok Fixes
for borok in ['Corrosive', 'Fire', 'Shock', 'Slag']:
    hfs.add_level_hotfix('badass_borok_{}'.format(borok),
        'BadassBorok{}'.format(borok),
        ",GD_Sage_Pop_Rhino.Balance.PawnBalance_Sage_RhinoBadass{},DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'".format(borok))

# Make Roscoe drop from the Badass loot pool
hfs.add_level_hotfix('scarlett_roscoe_badass', 'RoscoeBadass',
    "Orchid_WormBelly_P,GD_Orchid_Pop_RakkHive.Character.PawnBalance_Orchid_RakkHive,DefaultItemPoolIncludedLists,,(ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear')")

# Make Bulstoss drop from the Badass loot pool
hfs.add_level_hotfix('bulstoss_badass', 'BulstossBadass',
    ",GD_Sage_SM_AcquiredTasteData.Creature.PawnBalance_Sage_AcquiredTaste_Creature,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Thermitage always drop its rare skin
hfs.add_level_hotfix('hammerlock_thermitage', 'ThermitageDropSkin',
    ',GD_Sage_Ep3_Data.Creature.PawnBalance_Sage_Ep3_Creature,DefaultItemPoolList[0].PoolProbability,,(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Make Dribbles always drop its rare skin
hfs.add_level_hotfix('hammerlock_dribbles', 'DribblesDropSkin',
    'Sage_PowerStation_P,GD_Sage_SM_FollowGlowData.Creature.PawnBalance_Sage_FollowGlow_Creature,DefaultItemPoolList[0].PoolProbability,,(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Make Woundspike always drop its rare skin
hfs.add_level_hotfix('hammerlock_woundspike', 'WoundspikeDropSkin',
    'Sage_PowerStation_P,GD_Sage_Ep4_Data.Creature.PawnBalance_Sage_Ep4_Creature,DefaultItemPoolList[1].PoolProbability,,(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Make Bloodtail always drop its rare skin
hfs.add_level_hotfix('hammerlock_bloodtail', 'BloodtailDropSkin',
    'Sage_Cliffs_P,GD_Sage_SM_NowYouSeeItData.Creature.PawnBalance_Sage_NowYouSeeIt_Creature,DefaultItemPoolList[1].PoolProbability,,(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Voracidous drop pool seraph crystal fix
for idx in range(3):
    hfs.add_level_hotfix('vorac_seraph_{}'.format(idx), 'VoracSeraph',
        "Sage_Cliffs_P,GD_Sage_ItemPools.Raid.PoolList_Sage_Raid_Items,ItemPools[{}].ItemPool,,ItemPoolDefinition'GD_Sage_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7_Drop'".format(idx))

# UCP Compatibility fixes: As with the Hyperius and Master Gee Legendary
# pool drops, we need to account for the fact that UCP contains a definition
# to improve the Legendary drop rate for Voracidous. We've already done that
# via a 'set' command, so we need to introduce a hotfix to ensure that it
# stays that way.  One other note is that we've also changed the ordering of
# Voracidous's loot pools, so the element which UCP changes isn't the one it
# thinks it's changed, with this mod installed
hfs.add_level_hotfix('vorac_drop_ucp_fix', 'VoracidousDropUCPFix',
    ',GD_Sage_ItemPools.Raid.PoolList_Sage_Raid_Items,Itempools[0].PoolProbability.BaseValueConstant,,1.0')

# Make Elite Savages always drop something from the main GunsAndGear pool
# (this'll give them a chance to drop twice, actually, but whatever)
hfs.add_level_hotfix('hammerlock_elite_savage', 'EliteSavageDrop',
    """Sage_Cliffs_P,GD_Sage_Pop_Natives.Balance.PawnBalance_Native_Elite,DefaultItemPoolList,,
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
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGear',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        )
    )""")

# Make "MimicChest_NoMimic" chests from Tiny Tina have slightly better
# loot - they pull from the "regular" chest pool mostly; this will make
# some of their slots pull from the "epic" chest pool instead.
hfs.add_level_hotfix('nomimic_epic_1', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[0].ItemAttachments[1].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns'")
hfs.add_level_hotfix('nomimic_epic_2', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[0].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols'")
hfs.add_level_hotfix('nomimic_epic_3', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[1].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols'")
hfs.add_level_hotfix('nomimic_epic_4', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[1].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols'")
hfs.add_level_hotfix('nomimic_epic_5', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[3].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items'")
hfs.add_level_hotfix('nomimic_epic_6', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[3].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items'")
hfs.add_level_hotfix('nomimic_epic_7', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[4].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Shields'")
hfs.add_level_hotfix('nomimic_epic_8', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[4].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Shields'")
hfs.add_level_hotfix('nomimic_epic_9', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[5].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods'")
hfs.add_level_hotfix('nomimic_epic_10', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[5].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods'")
hfs.add_level_hotfix('nomimic_epic_11', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[7].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns'")
hfs.add_level_hotfix('nomimic_epic_12', 'NoMimicEpic',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[8].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Artifacts'")

# Make Arguk the Butcher (from 'Critical Fail') drop from the Badass loot pool
hfs.add_level_hotfix('dragonkeep_arguk_drop', 'ArgukDrop',
    "Dark_Forest_P,GD_Aster_Pop_Orcs.Balance.PawnBalance_Orc_Butcher,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Skeleton Giants drop from the Badass loot pool (not that Dragon Keep
# needs more loot being dropped, really, but whatever)
hfs.add_level_hotfix('dragonkeep_giant_skeleton', 'GiantSkeletonDrop',
    ",GD_Aster_Pop_Skeletons.Balance.PawnBalance_SkeletonGiant,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Gold Golem always drop one of its "special" legendary drops (effectively
# commenting out the first BalancedItem which would drop from a more general pool)
hfs.add_level_hotfix('dragonkeep_goldgolem_drop_pool', 'GoldGolemDropPool',
    'Mines_P,GD_GolemGold.LootPools.Pool_GoldGolemRunnable,BalancedItems[0].Probability,,(BaseValueConstant=0.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.0)')

# ...aaaand set the Gold Golem drop pool quantity to 3, to at least possibly drop
# one of each of those items (for nearly every other boss requiring this, we can
# just do it via 'set', but Gold Golem must be hotfixed.
hfs.add_level_hotfix('dragonkeep_goldgolem_drop_qty', 'GoldGolemDropQty',
    'Mines_P,GD_GolemGold.LootPools.Pool_GoldGolemRunnable,Quantity,,(BaseValueConstant=3.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Add more Eridium to Handsome Dragon's lootsplosion over the bridge
hfs.add_level_hotfix('dragonkeep_handsomedragon_drop1', 'HandsomeDragonEridium',
    "CastleExterior_P,GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_21,ItemPoolList[16].ItemPool,,ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick'")
hfs.add_level_hotfix('dragonkeep_handsomedragon_drop2', 'HandsomeDragonEridium',
    "CastleExterior_P,GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_21,ItemPoolList[17].ItemPool,,ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick'")
hfs.add_level_hotfix('dragonkeep_handsomedragon_drop3', 'HandsomeDragonEridium',
    "CastleExterior_P,GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_21,ItemPoolList[18].ItemPool,,ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick'")

# Make Badass Knights drop from the badass loot pool
hfs.add_level_hotfix('dragonkeep_badass_knights', 'BadassKnightsDrop',
    ",GD_Aster_Pop_Knights.Balance.PawnBalance_Knight_Badass,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Badass Fire Archers drop from the badass loot pool
hfs.add_level_hotfix('dragonkeep_badass_fire_archers', 'BadassFireArchersDrop',
    ",GD_Aster_Pop_Knights.Balance.PawnBalance_Knight_BadassFireArcher,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Sorcerer's Daughter drop 4 items from her legendary pool (which is 4 long)
hfs.add_level_hotfix('dragonkeep_sorcerersdaughter_drop_pool', 'SorcerersDaughterDropPool',
    'Dungeon_P,GD_AngelBoss.LootPools.Pool_AngelBossRunnable,Quantity.BaseValueConstant,,4.0')

# Normalize the probabilities for the Sorcerer's Daughter legendary pool
for num in range(4):
    hfs.add_level_hotfix('dragonkeep_sorcerersdaughter_normalize_{}'.format(num), 'SorcerersDaughterNormalize',
        'Dungeon_P,GD_AngelBoss.LootPools.Pool_AngelBossRunnable,BalancedItems[{}].Probability.BaseValueScaleConstant,,1.0'.format(num))

# Add more Eridium to Butt Stallion's victory trot after defeating the Handsome Sorcerr
hfs.add_level_hotfix('dragonkeep_buttstallion_drop1', 'ButtStallionEridium',
    """CastleKeep_P,GD_ButtStallion_Proto.Character.AIDef_ButtStallion_Proto:AIBehaviorProviderDefinition_1:Behavior_SpawnItems_44,ItemPoolList,,
    (
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
            PoolProbability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            )
        )
    )""")

# Make the individual Jack battles at the end of Dragon Keep drop from a badass pool
for suffix in ['', '_Demon', '_DemonFall', '_Phase2']:
    hfs.add_level_hotfix('dragonkeep_jack{}_drop1'.format(suffix),
        'DragonKeepJack{}Drop'.format(suffix),
        "CastleKeep_P,GD_Aster_Pop_Wizards.Balance.PawnBalance_JackWarlock{},DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear'".format(suffix))

# Ancient Dragons should always give you 28 Seraph Crystals (total - the pool gets called twice)
hfs.add_level_hotfix('dragonkeep_ancient_crystals0', 'DragonKeepAncientCrystals',
    """DungeonRaid_P,GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystals,BalancedItems,,
    (
        (
            ItmPoolDefinition=ItemPoolDefinition'GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystal_7',
            InvBalanceDefinition=None,
            Probability=(
                BaseValueConstant=1.0,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.0
            ),
            bDropOnDeath=true
        )
    )""")
hfs.add_level_hotfix('dragonkeep_ancient_crystals1', 'DragonKeepAncientCrystals',
    'DungeonRaid_P,GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystals,Quantity,,(BaseValueConstant=2.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Always drop crystals regardless of playthrough
hfs.add_level_hotfix('dragonkeep_ancient_crystals2', 'DragonKeepAncientCrystals',
    'DungeonRaid_P,GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystals,MinGameStageRequirement,,None')

# Drop three items from the Ancient Dragons' Uniques pool
hfs.add_level_hotfix('dragonkeep_ancient_uniques0', 'DragonKeepAncientUniques',
    'DungeonRaid_P,GD_Aster_ItemPools.Raid.Pool_Aster_Raid1_Uniques,Quantity,,(BaseValueConstant=3.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Tweak our two drop pools (they each get spawned twice, FYI)
hfs.add_level_hotfix('dragonkeep_ancient_drop1', 'DragonKeepAncientDrop',
    """DungeonRaid_P,GD_Aster_ItemPools.Raid.PoolList_Aster_Raid1A_Items,ItemPools,,
    (
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        )
    )""")

hfs.add_level_hotfix('dragonkeep_ancient_drop2', 'DragonKeepAncientDrop',
    """DungeonRaid_P,GD_Aster_ItemPools.Raid.PoolList_Aster_Raid1B_Items,ItemPools,,
    (
        (
            ItemPool=ItemPoolDefinition'GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystals',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=0.400000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        ),
        (
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',
            PoolProbability=(
                BaseValueConstant=1.000000,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
        )
    )""")

# Make Undead Badass Psychos (Bloody Harvest) drop from the Badass loot pool
hfs.add_level_hotfix('harvest_ubps', 'UndeadBadassPsychoDrop',
    "Pumpkin_Patch_P,GD_Pop_HallowSkeleton.Balance.PawnBalance_BadassUndeadPsycho,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Three tributes from the Wattle Gobbler Headhunter pack don't actually drop
# anything, whereas the others drop from the badass pool.  Fix that.
for (name, classname) in [
        ('cynder', 'GD_IncineratorFemale.Balance.PawnBalance_IncineratorFemale'),
        ('strip', 'GD_FleshripperFemale.Balance.PawnBalance_FleshripperFemale'),
        ('flay', 'GD_FleshripperMale.Balance.PawnBalance_FleshripperMale'),
        ]:
    hfs.add_level_hotfix('wattle_tribute_{}'.format(name),
        'WattleTribute{}Drop'.format(name),
        "Hunger_P,{},DefaultItemPoolIncludedLists,,(ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear')".format(classname))

# Make Badass Yeti (Mercenary Day) drop from the Badass loot pool
hfs.add_level_hotfix('mercenaryday_badass_yeti', 'BadassYetiDrop',
    "Xmas_P,GD_Allium_BadassYeti.Balance.PawnBalance_Allium_BadassYeti,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Bridget Hodunk and Colin Zaford (Wedding Day Massacre) drop from the Badass loot pool
hfs.add_level_hotfix('wedding_drop_bridget_0', 'WeddingDropBridget',
    "Distillery_P,GD_GoliathBride.Population.PawnBalance_GoliathBride,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")
hfs.add_level_hotfix('wedding_drop_bridget_1', 'WeddingDropBridget',
    "Distillery_P,GD_GoliathBride.Population.PawnBalance_GoliathBrideRaid,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")
hfs.add_level_hotfix('wedding_drop_colin_0', 'WeddingDropColin',
    "Distillery_P,GD_GoliathGroom.Population.PawnBalance_GoliathGroom,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")
hfs.add_level_hotfix('wedding_drop_colin_1', 'WeddingDropColin',
    "Distillery_P,GD_GoliathGroom.Population.PawnBalance_GoliathGroomRaid,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make the Loot Leprechaun (Wedding Day Massacre) drop from the Epic chest pool, rather than normal
hfs.add_level_hotfix('wedding_loot_leprechaun_0', 'WeddingLootLeprechaun',
    "Distillery_P,GD_Nast_Leprechaun.Character.CharClass_Nast_Leprechaun:BehaviorProviderDefinition_5.Behavior_SpawnItems_26,ItemPoolList[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns'")
hfs.add_level_hotfix('wedding_loot_leprechaun_1', 'WeddingLootLeprechaun',
    "Distillery_P,GD_Nast_Leprechaun.Character.CharClass_Nast_Leprechaun:BehaviorProviderDefinition_5.Behavior_SpawnItems_26,ItemPoolList[4].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols'")

# Make the BLNG Loader drop from the Badass pool, and add a lot of money drops
hfs.add_level_hotfix('wedding_blng_drop_0', 'WeddingBLNGDrop',
    "Distillery_P,GD_BlingLoader.Population.PawnBalance_BlingLoader,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")
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
hfs.add_level_hotfix('wedding_blng_drop_1', 'WeddingBLNGDrop',
    "Distillery_P,GD_BlingLoader.Population.PawnBalance_BlingLoader,DefaultItemPoolList,,({})".format(','.join(money_pool_list)))

# Make Giant Craboid (Son of Crawmerax) drop from the Badass loot pool
hfs.add_level_hotfix('crawmerax_giant_craboid', 'CrawmeraxGiantCraboidDrop',
    "Easter_P,GD_Population_Crabworms.Balance.PawnBalance_CraboidGiant,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Improve Son of Crawmerax's (non-raid) drops.  Basically just calling the
# RaidBossEnemyGunsAndGear pool three times instead of once.
hfs.add_level_hotfix('crawmerax_son_nonraid_drop', 'CrawmeraxSonNonRaidDrop',
    """Easter_P,GD_Crawmerax_Son.Population.PawnBalance_Crawmerax_Son,DefaultItemPoolIncludedLists,,
    (
        ItemPoolListDefinition'GD_Itempools.ListDefs.RaidBossEnemyGunsAndGear',
        ItemPoolListDefinition'GD_Itempools.ListDefs.RaidBossEnemyGunsAndGear',
        ItemPoolListDefinition'GD_Itempools.ListDefs.RaidBossEnemyGunsAndGear'
    )""")

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
    hfs.add_level_hotfix('euphoria_fix_{}'.format(idx),
        'EuphoriaChestFix',
        ',{},{}[{}].ItemAttachments[{}].ItemPool,,GD_Itempools.BuffDrinkPools.Pool_BuffDrinks_HealingRegen'.format(
            classname,
            propname,
            loot_idx,
            attachment_idx,
            ))

# Make safes a bit more reasonable - high chance for the eridium container, better
# cash otherwise.  Keep some of the item tiers in there as well, but make them
# always legendary (though more rare than they used to be).
hfs.add_level_hotfix('better_safes', 'BetterSafes',
    """,GD_Balance_Treasure.LootableGrades.ObjectGrade_Safe,DefaultLoot,,
    (
        ( 
            ConfigurationName="EridiumStick", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo4" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo3" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Eridium", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo4" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo3" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Safe_Cash", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo3" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo4" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Grenade", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_3_Uncommoner', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Grenade" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Grenades', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Shield" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Grenades', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Shield", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_3_Uncommoner', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Shield" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_ArtifactsReward', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.500000 
                    ), 
                    AttachmentPointName="Grenade" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Pistol", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_3_Uncommoner', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Grenade" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Repeater', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Shield" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ) 
            ) 
        )
    )
    """)

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
### Testing hotfixes, not really intended to be used for real.  These
### aren't referenced in the body of the mod, so they'll only activate
### on the standalone version.
###

# This one causes nearly every enemy to be a badass.
#hfs.add_level_hotfix('badasses', 'Badass',
#    """,GD_Balance.WeightingPlayerCount.Enemy_MajorUpgrade_PerPlayer,ConditionalInitialization,,
#    (
#        bEnabled=True,
#        ConditionalExpressionList=(
#            (
#                BaseValueIfTrue=(
#                    BaseValueConstant=500.000000,
#                    BaseValueAttribute=None,
#                    InitializationDefinition=None,
#                    BaseValueScaleConstant=20.000000
#                ),
#                Expressions=(
#                    (
#                        AttributeOperand1=AttributeDefinition'D_Attributes.GameProperties.NumberOfPlayers',
#                        ComparisonOperator=OPERATOR_LessThanOrEqual,
#                        Operand2Usage=OPERAND_PreferAttribute,
#                        AttributeOperand2=None,
#                        ConstantOperand2=4.000000
#                    )
#                )
#            )
#        ),
#        DefaultBaseValue=(
#            BaseValueConstant=0.000000,
#            BaseValueAttribute=None,
#            InitializationDefinition=None,
#            BaseValueScaleConstant=1.000000
#        )
#    )""")

# This makes nearly every SpiderAnt be Chubby -- similar techniques
# could be used to change enemy type rates in general
#hfs.add_level_hotfix('chubbies', 'ChubbySpawn',
#    ',GD_Population_SpiderAnt.Population.PopDef_SpiderantMix_Regular,ActorArchetypeList[9].Probability.BaseValueConstant,,1000')

###
### Everything below this point is constructing the actual patch file
###

# Process our forced GunsAndGear drop
gunsandgear_drop_str = ''
if force_gunsandgear_specific:
    gunsandgear_drop_str = """
    #<Force GunsAndGearDrop to {force_gunsandgear_specific_name}>

        # Forces the GunsAndGear drop pool to always drop {force_gunsandgear_specific_name}
        # Just used during my own testing to find out what exactly some items
        # are, when spawned in-game.

        set GD_Itempools.GeneralItemPools.Pool_GunsAndGear BalancedItems
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

        set {force_gunsandgear_drop_type} BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{force_gunsandgear_specific_name}',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

    #</Force GunsAndGearDrop to {force_gunsandgear_specific_name}>
    """.format(
        force_gunsandgear_drop_type=force_gunsandgear_drop_type,
        force_gunsandgear_specific_name=force_gunsandgear_specific_name,
        )
elif force_gunsandgear_drop:
    gunsandgear_drop_str = """
    #<Force GunsAndGearDrop to {force_gunsandgear_drop_type}>

        # Forces the GunsAndGear drop pool to always drop {force_gunsandgear_drop_type}
        # Just used during my own testing to get a feel for drop rates.

        set GD_Itempools.GeneralItemPools.Pool_GunsAndGear BalancedItems
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

# Process testing our drop pools
if test_drop_pools:
    drop_comment = ''
    drop_off = ''
    drop_wording = ''
else:
    drop_comment = '#'
    drop_off = '    <off>'
    drop_wording = ' (disabled by default)'
drop_chance_str_source = """

        #<{adjective} Enemy Loot Drop Chance{drop_wording}>

            {drop_comment}# Gives {description} chance to drop loot from enemies.{drop_off}
            {drop_comment}# Just used during my own testing to get a feel for drop rates.{drop_off}

            {drop_comment}set GD_Itempools.DropWeights.DropODDS_GunsAndGear:ConditionalAttributeValueResolver_0 ValueExpressions
            (
                bEnabled=True,
                ConditionalExpressionList=(
                    (
                        BaseValueIfTrue=(
                            BaseValueConstant={loot_drop_chance_1p},
                            BaseValueAttribute=None,
                            InitializationDefinition=None,
                            BaseValueScaleConstant=1.000000
                        ),
                        Expressions=(
                            (
                                AttributeOperand1=AttributeDefinition'D_Attributes.GameProperties.NumberOfPlayers',
                                ComparisonOperator=OPERATOR_EqualTo,
                                Operand2Usage=OPERAND_PreferAttribute,
                                AttributeOperand2=None,
                                ConstantOperand2=1.000000
                            )
                        )
                    ),
                    (
                        BaseValueIfTrue=(
                            BaseValueConstant={loot_drop_chance_2p},
                            BaseValueAttribute=None,
                            InitializationDefinition=None,
                            BaseValueScaleConstant=1.000000
                        ),
                        Expressions=(
                            (
                                AttributeOperand1=AttributeDefinition'D_Attributes.GameProperties.NumberOfPlayers',
                                ComparisonOperator=OPERATOR_EqualTo,
                                Operand2Usage=OPERAND_PreferAttribute,
                                AttributeOperand2=None,
                                ConstantOperand2=2.000000
                            )
                        )
                    ),
                    (
                        BaseValueIfTrue=(
                            BaseValueConstant={loot_drop_chance_3p},
                            BaseValueAttribute=None,
                            InitializationDefinition=None,
                            BaseValueScaleConstant=1.000000
                        ),
                        Expressions=(
                            (
                                AttributeOperand1=AttributeDefinition'D_Attributes.GameProperties.NumberOfPlayers',
                                ComparisonOperator=OPERATOR_EqualTo,
                                Operand2Usage=OPERAND_PreferAttribute,
                                AttributeOperand2=None,
                                ConstantOperand2=3.000000
                            )
                        )
                    ),
                    (
                        BaseValueIfTrue=(
                            BaseValueConstant={loot_drop_chance_4p},
                            BaseValueAttribute=None,
                            InitializationDefinition=None,
                            BaseValueScaleConstant=1.000000
                        ),
                        Expressions=(
                            (
                                AttributeOperand1=AttributeDefinition'D_Attributes.GameProperties.NumberOfPlayers',
                                ComparisonOperator=OPERATOR_EqualTo,
                                Operand2Usage=OPERAND_PreferAttribute,
                                AttributeOperand2=None,
                                ConstantOperand2=4.000000
                            )
                        )
                    )
                ),
                DefaultBaseValue=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                )
            ){drop_off}

        #</{adjective} Enemy Loot Drop Chance{drop_wording}>"""

drop_quantity_str_source = """
    #<Extreme Enemy Loot Drop Quantity{drop_wording}>

        {drop_comment}# Enemies drop {loot_drop_quantity} items instead of just one.{drop_off}
        {drop_comment}# Just used during my own testing to get a feel for drop rates.{drop_off}

        {drop_comment}set GD_Itempools.GeneralItemPools.Pool_GunsAndGear Quantity
        (
            BaseValueConstant={loot_drop_quantity},
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        ){drop_off}

        #<Torgue Biker Gangs>

            {drop_comment}set GD_Iris_ItemPools.EnemyDropPools.Pool_GunsAndGear_WeightedAngelGang Quantity
            (
                BaseValueConstant={loot_drop_quantity},
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            ){drop_off}

            {drop_comment}set GD_Iris_ItemPools.EnemyDropPools.Pool_GunsAndGear_WeightedDragonGang Quantity
            (
                BaseValueConstant={loot_drop_quantity},
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            ){drop_off}

            {drop_comment}set GD_Iris_ItemPools.EnemyDropPools.Pool_GunsAndGear_WeightedTorgueGang Quantity
            (
                BaseValueConstant={loot_drop_quantity},
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            ){drop_off}

        #</Torgue Biker Gangs>

    #</Extreme Enemy Loot Drop Quantity{drop_wording}>"""

# Guaranteed drop chance string
test_drop_chance_guaranteed_str = drop_chance_str_source.format(
        adjective='Guaranteed',
        description='a 100%',
        drop_comment=drop_comment,
        drop_off=drop_off,
        drop_wording=drop_wording,
        loot_drop_chance_1p=loot_drop_chance_1p,
        loot_drop_chance_2p=loot_drop_chance_2p,
        loot_drop_chance_3p=loot_drop_chance_3p,
        loot_drop_chance_4p=loot_drop_chance_4p,
    )

# Merely improved drop chance string
test_drop_chance_improved_str = drop_chance_str_source.format(
        adjective='Improved',
        description='a doubled',
        drop_comment='#',
        drop_off='    <off>',
        drop_wording=' (disabled by default)',
        loot_drop_chance_1p=loot_drop_chance_1p_alt,
        loot_drop_chance_2p=loot_drop_chance_2p_alt,
        loot_drop_chance_3p=loot_drop_chance_3p_alt,
        loot_drop_chance_4p=loot_drop_chance_4p_alt,
    )

# Concatenate our drop chance stanzas in one mutually-exclusive folder
test_drop_chance_str = """
    #<Enemy Loot Drop Chance Modification (choose one){drop_wording}><MUT>
{test_drop_chance_guaranteed_str}
{test_drop_chance_improved_str}

    #</Enemy Loot Drop Chance Modification (choose one){drop_wording}>
""".format(
        drop_wording=drop_wording,
        test_drop_chance_guaranteed_str=test_drop_chance_guaranteed_str,
        test_drop_chance_improved_str=test_drop_chance_improved_str,
    )

# Test drop quantity string
test_drop_quantity_str = drop_quantity_str_source.format(
        drop_comment=drop_comment,
        drop_off=drop_off,
        drop_wording=drop_wording,
        loot_drop_quantity=loot_drop_quantity,
    )

# Now read in our main input file
with open(input_filename, 'r') as df:
    loot_str = df.read()

# Loop through our profiles and generate the files
for profile in profiles:

    # Write our UCP-compatible version
    with open(profile.filename(mod_name, variant_ucp), 'w') as df:
        df.write(loot_str.format(
            mod_name=mod_name,
            mod_version=mod_version,
            mod_type='BL2',
            variant_name=variant_ucp,
            config=profile,
            hotfixes=hfs,
            hotfix_gearbox_base='',
            hotfix_transient_defs='',
            gunsandgear_drop_str=gunsandgear_drop_str,
            test_drop_chance_str=test_drop_chance_str,
            test_drop_quantity_str=test_drop_quantity_str,
            ))
    print('Wrote UCP-compatible ({}) mod file to: {}'.format(
        profile.profile_name,
        profile.filename(mod_name, variant_ucp),
        ))

    # Write to a standalone file
    with open(profile.filename(mod_name, variant_standalone), 'w') as df:
        df.write(loot_str.format(
            mod_name=mod_name,
            mod_version=mod_version,
            mod_type='BL2',
            variant_name=variant_standalone,
            config=profile,
            hotfixes=hfs,
            hotfix_gearbox_base=hfs.get_gearbox_hotfix_xml(),
            hotfix_transient_defs=hfs.get_transient_defs(),
            gunsandgear_drop_str=gunsandgear_drop_str,
            test_drop_chance_str=test_drop_chance_str,
            test_drop_quantity_str=test_drop_quantity_str,
            ))
    print('Wrote standalone ({}) mod file to: {}'.format(
        profile.profile_name,
        profile.filename(mod_name, variant_standalone),
        ))

    # Write to a standalone offline file
    with open(profile.filename(mod_name, variant_offline), 'w') as df:
        df.write(loot_str.format(
            mod_name=mod_name,
            mod_version=mod_version,
            mod_type='Offline',
            variant_name=variant_offline,
            config=profile,
            hotfixes=hfs,
            hotfix_gearbox_base=hfs.get_gearbox_hotfix_xml(),
            hotfix_transient_defs=hfs.get_transient_defs(offline=True),
            gunsandgear_drop_str=gunsandgear_drop_str,
            test_drop_chance_str=test_drop_chance_str,
            test_drop_quantity_str=test_drop_quantity_str,
            ))
    print('Wrote standalone offline ({}) mod file to: {}'.format(
        profile.profile_name,
        profile.filename(mod_name, variant_offline),
        ))
