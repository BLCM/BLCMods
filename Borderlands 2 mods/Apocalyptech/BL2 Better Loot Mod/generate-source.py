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

mod_name = 'BL2 Better Loot Mod by Apocalyptech'
variant_filtertool_name = 'UCP Compat'
variant_standalone_name = 'Standalone'
output_filename_filtertool = '{} - {}-source.txt'.format(mod_name, variant_filtertool_name)
output_filename_standalone = '{} - {}-source.txt'.format(mod_name, variant_standalone_name)

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

# Just some convenience vars
one = '1.000000'
zero = '0.000000'

# "BaseValueConstant values for the various gear drop types.  These
# are actually totally unchanged from the stock definitions; I'd just
# put them in here in case I felt like overriding them easily later.
weapon_base_common = one
weapon_base_uncommon = one
weapon_base_rare = one
weapon_base_veryrare = one
weapon_base_alien = one
weapon_base_legendary = one
cm_base_common = one
cm_base_uncommon = one
cm_base_rare = one
cm_base_veryrare = one
cm_base_legendary = one
grenade_base_common = zero
grenade_base_uncommon = zero
grenade_base_rare = zero
grenade_base_veryrare = zero
grenade_base_legendary = zero
shield_base_common = one
shield_base_uncommon = one
shield_base_rare = one
shield_base_veryrare = one
shield_base_legendary = one

# Custom weapon drop scaling
weapon_scale_common = '8.000000'
weapon_scale_uncommon = '85.000000'
weapon_scale_rare = '65.000000'
weapon_scale_veryrare = '50.000000'
weapon_scale_alien = '30.000000'
weapon_scale_legendary = '3.000000'
weapon_scale_iris_cobra = '1.000000'

# Custom COM drop scaling (identical to weapons, apart from an additional Alignment COM pool)
cm_scale_common = weapon_scale_common
cm_scale_uncommon = weapon_scale_uncommon
cm_scale_rare = weapon_scale_rare
cm_scale_veryrare = weapon_scale_veryrare
cm_scale_alignment = '30.000000'
cm_scale_legendary = weapon_scale_legendary

# Custom grenade drop scaling (identical to weapons)
grenade_scale_common = weapon_scale_common
grenade_scale_uncommon = weapon_scale_uncommon
grenade_scale_rare = weapon_scale_rare
grenade_scale_veryrare = weapon_scale_veryrare
grenade_scale_legendary = weapon_scale_legendary

# Custom shield drop scaling (identical to weapons)
shield_scale_common = weapon_scale_common
shield_scale_uncommon = weapon_scale_uncommon
shield_scale_rare = weapon_scale_rare
shield_scale_veryrare = weapon_scale_veryrare
shield_scale_legendary = weapon_scale_legendary

# Custom relic drop scaling
relic_scale_rare = '1.0'
relic_scale_veryrare = '2.0'

# Drop rates for "regular" treasure chests
treasure_scale_rare = '20.000000'
treasure_scale_veryrare = '60.000000'
treasure_scale_alien = '30.000000'
treasure_scale_legendary = '5.000000'

# Drop rates for "epic" treasure chests
epic_scale_veryrare = '1.000000'
epic_scale_alien = '1.000000'
epic_scale_legendary = '0.300000'
epic_scale_legendary_dbl = '0.600000'

# Drop rates within the "very high roll" pools of dice chests
dice_vhigh_veryrare = '1.000000'
dice_vhigh_alien = '1.000000'
dice_vhigh_legendary = '0.500000'

# 2.5x chance of both kinds of eridium
eridium_bar_drop = '0.003750'       # Stock: 0.001500
eridium_stick_drop = '0.020000'     # Stock: 0.008000

# Gun Type drop weights
drop_prob_pistol = 100
drop_prob_ar = 100
drop_prob_smg = 100
drop_prob_shotgun = 100
drop_prob_sniper = 80
drop_prob_launcher = 40

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
            ('Pistol', drop_prob_pistol),
            ('AR', drop_prob_ar),
            ('SMG', drop_prob_smg),
            ('Shotgun', drop_prob_shotgun),
            ('Sniper', drop_prob_sniper),
            ('Launcher', drop_prob_launcher),
            ]):
        hfs.add_level_hotfix('normalize_weapon_types_{}_{}'.format(rarity, guntype),
            'NormWeap{}{}'.format(rarity, guntype),
            ',GD_Itempools.WeaponPools.Pool_Weapons_All_{}_{},BalancedItems[{}].Probability.BaseValueConstant,,{}'.format(
                number,
                rarity,
                idx,
                gunprob))

# Make Shirtless Men drop from the badass pool pool
hfs.add_level_hotfix('shirtless_man_badass', 'ShirtlessManDrop',
    "Interlude_P,GD_Population_Marauder.Balance.Unique.PawnBalance_ShirtlessMan,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Gluttonous Thresher drop from the super badass pool pool
hfs.add_level_hotfix('gluttonous_badass', 'GluttonousDrop',
    "Outwash_P,GD_Population_Thresher.Balance.PawnBalance_ThresherGluttonous,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear'")

# Make Sinkhole drop from the badass pool pool
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
            BaseValueScaleConstant=0.600000
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

# Make Badass Knights drop from the badass pool pool
hfs.add_level_hotfix('dragonkeep_badass_knights', 'BadassKnightsDrop',
    ",GD_Aster_Pop_Knights.Balance.PawnBalance_Knight_Badass,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Badass Fire Archers drop from the badass pool pool
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

# Early-game weapon/grenade part unlocks - some of these have to be done via
# hotfixes, rather than `set` statements.  These are generated via
# `restricted_parts.py`, using data from FilterTool.
hfs.add_level_hotfix('part_early_game_fix_0', 'PartEarlyGameFix', ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_1', 'PartEarlyGameFix', ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_2', 'PartEarlyGameFix', ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_3', 'PartEarlyGameFix', ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_4', 'PartEarlyGameFix', ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_5', 'PartEarlyGameFix', ",GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_6', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223,BodyPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.Body.SMG_Body_Maliwan_VarC',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=0,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Body.SMG_Body_Maliwan_VarB',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1))")
hfs.add_level_hotfix('part_early_game_fix_7', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223,GripPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.Grip.SMG_Grip_Tediore',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Grip.SMG_Grip_Bandit',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Grip.SMG_Grip_Dahl',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Grip.SMG_Grip_Maliwan',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Grip.SMG_Grip_Hyperion',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1))")
hfs.add_level_hotfix('part_early_game_fix_8', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223,BarrelPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Aster_Weapons.SMGs.SMG_Barrel_Hyperion_Crit',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1))")
hfs.add_level_hotfix('part_early_game_fix_9', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223,SightPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.Sight.SMG_Sight_None',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Sight.SMG_Sight_Tedior',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Sight.SMG_Sight_Bandit',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Sight.SMG_Sight_Dahl',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Sight.SMG_Sight_Maliwan',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Sight.SMG_Sight_Hyperion',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1))")
hfs.add_level_hotfix('part_early_game_fix_10', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223,StockPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.Stock.SMG_Stock_Tediore',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Stock.SMG_Stock_Bandit',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Stock.SMG_Stock_Dahl',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Stock.SMG_Stock_Maliwan',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1),(Part=WeaponPartDefinition'GD_Weap_SMG.Stock.SMG_Stock_Hyperion',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1))")
hfs.add_level_hotfix('part_early_game_fix_11', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1))")
hfs.add_level_hotfix('part_early_game_fix_12', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223,Accessory1PartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.Accessory.SMG_Accessory_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=3)),MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_SMG.Accessory.SMG_Accessory_Bayonet_1',Manufacturers=((Manufacturer=None,DefaultWeightIndex=3)),MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.Accessory.SMG_Accessory_Body1_Accurate',Manufacturers=((Manufacturer=None,DefaultWeightIndex=3)),MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.Accessory.SMG_Accessory_Body2_Damage',Manufacturers=((Manufacturer=None,DefaultWeightIndex=3)),MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.Accessory.SMG_Accessory_Body3_Accelerated',Manufacturers=((Manufacturer=None,DefaultWeightIndex=3)),MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.Accessory.SMG_Accessory_Stock1_Stabilized',Manufacturers=((Manufacturer=None,DefaultWeightIndex=3)),MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload',Manufacturers=((Manufacturer=None,DefaultWeightIndex=3)),MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_13', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223,MaterialPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Aster_Weapons.ManufacturerMaterials.Mat_Maliwan_3_Crit',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=3,DefaultWeightIndex=1))")
hfs.add_level_hotfix('part_early_game_fix_14', 'PartEarlyGameFix', ",GD_Aster_RaidWeapons.Shotguns.Aster_Seraph_Omen_Balance:WeaponPartListCollectionDefinition_224,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_15', 'PartEarlyGameFix', ",GD_Aster_RaidWeapons.Pistols.Aster_Seraph_Stinger_Balance:WeaponPartListCollectionDefinition_225,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_16', 'PartEarlyGameFix', ",GD_Aster_Weapons.AssaultRifles.AR_Bandit_4_Quartz:WeaponPartListCollectionDefinition_231,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_17', 'PartEarlyGameFix', ",GD_Aster_Weapons.AssaultRifles.AR_Dahl_4_Emerald:WeaponPartListCollectionDefinition_232,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_18', 'PartEarlyGameFix', ",GD_Aster_Weapons.AssaultRifles.AR_Vladof_4_Garnet:WeaponPartListCollectionDefinition_233,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_19', 'PartEarlyGameFix', ",GD_Aster_Weapons.Pistols.Pistol_Bandit_4_Quartz:WeaponPartListCollectionDefinition_235,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_20', 'PartEarlyGameFix', ",GD_Aster_Weapons.Pistols.Pistol_Tediore_4_CubicZerconia:WeaponPartListCollectionDefinition_236,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_21', 'PartEarlyGameFix', ",GD_Aster_Weapons.Pistols.Pistol_Dahl_4_Emerald:WeaponPartListCollectionDefinition_237,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_22', 'PartEarlyGameFix', ",GD_Aster_Weapons.Pistols.Pistol_Vladof_4_Garnet:WeaponPartListCollectionDefinition_238,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_23', 'PartEarlyGameFix', ",GD_Aster_Weapons.Pistols.Pistol_Maliwan_4_Aquamarine:WeaponPartListCollectionDefinition_239,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2))")
hfs.add_level_hotfix('part_early_game_fix_24', 'PartEarlyGameFix', ",GD_Aster_Weapons.Pistols.Pistol_Hyperion_4_Diamond:WeaponPartListCollectionDefinition_241,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_25', 'PartEarlyGameFix', ",GD_Aster_Weapons.Shotguns.SG_Bandit_4_Quartz:WeaponPartListCollectionDefinition_242,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_26', 'PartEarlyGameFix', ",GD_Aster_Weapons.Shotguns.SG_Tediore_4_CubicZerconia:WeaponPartListCollectionDefinition_243,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_27', 'PartEarlyGameFix', ",GD_Aster_Weapons.Shotguns.SG_Hyperion_4_Diamond:WeaponPartListCollectionDefinition_245,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_28', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Bandit_4_Quartz:WeaponPartListCollectionDefinition_246,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_29', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Tediore_4_CubicZerconia:WeaponPartListCollectionDefinition_247,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_30', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Dahl_4_Emerald:WeaponPartListCollectionDefinition_248,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_31', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Maliwan_4_Aquamarine:WeaponPartListCollectionDefinition_249,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_32', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Hyperion_4_Diamond:WeaponPartListCollectionDefinition_250,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_33', 'PartEarlyGameFix', ",GD_Aster_Weapons.Snipers.SR_Dahl_4_Emerald:WeaponPartListCollectionDefinition_251,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_None',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Fire',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Shock',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Corrosive',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Slag',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2))")
hfs.add_level_hotfix('part_early_game_fix_34', 'PartEarlyGameFix', ",GD_Aster_Weapons.Snipers.SR_Vladof_4_Garnet:WeaponPartListCollectionDefinition_252,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_None',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Fire',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Shock',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Corrosive',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Slag',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2))")
hfs.add_level_hotfix('part_early_game_fix_35', 'PartEarlyGameFix', ",GD_Aster_Weapons.Snipers.SR_Hyperion_4_Diamond:WeaponPartListCollectionDefinition_255,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_None',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Fire',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Shock',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Corrosive',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Slag',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2))")
hfs.add_level_hotfix('part_early_game_fix_36', 'PartEarlyGameFix', ",GD_Aster_Weapons.SMGs.SMG_Bandit_3_Orc:WeaponPartListCollectionDefinition_258,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_37', 'PartEarlyGameFix', ",GD_Gladiolus_Weapons.Pistol.Pistol_Vladof_6_Stalker:WeaponPartListCollectionDefinition_260,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_38', 'PartEarlyGameFix', ",GD_Gladiolus_Weapons.AssaultRifle.AR_Dahl_6_Bearcat:WeaponPartListCollectionDefinition_262,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_39', 'PartEarlyGameFix', ",GD_Gladiolus_Weapons.SMG.SMG_Tediore_6_Avenger:WeaponPartListCollectionDefinition_263,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_40', 'PartEarlyGameFix', ",GD_Gladiolus_Weapons.Shotgun.SG_Hyperion_6_Butcher:WeaponPartListCollectionDefinition_264,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_41', 'PartEarlyGameFix', ",GD_Iris_ItemPools.BalDefs.BalDef_ClassMod_Torgue_Common:ItemPartListCollectionDefinition_39,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_42', 'PartEarlyGameFix', ",GD_Iris_Weapons.Shotguns.SG_Hyperion_3_SlowHand:WeaponPartListCollectionDefinition_267,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_43', 'PartEarlyGameFix', ",GD_Iris_Weapons.AssaultRifles.AR_Vladof_3_Kitten:WeaponPartListCollectionDefinition_272,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4))")
hfs.add_level_hotfix('part_early_game_fix_44', 'PartEarlyGameFix', ",GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho:ItemPartListCollectionDefinition_40,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_45', 'PartEarlyGameFix', ",GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_04_VeryRare:ItemPartListCollectionDefinition_44,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_46', 'PartEarlyGameFix', ",GD_Lobelia_Weapons.Pistol.Pistol_Maliwan_6_Wanderlust:WeaponPartListCollectionDefinition_274,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Pistol.elemental.Pistol_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_47', 'PartEarlyGameFix', ",GD_Orchid_RaidWeapons.SMG.Tattler.Orchid_Seraph_Tattler_Balance:WeaponPartListCollectionDefinition_282,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_48', 'PartEarlyGameFix', ",GD_Orchid_RaidWeapons.Shotgun.Spitter.Orchid_Seraph_Spitter_Balance:WeaponPartListCollectionDefinition_283,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3))")
hfs.add_level_hotfix('part_early_game_fix_49', 'PartEarlyGameFix', ",GD_Orchid_RaidWeapons.SMG.Actualizer.Orchid_Seraph_Actualizer_Balance:WeaponPartListCollectionDefinition_284,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_50', 'PartEarlyGameFix', ",GD_Orchid_RaidWeapons.sniper.Patriot.Orchid_Seraph_Patriot_Balance:WeaponPartListCollectionDefinition_286,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_None',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Fire',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Shock',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Corrosive',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Slag',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2))")
hfs.add_level_hotfix('part_early_game_fix_51', 'PartEarlyGameFix', ",GD_Orchid_BossWeapons.AssaultRifle.AR_Vladof_3_Rapier:WeaponPartListCollectionDefinition_289,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4))")
hfs.add_level_hotfix('part_early_game_fix_52', 'PartEarlyGameFix', ",GD_Orchid_BossWeapons.Shotgun.SG_Bandit_3_JollyRoger:WeaponPartListCollectionDefinition_290,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4))")
hfs.add_level_hotfix('part_early_game_fix_53', 'PartEarlyGameFix', ",GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk:WeaponPartListCollectionDefinition_292,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_SMG.elemental.SMG_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_54', 'PartEarlyGameFix', ",GD_Orchid_BossWeapons.SniperRifles.Sniper_Maliwan_3_Pimpernel:WeaponPartListCollectionDefinition_293,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Fire',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Shock',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Corrosive',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2),(Part=WeaponPartDefinition'GD_Weap_SniperRifles.elemental.SR_Elemental_Slag',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=2))")
hfs.add_level_hotfix('part_early_game_fix_55', 'PartEarlyGameFix', ",GD_Sage_RaidWeapons.Shotgun.Sage_Seraph_Interfacer_Balance:WeaponPartListCollectionDefinition_297,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5),(Part=WeaponPartDefinition'GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=5))")
hfs.add_level_hotfix('part_early_game_fix_56', 'PartEarlyGameFix', ",GD_Sage_RaidWeapons.AssaultRifle.Sage_Seraph_LeadStorm_Balance:WeaponPartListCollectionDefinition_298,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4))")
hfs.add_level_hotfix('part_early_game_fix_57', 'PartEarlyGameFix', ",GD_Sage_Weapons.AssaultRifle.AR_Bandit_3_Chopper:WeaponPartListCollectionDefinition_303,ElementalPartData.WeightedParts,,((Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_None',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=3),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4),(Part=WeaponPartDefinition'GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag',Manufacturers=((Manufacturer=None,DefaultWeightIndex=1)),MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=4))")
hfs.add_level_hotfix('part_early_game_fix_58', 'PartEarlyGameFix', ",GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer:ItemPartListCollectionDefinition_48,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_NoSkill',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")
hfs.add_level_hotfix('part_early_game_fix_59', 'PartEarlyGameFix', ",GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_04_VeryRare:ItemPartListCollectionDefinition_52,AlphaPartData.WeightedParts,,((Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0),(Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',Manufacturers=,MinGameStageIndex=0,MaxGameStageIndex=1,DefaultWeightIndex=0))")

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

# This will cause varkids to always morph into their next stage, up
# through Vermivorous (even in Normal mode).  Used to test Verm drops.
# Still have to wait for their timers to elapse before they evolve, of course.
#for morph in range(1,6):
#    hfs.add_level_hotfix('varkid_clear_{}'.format(morph),
#        'VarkidMorphClear',
#        ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase{},ConditionalInitialization.ConditionalExpressionList,,()'.format(morph))
#    hfs.add_level_hotfix('varkid_default_{}'.format(morph),
#        'VarkidMorphDefault',
#        ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase{},ConditionalInitialization.DefaultBaseValue.BaseValueConstant,,1.0'.format(morph))

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
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=2.200000
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
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
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
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=2.200000
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
test_drop_str = """

    #<Guaranteed Enemy Loot Drop Chance{drop_wording}>

        {drop_comment}# Gives a 100% chance to drop loot from enemies.{drop_off}
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

    #</Guaranteed Enemy Loot Drop Chance{drop_wording}>

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

    #</Extreme Enemy Loot Drop Quantity{drop_wording}>
    """.format(
            drop_comment=drop_comment,
            drop_off=drop_off,
            drop_wording=drop_wording,
            loot_drop_chance_1p=loot_drop_chance_1p,
            loot_drop_chance_2p=loot_drop_chance_2p,
            loot_drop_chance_3p=loot_drop_chance_3p,
            loot_drop_chance_4p=loot_drop_chance_4p,
            loot_drop_quantity=loot_drop_quantity,
        )

# Forcing the "Reward" Relic pool to obey our custom weights.  There's
# 22 of these definitions which are all identical (and one outlier), so
# we're going use a loop rather than a lot of copy+paste.
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
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={relic_scale_rare}
                    ),
                    (
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={relic_scale_veryrare}
                    )
                )
""".format(
    relic_type=relic_type,
    relic_scale_rare=relic_scale_rare,
    relic_scale_veryrare=relic_scale_veryrare,
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
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={relic_scale_rare}
                    ),
                    (
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={relic_scale_veryrare}
                    )
                )
""".format(
    relic_type=relic_type,
    relic_scale_rare=relic_scale_rare,
    relic_scale_veryrare=relic_scale_veryrare,
    ))
relic_weight_str = ''.join(relic_weight_parts).lstrip()

# Now read in our main input file and substitute all of our variables.
with open(input_filename, 'r') as df:
    loot_str = df.read().format(
        mod_name=mod_name,
        weapon_base_common=weapon_base_common,
        weapon_scale_common=weapon_scale_common,
        weapon_base_uncommon=weapon_base_uncommon,
        weapon_scale_uncommon=weapon_scale_uncommon,
        weapon_base_rare=weapon_base_rare,
        weapon_scale_rare=weapon_scale_rare,
        weapon_base_veryrare=weapon_base_veryrare,
        weapon_scale_veryrare=weapon_scale_veryrare,
        weapon_base_alien=weapon_base_alien,
        weapon_scale_alien=weapon_scale_alien,
        weapon_base_legendary=weapon_base_legendary,
        weapon_scale_legendary=weapon_scale_legendary,
        weapon_scale_iris_cobra=weapon_scale_iris_cobra,
        cm_base_common=cm_base_common,
        cm_scale_common=cm_scale_common,
        cm_base_uncommon=cm_base_uncommon,
        cm_scale_uncommon=cm_scale_uncommon,
        cm_base_rare=cm_base_rare,
        cm_scale_rare=cm_scale_rare,
        cm_base_veryrare=cm_base_veryrare,
        cm_scale_veryrare=cm_scale_veryrare,
        cm_scale_alignment=cm_scale_alignment,
        cm_base_legendary=cm_base_legendary,
        cm_scale_legendary=cm_scale_legendary,
        grenade_base_common=grenade_base_common,
        grenade_scale_common=grenade_scale_common,
        grenade_base_uncommon=grenade_base_uncommon,
        grenade_scale_uncommon=grenade_scale_uncommon,
        grenade_base_rare=grenade_base_rare,
        grenade_scale_rare=grenade_scale_rare,
        grenade_base_veryrare=grenade_base_veryrare,
        grenade_scale_veryrare=grenade_scale_veryrare,
        grenade_base_legendary=grenade_base_legendary,
        grenade_scale_legendary=grenade_scale_legendary,
        shield_base_common=shield_base_common,
        shield_scale_common=shield_scale_common,
        shield_base_uncommon=shield_base_uncommon,
        shield_scale_uncommon=shield_scale_uncommon,
        shield_base_rare=shield_base_rare,
        shield_scale_rare=shield_scale_rare,
        shield_base_veryrare=shield_base_veryrare,
        shield_scale_veryrare=shield_scale_veryrare,
        shield_base_legendary=shield_base_legendary,
        shield_scale_legendary=shield_scale_legendary,
        dice_vhigh_veryrare=dice_vhigh_veryrare,
        dice_vhigh_alien=dice_vhigh_alien,
        dice_vhigh_legendary=dice_vhigh_legendary,
        eridium_bar_drop=eridium_bar_drop,
        eridium_stick_drop=eridium_stick_drop,
        treasure_scale_rare=treasure_scale_rare,
        treasure_scale_veryrare=treasure_scale_veryrare,
        treasure_scale_alien=treasure_scale_alien,
        treasure_scale_legendary=treasure_scale_legendary,
        epic_scale_veryrare=epic_scale_veryrare,
        epic_scale_alien=epic_scale_alien,
        epic_scale_legendary=epic_scale_legendary,
        epic_scale_legendary_dbl=epic_scale_legendary_dbl,
        gunsandgear_drop_str=gunsandgear_drop_str,
        relic_weight_str=relic_weight_str,
        test_drop_str=test_drop_str,
        hotfixes=hfs,
        variant_name='{variant_name}',
        hotfix_gearbox_base='{hotfix_gearbox_base}',
        hotfix_transient_defs='{hotfix_transient_defs}',
    )

# Write to a filtertool/ucp compatible file
with open(output_filename_filtertool, 'w') as df:
    df.write(loot_str.format(
        variant_name=variant_filtertool_name,
        hotfix_gearbox_base='',
        hotfix_transient_defs='',
        ))
print('Wrote UCP-compatible mod file to: {}'.format(output_filename_filtertool))

# Write to a standalone file
with open(output_filename_standalone, 'w') as df:
    df.write(loot_str.format(
        variant_name=variant_standalone_name,
        hotfix_gearbox_base=hfs.get_gearbox_hotfix_xml(),
        hotfix_transient_defs=hfs.get_transient_defs(),
        ))
print('Wrote standalone mod file to: {}'.format(output_filename_standalone))
