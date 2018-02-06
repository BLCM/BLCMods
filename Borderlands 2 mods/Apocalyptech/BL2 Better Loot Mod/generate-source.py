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
variant_filtertool_name = 'FilterTool and UCP Compat'
variant_standalone_name = 'Standalone'
output_filename_filtertool = '{} - {}-source.txt'.format(mod_name, variant_filtertool_name)
output_filename_standalone = '{} - {}-source.txt'.format(mod_name, variant_standalone_name)

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
hfs.add_hotfix('scarlett_nobeard', 'SparkLevelPatchEntry-NoBeardDrop1',
    ',GD_Orchid_Pop_NoBeard.PawnBalance_Orchid_NoBeard,DefaultItemPoolList[1].PoolProbability.BaseValueConstant,,1.0')

# Make Big Sleep always drop his unique
hfs.add_hotfix('scarlett_bigsleep', 'SparkLevelPatchEntry-BigSleepDrop1',
    ',GD_Orchid_Pop_Sandman.Balance.PawnBalance_Orchid_BigSleep,DefaultItemPoolList[1].PoolProbability.BaseValueConstant,,1.0')

# Make the Chubby drop pool better.
hfs.add_hotfix('chubby_drop', 'SparkLevelPatchEntry-ChubbyDrop1',
    ",GD_Itempools.ListDefs.ChubbyEnemyGunsAndGear,ItemPools,,((ItemPool=ItemPoolDefinition'GD_Itempools.Runnables.Pool_ChubbieUniques',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGear',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGear',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.VehicleSkins.Pool_VehicleSkins_All',PoolProbability=(BaseValueConstant=0.000000,BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_VehicleSkins',InitializationDefinition=None,BaseValueScaleConstant=10.000000)),(ItemPool=CrossDLCItemPoolDefinition'GD_Lobelia_Itempools.WeaponPools.Pool_Lobelia_Pearlescent_Weapons_All',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.BuffDrinkPools.Pool_BuffDrinks_HealingInstant',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_NeedOnly',PoolProbability=(BaseValueConstant=0.000000,BaseValueAttribute=None,InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',BaseValueScaleConstant=0.250000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_Emergency',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)))")

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
        hfs.add_hotfix('grenade_{}_{}_0'.format(gm_type, man_num),
            'SparkLevelPatchEntry-Grenade{}{}-0'.format(gm_type, man_num),
            ',GD_GrenadeMods.A_Item.GM_{},Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage,,0'.format(
                gm_type, man_num,
            ))
        hfs.add_hotfix('grenade_{}_{}_1'.format(gm_type, man_num),
            'SparkLevelPatchEntry-Grenade{}{}-1'.format(gm_type, man_num),
            ',GD_GrenadeMods.A_Item.GM_{}_2_Uncommon,Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage,,0'.format(
                gm_type, man_num,
            ))
        hfs.add_hotfix('grenade_{}_{}_2'.format(gm_type, man_num),
            'SparkLevelPatchEntry-Grenade{}{}-2'.format(gm_type, man_num),
            ',GD_GrenadeMods.A_Item.GM_{}_3_Rare,Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage,,0'.format(
                gm_type, man_num,
            ))
        hfs.add_hotfix('grenade_{}_{}_3'.format(gm_type, man_num),
            'SparkLevelPatchEntry-Grenade{}{}-3'.format(gm_type, man_num),
            ',GD_GrenadeMods.A_Item.GM_{}_4_VeryRare,Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage,,0'.format(
                gm_type, man_num,
            ))

# Make Piston always drop the Slow Hand
hfs.add_hotfix('torgue_piston', 'SparkLevelPatchEntry-PistonDropSlowHand0',
    ',GD_Iris_Population_PistonBoss.Balance.Iris_PawnBalance_PistonBoss,DefaultItemPoolList[2].PoolProbability.BaseValueConstant,,1.0')

# Make Witch Doctors drop some slightly-more-interesting loot
for doctor in ['Fire', 'Shock', 'Slag', 'Slow', 'Vampire']:
    hfs.add_hotfix('witchdoctor_{}'.format(doctor),
        'SparkLevelPatchEntry-WitchDoctor{}Drops0'.format(doctor),
        ",GD_Sage_Pop_Natives.Balance.PawnBalance_WitchDoctor{},DefaultItemPoolList,,((ItemPool=ItemPoolDefinition'GD_CustomItemPools_Sage.Fanboat.Pool_Customs_Fanboat_All',PoolProbability=(BaseValueConstant=0.000000,BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_VehicleSkins',InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_ArtifactsReward',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.600000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)))".format(doctor))

# Badass Borok Fixes
for borok in ['Corrosive', 'Fire', 'Shock', 'Slag']:
    hfs.add_hotfix('badass_borok_{}'.format(borok),
        'SparkLevelPatchEntry-BadassBorok{}0'.format(borok),
        ",GD_Sage_Pop_Rhino.Balance.PawnBalance_Sage_RhinoBadass{},DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'".format(borok))

# Make Bulstoss also drop from the Badass loot pool
hfs.add_hotfix('bulstoss_badass', 'SparkLevelPatchEntry-BulstossBadass1',
    ",GD_Sage_SM_AcquiredTasteData.Creature.PawnBalance_Sage_AcquiredTaste_Creature,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Thermitage always drop its rare skin
hfs.add_hotfix('hammerlock_thermitage', 'SparkLevelPatchEntry-ThermitageDropSkin0',
    ',GD_Sage_Ep3_Data.Creature.PawnBalance_Sage_Ep3_Creature,DefaultItemPoolList[0].PoolProbability,,(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Make Dribbles always drop its rare skin
hfs.add_hotfix('hammerlock_dribbles', 'SparkLevelPatchEntry-DribblesDropSkin0',
    'Sage_PowerStation_P,GD_Sage_SM_FollowGlowData.Creature.PawnBalance_Sage_FollowGlow_Creature,DefaultItemPoolList[0].PoolProbability,,(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Make Woundspike always drop its rare skin
hfs.add_hotfix('hammerlock_woundspike', 'SparkLevelPatchEntry-WoundspikeDropSkin0',
    'Sage_PowerStation_P,GD_Sage_Ep4_Data.Creature.PawnBalance_Sage_Ep4_Creature,DefaultItemPoolList[1].PoolProbability,,(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Make Bloodtail always drop its rare skin
hfs.add_hotfix('hammerlock_bloodtail', 'SparkLevelPatchEntry-BloodtailDropSkin0',
    'Sage_Cliffs_P,GD_Sage_SM_NowYouSeeItData.Creature.PawnBalance_Sage_NowYouSeeIt_Creature,DefaultItemPoolList[1].PoolProbability,,(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Voracidous drop pool seraph crystal fix
for idx in range(3):
    hfs.add_hotfix('vorac_seraph_{}'.format(idx),
        'SparkLevelPatchEntry-VoracSeraph{}'.format(idx),
        "Sage_Cliffs_P,GD_Sage_ItemPools.Raid.PoolList_Sage_Raid_Items,ItemPools[{}].ItemPool,,ItemPoolDefinition'GD_Sage_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7_Drop'".format(idx))

# Make Elite Savages always drop something from the main GunsAndGear pool
# (this'll give them a chance to drop twice, actually, but whatever)
hfs.add_hotfix('hammerlock_elite_savage', 'SparkLevelPatchEntry-EliteSavageDrop0',
    "Sage_Cliffs_P,GD_Sage_Pop_Natives.Balance.PawnBalance_Native_Elite,DefaultItemPoolList,,((ItemPool=ItemPoolDefinition'GD_CustomItemPools_Sage.Fanboat.Pool_Customs_Fanboat_All',PoolProbability=(BaseValueConstant=0.000000,BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_VehicleSkins',InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGear',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)))")

# Make "MimicChest_NoMimic" chests from Tiny Tina have slightly better
# loot - they pull from the "regular" chest pool mostly; this will make
# some of their slots pull from the "epic" chest pool instead.
hfs.add_hotfix('nomimic_epic_1', 'SparkLevelPatchEntry-NoMimicEpic1',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[0].ItemAttachments[1].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns'")
hfs.add_hotfix('nomimic_epic_2', 'SparkLevelPatchEntry-NoMimicEpic2',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[0].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols'")
hfs.add_hotfix('nomimic_epic_3', 'SparkLevelPatchEntry-NoMimicEpic3',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[1].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols'")
hfs.add_hotfix('nomimic_epic_4', 'SparkLevelPatchEntry-NoMimicEpic4',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[1].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols'")
hfs.add_hotfix('nomimic_epic_5', 'SparkLevelPatchEntry-NoMimicEpic5',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[3].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items'")
hfs.add_hotfix('nomimic_epic_6', 'SparkLevelPatchEntry-NoMimicEpic6',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[3].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items'")
hfs.add_hotfix('nomimic_epic_7', 'SparkLevelPatchEntry-NoMimicEpic7',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[4].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Shields'")
hfs.add_hotfix('nomimic_epic_8', 'SparkLevelPatchEntry-NoMimicEpic8',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[4].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Shields'")
hfs.add_hotfix('nomimic_epic_9', 'SparkLevelPatchEntry-NoMimicEpic9',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[5].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods'")
hfs.add_hotfix('nomimic_epic_10', 'SparkLevelPatchEntry-NoMimicEpic10',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[5].ItemAttachments[3].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods'")
hfs.add_hotfix('nomimic_epic_11', 'SparkLevelPatchEntry-NoMimicEpic11',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[7].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns'")
hfs.add_hotfix('nomimic_epic_12', 'SparkLevelPatchEntry-NoMimicEpic12',
    ",GD_Aster_Lootables.Balance.ObjectGrade_MimicChest_NoMimic,DefaultLoot[8].ItemAttachments[2].ItemPool,,ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Artifacts'")

# Make Arguk the Butcher (from 'Critical Fail') drop from the Badass loot pool
hfs.add_hotfix('dragonkeep_arguk_drop', 'SparkLevelPatchEntry-ArgukDrop0',
    "Dark_Forest_P,GD_Aster_Pop_Orcs.Balance.PawnBalance_Orc_Butcher,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Skeleton Giants drop from the Badass loot pool (not that Dragon Keep
# needs more loot being dropped, really, but whatever)
hfs.add_hotfix('dragonkeep_giant_skeleton', 'SparkLevelPatchEntry-GiantSkeletonDrop0',
    ",GD_Aster_Pop_Skeletons.Balance.PawnBalance_SkeletonGiant,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Gold Golem always drop one of its "special" legendary drops (effectively
# commenting out the first BalancedItem which would drop from a more general pool)
hfs.add_hotfix('dragonkeep_goldgolem_drop_pool', 'SparkLevelPatchEntry-GoldGolemDropPool0',
    'Mines_P,GD_GolemGold.LootPools.Pool_GoldGolemRunnable,BalancedItems[0].Probability,,(BaseValueConstant=0.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.0)')

# ...aaaand set the Gold Golem drop pool quantity to 3, to at least possibly drop
# one of each of those items (for nearly every other boss requiring this, we can
# just do it via 'set', but Gold Golem must be hotfixed.
hfs.add_hotfix('dragonkeep_goldgolem_drop_qty', 'SparkLevelPatchEntry-GoldGolemDropQty0',
    'Mines_P,GD_GolemGold.LootPools.Pool_GoldGolemRunnable,Quantity,,(BaseValueConstant=3.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Add more Eridium to Handsome Dragon's lootsplosion over the bridge
hfs.add_hotfix('dragonkeep_handsomedragon_drop1', 'SparkLevelPatchEntry-HandsomeDragonEridium1',
    "CastleExterior_P,GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_21,ItemPoolList[16].ItemPool,,ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick'")
hfs.add_hotfix('dragonkeep_handsomedragon_drop2', 'SparkLevelPatchEntry-HandsomeDragonEridium2',
    "CastleExterior_P,GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_21,ItemPoolList[17].ItemPool,,ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick'")
hfs.add_hotfix('dragonkeep_handsomedragon_drop3', 'SparkLevelPatchEntry-HandsomeDragonEridium3',
    "CastleExterior_P,GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_21,ItemPoolList[18].ItemPool,,ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick'")

# Make Badass Knights drop from the badass pool pool
hfs.add_hotfix('dragonkeep_badass_knights', 'SparkLevelPatchEntry-BadassKnightsDrop0',
    ",GD_Aster_Pop_Knights.Balance.PawnBalance_Knight_Badass,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Badass Fire Archers drop from the badass pool pool
hfs.add_hotfix('dragonkeep_badass_fire_archers', 'SparkLevelPatchEntry-BadassFireArchersDrop0',
    ",GD_Aster_Pop_Knights.Balance.PawnBalance_Knight_BadassFireArcher,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Make Sorcerer's Daughter drop 4 items from her legendary pool (which is 4 long)
hfs.add_hotfix('dragonkeep_sorcerersdaughter_drop_pool', 'SparkLevelPatchEntry-SorcerersDaughterDropPool0',
    'Dungeon_P,GD_AngelBoss.LootPools.Pool_AngelBossRunnable,Quantity.BaseValueConstant,,4.0')

# Normalize the probabilities for the Sorcerer's Daughter legendary pool
for num in range(4):
    hfs.add_hotfix('dragonkeep_sorcerersdaughter_normalize_{}'.format(num),
        'SparkLevelPatchEntry-SorcerersDaughterNormalize{}'.format(num),
        'Dungeon_P,GD_AngelBoss.LootPools.Pool_AngelBossRunnable,BalancedItems[{}].Probability.BaseValueScaleConstant,,1.0'.format(num))

# Add more Eridium to Butt Stallion's victory trot after defeating the Handsome Sorcerr
hfs.add_hotfix('dragonkeep_buttstallion_drop1', 'SparkLevelPatchEntry-ButtStallionEridium1',
    "CastleKeep_P,GD_ButtStallion_Proto.Character.AIDef_ButtStallion_Proto:AIBehaviorProviderDefinition_1:Behavior_SpawnItems_44,ItemPoolList,,((ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)))")

# Make the individual Jack battles at the end of Dragon Keep drop from a badass pool
for suffix in ['', '_Demon', '_DemonFall', '_Phase2']:
    hfs.add_hotfix('dragonkeep_jack{}_drop1'.format(suffix),
        'SparkLevelPatchEntry-DragonKeepJack{}Drop1'.format(suffix),
        "CastleKeep_P,GD_Aster_Pop_Wizards.Balance.PawnBalance_JackWarlock{},DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear'".format(suffix))

# Ancient Dragons should always give you 28 Seraph Crystals (total - the pool gets called twice)
hfs.add_hotfix('dragonkeep_ancient_crystals0', 'SparkLevelPatchEntry-DragonKeepAncientCrystals0',
    "DungeonRaid_P,GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystals,BalancedItems,,((ItmPoolDefinition=ItemPoolDefinition'GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystal_7',InvBalanceDefinition=None,Probability=(BaseValueConstant=1.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0),bDropOnDeath=true))")
hfs.add_hotfix('dragonkeep_ancient_crystals1', 'SparkLevelPatchEntry-DragonKeepAncientCrystals1',
    'DungeonRaid_P,GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystals,Quantity,,(BaseValueConstant=2.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Always drop crystals regardless of playthrough
hfs.add_hotfix('dragonkeep_ancient_crystals2', 'SparkLevelPatchEntry-DragonKeepAncientCrystals2',
    'DungeonRaid_P,GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystals,MinGameStageRequirement,,None')

# Drop three items from the Ancient Dragons' Uniques pool
hfs.add_hotfix('dragonkeep_ancient_uniques0', 'SparkLevelPatchEntry-DragonKeepAncientUniques0',
    'DungeonRaid_P,GD_Aster_ItemPools.Raid.Pool_Aster_Raid1_Uniques,Quantity,,(BaseValueConstant=3.0,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.0)')

# Tweak our two drop pools (they each get spawned twice, FYI)
hfs.add_hotfix('dragonkeep_ancient_drop1', 'SparkLevelPatchEntry-DragonKeepAncientDrop1',
    "DungeonRaid_P,GD_Aster_ItemPools.Raid.PoolList_Aster_Raid1A_Items,ItemPools,,((ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)))")

hfs.add_hotfix('dragonkeep_ancient_drop2', 'SparkLevelPatchEntry-DragonKeepAncientDrop2',
    "DungeonRaid_P,GD_Aster_ItemPools.Raid.PoolList_Aster_Raid1B_Items,ItemPools,,((ItemPool=ItemPoolDefinition'GD_Aster_ItemPools.Raid.Pool_Aster_SeraphCrystals',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=0.400000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)),(ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG',PoolProbability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000)))")

# Make Undead Badass Psychos (Bloody Harvest) drop from the Badass loot pool
hfs.add_hotfix('harvest_ubps', 'SparkLevelPatchEntry-UndeadBadassPsychoDrop0',
    "Pumpkin_Patch_P,GD_Pop_HallowSkeleton.Balance.PawnBalance_BadassUndeadPsycho,DefaultItemPoolIncludedLists[0],,ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'")

# Three tributes from the Wattle Gobbler Headhunter pack don't actually drop
# anything, whereas the others drop from the badass pool.  Fix that.
for (name, classname) in [
        ('cynder', 'GD_IncineratorFemale.Balance.PawnBalance_IncineratorFemale'),
        ('strip', 'GD_FleshripperFemale.Balance.PawnBalance_FleshripperFemale'),
        ('flay', 'GD_FleshripperMale.Balance.PawnBalance_FleshripperMale'),
        ]:
    hfs.add_hotfix('wattle_tribute_{}'.format(name),
        'SparkLevelPatchEntry-WattleTribute{}Drop0'.format(name),
        "Hunger_P,{},DefaultItemPoolIncludedLists,,(ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear')".format(classname))

###
### Testing hotfixes, not really intended to be used for real.  These
### aren't referenced in the body of the mod, so they'll only activate
### on the standalone version.
###

# This one causes nearly every enemy to be a badass.
#hfs.add_hotfix('badasses', 'SparkLevelPatchEntry-Badass1',
#    ",GD_Balance.WeightingPlayerCount.Enemy_MajorUpgrade_PerPlayer,ConditionalInitialization,,(bEnabled=True,ConditionalExpressionList=((BaseValueIfTrue=(BaseValueConstant=500.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=20.000000),Expressions=((AttributeOperand1=AttributeDefinition'D_Attributes.GameProperties.NumberOfPlayers',ComparisonOperator=OPERATOR_LessThanOrEqual,Operand2Usage=OPERAND_PreferAttribute,AttributeOperand2=None,ConstantOperand2=4.000000)))),DefaultBaseValue=(BaseValueConstant=0.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000))")

# This makes nearly every SpiderAnt be Chubby -- similar techniques
# could be used to change enemy type rates in general
#hfs.add_hotfix('chubbies', 'SparkLevelPatchEntry-ChubbySpawn1',
#    ',GD_Population_SpiderAnt.Population.PopDef_SpiderantMix_Regular,ActorArchetypeList[9].Probability.BaseValueConstant,,1000')

# This will cause varkids to always morph into their next stage, up
# through Vermivorous (even in Normal mode).  Used to test Verm drops.
# Still have to wait for their timers to elapse before they evolve, of course.
#for morph in range(1,6):
#    hfs.add_hotfix('varkid_clear_{}'.format(morph),
#        'SparkLevelPatchEntry-VarkidMorphClear{}'.format(morph),
#        ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase{},ConditionalInitialization.ConditionalExpressionList,,()'.format(morph))
#    hfs.add_hotfix('varkid_default_{}'.format(morph),
#        'SparkLevelPatchEntry-VarkidMorphDefault{}'.format(morph),
#        ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase{},ConditionalInitialization.DefaultBaseValue.BaseValueConstant,,1.0'.format(morph))

# Just testing to see if I've got the right place to modify Handsome Dragon loot drops
#for num in [17, 18, 19, 20, 21, 26, 27, 28, 29, 30, 31, 32, 53]:
#    hfs.add_hotfix('hd_loot_reg_{}'.format(num),
#        'SparkLevelPatchEntry-HandsomeLootRegular{}'.format(num),
#        ",GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_{},ItemPoolList,,((ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1or2',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=none,InitializationDefinition=none,BaseValueScaleConstant=1.0)))".format(num))
#for num in [26, 53]:
#    hfs.add_hotfix('hd_loot_link_{}'.format(num),
#        'SparkLevelPatchEntry-HandsomeLootLink{}'.format(num),
#        ',GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_{},ItemPoolIncludedLists,,()'.format(num))
#for (num, pool) in [
#        (17, 'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_01_Common'),
#        (18, 'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_02_Uncommon'),
#        (19, 'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare'),
#        (20, 'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare'),
#        (21, 'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare_Alien'),
#        (26, 'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_01_Common'),
#        (27, 'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_02_Uncommon'),
#        (28, 'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare'),
#        (29, 'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare'),
#        (30, 'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare_Alien'),
#        (31, 'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common'),
#        (32, 'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_02_Uncommon'),
#        (53, 'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare'),
#        ]:
#    hfs.add_hotfix('hd_loot_reg_{}'.format(num),
#        'SparkLevelPatchEntry-HandsomeLootRegular{}'.format(num),
#        ",GD_DragonBridgeBoss.InteractiveObjects.IO_DragonBridgeBoss_LootExplosion:BehaviorProviderDefinition_0.Behavior_SpawnItems_{num},ItemPoolList,,((ItemPool=ItemPoolDefinition'{pool}',PoolProbability=(BaseValueConstant=1.0,BaseValueAttribute=none,InitializationDefinition=none,BaseValueScaleConstant=1.0)))".format(num=num, pool=pool))

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

# Now start constructing the actual gigantic mod string.
loot_str = """
#<{mod_name} ({variant_name})>

    # All sorts of tweaks to loot in general, with the aim of basically making all
    # the loot drops in the game "better".  Greatly increased chances of blues/purples/etech/legendary
    # across the board, slightly more Eridium, etc.  Also basically all game items will be
    # available as regular drops, including legendaries, uniques, pearls, and seraph items.

{hotfix_gearbox_base}

    #<Better Treasure Chests>

        # Makes regular treasure chests better: will only drop blue and higher,
        # and adds a decent chance to include a legendary.

        set GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_LongGuns BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_Pistols BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Artifacts BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_03_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_04_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_05_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_ClassMods BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_GrenadeMods BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Items BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Shields BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Weapons_Launchers BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={treasure_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

    #</Better Treasure Chests>

    #<Better Epic Chests>

        # Makes "epic" chests better: Only Purple and higher, and extremely high chance for
        # a legendary.

        set GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Artifacts BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_04_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_05_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_EpicChest_ClassMods BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Shields BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Launchers BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_Launchers_07_LegendaryPlusPearl',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary_dbl}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_07_LegendaryPlusPearl',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary_dbl}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_Shotguns_07_LegendaryPlusPearl',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary_dbl}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_SMG_07_LegendaryPlusPearl',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary_dbl}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_SniperRifles_07_LegendaryPlusPearl',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary_dbl}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_Pistols_07_LegendaryPlusPearl',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        #<Captain Scarlett DLC Endgame Chests>

            # Convert the Captain Scarlett endgame chests into our custom
            # "epic" chest types.

            set GD_Orchid_ItemPools.EndGame.Pool_PirateChest_EndGame_ClassMods BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_ClassMods',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Orchid_ItemPools.EndGame.Pool_PirateChest_EndGame_GrenadeMods BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Orchid_ItemPools.EndGame.Pool_PirateChest_EndGame_Launchers BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Launchers',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Orchid_ItemPools.EndGame.Pool_PirateChest_EndGame_LongGuns BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Orchid_ItemPools.EndGame.Pool_PirateChest_EndGame_Pistols BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Orchid_ItemPools.EndGame.Pool_PirateChest_EndGame_Shields BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Shields',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

        #</Captain Scarlett DLC Endgame Chests>

        #<Hammerlock DLC Endgame Chests>

            # Convert the Hammerlock DLC's endgame chests into our custom
            # "epic" chest types.

            set GD_Sage_ItemPools.EndGame.Pool_HyperionChest_EndGame_ClassMods BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_ClassMods',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Sage_ItemPools.EndGame.Pool_HyperionChest_EndGame_GrenadeMods BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Sage_ItemPools.EndGame.Pool_HyperionChest_EndGame_Launchers BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Launchers',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Sage_ItemPools.EndGame.Pool_HyperionChest_EndGame_LongGuns BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Sage_ItemPools.EndGame.Pool_HyperionChest_EndGame_Pistols BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_Pistols',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Sage_ItemPools.EndGame.Pool_HyperionChest_EndGame_Shields BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Shields',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000,
                    ),
                    bDropOnDeath=True
                )
            )

        #</Hammerlock DLC Endgame Chests>

    #</Better Epic Chests>

    #<Tiny Tina DLC Chest Changes>

        #<Tweaked Dice Chests>

            # Adds a chance to drop legendary on a very good roll, and normalizes the
            # odds when it chooses between purples and e-tech.  Also incidentally fixes
            # an error in the "Longs" pool which wasn't properly pulling in E-Tech ARs.
            # The actual probabilities for what pools get dropped for which rolls remains
            # unchanged (and not just because that data is daunting to parse)

            set GD_Aster_ItemPools.DiceChestPools.Pool_DiceChest_4_VeryHighRoll_Launchers BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Aster_ItemPools.DiceChestPools.Pool_DiceChest_4_VeryHighRoll_Longs BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_legendary}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_legendary}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_legendary}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Aster_ItemPools.DiceChestPools.Pool_DiceChest_4_VeryHighRoll_Pistols BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={dice_vhigh_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

        #</Tweaked Dice Chests>

        #<Improved Non-Mimic Chests>

            # The chests which could be mimics but aren't already have good loot
            # when combined with the rest of this mod, but this will improve them
            # a bit more.  Half the gear in the chest (rounded down) will take from
            # the "Epic" chest pool, rather than the normal chest pool.

            {hotfixes:nomimic_epic_1}

            {hotfixes:nomimic_epic_2}

            {hotfixes:nomimic_epic_3}

            {hotfixes:nomimic_epic_4}

            {hotfixes:nomimic_epic_5}

            {hotfixes:nomimic_epic_6}

            {hotfixes:nomimic_epic_7}

            {hotfixes:nomimic_epic_8}

            {hotfixes:nomimic_epic_9}

            {hotfixes:nomimic_epic_10}

            {hotfixes:nomimic_epic_11}

            {hotfixes:nomimic_epic_12}

        #</Improved Non-Mimic Chests>

    #</Tiny Tina DLC Chest Changes>

    #<Better Lockers>

        # Makes locker drops a bit different - will drop Blue-rarity loot, though if
        # GD_Itempools.GeneralItemPools.Pool_Gear gets chosen by the engine, it'll end
        # up dropping from a more "usual" loot pool.  
        #
        # This may not technically count as "better" since lockers previously had
        # a chance to drop all the way up to Legendary, but with our other loot
        # changes, getting something special from a lockers wouldn't be special anyway.

        set GD_Itempools.LootablePools.Pool_Locker_Items BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                    InitializationDefinition=None,
                    BaseValueScaleConstant=50.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_0_VeryCommon',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=False
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_Gear',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.LootablePools.Pool_Locker_Items_SMGsAndPistols BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=False
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_3_Uncommoner',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

    #</Better Lockers>

    #<Better Badass Pool Definitions>

        # Improves the drop types of badass enemies, including a few like Bad Maw
        # who are internally classified as a special kind of "badass."  Note that
        # internally the game uses "SuperBadass" and "UltimateBadass" to describe
        # some of these special enemies, though that does NOT correspond to the
        # enemies which actually show up as "Super Badass" or "Ultimate Badass"
        # in the game.

        #<Badass Enemies>

            set GD_Itempools.ListDefs.BadassEnemyGunsAndGear ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.100000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.VehicleSkins.Pool_VehicleSkins_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_VehicleSkins',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=KeyedItemPoolDefinition'GD_CustomItemPools_MainGame.Rewards.Head10',
                    PoolProbability=(
                        BaseValueConstant=0.005000,
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
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_EridiumBar',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=10.000000
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
                        BaseValueScaleConstant=0.500000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
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
                        BaseValueScaleConstant=0.500000
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
            )

            set GD_Itempools.ListDefs.BadassEnemyWeightedShotgun ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.100000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.VehicleSkins.Pool_VehicleSkins_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_VehicleSkins',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=KeyedItemPoolDefinition'GD_CustomItemPools_MainGame.Rewards.Head10',
                    PoolProbability=(
                        BaseValueConstant=0.005000,
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
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_EridiumBar',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=10.000000
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
                        BaseValueScaleConstant=0.500000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
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
                        BaseValueScaleConstant=0.500000
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
            )

        #</Badass Enemies>

        #<Super Badass Enemies>

            # This is actually enemies like Bad Maw, Badass Constructors...

            set GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
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
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
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
            )

        #</Super Badass Enemies>

        #<Ultimate Badass Enemies>

            # This is actually enemies like Saturn, Slappy, King Mong, etc.

            set GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear ItemPools
            (
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.500000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.500000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.500000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.250000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.500000
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.500000
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.VehicleSkins.Pool_VehicleSkins_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_VehicleSkins',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=10.000000
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
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_EridiumBar',
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
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_EridiumStick',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=100.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_EridiumStick',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=100.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
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
            )

        #</Ultimate Badass Enemies>

        #<Chubby Enemies>

            # Unfortunately, this has to be done via Hotfix.  GD_Itempools.ListDefs.ChubbyEnemyGunsAndGear
            # is defined in the base files, and can be altered via "set", but Lobelia uses some kind of
            # hotfix of its own to alter the pool when levels get loaded, which will overwrite various
            # values in there.  So, we have to put it in as a hotfix at the end, instead.

            {hotfixes:chubby_drop}

        #</Chubby Enemies>

        #<Badass Enemy Fixes>

            # Various "Badass" enemies in some DLCs were presumably accidentally set to
            # pull from the standard enemy drop pool, rather than badass.  This section
            # fixes those up.

            #<Badass Boroks>

                {hotfixes:badass_borok_Corrosive}

                {hotfixes:badass_borok_Fire}

                {hotfixes:badass_borok_Shock}

                {hotfixes:badass_borok_Slag}

            #</Badass Boroks>

            #<Badass Knights>

                {hotfixes:dragonkeep_badass_knights}

            #</Badass Knights>

            #<Badass Fire Archers>

                {hotfixes:dragonkeep_badass_fire_archers}

            #</Badass Fire Archers>

            #<Undead Badass Psychos>

                {hotfixes:harvest_ubps}

            #</Undead Badass Psychos>

        #</Badass Enemy Fixes>

    #</Better Badass Pool Definitions>

    #<Better Miscellaneous Boss Drops>

        # These options improve the drops for a few specific bosses

        #<RaidBossEnemyGunsAndGear Improvements>

            # This is a tweak to the pool named "RaidBossEnemyGunsAndGear," though it doesn't
            # usually apply to Raid bosses, and is rather weirdly distributed.  As far as I
            # can tell, these are the only bosses in the game which take from this pool:
            # Son of Crawmerax, One (or more?) of the threshers from the Wedding Day Massacre
            # Headhunter Pack, Vermivorous, Handsome Dragon, The Warrior, and BNK3R.  Anyway,
            # it's a bit anemic and at least one of those relies on this as its primary pool,
            # so we're buffing it up a bit.

            set GD_Itempools.ListDefs.RaidBossEnemyGunsAndGear ItemPools
            (
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne',
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
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
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
            )

        #</RaidBossEnemyGunsAndGear Improvements>

        #<Handsome Dragon Improvements>

            # Handsome Dragon actually gets its main benefit from the above
            # pool tweak, but for the hell of it I'm also adding more Eridium
            # sticks to the bridgewide lootsplosion.  Why not.

            {hotfixes:dragonkeep_handsomedragon_drop1}

            {hotfixes:dragonkeep_handsomedragon_drop2}

            {hotfixes:dragonkeep_handsomedragon_drop3}

        #</Handsome Dragon Improvements>

        #<Butt Stallion Endgame Improvements>

            # Mostly just adding some more Eridium to Butt Stallion's endgame
            # drop, after defeating the Handsome Sorcerer.  I feel as though I'm
            # probably going overboard at this point.

            {hotfixes:dragonkeep_buttstallion_drop1}

        #</Butt Stallion Endgame Improvements>

    #</Better Miscellaneous Boss Drops>

    #<Regular Enemey Drop Improvements>

        # There are a handful of enemy types which are somewhere between regular
        # enemies and Badasses, whose drop pools I felt could use a slight buff.
        # Also a few enemies who claim to be Badasses but who didn't actually
        # drop from the badass pool originally.

        #<Witch Doctors>

            # Adds a guaranteed Eridium stick, and chance at a good Relic

            {hotfixes:witchdoctor_Fire}

            {hotfixes:witchdoctor_Shock}

            {hotfixes:witchdoctor_Slag}

            {hotfixes:witchdoctor_Slow}

            {hotfixes:witchdoctor_Vampire}

        #</Witch Doctors>

        #<Bulstoss>

            # Makes Bulstoss pull from the badass loot pool, rather than standard

            {hotfixes:bulstoss_badass}

        #</Bulstoss>

        #<Elite Savages>

            # Force Elite Savages to always drop from the main GunsAndGear loot pool

            {hotfixes:hammerlock_elite_savage}

        #</Elite Savages>

        #<Arguk the Butcher>

            # Make Arguk the Butcher drop from the badass pool

            {hotfixes:dragonkeep_arguk_drop}

        #</Arguk the Butcher>

        #<Giant Skeletons>

            # Make Giant Skeletons drop from the badass pool

            {hotfixes:dragonkeep_giant_skeleton}

        #</Giant Skeletons>

        #<Handsome Sorcerer Stages>

            # The individual Handsome Sorcerer stages don't actually drop anything
            # special.  Let's make 'em do so!

            {hotfixes:dragonkeep_jack_drop1}

            {hotfixes:dragonkeep_jack_Demon_drop1}

            {hotfixes:dragonkeep_jack_DemonFall_drop1}

            {hotfixes:dragonkeep_jack_Phase2_drop1}

        #</Handsome Sorcerer Stages>

        #<Wattle Gobbler Tributes>

            # Three tributes from the Wattle Gobler Headhunter Pack don't have
            # any drops defined, but the rest drop from the badass pool.  Fix that.

            {hotfixes:wattle_tribute_cynder}

            {hotfixes:wattle_tribute_strip}

            {hotfixes:wattle_tribute_flay}

        #</Wattle Gobbler Tributes>

    #</Regular Enemey Drop Improvements>

    #<Better Relic Drops>

        # Allow all legendary/unique/seraph relics to spawn from the main loot pool.

        # Note that there are two identical "rare" relic pools defined in the game:
        #   GD_Itempools.ArtifactPools.Pool_ArtifactsReward
        #   GD_Itempools.ArtifactPools.Pool_Artifacts_05_Legendary
        # Both appear to be identical apart from their names and IDs.  So to be
        # safe we're going to add to both.

        # First up, add rare relics to the global loot drop

        set GD_Itempools.GeneralItemPools.Pool_GunsAndGear BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=0.450000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_All',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=3.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_All',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=2.200000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_ArtifactsAll',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=0.200000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_ArtifactsReward',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_2_Uncommon',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=KeyedItemPoolDefinition'GD_CustomItemPools_MainGame.Rewards.DahlUncommon',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_6_Legendary',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=KeyedItemPoolDefinition'GD_CustomItemPools_MainGame.Rewards.GreenNinja',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_6_Legendary',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=KeyedItemPoolDefinition'GD_CustomItemPools_MainGame.Rewards.CyanBoldAccent',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_6_Legendary',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=KeyedItemPoolDefinition'GD_CustomItemPools_MainGame.Rewards.PinkPale',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_6_Legendary',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_CustomItemPools_Peony.AllCustomizationsItemPool',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_6_Legendary',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_CustomItemPools_CommDay2013.AllCustomizationsItemPool',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_6_Legendary',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        # And now, add all the legendaries/uniques/seraph relics to our two pools

        set GD_Itempools.ArtifactPools.Pool_ArtifactsReward BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Vitality_Rare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=4.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Stockpile_Rare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=4.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Protection_Rare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=4.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Strength_Rare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=4.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Resistance_Rare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=4.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_ElementalReward',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=6.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Tenacity_Rare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=4.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Proficiency_Rare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=4.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_AggressionReward',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=10.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_Artifacts_AllegianceReward',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=10.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item_Unique.A_Afterburner',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Orchid_Artifacts.A_Item_Unique.A_Blade',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item_Unique.A_Endowment',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item_Unique.A_Opportunity',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item_Unique.A_Sheriff',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item_Unique.A_Deputy',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Iris_SeraphItems.Might.Iris_Seraph_Artifact_Might_Balance',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Orchid_Artifacts.A_Item_Unique.A_SeraphBloodRelic',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Sage_Artifacts.A_Item.A_SeraphBreath',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_Artifacts.A_Item_Unique.A_SeraphShadow',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item_Unique.A_Terramorphous',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_Artifacts.A_Item_Unique.A_MysteryAmulet',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=0.500000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityAssault_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=0.500000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityLauncher_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=0.500000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityPistol_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=0.500000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacityShotgun_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=0.500000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacitySMG_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=0.500000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_AggressionTenacitySniper_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=0.500000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_ElementalProficiency_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_ResistanceProtection_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Gladiolus_Artifacts.A_Item.A_VitalityStockpile_VeryRare',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ArtifactPools.Pool_Artifacts_05_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ArtifactPools.Pool_ArtifactsReward',
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

        # Finally, fix Blood of the Seraph spawning.  (The only change here is MinGameStage, from 50 -> 1)

        set GD_Orchid_Artifacts.A_Item_Unique.A_SeraphBloodRelic Manufacturers
        (
            (
                Manufacturer=ManufacturerDefinition'GD_Manufacturers.Artifacts.Artifact_TypeA',
                Grades=(
                    (
                        GradeModifiers=(
                            ExpLevel=0,
                            CustomInventoryDefinition=None
                        ),
                        GameStageRequirement=(
                            MinGameStage=1,
                            MaxGameStage=100
                        ),
                        MinSpawnProbabilityModifier=(
                            BaseValueConstant=1.000000,
                            BaseValueAttribute=None,
                            InitializationDefinition=None,
                            BaseValueScaleConstant=1.000000
                        ),
                        MaxSpawnProbabilityModifier=(
                            BaseValueConstant=1.000000,
                            BaseValueAttribute=None,
                            InitializationDefinition=None,
                            BaseValueScaleConstant=1.000000
                        )
                    )
                )
            )
        )

        # Now tweak the Reward weighting to follow our own numbers

        {relic_weight_str}

    #</Better Relic Drops>

    #<Better Weapon Rarity Drops>

        # Make the general weapon drops skew rare

        set GD_Itempools.WeaponPools.Pool_Weapons_All BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_01_Common',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={weapon_base_common},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={weapon_scale_common}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_02_Uncommon',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={weapon_base_uncommon},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={weapon_scale_uncommon}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={weapon_base_rare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={weapon_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={weapon_base_veryrare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={weapon_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={weapon_base_alien},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={weapon_scale_alien}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={weapon_base_legendary},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={weapon_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        #<Better Torgue Biker Gang Rarity Drops>

            # The three biker gangs in Iris have custom pools for their weapon drops.  Note that
            # these gangs will NOT drop from our own custom Legendary pool, but I figure that's
            # okay given that it's just one DLC.

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Pistols BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Pistols_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Pistols_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Pistols_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Pistols_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Pistols_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Pistols_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Shotguns BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Shotguns_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Shotguns_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Shotguns_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Shotguns_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Shotguns_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_Shotguns_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SMG BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SMG_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SMG_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SMG_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SMG_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SMG_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SMG_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SniperRifles BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SniperRifles_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SniperRifles_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SniperRifles_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SniperRifles_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SniperRifles_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_AngelGang_SniperRifles_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Iris_Weapons.SniperRifles.Sniper_Jakobs_3_Cobra',
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_iris_cobra}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_Pistols BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_Pistols_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_Pistols_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_Pistols_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_Pistols_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_Pistols_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_Pistols_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SMG BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SMG_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SMG_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SMG_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SMG_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SMG_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SMG_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SniperRifles BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SniperRifles_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SniperRifles_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SniperRifles_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SniperRifles_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SniperRifles_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_DragonGang_SniperRifles_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Iris_Weapons.SniperRifles.Sniper_Jakobs_3_Cobra',
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_iris_cobra}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_AR BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_AR_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_AR_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_AR_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_AR_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_AR_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_AR_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Pistols BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Pistols_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Pistols_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Pistols_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Pistols_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Pistols_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Pistols_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Shotguns BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Shotguns_01_Common',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_common},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_common}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Shotguns_02_Uncommon',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_uncommon},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_uncommon}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Shotguns_04_Rare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_rare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_rare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Shotguns_05_VeryRare',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_veryrare},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_veryrare}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Shotguns_05_VeryRare_Alien',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_alien},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_alien}
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Iris_ItemPools.WeaponPools.Pool_Weapons_TorgueGang_Shotguns_06_Legendary',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant={weapon_base_legendary},
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                        BaseValueScaleConstant={weapon_scale_legendary}
                    ),
                    bDropOnDeath=True
                )
            )

        #</Better Torgue Biker Gang Rarity Drops>

        #<Equalize Tiny Tina DLC Gemstone Distribution>

            # The default Gemstone pool in the Tiny Tina DLC vastly weights pistols
            # over the others.  This sets them all equal.  (I'd noticed this thanks
            # to Orudeon's "Gemstone Loot Pools")

            set GD_Aster_ItemPools.WeaponPools.Pool_Weapons_04_Gemstone BalancedItems
            (
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Pistols_04_Gemstone',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Shotguns_04_Gemstone',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_SMGs_04_Gemstone',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_ARs_04_Gemstone',
                    InvBalanceDefinition=None,
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=ItemPoolDefinition'GD_Aster_ItemPools.WeaponPools.Pool_Weapons_Snipers_04_Gemstone',
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

        #</Equalize Tiny Tina DLC Gemstone Distribution>

    #</Better Weapon Rarity Drops>

    #<Better Class Mod Rarity Drops>

        # Make the general class mod drops skew rare, include all legendary
        # class mods in the legendary pool, and add Dragon Keep Alignment
        # mods in the global COM pool.

        set GD_Itempools.ClassModPools.Pool_ClassMod_All BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_01_Common',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={cm_base_common},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={cm_scale_common}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_02_Uncommon',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={cm_base_uncommon},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={cm_scale_uncommon}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={cm_base_rare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={cm_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={cm_base_veryrare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={cm_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Aster_ItemPools.ClassModPools.Pool_ClassMod_00_Aster',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={cm_base_veryrare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={cm_scale_alignment}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={cm_base_legendary},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={cm_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ClassModPools.Pool_ClassMod_Assassin_05_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_06_SlayerOfTerramorphous',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Assassin_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=3.000000
                ),
                bDropOnDeath=True
            ),
        )

        set GD_Itempools.ClassModPools.Pool_ClassMod_Merc_05_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_06_SlayerOfTerramorphous',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Merc_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=3.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ClassModPools.Pool_ClassMod_Siren_05_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_06_SlayerOfTerramorphous',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Siren_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=3.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ClassModPools.Pool_ClassMod_Soldier_05_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_06_SlayerOfTerramorphous',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Soldier_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=3.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Tulip_Itempools.ClassModPools.Pool_ClassMod_Mechromancer_05_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_06_SlayerOfTerramorphous',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Mechromancer_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=3.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Lilac_Itempools.ClassModPools.Pool_ClassMod_LilacPlayerClass_05_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_06_SlayerOfTerramorphous',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=ClassModBalanceDefinition'GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Psycho_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=3.000000
                ),
                bDropOnDeath=True
            )
        )

        #<Force Alignment COMs Blue And Higher>

            # Forces Dragon Keep Alignment COMs to be at least blue rarity.
            # COMs in the base game are nicely separated into rarity groups
            # which manage the Alpha/Beta/Gamma attributes via some fancy
            # property management, but the Dragon Keep ones are all in one
            # gigantic group.  So, we alter the main pools to just exclude
            # the lower-quality parts, like Noskill/AS1/AS2 in Alpha, and
            # the x0/x1 levels in Beta and Gamma.

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_42 AlphaPartData
            (
                bEnabled=True,
                WeightedParts=
                (
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_42 BetaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A2_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A3_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A4_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A5_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_42 GammaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B2_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B3_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B4_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B5_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_43 AlphaPartData
            (
                bEnabled=True,
                WeightedParts=
                (
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_43 BetaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A2_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A3_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A4_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A5_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_43 GammaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B2_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B3_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B4_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B5_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_44 AlphaPartData
            (
                bEnabled=True,
                WeightedParts=
                (
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_44 BetaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A2_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A3_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A4_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A5_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_44 GammaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B2_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B3_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B4_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B5_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_45 AlphaPartData
            (
                bEnabled=True,
                WeightedParts=
                (
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_45 BetaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A2_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A3_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A4_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A5_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_45 GammaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B2_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B3_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B4_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B5_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_46 AlphaPartData
            (
                bEnabled=True,
                WeightedParts=
                (
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_46 BetaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A2_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A3_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A4_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A5_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_46 GammaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B2_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B3_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B4_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B5_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_47 AlphaPartData
            (
                bEnabled=True,
                WeightedParts=
                (
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2',
                        Manufacturers=,
                        MinGameStageIndex=2,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_47 BetaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A2_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A3_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A4_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary.PrimaryStat_A5_B0_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

            set GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_47 GammaPartData
            (
                bEnabled=True,
                WeightedParts=(
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B2_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B3_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B4_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    ),
                    (
                        Part=ClassModPartDefinition'GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B5_C0',
                        Manufacturers=,
                        MinGameStageIndex=0,
                        MaxGameStageIndex=1,
                        DefaultWeightIndex=0
                    )
                )
            )

        #</Force Alignment COMs Blue And Higher>

    #</Better Class Mod Rarity Drops>

    #<Better Grenade Rarity Drops>

        # Make the general grenade drops skew rare

        set GD_Itempools.GrenadeModPools.Pool_GrenadeMods_All BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_01_Common',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={grenade_base_common},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={grenade_scale_common}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_02_Uncommon',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={grenade_base_uncommon},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={grenade_scale_uncommon}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={grenade_base_rare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={grenade_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={grenade_base_veryrare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={grenade_scale_veryrare}
                ),
                bDropOnDeath=True
            ),(
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={grenade_base_legendary},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={grenade_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

    #</Better Grenade Rarity Drops>

    #<Better Shield Rarity Drops>

        # Make the general shield drops skew rare

        set GD_Itempools.ShieldPools.Pool_Shields_All BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_01_Common',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={shield_base_common},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={shield_scale_common}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_02_Uncommon',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={shield_base_uncommon},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={shield_scale_uncommon}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={shield_base_rare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={shield_scale_rare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={shield_base_veryrare},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={shield_scale_veryrare}
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={shield_base_legendary},
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={shield_scale_legendary}
                ),
                bDropOnDeath=True
            )
        )

    #</Better Shield Rarity Drops>

    #<E-Tech Pool Makeover>

        # Put Gemstone weapons into the global E-Tech pools, and reduce the
        # chances of spawning lamer E-Tech weapons (Darts/Spikers, specifically)

        set GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare_Alien BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=2.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=2.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=2.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.AssaultRifles.AR_Dahl_4_Emerald',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.AssaultRifles.AR_Bandit_4_Quartz',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.AssaultRifles.AR_Vladof_4_Garnet',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.AssaultRifles.AR_Jakobs_4_Citrine',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.AssaultRifles.AR_Torgue_4_Rock',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.AssaultRifles.AR_Vladof_4_Garnet',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare_Alien BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons.RL_Bandit_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons.RL_Tediore_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons.RL_Vladof_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons.RL_Maliwan_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare_Alien BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons.Pistol_Bandit_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=0.200000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons.Pistol_Dahl_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=0.200000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons.Pistol_Tediore_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=0.200000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons.Pistol_Vladof_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=0.200000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=0.200000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=0.200000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Pistols.Pistol_Jakobs_4_Citrine',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Pistols.Pistol_Hyperion_4_Diamond',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Pistols.Pistol_Maliwan_4_Aquamarine',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Pistols.Pistol_Vladof_4_Garnet',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Pistols.Pistol_Torgue_4_Rock',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare_Alien BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons.SG_Bandit_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.666666
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons.SG_Tediore_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.666666
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons.SG_Hyperion_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.666666
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Shotguns.SG_Torgue_4_Rock',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Shotguns.SG_Hyperion_4_Diamond',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Shotguns.SG_Jakobs_4_Citrine',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Shotguns.SG_Tediore_4_CubicZerconia',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Shotguns.SG_Bandit_4_Quartz',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare_Alien BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons.SMG_Bandit_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons.SMG_Tediore_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons.SMG_Dahl_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons.SMG_Maliwan_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons.SMG_Hyperion_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.SMGs.SMG_Tediore_4_CubicZerconia',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.SMGs.SMG_Bandit_4_Quartz',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.SMGs.SMG_Hyperion_4_Diamond',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.SMGs.SMG_Dahl_4_Emerald',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare_Alien BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_5_Alien',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Snipers.SR_Jakobs_4_Citrine',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Snipers.SR_Hyperion_4_Diamond',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Snipers.SR_Dahl_4_Emerald',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Snipers.SR_Vladof_4_Garnet',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

    #</E-Tech Pool Makeover>

    #<Pearls and Seraph in Legendary Pool>

        # Puts Pearlescent and Seraph weapons into the Legendary loot pools.

        # First up, Gladiolus specifies its own weapon pools, GD_Gladioulus_Itempools.WeaponPools.Pool_Weapons_*_LegendaryPlusPearl,
        # and we want to make sure that anything looking for legendaries looks in our overridden classes here.  So
        # we're going to point all of its custom objects back to the "main" ones which we'll then override

        set GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_07_LegendaryPlusPearl BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_Launchers_07_LegendaryPlusPearl BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_Pistols_07_LegendaryPlusPearl BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_Shotguns_07_LegendaryPlusPearl BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_SMG_07_LegendaryPlusPearl BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_SniperRifles_07_LegendaryPlusPearl BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        # Now on to setting up the pools.

        set GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Bandit_5_Madhouse',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Dahl_5_Veruc',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBuster',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Torgue_5_KerBlaster',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Vladof_5_Sherdifier',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Iris_Weapons.AssaultRifles.AR_Torgue_3_BoomPuppy',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_Weapons.AssaultRifle.AR_Bandit_3_Chopper',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_Weapons.AssaultRifle.AR_Jakobs_3_DamnedCowboy',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Torgue_3_EvilSmasher',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Vladof_3_Hail',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Iris_Weapons.AssaultRifles.AR_Vladof_3_Kitten',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.AssaultRifle.AR_Vladof_3_Rapier',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Dahl_3_Scorpio',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.AssaultRifle.AR_Jakobs_3_Stinkpot',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.AssaultRifles.AR_Bandit_3_Ogre',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Jakobs_3_Stomper',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Gladiolus_Weapons.AssaultRifle.AR_Dahl_6_Bearcat',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Gladiolus_Weapons.AssaultRifle.AR_Bandit_6_Sawbar',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Lobelia_Weapons.AssaultRifles.AR_Jakobs_6_Bekah',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.AssaultRifle.Seraphim.Orchid_Seraph_Seraphim_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_RaidWeapons.AssaultRifle.Sage_Seraph_LeadStorm_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_RaidWeapons.AssaultRifles.Aster_Seraph_Seeker_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Pyrophobia',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Legendary.RL_Tediore_5_Bunny',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_3_TheHive',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.Launcher.RL_Torgue_3_12Pounder',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Unique.RL_Bandit_3_Roaster',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Gladiolus_Weapons.Launchers.RL_Torgue_6_Tunguska',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.RPG.Ahab.Orchid_Seraph_Ahab_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Gub',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Gunerang',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Hornet',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Vladof_5_Infinity',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Maliwan_5_ThunderballFists',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Judge',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Pistols.Pistol_Maliwan_3_GrogNozzle',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.Pistol.Pistol_Jakobs_ScarletsGreed',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensHead',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Dahlminator',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Iris_Weapons.Pistols.Pistol_Torgue_3_PocketRocket',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_Weapons.Pistols.Pistol_Jakobs_3_Rex',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Law',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.Pistol.Pistol_Maliwan_3_LittleEvie',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Teapot',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Vladof_3_Veritas',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Bandit_3_Tenderbox',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Gladiolus_Weapons.Pistol.Pistol_Jakobs_6_Unforgiven',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Gladiolus_Weapons.Pistol.Pistol_Vladof_6_Stalker',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Lobelia_Weapons.Pistol.Pistol_Maliwan_6_Wanderlust',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.Pistol.Devastator.Orchid_Seraph_Devastator_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_RaidWeapons.Pistol.Sage_Seraph_Infection_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_RaidWeapons.Pistols.Aster_Seraph_Stinger_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Tediore_5_Deliverance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Hydra',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.Shotgun.SG_Bandit_3_JollyRoger',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_HeartBreaker',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Dog',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Blockhead',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.Shotgun.SG_Jakobs_3_OrphanMaker',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Landscaper',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Iris_Weapons.Shotguns.SG_Hyperion_3_SlowHand',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_Shotgun1340',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_RokSalt',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_TidalWave',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Teeth',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.Shotguns.SG_Torgue_3_SwordSplosion',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Twister',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Triquetra',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Gladiolus_Weapons.Shotgun.SG_Hyperion_6_Butcher',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Lobelia_Weapons.Shotguns.SG_Torgue_6_Carnage',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.Shotgun.Spitter.Orchid_Seraph_Spitter_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_RaidWeapons.Shotgun.Sage_Seraph_Interfacer_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_RaidWeapons.Shotguns.Aster_Seraph_Omen_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Legendary.SMG_Bandit_5_Slagga',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_BabyMaker',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Emperor',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_BoneShredder',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Bane',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Commerce',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Chulainn',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Lascaux',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_Weapons.SMG.SMG_Hyperion_3_YellowJacket',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_Weapons.SMGs.SMG_Bandit_3_Orc',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Gladiolus_Weapons.SMG.SMG_Tediore_6_Avenger',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.SMG.Tattler.Orchid_Seraph_Tattler_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.SMG.Actualizer.Orchid_Seraph_Actualizer_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Aster_RaidWeapons.SMGs.Aster_Seraph_Florentine_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Lyudmila',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Volcano',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_Weapons.SniperRifles.Sniper_Jakobs_3_ElephantGun',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Buffalo',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Iris_Weapons.SniperRifles.Sniper_Jakobs_3_Cobra',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_BossWeapons.SniperRifles.Sniper_Maliwan_3_Pimpernel',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Morningstar',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_Sloth',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Tresspasser',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Longbow',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Gladiolus_Weapons.sniper.Sniper_Maliwan_6_Storm',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Lobelia_Weapons.sniper.Sniper_Jakobs_6_Godfinger',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.sniper.Patriot.Orchid_Seraph_Patriot_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Sage_RaidWeapons.sniper.Sage_Seraph_HawkEye_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_BonusPackage',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_BouncingBonny',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_Fastball',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_FireBee',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_Leech',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_Pandemic',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_Quasar',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_RollingThunder',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_StormFront',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_NastySurprise',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Custom.GM_KissOfDeath',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_FlameSpurt',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_GrenadeMods.A_Item.GM_Fireball',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Custom.GM_FusterCluck',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_GrenadeMods.A_Item.GM_LightningBolt',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_GrenadeMods.A_Item.GM_MagicMissileRare',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_GrenadeMods.A_Item.GM_ChainLightning',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_GrenadeMods.A_Item.GM_FireStorm',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Iris_SeraphItems.MeteorShower.Iris_Seraph_GrenadeMod_MeteorShower_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Iris_SeraphItems.Crossfire.Iris_Seraph_GrenadeMod_Crossfire_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Iris_SeraphItems.ONegative.Iris_Seraph_GrenadeMod_ONegative_Balance',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_Absorption_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryShock',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryNormal',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_1340',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_Equitas',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Iris_SeraphItems.Sponge.Iris_Seraph_Shield_Sponge_Balance',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_Booster_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_PotOGold',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Iris_SeraphItems.BigBoomBlaster.Iris_Seraph_Shield_Booster_Balance',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_Chimera_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Orchid_RaidWeapons.Shield.Anshin.Orchid_Seraph_Anshin_Shield_Balance',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_Impact_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_Juggernaut_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Iris_SeraphItems.Hoplite.Iris_Seraph_Shield_Juggernaut_Balance',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_NovaShields_All_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Singularity',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_NovaShields_Explosive_06_Legendary',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_NovaShields_Fire_06_Legendary',
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

        set GD_Itempools.ShieldPools.Pool_Shields_NovaShields_Explosive_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_DeadlyBloom',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_NovaShields_Fire_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Phoenix',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_Roid_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_ThresherRaid',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_Order',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_04_LoveThumper',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Iris_SeraphItems.Pun-chee.Iris_Seraph_Shield_Pun-chee_Balance',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        # Note that unlike with Nova shields, the "All" definition here just duplicates in Corrosive.
        set GD_Itempools.ShieldPools.Pool_Shields_SpikeShields_All_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_SpikeShields_Corrosive_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.ShieldPools.Pool_Shields_Standard_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_05_Legendary',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Orchid_Shields.A_Item_Custom.S_BladeShield',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Sage_Shields.A_Item_Custom.S_BucklerShield',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_ItemGrades.Shields.Aster_Seraph_Antagonist_Shield_Balance',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Aster_ItemGrades.Shields.Aster_Seraph_Blockade_Shield_Balance',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary BalancedItems
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_07_LegendaryPlusPearl',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant={epic_scale_legendary_dbl}
                ),
                bDropOnDeath=True
            )
        )

    #</Pearls and Seraph in Legendary Pool>

    #<More Frequent Eridium>

        # Makes Eridium drop a little more frequently

        set GD_Itempools.DropWeights.DropODDS_EridiumBar:ConstantAttributeValueResolver_1 ConstantValue {eridium_bar_drop}

        set GD_Itempools.DropWeights.DropODDS_EridiumStick:ConstantAttributeValueResolver_1 ConstantValue {eridium_stick_drop}

    #</More Frequent Eridium>

    #<Torgue Token Quantity Improvements>

        # Improvements to the amount of Torgue Tokens dropped, at least by enemies who
        # ordinarily drop smallish amounts

        set GD_Iris_ItemPools.TorgueToken.ItemPool_TorgueToken_Single Quantity
        (
            BaseValueConstant=3.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Iris_ItemPools.TorgueToken.ItemPool_TorgueToken_Qty3 Quantity
        (
            BaseValueConstant=7.0
        )

        set GD_Iris_ItemPools.TorgueToken.ItemPool_TorgueToken_Qty5 Quantity
        (
            BaseValueConstant=10.0
        )

        set GD_Iris_ItemPools.TorgueToken.ItemPool_TorgueToken_Qty7 Quantity
        (
            BaseValueConstant=14.0
        )

        set GD_Iris_ItemPools.TorgueToken.ItemPool_TorgueToken_Qty10 Quantity
        (
            BaseValueConstant=17.0
        )

        set GD_Iris_ItemPools.TorgueToken.ItemPool_TorgueToken_Qty15 Quantity
        (
            BaseValueConstant=20.0
        )

    #</Torgue Token Quantity Improvements>

    #<Guaranteed Boss Drops>

        # Bosses will always drop their unique/legendary rewards

        #<Base Game>

            set GD_Itempools.DropWeights.DropODDs_BossUniques:ConstantAttributeValueResolver_0 ConstantValue 10

            set GD_Itempools.DropWeights.DropODDs_BossUniqueRares:ConstantAttributeValueResolver_0 ConstantValue 10

        #</Base Game>

        # Some DLC minibosses don't use the DropODDs_BossUniques* vars and
        # have to be patched manually

        #<Captain Scarlett DLC>

            {hotfixes:scarlett_nobeard}

            {hotfixes:scarlett_bigsleep}

        #</Captain Scarlett DLC>

        #<Torgue DLC>

            {hotfixes:torgue_piston}

        #</Torgue DLC>

        #<Hammerlock DLC>

            {hotfixes:hammerlock_thermitage}

            {hotfixes:hammerlock_dribbles}

            {hotfixes:hammerlock_woundspike}

            {hotfixes:hammerlock_bloodtail}

        #</Hammerlock DLC>

        #<Tiny Tina DLC>

            {hotfixes:dragonkeep_goldgolem_drop_pool}

        #</Tiny Tina DLC>

    #</Guaranteed Boss Drops>

    #<Boss Drop Improved Quantities>

        # Bosses which have more than one possible unique/legendary reward will always
        # drop that many items on death, so you should have some chance of getting both.

        set GD_Itempools.Runnables.Pool_Bunker Quantity
        (
            BaseValueConstant=3.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_CaptFlynt Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_ChubbieUniques Quantity
        (
            BaseValueConstant=4.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_FourAssassins Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_Henry Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_KingMong Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_Sheriff Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_SkagzillaMom Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_SonOfMothrakk Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_Talos Quantity
        (
            BaseValueConstant=3.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_Terramorphous Quantity
        (
            BaseValueConstant=7.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_UltimateBadassVarkid Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_Verm Quantity
        (
            BaseValueConstant=5.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_Warrior Quantity
        (
            BaseValueConstant=8.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_Wilhelm Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        set GD_Itempools.Runnables.Pool_SonOfMothrakk Quantity
        (
            BaseValueConstant=2.000000,
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1.000000
        )

        # The rest have to be done via Hotfix

        {hotfixes:dragonkeep_goldgolem_drop_qty}

        {hotfixes:dragonkeep_sorcerersdaughter_drop_pool}

    #</Boss Drop Improved Quantities>

    #<Boss Drop Normalization>

        #  Make loot pools for bosses have equal probabilities for all items

        set GD_Itempools.Runnables.Pool_Sheriff BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item_Unique.A_Sheriff',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Law',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set GD_Itempools.Runnables.Pool_UltimateBadassVarkid BalancedItems
        (
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Legendary.GM_Quasar',
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            ),
            (
                ItmPoolDefinition=KeyedItemPoolDefinition'GD_CustomItemPools_MainGame.Rewards.YellowNinja',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=0.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        # Hotfixes for the rest

        {hotfixes:dragonkeep_sorcerersdaughter_normalize_0}

        {hotfixes:dragonkeep_sorcerersdaughter_normalize_1}

        {hotfixes:dragonkeep_sorcerersdaughter_normalize_2}

        {hotfixes:dragonkeep_sorcerersdaughter_normalize_3}

    #</Boss Drop Normalization>

    #<Raid Boss Drop Improvements>

        # Similar to Boss Drop Improved Quantities, this improves drops from
        # raid bosses, which IMO are often quite anemic.  They will drop more
        # Eridium, more rare gear, and will drop N legendaries/uniques/pearls
        # for all possible weapons in that pool.  They will also drop more
        # Seraph crystals, and will drop crystals even in Normal/TVHM.

        #<Hyperius>

            # For Hyperius, we also tweak his "PinkWeapons" and "Legendary" pools to make
            # a little more sense.

            set GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid1_Legendary BalancedItems
            (
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Hornet',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Vladof_5_Sherdifier',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=InventoryBalanceDefinition'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_05_Legendary',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=InventoryBalanceDefinition'GD_GrenadeMods.A_Item_Custom.GM_KissOfDeath',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Pyrophobia',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                )
            )

            set GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid1_PinkWeapons BalancedItems
            (
                ( 
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.Pistol.Devastator.Orchid_Seraph_Devastator_Balance',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.SMG.Tattler.Orchid_Seraph_Tattler_Balance',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.Shotgun.Spitter.Orchid_Seraph_Spitter_Balance',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                ),
                (
                    ItmPoolDefinition=None,
                    InvBalanceDefinition=WeaponBalanceDefinition'GD_Orchid_RaidWeapons.SMG.Actualizer.Orchid_Seraph_Actualizer_Balance',
                    Probability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    ),
                    bDropOnDeath=True
                )
            )

            # Now on to the more usual drop pool tweaking

            set GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid1_Legendary Quantity
            (
                    BaseValueConstant=7.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
            )

            set GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid1_PinkWeapons Quantity
            (
                    BaseValueConstant=4.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
            )

            set GD_Orchid_ItemPools.Raid.PoolList_Orchid_Raid1_Items ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid1_PinkWeapons',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid1_Legendary',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne',
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
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
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
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=100.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=100.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=100.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=200.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=200.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Orchid_ItemPools.SeraphCrystal.Pool_SeraphCrystal_10_Drop',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=200.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Orchid_ItemPools.SeraphCrystal.Pool_SeraphCrystal_10_Drop',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=200.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
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
            )

        #</Hyperius>

        #<Master Gee>

            set GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid3_PinkWeapons Quantity
            (
                    BaseValueConstant=4.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
            )

            set GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid3_Legendary Quantity
            (
                    BaseValueConstant=6.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
            )

            set GD_Orchid_ItemPools.Raid.PoolList_Orchid_Raid3_Items ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid3_PinkWeapons',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Orchid_ItemPools.Raid.Pool_Orchid_Raid3_Legendary',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne',
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
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
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
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=100.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=100.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Bar',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=100.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=200.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Eridium_Stick',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=200.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Orchid_ItemPools.SeraphCrystal.Pool_SeraphCrystal_10_Drop',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=200.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Orchid_ItemPools.SeraphCrystal.Pool_SeraphCrystal_10_Drop',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=200.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
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
            )

        #</Master Gee>

        #<Pyro Pete>

            # Pete actually includes GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear already
            # so there's not much to do here.  Everything but the Seraph Crystal + Torgue Token
            # lines are just copied from stock

            set GD_Iris_ItemPools.Raid.PoolList_Iris_Raid1A_Items ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.TorgueToken.ItemPool_TorgueToken_Qty15',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=0.020000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=0.700000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_02_Uncommon',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=0.100000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=0.350000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=0.020000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=0.700000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_02_Uncommon',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=0.100000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_02_Uncommon',
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
            )

            # I'm not actually sure what this "Raid1B" controls, though I suspect
            # it's probably the same Raid battle, but in TVHM or UVHM.  Adding
            # the seraph+torguetokens anyway, and upping some of the probabilities
            # here, just in case.

            set GD_Iris_ItemPools.Raid.PoolList_Iris_Raid1B_Items ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.TorgueToken.ItemPool_TorgueToken_Qty15',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Iris_ItemPools.SeraphCrystal.Pool_SeraphCrystal_7',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=0.020000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=0.700000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=0.100000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=0.700000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=0.700000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=0.100000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare',
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
            )

        #</Pyro Pete>

        #<Dexiduous>

            # Note that the Chopper drop happens outside this ItemPool list, and is already
            # buffed by our DropODDs_BossUniqueRares change.  Regardless, vastly buffing this
            # list to make up for the ridiculous time requirements to fight Dexiduous.  Also
            # note that this entire PoolList is dropped three times on Dexi's death!

            set GD_Sage_ItemPools.Raid.PoolList_Sage_DifterRaid_Items ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Sage_ItemPools.Raid.Pool_Sage_Raid_PinkWeapons',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Sage_ItemPools.Raid.Pool_Sage_Raid_PinkWeapons',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.333333
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Sage_ItemPools.Raid.Pool_Sage_Raid_Legendary',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_BossUniques',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Sage_ItemPools.Raid.Pool_Sage_Raid_Legendary',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_BossUniques',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=0.333333
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne',
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
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
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
            )

        #</Dexiduous>

        #<Voracidous>

            # We're playing a strange game with the drop pool here.  Unlike
            # other DLCs, the item definition for the seraph crystals doesn't get
            # loaded until the level does, so we can't specify seraph crystal
            # rewards directly.  Rather than have a gigantic hotfix, what I'm doing
            # is substituting GD_Itempools.WeaponPools.Pool_Weapons_All_01_Common
            # and then just hotfixing *those* values.

            set GD_Sage_ItemPools.Raid.Pool_Sage_Raid_PinkWeapons Quantity
            (
                    BaseValueConstant=4.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
            )

            set GD_Sage_ItemPools.Raid.Pool_Sage_Raid_Legendary Quantity
            (
                    BaseValueConstant=4.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
            )

            set GD_Sage_ItemPools.Raid.PoolList_Sage_Raid_Items ItemPools
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_01_Common',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_01_Common',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_01_Common',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Sage_ItemPools.Raid.Pool_Sage_Raid_PinkWeapons',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Sage_ItemPools.Raid.Pool_Sage_Raid_Legendary',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne',
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
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.GearDrops_PerPlayer',
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
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health',
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
                        BaseValueScaleConstant=1.000000
                    )
                ),
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways',
                    PoolProbability=(
                        BaseValueConstant=0.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer',
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
            )

            {hotfixes:vorac_seraph_0}

            {hotfixes:vorac_seraph_1}

            {hotfixes:vorac_seraph_2}

        #</Voracidous>

        #<Ancient Dragons>

            # First up, set the Seraph Crystal drop pool to always drop 28,
            # and drop regardless of playthrough

            {hotfixes:dragonkeep_ancient_crystals0}

            {hotfixes:dragonkeep_ancient_crystals1}

            {hotfixes:dragonkeep_ancient_crystals2}

            # Drop three items from their Uniques pool

            {hotfixes:dragonkeep_ancient_uniques0}

            # Aaand tweak the drop pools in general

            {hotfixes:dragonkeep_ancient_drop1}

            {hotfixes:dragonkeep_ancient_drop2}

        #</Ancient Dragons>

    #</Raid Boss Drop Improvements>

    #<Remove Level-Based Loot Restrictions (enhancement of UCP 4.0)>

        # This is a superset of a similar UCP 4.0 mod section.  In addition to the
        # basic early-game weapon unlocks that UCP provides, this additionally allows
        # Relics, Class Mods, all shield types, all grenade types, and probably
        # just about everything to spawn from the beginning.
        #
        # Either UCP or the "UCP 4.0 Duplicates" section here, at least, will need to
        # be active if the rest of this mod is active, because otherwise the early
        # game will drop literally no loot.
        #
        # There's no problem with having both this and UCP enabled -- it'll just mean
        # that a few statements get executed twice.

        #<UCP 4.0 Duplicates>

            set GD_Itempools.Scheduling.Gamestage_07:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_03:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_02:ConstantAttributeValueResolver_0 ConstantValue 1

        #</UCP 4.0 Duplicates>

        #<Additional Unlocks>

            # These take care of a ton of other stuff, like other weapon types (rocket launchers,
            # etc), Relics, etc.

            set GD_Itempools.Scheduling.Gamestage_04:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_05:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_06:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_08:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_09:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_10:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_11:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_12:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_13:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_14:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_15:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_16:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_17:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_18:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_19:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_20:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_21:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_22:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_23:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.Gamestage_24:ConstantAttributeValueResolver_0 ConstantValue 1

        #</Additional Unlocks>

        #<Class Mods>

            # Class Mods have their own set of scheduling parameters

            set GD_Itempools.Scheduling.LootSchedule_ClassMod_01_Common:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.LootSchedule_ClassMod_02_Uncommon:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.LootSchedule_ClassMod_03_Rare:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.LootSchedule_ClassMod_04_VeryRare:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_Itempools.Scheduling.LootSchedule_ClassMod_05_Legendary:ConstantAttributeValueResolver_0 ConstantValue 1

        #</Class Mods>

        #<Grenade Mods>

            # The various grenade mod components are restricted by level

            set GD_GrenadeMods.BalanceAttributes.MinGameStage_CorrosiveGrenade:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_GrenadeMods.BalanceAttributes.MinGameStage_Homing:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_GrenadeMods.BalanceAttributes.MinGameStage_IncendiaryGrenade:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_GrenadeMods.BalanceAttributes.MinGameStage_Longbow:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_GrenadeMods.BalanceAttributes.MinGameStage_Rubberized:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_GrenadeMods.BalanceAttributes.MinGameStage_ShockGrenade:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_GrenadeMods.BalanceAttributes.MinGameStage_SlagGrenade:ConstantAttributeValueResolver_0 ConstantValue 1

            set GD_GrenadeMods.BalanceAttributes.MinGameStage_Sticky:ConstantAttributeValueResolver_0 ConstantValue 1

            # These definitions could be done with "set" as with other stuff, but
            # it's actually a little more convenient to do 'em with hotfixes

            {hotfixes:grenade_AreaEffect_0_0}

            {hotfixes:grenade_AreaEffect_0_1}

            {hotfixes:grenade_AreaEffect_0_2}

            {hotfixes:grenade_AreaEffect_0_3}

            {hotfixes:grenade_BouncingBetty_0_0}

            {hotfixes:grenade_BouncingBetty_0_1}

            {hotfixes:grenade_BouncingBetty_0_2}

            {hotfixes:grenade_BouncingBetty_0_3}

            {hotfixes:grenade_BouncingBetty_1_0}

            {hotfixes:grenade_BouncingBetty_1_1}

            {hotfixes:grenade_BouncingBetty_1_2}

            {hotfixes:grenade_BouncingBetty_1_3}

            {hotfixes:grenade_Mirv_0_0}

            {hotfixes:grenade_Mirv_0_1}

            {hotfixes:grenade_Mirv_0_2}

            {hotfixes:grenade_Mirv_0_3}

            {hotfixes:grenade_Mirv_1_0}

            {hotfixes:grenade_Mirv_1_1}

            {hotfixes:grenade_Mirv_1_2}

            {hotfixes:grenade_Mirv_1_3}

            {hotfixes:grenade_Singularity_0_0}

            {hotfixes:grenade_Singularity_0_1}

            {hotfixes:grenade_Singularity_0_2}

            {hotfixes:grenade_Singularity_0_3}

            {hotfixes:grenade_Transfusion_0_0}

            {hotfixes:grenade_Transfusion_0_1}

            {hotfixes:grenade_Transfusion_0_2}

            {hotfixes:grenade_Transfusion_0_3}

        #</Grenade Mods>

        #<Lobelia Pearlescent Pool>

            # Ordinarily, Pearlescent weapons which come from this pool won't drop until
            # level 61 or so.  (So far I've only seen the Chubby pool as something using
            # this drop pool, but other things might too.)

            set GD_Lobelia_Itempools.WeaponPools.Pool_Lobelia_Pearlescent_Weapons_All MinGameStageRequirement None

        #</Lobelia Pearlescent Pool>

    #</Remove Level-Based Loot Restrictions (enhancement of UCP 4.0)>

{test_drop_str}
{gunsandgear_drop_str}

#</{mod_name} ({variant_name})>

{hotfix_transient_defs}

""".format(
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
print('Wrote FilterTool/UCP-compatible mod file to: {}'.format(output_filename_filtertool))

# Write to a standalone file
with open(output_filename_standalone, 'w') as df:
    df.write(loot_str.format(
        variant_name=variant_standalone_name,
        hotfix_gearbox_base=hfs.get_gearbox_hotfix_xml(),
        hotfix_transient_defs=hfs.get_transient_defs(),
        ))
print('Wrote standalone mod file to: {}'.format(output_filename_standalone))
