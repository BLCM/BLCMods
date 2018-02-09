#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Python script to generate my BL2 Better Loot Mod.  All the drop
# weights and stuff can be controlled by all the variables at the
# top of the file.  Generates a human-readable multiline file which
# must be converted using conv_to_mod.py in order to be loaded by
# Borderlands / FilterTool.

from hotfixes import Hotfixes

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

hfs = Hotfixes()

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
weapon_scale_rare = '55.000000'
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
treasure_scale_rare = '10.000000'
treasure_scale_veryrare = '65.000000'
treasure_scale_alien = '30.000000'
treasure_scale_legendary = '10.000000'

# Drop rates for "epic" treasure chests
epic_scale_veryrare = '1.000000'
epic_scale_alien = '1.000000'
epic_scale_legendary = '0.500000'
epic_scale_legendary_dbl = '1.000000'

# Drop rates within the "very high roll" pools of dice chests
dice_vhigh_veryrare = '1.000000'
dice_vhigh_alien = '1.000000'
dice_vhigh_legendary = '0.050000'

# 3x chance of both kinds of eridium
eridium_bar_drop = '0.004500'       # Stock: 0.001500
eridium_stick_drop = '0.024000'     # Stock: 0.008000

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

# Make No-Beard always drop his unique
hfs.add_level_hotfix('scarlett_nobeard', 'NoBeardDrop',
    ',GD_Orchid_Pop_NoBeard.PawnBalance_Orchid_NoBeard,DefaultItemPoolList[1].PoolProbability.BaseValueConstant,,1.0')

# Make Big Sleep always drop his unique
hfs.add_level_hotfix('scarlett_bigsleep', 'BigSleepDrop',
    ',GD_Orchid_Pop_Sandman.Balance.PawnBalance_Orchid_BigSleep,DefaultItemPoolList[1].PoolProbability.BaseValueConstant,,1.0')

# UCP Compatibility fixes: We need to add in a hotfix to set Hyperius and
# Master Gee to always drop from their Legendary pool.  We hardcode that
# with a regular "set" command, but a UCP hotfix (to improve the Legendary
# drop rate) would overwrite our 100% chance.  So, in addition to the "set"
# command, we'll overwrite the probability again.
hfs.add_level_hotfix('scarlett_hyperius_ucp_fix', 'HyperiusUCPFix',
    ',GD_Orchid_ItemPools.Raid.PoolList_Orchid_Raid1_Items,Itempools[0].PoolProbability.BaseValueConstant,,1.0')
hfs.add_level_hotfix('scarlett_mastergee_ucp_fix', 'MasterGeeUCPFix',
    ',GD_Orchid_ItemPools.Raid.PoolList_Orchid_Raid3_Items,Itempools[0].PoolProbability.BaseValueConstant,,1.0')

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

# Make Bulstoss also drop from the Badass loot pool
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
