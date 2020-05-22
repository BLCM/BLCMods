#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Original section which was buffing up FFYL anim speed.  In the end I felt it wasn't really
# appropriate for the mod, so out it goes.

ffyl_in_anim_speed_scale = 2
ffyl_res_anim_speed_scale = 5

# FFYL Animations
lines.append("""#<Fight For Your Life Animations>

    # This is a direct copy from an unreleased mod by Gronp which speeds up the FFYL
    # animation speed (going into FFYL, and being resurrected after failing to get out).
    # Many thanks for the donation!  Entering FFYL is speeded up by {ffyl_in_anim_speed_scale}x, whereas
    # resurrection is speeded up by {ffyl_res_anim_speed_scale}x.

    #<Faster Downed Animations>

        # Yes, Psycho and Mechromancer *do* use the Assassin animation for this

        demand GD_Siren_Streaming set GD_Siren_Streaming.Anims.Anim_Injured PlayRate {ffyl_in_anim_speed_scale}

        demand GD_Mercenary_Streaming set GD_Mercenary_Streaming.Anims.Anim_Injured PlayRate {ffyl_in_anim_speed_scale}

        demand GD_Lilac_Psycho_Streaming set GD_Assassin_Streaming.Anims.Anim_Injured PlayRate {ffyl_in_anim_speed_scale}

        demand GD_Tulip_Mechro_Streaming set GD_Assassin_Streaming.Anims.Anim_Injured PlayRate {ffyl_in_anim_speed_scale}

        demand GD_Soldier_Streaming set GD_Soldier_Streaming.Anims.Anim_Injured PlayRate {ffyl_in_anim_speed_scale}

        demand GD_Assassin_Streaming set GD_Assassin_Streaming.Anims.Anim_Injured PlayRate {ffyl_in_anim_speed_scale}

    #</Faster Downed Animations>

    #<Screen Effect Changes>

        # This just removes the bright white flash when entering FFYL - technically it doesn't
        # actually change any timing really.

        level None set FX_INT_Screen.Particles.Part_DownState_Screen:ParticleModuleColorOverLife_78 ColorOverLife.LookupTable[1] 1

        level None set FX_INT_Screen.Particles.Part_DownState_Screen:ParticleModuleColorOverLife_78 ColorOverLife.LookupTable[2] 1

        level None set FX_INT_Screen.Particles.Part_DownState_Screen:ParticleModuleColorOverLife_78 ColorOverLife.LookupTable[3] 1

        level None set FX_INT_Screen.Particles.Part_DownState_Screen:ParticleModuleColorOverLife_78 ColorOverLife.LookupTable[4] 1

    #</Screen Effect Changes>

    #<Faster Respawn Animation>

        # This is stuff that triggers if you fail to get out of FFYL and end up at a New-U instead

        set GD_Globals.General.Globals RespawnCameraLerpTime 0.100000

        set GD_Globals.General.Globals RespawnDelayBeforeCoordinatedEffect 0.100000

        set GD_Globals.General.Globals InjuredDeadDelayBetweenDeathAnimAndDigistruct 0.100000

        set GD_CoordinatedEffects.Player.Player_Digistruct EffectDuration 2.000000

        level None set GD_PlayerShared.Anims.Player_ReRez PlayRate {ffyl_res_anim_speed_scale}

        level None set GD_CoordinatedEffects.Player.Player_ReRez EffectDuration {ffyl_rerez_duration}

    #</Faster Respawn Animation>

#</Fight For Your Life Animations>
""".format(
        ffyl_in_anim_speed_scale=ffyl_in_anim_speed_scale,
        ffyl_res_anim_speed_scale=ffyl_res_anim_speed_scale,
        ffyl_rerez_duration=5/ffyl_res_anim_speed_scale,
        ))
