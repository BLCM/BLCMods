#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

from modprocessor import ModProcessor
mp = ModProcessor()

output_filename = 'loot-container-testing.blcm'

lines = []
lines.append("""TPS
#<Loot Container Testing>

""")

attach = 'Ammo1'
containers = [
    #('GD_Ma_Balance_Treasure.LootableGrades.ObjectGrade_MetalCrate_Marigold',
    #    'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary'),
    #('GD_Ma_Balance_Treasure.LootableGrades.ObjectGrade_Bandit_Ammo_Marigold',
    #    'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary'),
    #('GD_Ma_Balance_Treasure.ChestGrades.ObjectGrade_DahlWeaponChest_Marigold',
    #    'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary'),
    #('GD_Ma_Balance_Treasure.ChestGrades.ObjectGrade_DahlWeaponChest_Glitched',
    #    'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary'),
    #('GD_Balance_Treasure.LootableGrades.ObjectGrade_Mailbox',
    #    'GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary'),
    #('GD_Ma_Balance_Treasure.LootableGrades.ObjectGrade_StrongBox_CashOnly_Marigold',
    #    'GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary'),
    ]
for idx, (container, pool) in enumerate(containers):
    lines.append('level None set {} DefaultIncludedLootLists ()'.format(container))
    lines.append('')
    lines.append("""level None set {container} DefaultLoot
        (
            ( 
                ConfigurationName="Testing", 
                bIgnoreGameStageRestrictions=True, 
                LootGameStageVarianceFormula=None, 
                Weight=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000 
                ), 
                ItemAttachments=( 
                    ( 
                        ItemPool=ItemPoolDefinition'{pool}', 
                        PoolProbability=( 
                            BaseValueConstant=1.000000, 
                            BaseValueAttribute=None, 
                            InitializationDefinition=None, 
                            BaseValueScaleConstant=1.000000 
                        ), 
                        InvBalanceDefinition=None, 
                        AttachmentPointName="{attach}" 
                    ) 
                ) 
            )
        )
        """.format(
            container=container,
            pool=pool,
            attach=attach,
            ))
    lines.append('')
#lines.append("level None set GD_Meteorites.Projectiles.Projectile_Meteorite:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_123.PopulationFactoryPopulationDefinition_1 PopulationDef PopulationDefinition'GD_Meteorites.Population.Pop_Meteorite_LootPile_Chest'")
#lines.append('')
#lines.append("level None set GD_Meteorites.Projectiles.Projectile_Meteorite:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_124.PopulationFactoryPopulationDefinition_0 PopulationDef PopulationDefinition'GD_Meteorites.Population.Pop_Meteorite_LootPile_Chest'")
#lines.append('')

def chest_overload(lines, x, z, cur_y, y_inc, yaw, chest_type, level, object_base, points):
    for idx, point in enumerate(points):
        lines.append("level {} set {}_{} PopulationDef PopulationDefinition'{}'".format(level, object_base, point, chest_type))
        lines.append('')
        lines.append("level {} set {}_{} Location.X {}".format(level, object_base, point, x))
        lines.append('')
        lines.append("level {} set {}_{} Location.Y {}".format(level, object_base, point, cur_y))
        lines.append('')
        lines.append("level {} set {}_{} Location.Z {}".format(level, object_base, point, z))
        lines.append('')
        lines.append("level {} set {}_{} Rotation.Yaw {}".format(level, object_base, point, yaw))
        lines.append('')
        cur_y += y_inc

# Titan Robot Production Factory
x = -16778
z = 5920
cur_y = 29010
y_inc = 200
yaw = '8192'
#chest_type = 'GD_Population_Treasure.TreasureChests.EpicChest_Dahl_Respawning'
chest_type = 'GD_Population_Treasure.TreasureChests.EpicChest_Moonstone'
level = 'DahlFactory_Boss'
object_base = 'DahlFactory_BossDynamic.TheWorld:PersistentLevel.PopulationOpportunityPoint'
points = [31, 32, 33, 34, 35, 36, 37, 20, 22, 24, 25, 26]
lines.append('level None set GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Moonstone:BehaviorProviderDefinition_1.Behavior_SetUsabilityCost_46 CostAmount 0')
lines.append('')
chest_overload(lines, x, z, cur_y, y_inc, yaw, chest_type, level, object_base, points)

# Cluster Pandora.  These are actually by the level exit, and are fairly amusingly
# tilted, since all we correct is yaw.
x = 4046
z = 2650
cur_y = -22208
y_inc = 250
yaw = '0'
chest_type = 'GD_Ma_Population_Treasure.TreasureChests.EpicChest_Red_Glitched'
level = 'Ma_LeftCluster_P'
object_base = 'Ma_LeftCluster_Combat.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint'
points = [0, 1, 10, 100, 101, 103, 104]
chest_overload(lines, x, z, cur_y, y_inc, yaw, chest_type, level, object_base, points)

# Cluster Overlook.  Over by the level exit.
x = 47326
z = 453
cur_y = 2562
y_inc = 250
yaw = '16384'
chest_type = 'GD_Ma_Population_Treasure.TreasureChests.EpicChest_Hyperion_Glitched'
level = 'Ma_RightCluster_P'
object_base = 'Ma_RightCluster_Combat.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint'
points = [0, 1, 10, 100, 101, 102, 103, 104]
chest_overload(lines, x, z, cur_y, y_inc, yaw, chest_type, level, object_base, points)

# Outlands Canyon
x = -15766
z = -1252
cur_y = 51197
y_inc = 200
yaw = '33664'
chest_type = 'GD_Population_Treasure.TreasureChests.WeaponChest_BanditPotty'
level = 'Outlands_P2'
object_base = 'Outlands_P2.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint'
points = [1, 10, 11, 12, 13, 15, 2, 21, 22]
chest_overload(lines, x, z, cur_y, y_inc, yaw, chest_type, level, object_base, points)

# Crisis Scar
x = -4945
z = -2091
cur_y = 4359
y_inc = 200
yaw = '33664'
chest_type = 'GD_Population_Treasure.Lootables.Safe'
level = 'ComFacility_P'
object_base = 'ComFacility_P.TheWorld:PersistentLevel.PopulationOpportunityPoint'
points = [0, 1, 100, 101, 102]
chest_overload(lines, x, z, cur_y, y_inc, yaw, chest_type, level, object_base, points)

# Badass scavs (at least in the Outlands)
#lines.append('level None set GD_Population_Scavengers.Mixes.PopDef_ScavGroundMix_Outlands ActorArchetypeList[3].Probability.BaseValueConstant 500000')
#lines.append('')
#lines.append('level None set GD_Population_Scavengers.Mixes.PopDef_ScavGroundMix_Outlands ActorArchetypeList[3].MaxActiveAtOneTime.BaseValueConstant 500000')
#lines.append('')

# Chubby Stalkers (these are the only chubby types in TPS, it seems)
#lines.append('level None set GD_Population_Stalker.Mixes.PopDef_StalkerMix_Ambush ActorArchetypeList[2].Probability.BaseValueConstant 10000')
#lines.append('')
#lines.append('level None set GD_Population_Stalker.Mixes.PopDef_StalkerMix_Needle ActorArchetypeList[1].Probability.BaseValueConstant 10000')
#lines.append('')
#lines.append('level None set GD_Population_Stalker.Mixes.PopDef_StalkerMix_Spring ActorArchetypeList[1].Probability.BaseValueConstant 10000')
#lines.append('')

lines.append('#</Loot Container Testing>')

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))
