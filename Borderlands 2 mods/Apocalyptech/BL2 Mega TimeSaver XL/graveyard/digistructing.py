#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Original section to buff up Digistructing Enemies.  Not ready for prime time yet;
# there's a few cases (that I know of, presumably there are more) which need attention:
#   1) Enemies that have just been constructed by a Constructor just kind of stand
#      there for a few seconds before becoming active and vulnerable
#   2) The set of four turrets near the end of Digi Peak seem to do the same
#
# Things to make sure to test:
#  1) Dark Web and Dark Web Minions
#  2) Control Core Angel
#  3) Area in Helios Fallen
#  4) Highlands Overlook fast travel setup
#  Plenty of other places too, I'm sure

digi_scale = 3

# Digistructing
digi_coordinated_effect_std = round(7/digi_scale, 6)
digi_coordinated_effect_topdown = round(4/digi_scale, 6)
digi_coordinated_effect_turret = round(8.7/digi_scale, 6)
digi_coordinated_effect_clone = round(3.5/digi_scale, 6)
digi_part_effect_0_2 = round(0.2/digi_scale/2, 6)
digi_part_effect_5 = round(5/digi_scale/2, 6)
digi_part_effect_7 = round(7/digi_scale/2, 6)
digi_crate_delay = round(6/digi_scale, 6)
digi_playrate_0_1 = round(0.1*digi_scale, 6)
digi_playrate_0_15 = round(0.15*digi_scale, 6)
digi_playrate_0_22 = round(0.22*digi_scale, 6)
digi_playrate_0_23 = round(0.23*digi_scale, 6)
digi_playrate_0_3 = round(0.3*digi_scale, 6)
digi_playrate_0_35 = round(0.35*digi_scale, 6)
digi_playrate_0_4 = round(0.4*digi_scale, 6)
digi_playrate_0_45 = round(0.45*digi_scale, 6)
digi_playrate_0_5 = round(0.5*digi_scale, 6)
digi_playrate_1 = round(1*digi_scale, 6)
lines.append("""#<Digistructing>

        # Sets the speed for various digistructing things throughout the game,
        # primarily enemies like Loaders (but also all the Digistruct Peak enemies).
        # These are getting a {digi_scale}x speedup.  Note that the digistructed ammo
        # boxes you see in many boss arenas are sped up in the "Containers" section,
        # not here.
        #
        # Note that the Loader/Turret definitions in here will likely buff
        # Constructors a bit, since you won't have as much time to interrupt their
        # digistructing process.  This will also probably buff Repair Surveyors.
        #
        # This section is based on Gronp's "Faster Enemy Spawn Animations in Digi-Peak,"
        # which was graciously donated to this mod -- it's been expanded a bit to
        # include all other digistructing enemies as well.  Many thanks!
        # https://www.nexusmods.com/borderlands2/mods/176

        #<General Effect Durations>

            level None set GD_CoordinatedEffects.Digistruct_Standard EffectDuration {digi_coordinated_effect_std}

            level None set GD_CoordinatedEffects.Digistruct_TopDown EffectDuration {digi_coordinated_effect_topdown}

            level None set GD_CoordinatedEffects.Digistruct_Turret EffectDuration {digi_coordinated_effect_turret}

            level None set GD_CoordinatedEffects.Digistruct_Clone EffectDuration {digi_coordinated_effect_clone}

        #</General Effect Durations>

        #<Dark Web>

            # The digistructy Spiderants (both minions and the main miniboss) found during Claptocurrency, in Dahl Abandon

            level OldDust_P set GD_Anemone_A_Queen_Digi.Den.PopPointDef_GroundEmergeDigi_Den:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_4}

            level OldDust_P set GD_Anemone_TheDarkWeb.Den.PopPointDef_GroundEmergeDigi_Den:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_4}

            # Fixing the timing on some other effects which are in play here (and actually removing one effect from the spawn)

            level OldDust_P set GD_Anemone_TheDarkWeb.Den.PopPointDef_GroundEmergeDigi_Den:SpecialMove_Spawned_0.BehaviorProviderDefinition_6.Behavior_SpawnParticleSystem_0 ParticleEffect None

            level OldDust_P set GD_Anemone_A_Queen_Digi.Den.PopPointDef_GroundEmergeDigi_Den:SpecialMove_Spawned_0.BehaviorProviderDefinition_6.Behavior_SpawnParticleSystem_0 ParticleEffect None

            level OldDust_P set FX_CREA_Constructor.Particles.Part_ConstructorEyeBeamConstruction:ParticleModuleLifetime_0 Lifetime.LookupTable (
                {digi_part_effect_7},
                {digi_part_effect_7},
                {digi_part_effect_7},
                {digi_part_effect_7}
            )

            level OldDust_P set FX_CREA_Constructor.Particles.Part_ConstructorEyeBeamConstruction:ParticleModuleLifetime_8 Lifetime.LookupTable (
                {digi_part_effect_0_2},
                {digi_part_effect_0_2},
                {digi_part_effect_0_2},
                {digi_part_effect_0_2}
            )

            level OldDust_P set FX_CREA_Constructor.Particles.Part_ConstructorEyeBeamConstruction:ParticleModuleLifetime_9 Lifetime.LookupTable (
                {digi_part_effect_5},
                {digi_part_effect_5},
                {digi_part_effect_5},
                {digi_part_effect_5}
            )

        #</Dark Web Minions>

        #<Digistruct Peak Enemies>

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_22}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_2 PlayRate {digi_playrate_0_3}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_3 PlayRate {digi_playrate_0_45}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_4 PlayRate {digi_playrate_0_45}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_5 PlayRate {digi_playrate_0_1}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_6 PlayRate {digi_playrate_0_35}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_7 PlayRate {digi_playrate_0_5}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_8 PlayRate {digi_playrate_0_5}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_9 PlayRate {digi_playrate_0_5}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_10 PlayRate {digi_playrate_0_4}

            level TestingZone_P set GD_DigiCreaturesShared.Den.PopPointDef_DigiCreature_StandStill:SpecialMove_Spawned_13 PlayRate {digi_playrate_0_15}

        #</Digistruct Peak Enemies>

        #<Digistruct Peak Loot Crates>

            # Note that this section only affects the delay between starting the digistruct
            # animation and kicking off the auto-open.  The auto-open speed itself is set
            # in the "Conatiners" section.

            level TestingZone_P set GD_Lobelia_DahlDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1 BehaviorSequences[0].BehaviorData2[14].LinkedVariables.ArrayIndexAndLength 0

            level TestingZone_P set GD_Lobelia_DahlDigi.InteractiveObjectsUnique.InteractiveObject_DahlEpicCrate_Digi:BehaviorProviderDefinition_1.Behavior_Delay_279 Delay {digi_crate_delay}

        #</Digistruct Peak Loot Crates>

        #<Loaders>

            # These should take care of nearly all loader digistructs

            level None set GD_Loadershared.Den.PopPointDef_Digistruct:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_3}

            level None set GD_Loadershared.Den.PopPointDef_DigistructStanchion:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_3}

            level None set GD_Loadershared.Den.PopPointDef_DigistructVOGChamber:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_3}
            
            level HyperionCity_P set GD_Loadershared.Den.PopPointDef_DigistructOpportunity:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_3}

        #</Loaders>

        #<Surveyors>

            # Might be that I should also/instead do SpecialMove_Spawned_1 on these

            level None set GD_ProbeShared.Den.PopPointDef_ProbeShared_Digistruct:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_23}

            level None set GD_ProbeShared.Den.PopPointDef_ProbeShared_DigistructStation:SpecialMove_Spawned_0 PlayRate {digi_playrate_0_23}

        #</Surveyors>

        #<Turrets>

            level None set GD_Hyperion_AutoCannon.Den.PopPointDef_DigistructHexPad:SpecialMove_Spawned_0 PlayRate {digi_playrate_1}

            level None set GD_Hyperion_AutoCannon.Den.PopPointDef_Digistruct:SpecialMove_Spawned_0 PlayRate {digi_playrate_1}

        #</Turrets>

    #</Digistructing>
""".format(
    digi_scale=digi_scale,
    digi_coordinated_effect_std=digi_coordinated_effect_std,
    digi_coordinated_effect_topdown=digi_coordinated_effect_topdown,
    digi_coordinated_effect_turret=digi_coordinated_effect_turret,
    digi_coordinated_effect_clone=digi_coordinated_effect_clone,
    digi_part_effect_0_2=digi_part_effect_0_2,
    digi_part_effect_5=digi_part_effect_5,
    digi_part_effect_7=digi_part_effect_7,
    digi_crate_delay=digi_crate_delay,
    digi_playrate_0_1=digi_playrate_0_1,
    digi_playrate_0_15=digi_playrate_0_15,
    digi_playrate_0_22=digi_playrate_0_22,
    digi_playrate_0_23=digi_playrate_0_23,
    digi_playrate_0_3=digi_playrate_0_3,
    digi_playrate_0_35=digi_playrate_0_35,
    digi_playrate_0_4=digi_playrate_0_4,
    digi_playrate_0_45=digi_playrate_0_45,
    digi_playrate_0_5=digi_playrate_0_5,
    digi_playrate_1=digi_playrate_1,
    ))
