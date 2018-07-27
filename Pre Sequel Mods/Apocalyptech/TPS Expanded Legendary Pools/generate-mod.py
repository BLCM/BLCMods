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

mod_name = 'TPS Expanded Legendary Pools'
mod_version = '1.0.0'
input_filename = 'input-file-mod.txt'
output_filename = '{}.blcm'.format(mod_name)

###
### Construct the mod!
###

# Legendary Pool management
unique_hotfixes = []
uniqueglitch_hotfixes = []
for (guntype, legendaries, uniques, uniqueglitches, num_undesirables) in [
        (
            'AssaultRifles',
            [
                # Regular Legendaries
                'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Torgue_5_KerBoom',
                'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier',
                'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom',
                'gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBreaker',
                'GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade',
            ],
            [
                # Uniques
                'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Jakobs_3_Wallop',
                'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail',
                'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_IceScream',
                'gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful',
                'GD_Cypressure_Weapons.A_Weapons_Unique.AR_Bandit_3_BossNova',
                'GD_Petunia_Weapons.AssaultRifles.AR_Bandit_3_CryBaby',
            ],
            [
                # Unique Glitches
            ],
            0,
        ),
        (
            'Launchers',
            [
                # Regular Legendaries
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom',
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Cryophobia',
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem',
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol',
                'GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_Thingy',
                'GD_Ma_Weapons.A_Weapons_Legendary.RL_Tediore_5_KanedasLaser',
                'GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace',
            ],
            [
                # Uniques
                'GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Tediore_3_Rocketeer',
                'GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer',
            ],
            [
                # Unique Glitches
            ],
            0,
        ),
        (
            'Pistols',
            [
                # Regular Legendaries
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Zim',
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang',
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Blowfly',
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_88Fragnum',
                'GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie',
                'GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun',
                'GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Jakobs_5_LuckCannon',
                'GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander',
            ],
            [
                # Uniques
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Globber',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Smasher',
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_CyberColt',
                'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Bandit_3_PartyPopper',
                'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Maliwan_3_HardReboot',
                'GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr',
            ],
            [
                # Unique Glitches
            ],
            1,
        ),
        (
            'Shotguns',
            [
                # Regular Legendaries
                'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun',
                'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker',
                'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker',
                'GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall',
                'GD_Ma_Weapons.A_Weapons_Legendary.SG_Jakobs_5_Flayer',
            ],
            [
                # Uniques
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Moonface',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_TooScoops',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Torguemada',
                'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Wombat',
                'GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan',
                'GD_Cypressure_Weapons.A_Weapons_Unique.SG_Torgue_3_Landscaper2',
                'GD_Petunia_Weapons.Shotguns.SG_Tediore_3_PartyLine',
            ],
            [
                # Unique Glitches
            ],
            0,
        ),
        (
            'SMG',
            [
                # Regular Legendaries
                'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF',
                'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire',
                'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent',
                'GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch',
                'GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode',
            ],
            [
                # Uniques
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MareksMouth',
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder',
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch',
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch',
                'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Old_Hyperion_BlackSnake',
                'GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker',
                'GD_Petunia_Weapons.SMGs.SMG_Tediore_3_Boxxy',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Fridgia',
                'GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Frostfire',
            ],
            [
                # Unique Glitches
                'GD_Ma_Weapons.A_Weapons_Unique.SMG_Bandit_6_Glitch_CutieKiller',
            ],
            0,
        ),
        (
            'SniperRifles',
            [
                # Regular Legendaries
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Magma',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader',
                'GD_Ma_Weapons.A_Weapons_Legendary.Sniper_Old_Hyperion_5_OmniCannon',
            ],
            [
                # Uniques
                'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Razorback',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie',
                'GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine',
                'GD_Petunia_Weapons.Snipers.Sniper_Jakobs_3_Plunkett',
                'GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge',
            ],
            [
                # Unique Glitches
            ],
            0,
        ),
        (
            'Lasers',
            [
                # Regular Legendaries
                'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_ZX1',
                'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Tediore_5_Tesla',
                'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_Ricochet',
                'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Old_Hyperion_5_Excalibastard',
                'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard',
                'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_FusionBeam',
                'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_Thunderfire',
                'GD_Ma_Weapons.A_Weapons_Legendary.Laser_Tediore_5_LaserDisker',
            ],
            [
                # Uniques
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Dahl_3_Firestarta',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_Blizzard',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_VibraPulse',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Egun',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_SavorySideSaber',
                'GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Tediore_3_Vandergraffen',
                'GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Enlightenment',
                'GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Minac',
            ],
            [
                # Unique Glitches
                'GD_Ma_Weapons.A_Weapons_Unique.Laser_Dahl_6_Glitch_HeartfullSplodger',
            ],
            0,
        ),
        ]:

    # First set up a hotfix for the base pool initialization
    initial_pool = []
    for legendary in legendaries:
        initial_pool.append((legendary, 1, 'WeaponBalanceDefinition'))
    for i in range(len(uniques) + len(uniqueglitches) + num_undesirables):
        initial_pool.append((None, 0))
    mp.register_str('weapon_pool_clear_{}'.format(guntype.lower()),
        'level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems {}'.format(
            guntype,
            mp.get_balanced_items(initial_pool),
            ))  

    # Hotfixes to add uniques
    for (idx, unique) in enumerate(uniques):
        unique_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + idx,
                unique
                ))

    # Hotfixes to add unique glitches
    for (idx, uniqueglitch) in enumerate(uniqueglitches):
        uniqueglitch_hotfixes.append(
            """level None set GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary BalancedItems[{}]
            (
                ItmPoolDefinition=None,
                InvBalanceDefinition=WeaponBalanceDefinition'{}',
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(
                guntype,
                len(legendaries) + len(uniques) + idx,
                uniqueglitch
                ))

mp.register_str('legendary_unique_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in unique_hotfixes]
    ))

mp.register_str('legendary_uniqueglitch_adds', "\n\n".join(
        ['{}{}'.format(' '*(4*4), hotfix) for hotfix in uniqueglitch_hotfixes]
    ))


# Legendary shield/grenade pool configuration.  Doing this a bit differently since there's
# not nearly as many shields/grenades to handle as weapons.

items = {
    'shield': {
        'GD_Itempools.ShieldPools.Pool_Shields_Booster_06_Legendary': [
            ('asteroidbelt', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_AsteroidBelt', 1),
            ('slammer', 2, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_MoxxisSlammer', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Chimera_06_Legendary': [
            ('haymaker', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_Haymaker', 1),
            ('m0rq', 2, 'GD_Ma_Shields.A_Item_Legendary.ItemGrade_Gear_Shield_Chimera_05_M0RQ', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Juggernaut_06_Legendary': [
            ('shieldofages', 1, 'GD_Ma_Shields.A_Item_Unique.ItemGrade_Gear_Shield_Juggernaut_03_ShieldOfAges', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_NovaShields_All_06_Legendary': [
            ('sunshine', 3, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Starburst', 1),
            ('rapidrelease', 4, 'GD_Cork_Shields.A_Item_Custom.ItemGrade_Shield_RapidRelease', 1),
            ],
        'GD_Itempools.ShieldPools.Pool_Shields_Standard_06_Legendary': [
            ('naught', 1, 'GD_Ma_Shields.A_Item_Unique.ItemGrade_Gear_Shield_Naught', 1),
            ('cracked_sash', 2, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_CrackedSash', 1),
            ],
        },
    'grenade': {
        'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary': [
            ('baby_boomer', 11, 'GD_GrenadeMods.A_Item_Custom.GM_BabyBoomer', 1),
            ('data_scrubber', 12, 'GD_Ma_GrenadeMods.A_Item_Unique.GM_DataScrubber', 1),
            ('kiss_of_death', 13, 'GD_Cork_GrenadeMods.A_Item_Custom.GM_KissOfDeath', 1),
            ('snowball', 14, 'GD_GrenadeMods.A_Item_Custom.GM_Snowball', 1),
            ('sky_rocket', 15, 'GD_GrenadeMods.A_Item_Custom.GM_SkyRocket', 1),
            ('monster_trap', 16, 'GD_Cork_GrenadeMods.A_Item_Custom.GM_MonsterTrap', 1),
            ],
        },
    'ozkit': {
        'GD_Itempools.MoonItemPools.Pool_MoonItem_06_Legendary': [
            ('cathartic', 5, 'GD_MoonItems.A_Item_Unique.A_Poopdeck', 1),
            ('freedom', 6, 'GD_MoonItems.A_Item_Unique.A_Freedom', 1),
            ('invigoration', 7, 'GD_MoonItems.A_Item_Unique.A_Invigoration', 1),
            ('systems_purge', 8, 'GD_MoonItems.A_Item_Unique.A_SystemsPurge', 1),
            ('perdy_lights', 9, 'GD_Pet_MoonItems.A_Item_Unique.A_AntiAir_PerdyLights', 1),
            ('springs', 10, 'GD_MoonItems.A_Item_Unique.A_Springs', 1),
            ],
        },
    'pistol': {
        'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary': [
            ('probe', 17, 'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe', 1),
            ],
        },
    }
for (itemtype, itemdict) in items.items():
    for (pool, itemlist) in itemdict.items():
        for (label, index, itemname, scale) in itemlist:
            if itemtype == 'pistol':
                invbalance = 'WeaponBalanceDefinition'
            else:
                invbalance = 'InventoryBalanceDefinition'
            mp.set_bi_item_pool('{}_{}'.format(itemtype, label),
                pool,
                index,
                itemname,
                invbalance=invbalance,
                scale=scale,
                )

###
### Everything below this point is constructing the actual patch file
###

# Write out the file
with open(input_filename, 'r') as df:
    mod_str = df.read().format(
        mod_name=mod_name,
        mod_version=mod_version,
        mp=mp,
        )
mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod to: {}'.format(output_filename))
