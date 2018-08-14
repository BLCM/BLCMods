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
    from modprocessor import ModProcessor, Config
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

mod_name = 'Easier ECLIPSE and EOS'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

###
### Control classes
###

class EclipseUltimate(Config):
    """
    Buff ECLIPSE instead of nerfing him.  'cause why not?
    """

    label = 'Infinite Badass Difficulty (this is a buff, not a nerf!)'

    health_mult = 240
    shield_mult = 200
    nonweapon_damage_mult = 9

    arm_laser_damage_scale = 0.7

    rocket_speed = 1900
    rocket_damage_scale = 1.2

    shock_orb_damage_scale = 1
    shock_orb_effect_chance_scale = 2

class EclipseStock(Config):
    """
    Stock definitions for ECLIPSE
    """

    label = 'Stock Difficulty'

    health_mult = 180
    shield_mult = 160
    nonweapon_damage_mult = 7

    arm_laser_damage_scale = 0.4

    rocket_speed = 1500
    rocket_damage_scale = 1

    shock_orb_damage_scale = 0.5
    shock_orb_effect_chance_scale = 1

class EclipseEasier(Config):
    """
    Easier definitions for ECLIPSE
    """

    label = 'Easier ECLIPSE'

    health_mult = 120
    shield_mult = 110
    nonweapon_damage_mult = 6

    arm_laser_damage_scale = 0.35

    rocket_speed = 1300
    rocket_damage_scale = 0.8

    # Honestly, these aren't too bad IMO, just keeping them at the default.
    shock_orb_damage_scale = 0.5
    shock_orb_effect_chance_scale = 1

class EclipseWeak(Config):
    """
    Weak definitions for ECLIPSE
    """

    label = 'Even Easier ECLIPSE'

    health_mult = 60
    shield_mult = 60
    nonweapon_damage_mult = 5

    arm_laser_damage_scale = 0.2

    rocket_speed = 1100
    rocket_damage_scale = 0.6

    shock_orb_damage_scale = 0.4
    shock_orb_effect_chance_scale = 0.8

class EclipseChump(Config):
    """
    And, why not.  Total shrimp of a boss.
    """

    label = 'Total Chump'

    health_mult = 5
    shield_mult = 5
    nonweapon_damage_mult = 2

    arm_laser_damage_scale = 0.1

    rocket_speed = 550
    rocket_damage_scale = 0.2

    shock_orb_damage_scale = 0.2
    shock_orb_effect_chance_scale = 0.5

###
### Start generating the mod
###

mod_list = []
mod_list.append("""TPS
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Makes the boss fights against ECLIPSE and EOS easier.  Each has a few different
    # options, and can be toggled independently of each other (including setting them
    # to the stock values, in case you want to nerf one but not the other).
    #
    # Should you be feeling masochistic, there's also an option which buffs both of
    # them, rather than nerfing.

    #<ECLIPSE><MUT>

    """.format(mod_name=mod_name, mod_version=mod_version))

###
### ECLIPSE
###
for config in [EclipseEasier(), EclipseWeak(), EclipseChump(), EclipseStock(), EclipseUltimate()]:
    mod_list.append("""
        #<{config:label}>

            #<Health Multiplier>

                level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Character.CharClass_LoaderUltimateBadass AttributeStartingValues[0].BaseValue.BaseValueConstant {config:health_mult}

            #</Health Multiplier>

            #<Shield Multiplier>

                level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Character.CharClass_LoaderUltimateBadass AttributeStartingValues[6].BaseValue.BaseValueConstant {config:shield_mult}

            #</Shield Multiplier>

            #<"Non-Weapon" Damage Multiplier>

                # This ends up affecting most of ECLIPSE's attacks, such as arm lasers,
                # rocket attacks, and shock balls.  Could affect other damage output from
                # him as well.  The extra damage reduction done in the individual
                # categories below will be on top of this tweak.

                level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Character.CharClass_LoaderUltimateBadass AttributeStartingValues[1].BaseValue.BaseValueConstant {config:nonweapon_damage_mult}

            #</"Non-Weapon" Damage Multiplier>

            #<Arm Lasers>

                level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Anims.Anim_LoaderUltimateBadass_ArmGun_Loop:BehaviorProviderDefinition_32.Behavior_AIThrowProjectileAtTarget_7 ChildProjectileBaseValues[0].BaseValue.BaseValueScaleConstant {config:arm_laser_damage_scale}

            #</Arm Lasers>

            #<Rockets>

                #<Rocket Speed>

                    level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Projectiles.Proj_RocketLaunch SpeedFormula.BaseValueConstant {config:rocket_speed}

                #</Rocket Speed>

                #<Rocket Damage Scale>

                    level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Anims.Anim_LoaderUltimateBadass_Missile_Loop:BehaviorProviderDefinition_32.Behavior_SpawnProjectile_50 ChildProjectileBaseValues[0].BaseValue.BaseValueScaleConstant {config:rocket_damage_scale}

                    level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Anims.Anim_LoaderUltimateBadass_Missile_Loop:BehaviorProviderDefinition_32.Behavior_SpawnProjectile_51 ChildProjectileBaseValues[0].BaseValue.BaseValueScaleConstant {config:rocket_damage_scale}

                    level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Anims.Anim_LoaderUltimateBadass_Missile_Loop:BehaviorProviderDefinition_32.Behavior_SpawnProjectile_52 ChildProjectileBaseValues[0].BaseValue.BaseValueScaleConstant {config:rocket_damage_scale}

                    level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Anims.Anim_LoaderUltimateBadass_Missile_Loop:BehaviorProviderDefinition_32.Behavior_SpawnProjectile_53 ChildProjectileBaseValues[0].BaseValue.BaseValueScaleConstant {config:rocket_damage_scale}

                #</Rocket Damage Scale>

            #</Rockets>

            #<Shock Orbs>

                level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Projectiles.Proj_ShockBall:BehaviorProviderDefinition_0.Behavior_Explode_5 StatusEffectDamage.BaseValueScaleConstant {config:shock_orb_damage_scale}

                level Ma_FinalBoss_P set GD_Ma_VoltronTrap.Projectiles.Proj_ShockBall:BehaviorProviderDefinition_0.Behavior_Explode_5 StatusEffectChance.BaseValueScaleConstant {config:shock_orb_effect_chance_scale}

            #</Shock Orbs>

        #</{config:label}>
        """.format(config=config))

###
### End of ECLIPSE
###

mod_list.append('#</ECLIPSE>')

###
### EOS
###

mod_list.append('#<EOS><MUT>')

class EosUltimate(Config):
    """
    Buff EOS instead of nerfing him.  'cause why not?
    """

    label = 'Infinite Badass Difficulty (this is a buff, not a nerf!)'

    health_mult = 290
    shield_mult = 170
    nonweapon_damage_mult = 11

    turret_health_scale = 45
    turret_damage_scale = 2
    rocket_launcher_health_scale = 40
    rocket_damage_scale = 2

    moonshot_damage_scale_0 = 15
    moonshot_damage_scale_1 = 20

    moonshot_badass_pawn = 'GD_Ma_Pop_Glitches.Balance.PawnBalance_BadassGlitch'
    moonshot_regular_pawn_0 = 'GD_Ma_Pop_ClaptrapForces.Population.Uniques.PopDef_ShadowClone_Eos'
    moonshot_regular_pawn_1 = 'GD_Ma_Pop_Glitches.Population.PopDef_Glitch'
    moonshot_regular_pawn_2 = 'GD_Ma_Pop_Virus.Population.PopDef_VirusLauncher'
    moonshot_regular_pawn_3 = 'GD_Ma_Pop_Virus.Population.PopDef_Virus'
    moonshot_regular_pawn_4 = 'GD_Ma_Pop_Virus.Population.PopDef_ParasiticVirus'

    # I *think* this is for the first bit of the battle
    moonshot_regular_pawn_0_weight_0 = 1.0
    moonshot_regular_pawn_1_weight_0 = 0.6
    moonshot_regular_pawn_2_weight_0 = 1.0
    moonshot_regular_pawn_3_weight_0 = 0.6
    moonshot_regular_pawn_4_weight_0 = 1.0

    # And then this is after EOS is hurt a bit
    moonshot_regular_pawn_0_weight_1 = 1.0
    moonshot_regular_pawn_1_weight_1 = 0.3
    moonshot_regular_pawn_2_weight_1 = 2.0
    moonshot_regular_pawn_3_weight_1 = 0.5
    moonshot_regular_pawn_4_weight_1 = 1.2

    eye_of_helios_delay = 0
    eye_of_helios_damage_scale = 99
    eye_of_helios_damage_radius = 2000

class EosStock(Config):
    """
    Stock definitions for ECLIPSE
    """

    # Not going to do anything with the yellow sticky-grenade things that EOS
    # lobs at you when its turrets are down.  They're at GD_Ma_Helios.Projectiles.Proj_SpamGrenade.
    # Would be pretty trivial to do so if we wanted, though.

    label = 'Stock Difficulty'

    health_mult = 220
    shield_mult = 130
    nonweapon_damage_mult = 8

    turret_health_scale = 35
    turret_damage_scale = 1
    rocket_launcher_health_scale = 25
    rocket_damage_scale = 1

    moonshot_damage_scale_0 = 12
    moonshot_damage_scale_1 = 15

    moonshot_badass_pawn = 'GD_Ma_Pop_Glitches.Balance.PawnBalance_BadassGlitch'
    moonshot_regular_pawn_0 = 'GD_Ma_Pop_ClaptrapForces.Population.Uniques.PopDef_ShadowClone_Eos'
    moonshot_regular_pawn_1 = 'GD_Ma_Pop_Glitches.Population.PopDef_Glitch'
    moonshot_regular_pawn_2 = 'GD_Ma_Pop_Virus.Population.PopDef_VirusLauncher'
    moonshot_regular_pawn_3 = 'GD_Ma_Pop_Virus.Population.PopDef_Virus'
    moonshot_regular_pawn_4 = 'GD_Ma_Pop_Virus.Population.PopDef_ParasiticVirus'

    # I *think* this is for the first bit of the battle
    moonshot_regular_pawn_0_weight_0 = 0.4
    moonshot_regular_pawn_1_weight_0 = 1.0
    moonshot_regular_pawn_2_weight_0 = 0.25
    moonshot_regular_pawn_3_weight_0 = 1.0
    moonshot_regular_pawn_4_weight_0 = 1.0

    # And then this is after EOS is hurt a bit
    moonshot_regular_pawn_0_weight_1 = 0.25
    moonshot_regular_pawn_1_weight_1 = 1.0
    moonshot_regular_pawn_2_weight_1 = 1.0
    moonshot_regular_pawn_3_weight_1 = 1.0
    moonshot_regular_pawn_4_weight_1 = 1.0

    eye_of_helios_delay = 0
    eye_of_helios_damage_scale = 99
    eye_of_helios_damage_radius = 1500

class EosEasier(Config):
    """
    Easier definitions for ECLIPSE
    """

    label = 'Easier EOS'

    health_mult = 170
    shield_mult = 90
    nonweapon_damage_mult = 6

    turret_health_scale = 20
    turret_damage_scale = 0.9
    rocket_launcher_health_scale = 20
    rocket_damage_scale = 0.9

    moonshot_damage_scale_0 = 10
    moonshot_damage_scale_1 = 13

    moonshot_badass_pawn = 'GD_Ma_Pop_Glitches.Balance.PawnBalance_BadassGlitch'
    moonshot_regular_pawn_0 = 'GD_Ma_Pop_ClaptrapForces.Population.Uniques.PopDef_ShadowClone_Eos'
    moonshot_regular_pawn_1 = 'GD_Ma_Pop_Glitches.Population.PopDef_Glitch'
    moonshot_regular_pawn_2 = 'GD_Ma_Pop_Virus.Population.PopDef_VirusLauncher'
    moonshot_regular_pawn_3 = 'GD_Ma_Pop_Virus.Population.PopDef_Virus'
    moonshot_regular_pawn_4 = 'GD_Ma_Pop_Virus.Population.PopDef_ParasiticVirus'

    # I *think* this is for the first bit of the battle
    moonshot_regular_pawn_0_weight_0 = 0.2
    moonshot_regular_pawn_1_weight_0 = 1.0
    moonshot_regular_pawn_2_weight_0 = 0.2
    moonshot_regular_pawn_3_weight_0 = 1.0
    moonshot_regular_pawn_4_weight_0 = 0.9

    # And then this is after EOS is hurt a bit
    moonshot_regular_pawn_0_weight_1 = 0.25
    moonshot_regular_pawn_1_weight_1 = 1.0
    moonshot_regular_pawn_2_weight_1 = 0.5
    moonshot_regular_pawn_3_weight_1 = 1.0
    moonshot_regular_pawn_4_weight_1 = 1.0

    eye_of_helios_delay = 0.5
    eye_of_helios_damage_scale = 90
    eye_of_helios_damage_radius = 1300

class EosWeak(Config):
    """
    Weak definitions for ECLIPSE
    """

    label = 'Even Easier EOS'

    health_mult = 120
    shield_mult = 60
    nonweapon_damage_mult = 5

    turret_health_scale = 15
    turret_damage_scale = 0.4
    rocket_launcher_health_scale = 15
    rocket_damage_scale = 0.8

    moonshot_damage_scale_0 = 8
    moonshot_damage_scale_1 = 10

    moonshot_badass_pawn = 'GD_Ma_Pop_Virus.Balance.PawnBalance_VirusLauncher'
    moonshot_regular_pawn_0 = 'GD_Ma_Pop_ClaptrapForces.Population.Uniques.PopDef_ShadowClone_Eos'
    moonshot_regular_pawn_1 = 'GD_Ma_Pop_Glitches.Population.PopDef_Glitch'
    moonshot_regular_pawn_2 = 'GD_Ma_Pop_Glitches.Mixes.PopDef_Glitches_Mix_FinalBoss_Weak'
    moonshot_regular_pawn_3 = 'GD_Ma_Pop_Virus.Population.PopDef_Virus'
    moonshot_regular_pawn_4 = 'GD_Ma_Pop_Virus.Population.PopDef_ParasiticVirus'

    # I *think* this is for the first bit of the battle
    moonshot_regular_pawn_0_weight_0 = 0
    moonshot_regular_pawn_1_weight_0 = 1.0
    moonshot_regular_pawn_2_weight_0 = 1.0
    moonshot_regular_pawn_3_weight_0 = 1.0
    moonshot_regular_pawn_4_weight_0 = 0.4

    # And then this is after EOS is hurt a bit
    moonshot_regular_pawn_0_weight_1 = 0.25
    moonshot_regular_pawn_1_weight_1 = 1.0
    moonshot_regular_pawn_2_weight_1 = 1.0
    moonshot_regular_pawn_3_weight_1 = 1.0
    moonshot_regular_pawn_4_weight_1 = 0.8

    eye_of_helios_delay = 1
    eye_of_helios_damage_scale = 80
    eye_of_helios_damage_radius = 1200

class EosChump(Config):
    """
    And, why not.  Total shrimp of a boss.
    """

    label = 'Total Chump'

    health_mult = 40
    shield_mult = 10
    nonweapon_damage_mult = 2

    turret_health_scale = 5
    turret_damage_scale = 0.4
    rocket_launcher_health_scale = 5
    rocket_damage_scale = 0.4

    moonshot_damage_scale_0 = 4
    moonshot_damage_scale_1 = 6

    moonshot_badass_pawn = 'GD_Ma_Pop_Virus.Balance.PawnBalance_ParasiticVirus'
    moonshot_regular_pawn_0 = 'GD_Ma_Pop_ClaptrapForces.Population.Uniques.PopDef_ShadowClone_Eos'
    moonshot_regular_pawn_1 = 'GD_Ma_Pop_Glitches.Population.PopDef_Glitch'
    moonshot_regular_pawn_2 = 'GD_Ma_Pop_Glitches.Mixes.PopDef_Glitches_Mix_FinalBoss_Weak'
    moonshot_regular_pawn_3 = 'GD_Ma_Pop_Virus.Population.PopDef_Virus'
    moonshot_regular_pawn_4 = 'GD_Ma_Pop_Glitches.Mixes.PopDef_Glitches_Mix_FinalBoss_Weak'

    # I *think* this is for the first bit of the battle
    moonshot_regular_pawn_0_weight_0 = 0
    moonshot_regular_pawn_1_weight_0 = 1.0
    moonshot_regular_pawn_2_weight_0 = 1.0
    moonshot_regular_pawn_3_weight_0 = 1.0
    moonshot_regular_pawn_4_weight_0 = 1.0

    # And then this is after EOS is hurt a bit
    moonshot_regular_pawn_0_weight_1 = 0
    moonshot_regular_pawn_1_weight_1 = 1.0
    moonshot_regular_pawn_2_weight_1 = 1.0
    moonshot_regular_pawn_3_weight_1 = 1.0
    moonshot_regular_pawn_4_weight_1 = 1.0

    eye_of_helios_delay = 2
    eye_of_helios_damage_scale = 70
    eye_of_helios_damage_radius = 1000

for config in [EosEasier(), EosWeak(), EosChump(), EosStock(), EosUltimate()]:
    mod_list.append("""
        #<{config:label}>

            #<Health and Shield Multiplier>

                # For some reason completely unbeknownst to me, some of our earlier statements
                # which modify ECLIPSE end up altering the EOS AIPawnBalanceDefinition;
                # specifically, they remove its PlayThroughs[0].AttributeStartingValues
                # array.  Damned if I know why.  It's the sets to the AttributeStartingValues
                # array in GD_Ma_VoltronTrap.Character.CharClass_LoaderUltimateBadass which
                # does it, which makes no bloody sense at all.  They're two totally different
                # objects.  And not even the same *kind* of object.  I don't know.  Weird.
                # Anyway, we have to recreate it entirely in here.  We *could* just use
                # the CharClass instead, and leave them blank here, of course, but it's a
                # point of pride to keep this in here, at this point.

                level Ma_FinalBoss_P set GD_Ma_Pop_BossFights.Balance.PawnBalance_Helios PlayThroughs[0].AttributeStartingValues
                (
                    (
                        Attribute = AttributeDefinition'GD_Balance_HealthAndDamage.AIParameters.Attribute_HealthMultiplier',
                        BaseValue =
                        (
                            BaseValueConstant = {config:health_mult},
                            BaseValueAttribute = None,
                            InitializationDefinition = None,
                            BaseValueScaleConstant = 1.000000
                        )
                    ),
                    (
                        Attribute = AttributeDefinition'GD_Balance_HealthAndDamage.AIParameters.Attribute_EnemyShieldMaxValueMultiplier',
                        BaseValue =
                        (
                            BaseValueConstant = {config:shield_mult},
                            BaseValueAttribute = None,
                            InitializationDefinition = None,
                            BaseValueScaleConstant = 1.000000
                        )
                    )
                )

            #</Health and Shield Multiplier>

            #<"Non-Weapon" Damage Multiplier>

                # This ends up affecting most of EOS's attacks

                level Ma_FinalBoss_P set GD_Ma_Helios.Character.CharClass_Ma_Helios AttributeStartingValues[1].BaseValue.BaseValueConstant {config:nonweapon_damage_mult}

            #</"Non-Weapon" Damage Multiplier>

            #<Turrets>

                #<Regular Turrets>

                    #<Health>

                        level Ma_FinalBoss_P set GD_Ma_HeliosTurret.Character.CharClass_Ma_HeliosTurret AttributeStartingValues[1].BaseValue.BaseValueConstant {config:turret_health_scale}

                    #</Health>

                    #<Damage>

                        # I'm actually not totally sure what buffs these up to begin with, but we can scale the final damage var pretty easily.
                        # (I'm guessing it's the non-weapon multiplier, above, though I'm not sure how)

                        level Ma_FinalBoss_P set GD_Ma_HeliosTurret.Weapons.Ma_HeliosTurret_WeaponType InstantHitDamage.BaseValueScaleConstant {config:turret_damage_scale}

                    #</Damage>
                
                #</Regular Turrets>

                #<Rocket Launchers>

                    #<Health>

                        level Ma_FinalBoss_P set GD_Ma_EosRocketTurret.Character.CharClass_Ma_EosRocketTurret AttributeStartingValues[1].BaseValue.BaseValueConstant {config:rocket_launcher_health_scale}

                    #</Health>

                    #<Damage>

                        # I'm actually not totally sure what buffs these up to begin with, but we can scale the final damage var pretty easily.
                        # (I'm guessing it's the non-weapon multiplier, above, though I'm not sure how)

                        level Ma_FinalBoss_P set GD_Ma_EosRocketTurret.Projectiles.Projectile_Rocket:BehaviorProviderDefinition_0.Behavior_Explode_351 DamageFormula.BaseValueScaleConstant {config:rocket_damage_scale}

                    #</Damage>

                #</Rocket Launchers>

            #</Turrets>

            #<Moonshot Attack>

                #<Overall Damage>

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_Explode_5 DamageFormula.BaseValueScaleConstant {config:moonshot_damage_scale_0}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_Explode_6 DamageFormula.BaseValueScaleConstant {config:moonshot_damage_scale_1}

                #</Overall Damage>

                #<Spawned Reinforcements>

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_1.PopulationFactoryBalancedAIPawn_0 PawnBalanceDefinition AIPawnBalanceDefinition'{config:moonshot_badass_pawn}'

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_20.PopulationFactoryPopulationDefinition_0 PopulationDef WillowPopulationDefinition'{config:moonshot_regular_pawn_1}'

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_21.PopulationFactoryPopulationDefinition_0 PopulationDef WillowPopulationDefinition'{config:moonshot_regular_pawn_0}'

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_22.PopulationFactoryPopulationDefinition_0 PopulationDef WillowPopulationDefinition'{config:moonshot_regular_pawn_2}'

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_23.PopulationFactoryPopulationDefinition_0 PopulationDef WillowPopulationDefinition'{config:moonshot_regular_pawn_4}'

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_24.PopulationFactoryPopulationDefinition_0 PopulationDef WillowPopulationDefinition'{config:moonshot_regular_pawn_3}'

                #</Spawned Reinforcements>

                #<Spawn Weights>

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0 BehaviorSequences[2].BehaviorData2[3].LinkedVariables.ArrayIndexAndLength 0

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0 BehaviorSequences[2].BehaviorData2[16].LinkedVariables.ArrayIndexAndLength 0

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_11 Conditions[0] {config:moonshot_regular_pawn_0_weight_0}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_11 Conditions[1] {config:moonshot_regular_pawn_1_weight_0}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_11 Conditions[2] {config:moonshot_regular_pawn_2_weight_0}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_11 Conditions[3] {config:moonshot_regular_pawn_3_weight_0}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_11 Conditions[4] {config:moonshot_regular_pawn_4_weight_0}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_12 Conditions[0] {config:moonshot_regular_pawn_0_weight_1}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_12 Conditions[1] {config:moonshot_regular_pawn_1_weight_1}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_12 Conditions[2] {config:moonshot_regular_pawn_2_weight_1}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_12 Conditions[3] {config:moonshot_regular_pawn_3_weight_1}

                    level Ma_FinalBoss_P set GD_Ma_Helios.Projectiles.Proj_MoonShotCannon:BehaviorProviderDefinition_0.Behavior_RandomBranch_12 Conditions[4] {config:moonshot_regular_pawn_4_weight_1}

                #</Spawn Weights>

            #</Moonshot Attack>

            #<Eye of Helios>

                #<Attack Delay>

                    # Increasing the delay here will also have the effect of shortening the laser beam by that much.
                    # I'd love to figure out how to inject this delay *before* the laser-charging animation comes
                    # on, but the BPDs for EOS are just hideous, and I found this first, and it works, so I'm just
                    # leaving it there.  :)  It's easy to extend the laser duration by adding a delay to COLD[205]
                    # but the eye closes according to its original schedule, and I hadn't found where that timing was.

                    level Ma_FinalBoss_P set GD_Ma_Helios.Character.AiDef_Ma_Helios:AIBehaviorProviderDefinition_0 BehaviorSequences[0].ConsolidatedOutputLinkData[203].ActivateDelay {config:eye_of_helios_delay}

                #</Attack Delay>

                #<Attack Damage + Radius>

                    # I actually don't intend on nerfing this too much; it should remain a very deadly attack

                    level Ma_FinalBoss_P set GD_Ma_ShadowTrapEye.Character.AIDef_EyeOfHelios:AIBehaviorProviderDefinition_0.Behavior_FireBeam_88 DamagePerSecondFormula.BaseValueScaleConstant {config:eye_of_helios_damage_scale}

                    level Ma_FinalBoss_P set GD_Ma_ShadowTrapEye.Character.AIDef_EyeOfHelios:AIBehaviorProviderDefinition_0.Behavior_FireBeam_88 RadiusToDoDamageAroundImpact.BaseValueConstant {config:eye_of_helios_damage_radius}

                #</Attack Damage + Radius>

            #</Eye of Helios>

        #</{config:label}>
        """.format(config=config))

###
### Close out the mod
###

mod_list.append('#</EOS>')
mod_list.append('#</{}>'.format(mod_name))

###
### Output to a file.
###

mp.human_str_to_blcm_filename("\n\n".join(mod_list), output_filename)
print('Wrote mod file to: {}'.format(output_filename))
