#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Loops through our FT-Explorer data to find unique/legendary weapons
# and generate a bunch of hotfixes which make them guaranteed to drop
# with Luneshine.  For most weapons, this is just disabling the "no
# luneshine" option (if we remove the option entirely, vanilla non-
# Luneshine'd guns loaded with this patch would be removed, but
# simply disabling it works fine).  A handful of other guns were
# missing a Luneshine accessory definition stanza entirely, so we add
# that in, for those.

# This requires my FT Explorer project from https://github.com/apocalyptech/ft-explorer
# In the end it's probably best to copy it in the base dir of that,
# and run it from there.

import re
import sys
from ftexplorer.data import Data

print('Loading weapon list')
weapons = [
    'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom',
    'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBreaker',
    'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Torgue_5_KerBoom',
    'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier',
    'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Jakobs_3_Wallop',
    'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail',
    'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_IceScream',
    'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful',
    'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_Ricochet',
    'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_ZX1',
    'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Old_Hyperion_5_Excalibastard',
    'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Tediore_5_Tesla',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Dahl_3_Firestarta',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_Blizzard',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_VibraPulse',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Egun',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_SavorySideSaber',
    'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Tediore_3_Vandergraffen',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_Thingy',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Cryophobia',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem',
    'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol',
    'GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Tediore_3_Rocketeer',
    'GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Zim',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Blowfly',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang',
    'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_88Fragnum',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Globber',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Smasher',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_CyberColt',
    'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe',
    'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent',
    'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch',
    'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire',
    'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MareksMouth',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch',
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Old_Hyperion_BlackSnake',
    'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun',
    'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall',
    'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker',
    'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Moonface',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_TooScoops',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Torguemada',
    'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Wombat',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Magma',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Razorback',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine',
    'GD_Cypressure_Weapons.A_Weapons_Unique.AR_Bandit_3_BossNova',
    'GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan',
    'GD_Cypressure_Weapons.A_Weapons_Unique.SG_Torgue_3_Landscaper2',
    'GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker',
    'GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade',
    'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard',
    'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_FusionBeam',
    'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_Thunderfire',
    'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Tediore_5_LaserDisker',
    'GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Jakobs_5_LuckCannon',
    'GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander',
    'GD_Ma_Weapons.A_Weapons_Legendary.RL_Tediore_5_KanedasLaser',
    'GD_Ma_Weapons.A_Weapons_Legendary.SG_Jakobs_5_Flayer',
    'GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode',
    'GD_Ma_Weapons.A_Weapons_Legendary.Sniper_Old_Hyperion_5_OmniCannon',
    'GD_Ma_Weapons.A_Weapons_Unique.Laser_Dahl_6_Glitch_HeartfullSplodger',
    'GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Enlightenment',
    'GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Minac',
    'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Bandit_3_PartyPopper',
    'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Maliwan_3_HardReboot',
    'GD_Ma_Weapons.A_Weapons_Unique.SMG_Bandit_6_Glitch_CutieKiller',
    'GD_Petunia_Weapons.AssaultRifles.AR_Bandit_3_CryBaby',
    'GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace',
    'GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr',
    'GD_Petunia_Weapons.SMGs.SMG_Tediore_3_Boxxy',
    'GD_Petunia_Weapons.Shotguns.SG_Tediore_3_PartyLine',
    'GD_Petunia_Weapons.Snipers.Sniper_Jakobs_3_Plunkett',
    'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun',
    'GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Fridgia',
    'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Frostfire',
    'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge',
    ]

# Some weapons get a pass because they have custom Luneshine attachments
# (or, in some cases, are glitch guns)
weap_exclude = set([
    'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MareksMouth',
    'GD_Ma_Weapons.A_Weapons_Unique.Laser_Dahl_6_Glitch_HeartfullSplodger',
    'GD_Ma_Weapons.A_Weapons_Unique.SMG_Bandit_6_Glitch_CutieKiller',
    'GD_Petunia_Weapons.AssaultRifles.AR_Bandit_3_CryBaby',
    'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail',
    ])

print('Loading TPS index')
data = Data('TPS')

print('Checking data')
hotfix_idx = 0
create_luneshine_attachments = []
for weapon_obj in weapons:

    if weapon_obj in weap_exclude:
        continue

    node = data.get_node_by_full_object(weapon_obj)
    struct = node.get_structure()
    if 'RuntimePartListCollection' in struct:
        (junk1, runtime_parts, junk2) = struct['RuntimePartListCollection'].split("'", 2)
    else:
        raise Exception('No runtime part list found for {}'.format(weapon_obj))

    if runtime_parts:
        partnode = data.get_node_by_full_object(runtime_parts)
        struct = partnode.get_structure()
        acc2_parts = struct['Accessory2PartData']['WeightedParts']
        if 'Launchers' in weapon_obj or 'KanedasLaser' in weapon_obj:
            proper_num = 8
        else:
            proper_num = 9
        do_full_create = False
        if len(acc2_parts) == proper_num:
            found_none = False
            found_disabled = False
            for idx, part in enumerate(acc2_parts):
                if part['Part'] == "WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_None'":
                    none_idx = idx
                    found_none = True
                if part['bDisabled'] == 'True':
                    found_disabled = True

            if found_disabled:
                #print('WARNING: {} - found disabled luneshine accessories'.format(weapon_obj))
                #print('')
                do_full_create = True
            elif found_none:
                print('{{hotfixes:guaranteed_luneshine_{}}}'.format(hotfix_idx))
                print('')
                print("""hfs.add_level_hotfix('guaranteed_luneshine_{hotfix_idx}',
    'GuaranteedLuneshine',
    ',{runtime_parts},Accessory2PartData.WeightedParts[{none_idx}].bDisabled,,True')""".format(
                    hotfix_idx=hotfix_idx,
                    runtime_parts=runtime_parts,
                    none_idx=none_idx), file=sys.stderr)
                hotfix_idx += 1
            else:
                print('{} - No "None" attachment found'.format(weapon_obj))
                print('')

        else:
            # We know from previous runs that anything in here just needs its
            # entire attach2 structure set, so I won't bother to try and be
            # clever about it.
            do_full_create = True

        if do_full_create:

            #print('{} - {} acc2 parts:'.format(weapon_obj, len(acc2_parts)))
            #for part in acc2_parts:
            #    print(' * {}'.format(part['Part']))
            #print('')

            create_luneshine_attachments.append(runtime_parts)

    else:
        print('WARNING: No runtime parts found for {}'.format(weapon_obj))
        print('')

print('for idx, partlist in enumerate([', file=sys.stderr)
for idx, part in enumerate(create_luneshine_attachments):
    print('{{hotfixes:luneshine_override_{}}}'.format(idx))
    print('')
    print("        '{}',".format(part), file=sys.stderr)
print('        ]):', file=sys.stderr)
print("    hfs.add_level_hotfix('luneshine_override_{}'.format(idx),", file=sys.stderr)
print("        'LuneshineOverride',", file=sys.stderr)
print('        """,{partlist},Accessory2PartData,,', file=sys.stderr)
print("""        (
            bEnabled=True,
            WeightedParts=(
                (
                    bDisabled=True,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_None',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_FastLearner',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_HardenUp',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Boominator',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Safeguard',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Oxygenator',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_PiercingRounds',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Punisher',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                ),
                (
                    bDisabled=False,
                    Part=WeaponPartDefinition'GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Serenity',
                    Manufacturers=(
                        (
                            Manufacturer=None,
                            DefaultWeightIndex=1
                        )
                    ),
                    MinGameStageIndex=0,
                    MaxGameStageIndex=1,
                    DefaultWeightIndex=1
                )
            )
        )""", file=sys.stderr)
print('        """.format(partlist))', file=sys.stderr)
print('', file=sys.stderr)
