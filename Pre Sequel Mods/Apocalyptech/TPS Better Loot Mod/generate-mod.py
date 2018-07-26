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

# Python script to generate my TPS Better Loot Mod.  All the drop
# weights and stuff can be controlled by all the variables at the
# top of the file.  Generates a human-readable multiline file which
# must be converted using conv_to_mod.py in order to be loaded by
# Borderlands / FilterTool.

import sys
import math

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

mod_name = 'TPS Better Loot Mod'
mod_version = '1.1.0-prerelease'
input_filename = 'input-file-mod.txt'
output_filename = '{}.blcm'.format(mod_name)

###
### Variables which control drop rates and stuff like that
###

class Config(object):
    """
    Base class which allows us to use constants as format strings
    """

    def set_balanced_pct_reports(self, basename, weights, fixedlen=False):
        """
        Given a list of numerical `weights`, sets some attributes in our
        object based on `basename` which describe the percent chances
        of drops.  Var names will be `basename_pct_idx`, where `idx`
        relates to the position of the weight in question in `weights`.
        If `fixedlen` is true, the percentages will be stored as
        right-aligned strings, otherwise it should be numbers.
        """
        total = sum(weights)
        for (idx, weight) in enumerate(weights):
            varname = '{}_pct_{}'.format(basename, idx)
            pct = weight/total*100
            if pct >= 1:
                pct = round(pct)
            elif pct != 0:
                pct = round(pct, 2)
                if str(pct) == '1.0':
                    pct = 1
            if fixedlen:
                if pct == 0 or pct >= 1:
                    setattr(self, varname, '{:4d}'.format(round(pct)))
                else:
                    setattr(self, varname, '{:4.2f}'.format(pct))
            else:
                setattr(self, varname, pct)

    def set_badass_qty_reports(self, basename, quantities):
        """
        This is only really used when reporting likely numbers of drops from
        the various badass enemy definitions.  Will always set fixed-width
        strings.  Will set the vars `badass_basename_idx`.
        """
        for (idx, quantity) in enumerate(quantities):
            varname = 'badass_{}_{}'.format(basename, idx)
            if int(quantity) == quantity:
                setattr(self, varname, '{:4d}'.format(int(quantity)))
            elif round(quantity,1) == quantity:
                setattr(self, varname, '{:4.1f}'.format(quantity))
            else:
                setattr(self, varname, '{:4.2f}'.format(quantity))

    def __format__(self, formatstr):
        """
        A bit of magic so that we can use our values in format strings
        """
        attr = getattr(self, formatstr)
        if type(attr) == str:
            return attr
        elif type(attr) == int or type(attr) == float:
            return str(attr)
        else:
            return attr()

class ConfigBase(Config):
    """
    Class to hold all our weights, and other vars which alter the probabilities of
    various things dropping.  Derive from this class to actually define the
    values.
    """

    # 2x chance of both kinds of moonstone
    moonstone_drop = 0.1          # Stock: 0.050000
    moonstone_cluster_drop = 0.05 # Stock: 0.025000

    # Gun Type drop weights.  Note that because these values are going into
    # our hotfix object, these variables *cannot* be successfully overridden
    # in an extending class.  These probabilities aren't actually too much
    # different than the stock ones.
    drop_prob_pistol = 100
    drop_prob_ar = 100
    drop_prob_smg = 100
    drop_prob_shotgun = 100
    drop_prob_sniper = 80
    drop_prob_launcher = 40
    drop_prob_laser = 80

    def full_profile_name(self):
        if self.profile_name_orig:
            return '{} Quality (formerly "{}")'.format(self.profile_name, self.profile_name_orig)
        else:
            return '{} Quality'.format(self.profile_name)

###
### Config classes which define the actual contstants that we use
### for things like drop weights, etc.
###

class ConfigExcellent(ConfigBase):
    """
    This is our default config, which I personally find quite pleasant.
    Many folks will consider this a bit too OP/Extreme.
    """

    profile_name = 'Excellent'
    profile_name_orig = 'Lootsplosion'
    profile_desc = 'Original "Lootsplosion" presets.  This is the version I prefer.'

    # Custom weapon drop scaling
    weapon_base_common = 8
    weapon_base_uncommon = 85
    weapon_base_rare = 65
    weapon_base_veryrare = 50
    weapon_base_glitch = 8
    weapon_base_legendary = 2

    # Custom weapon drop scaling for Claptastic Voyage
    weapon_clap_base_common = 8
    weapon_clap_base_uncommon = 85
    weapon_clap_base_rare = 65
    weapon_clap_base_veryrare = 50
    weapon_clap_base_glitch = 16
    weapon_clap_base_legendary = 3

    # Custom ozkit drop scaling (identical to weapons)
    ozkit_base_common = weapon_base_common
    ozkit_base_uncommon = weapon_base_uncommon
    ozkit_base_rare = weapon_base_rare
    ozkit_base_veryrare = weapon_base_veryrare
    ozkit_base_legendary = weapon_base_legendary

    # Custom COM drop scaling (identical to weapons, apart from buffing
    # legendary rates a bit)
    com_base_common = weapon_base_common
    com_base_uncommon = weapon_base_uncommon
    com_base_rare = weapon_base_rare
    com_base_veryrare = weapon_base_veryrare
    com_base_legendary = 5

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

    # Drop rates for "regular" treasure chests
    treasure_base_common = 0
    treasure_base_uncommon = 0
    treasure_base_rare = 30
    treasure_base_veryrare = 60
    treasure_base_glitch = 10
    treasure_base_legendary = 4

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = 0
    epic_base_rare = 0
    epic_base_veryrare = 1.4
    epic_base_glitch = .6
    epic_base_legendary = 0.2
    epic_base_legendary_dbl = 0.4

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = 0
    epic_glitch_base_rare = 0
    epic_glitch_base_veryrare = 0.9
    epic_glitch_base_glitch = 1.1
    epic_glitch_base_legendary_dbl = 0.5

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.4
    badass_pool_glitch = 0.3
    badass_pool_epicchest = 0.1

    # Claptastic Voyage Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_clap_veryrare = 0.2
    badass_pool_clap_glitch = 0.5
    badass_pool_clap_epicchest = 0.1

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 1
    super_badass_pool_veryrare = 1
    super_badass_pool_glitch = 1
    super_badass_pool_legendary = 1
    super_badass_pool_epicchest = 1

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 1
    ultimate_badass_pool_veryrare_2 = 0.5
    ultimate_badass_pool_glitch_1 = 1
    ultimate_badass_pool_glitch_2 = 0.5
    ultimate_badass_pool_legendary_1 = 1
    ultimate_badass_pool_legendary_2 = 0.5
    ultimate_badass_pool_legendary_3 = 0.25
    ultimate_badass_pool_epicchest_1 = 1
    ultimate_badass_pool_epicchest_2 = 0.5
    ultimate_badass_pool_epicchest_3 = 0.5

    # A few tweaks to the ultimate badass pool for Claptastic Voyage (the
    # legendary + epic chest drops are untouched)
    ultimate_badass_pool_clap_veryrare_1 = 1
    ultimate_badass_pool_clap_veryrare_2 = 0.2
    ultimate_badass_pool_clap_glitch_1 = 1
    ultimate_badass_pool_clap_glitch_2 = 0.8

class ConfigGood(ConfigBase):
    """
    Alternate config which has slightly-more-reasonable drop rates for stuff
    like legendaries.  Unsurprisingly, most folks find my default values a
    bit excessive.
    """

    profile_name = 'Good'
    profile_name_orig = 'Reasonable'
    profile_desc = 'Original "Reasonable" presets.  Attempts to be somewhat restrained.'

    # Weapon drops
    weapon_base_common = 32.75
    weapon_base_uncommon = 35
    weapon_base_rare = 25
    weapon_base_veryrare = 5
    weapon_base_glitch = 2
    weapon_base_legendary = 0.25

    # Custom weapon drop scaling for Claptastic Voyage
    weapon_clap_base_common = 32.75
    weapon_clap_base_uncommon = 35
    weapon_clap_base_rare = 25
    weapon_clap_base_veryrare = 4
    weapon_clap_base_glitch = 4
    weapon_clap_base_legendary = 0.25

    # Custom ozkit drop scaling (identical to weapons)
    ozkit_base_common = weapon_base_common
    ozkit_base_uncommon = weapon_base_uncommon
    ozkit_base_rare = weapon_base_rare
    ozkit_base_veryrare = weapon_base_veryrare
    ozkit_base_legendary = weapon_base_legendary

    # Class mods (identical to weapons)
    com_base_common = weapon_base_common
    com_base_uncommon = weapon_base_uncommon
    com_base_rare = weapon_base_rare
    com_base_veryrare = weapon_base_veryrare
    com_base_legendary = weapon_base_legendary

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

    # Boss drop rates
    boss_drop_uniques = 0.5
    boss_drop_rares = 0.25
    holodome_drop_uniques = 0.1

    # Drop rates for "regular" treasure chests
    treasure_base_common = 32.5
    treasure_base_uncommon = 40
    treasure_base_rare = 20
    treasure_base_veryrare = 5
    treasure_base_glitch = 3
    treasure_base_legendary = 0.5

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = 25
    epic_base_rare = 49
    epic_base_veryrare = 20
    epic_base_glitch = 5
    epic_base_legendary = 1
    epic_base_legendary_dbl = 2

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = 25
    epic_glitch_base_rare = 49
    epic_glitch_base_veryrare = 10
    epic_glitch_base_glitch = 15
    epic_glitch_base_legendary_dbl = 2

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = 0.2
    badass_pool_glitch = 0.15
    badass_pool_epicchest = 0.1

    # Claptastic Voyage Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_clap_veryrare = 0.1
    badass_pool_clap_glitch = 0.25
    badass_pool_clap_epicchest = 0.1

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = 1
    super_badass_pool_veryrare = 0.4
    super_badass_pool_glitch = 0.15
    super_badass_pool_legendary = .03
    super_badass_pool_epicchest = 1

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = 1
    ultimate_badass_pool_veryrare_2 = 0
    ultimate_badass_pool_glitch_1 = 0.4
    ultimate_badass_pool_glitch_2 = 0
    ultimate_badass_pool_legendary_1 = 0.08
    ultimate_badass_pool_legendary_2 = 0
    ultimate_badass_pool_legendary_3 = 0
    ultimate_badass_pool_epicchest_1 = 1
    ultimate_badass_pool_epicchest_2 = 1
    ultimate_badass_pool_epicchest_3 = 1

    # A few tweaks to the ultimate badass pool for Claptastic Voyage (the
    # legendary + epic chest drops are untouched)
    ultimate_badass_pool_clap_veryrare_1 = 0.4
    ultimate_badass_pool_clap_veryrare_2 = 0
    ultimate_badass_pool_clap_glitch_1 = 1
    ultimate_badass_pool_clap_glitch_2 = 0

# The profiles we'll generate
profiles = [
    ConfigExcellent(),
    ConfigGood(),
    ]

###
### Hotfixes; these are handled a little differently than everything
### else.
###

# Remove bias for dropping Pistols in the main game.  Also buffs drop rates
# for snipers, lasers, and launchers, though it does not bring them up to the
# level of pistols/ARs/SMGs/shotguns.  This could be done with a `set`
# statement, but this is more concise.  We don't need to touch the Claptastic
# Voyage pool GD_Ma_ItemPools.WeaponPools.Pool_Weapons_All_Glitch_Marigold
# beacuse that pool already has equal weights for all weapon types.
for (number, rarity) in [
        ('01', 'Common'),
        ('02', 'Uncommon'),
        ('04', 'Rare'),
        ('05', 'VeryRare'),
        ('06', 'Legendary'),
        ]:
    for (idx, (guntype, gunprob)) in enumerate([
            ('Pistol', ConfigBase.drop_prob_pistol),
            ('AR', ConfigBase.drop_prob_ar),
            ('SMG', ConfigBase.drop_prob_smg),
            ('Shotgun', ConfigBase.drop_prob_shotgun),
            ('Sniper', ConfigBase.drop_prob_sniper),
            ('Launcher', ConfigBase.drop_prob_launcher),
            ('Laser', ConfigBase.drop_prob_laser),
            ]):
        mp.register_str('normalize_weapon_types_{}_{}'.format(rarity, guntype),
            'level None set GD_Itempools.WeaponPools.Pool_Weapons_All_{}_{} BalancedItems[{}].Probability.BaseValueConstant {}'.format(
                number,
                rarity,
                idx,
                gunprob))

# Guaranteed Luneshine for Unique/Legendary weapons.  This is generated
# automatically by `gen_guaranteed_luneshine.py`.  Note that removing the
# "None" Luneshine attachment entirely would result in vanilla guns being
# removed from inventory, if loaded with this mod active, but we're okay
# if we just set `bDisabled` to `True`.
mp.register_str('guaranteed_luneshine_0',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom:WeaponPartListCollectionDefinition_23 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_1',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBreaker:WeaponPartListCollectionDefinition_27 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_2',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Torgue_5_KerBoom:WeaponPartListCollectionDefinition_31 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_3',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier:WeaponPartListCollectionDefinition_35 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_4',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Jakobs_3_Wallop:WeaponPartListCollectionDefinition_36 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_5',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_6',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_IceScream:WeaponPartListCollectionDefinition_38 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_7',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful:WeaponPartListCollectionDefinition_39 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_8',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_Ricochet:WeaponPartListCollectionDefinition_52 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_9',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Old_Hyperion_5_Excalibastard:WeaponPartListCollectionDefinition_53 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_10',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Tediore_5_Tesla:WeaponPartListCollectionDefinition_54 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_11',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Dahl_3_Firestarta:WeaponPartListCollectionDefinition_56 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_12',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining:WeaponPartListCollectionDefinition_57 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_13',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_Blizzard:WeaponPartListCollectionDefinition_58 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_14',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_VibraPulse:WeaponPartListCollectionDefinition_59 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_15',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Egun:WeaponPartListCollectionDefinition_8 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_16',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie:WeaponPartListCollectionDefinition_60 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_17',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_SavorySideSaber:WeaponPartListCollectionDefinition_61 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_18',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Tediore_3_Vandergraffen:WeaponPartListCollectionDefinition_62 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_19',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom:WeaponPartListCollectionDefinition_66 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_20',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_Thingy:WeaponPartListCollectionDefinition_67 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_21',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Cryophobia:WeaponPartListCollectionDefinition_71 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_22',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem:WeaponPartListCollectionDefinition_75 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_23',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol:WeaponPartListCollectionDefinition_79 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_24',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Tediore_3_Rocketeer:WeaponPartListCollectionDefinition_81 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_25',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer:WeaponPartListCollectionDefinition_82 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_26',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Zim:WeaponPartListCollectionDefinition_86 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_27',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Blowfly:WeaponPartListCollectionDefinition_90 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_28',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie:WeaponPartListCollectionDefinition_94 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_29',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang:WeaponPartListCollectionDefinition_98 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_30',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_88Fragnum:WeaponPartListCollectionDefinition_102 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_31',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead:WeaponPartListCollectionDefinition_103 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_32',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber:WeaponPartListCollectionDefinition_106 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_33',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Globber:WeaponPartListCollectionDefinition_107 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_34',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist:WeaponPartListCollectionDefinition_108 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_35',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Smasher:WeaponPartListCollectionDefinition_109 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_36',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe:WeaponPartListCollectionDefinition_11 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_37',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent:WeaponPartListCollectionDefinition_141 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_38',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch:WeaponPartListCollectionDefinition_145 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_39',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire:WeaponPartListCollectionDefinition_149 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_40',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF:WeaponPartListCollectionDefinition_153 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_41',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder:WeaponPartListCollectionDefinition_157 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_42',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch:WeaponPartListCollectionDefinition_158 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_43',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch:WeaponPartListCollectionDefinition_159 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_44',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun:WeaponPartListCollectionDefinition_113 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_45',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall:WeaponPartListCollectionDefinition_117 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_46',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker:WeaponPartListCollectionDefinition_121 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_47',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker:WeaponPartListCollectionDefinition_125 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_48',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella:WeaponPartListCollectionDefinition_126 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_49',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Moonface:WeaponPartListCollectionDefinition_128 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_50',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup:WeaponPartListCollectionDefinition_131 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_51',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo:WeaponPartListCollectionDefinition_134 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_52',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon:WeaponPartListCollectionDefinition_135 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_53',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Torguemada:WeaponPartListCollectionDefinition_136 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_54',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Wombat:WeaponPartListCollectionDefinition_137 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_55',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork:WeaponPartListCollectionDefinition_167 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_56',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader:WeaponPartListCollectionDefinition_171 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_57',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher:WeaponPartListCollectionDefinition_175 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_58',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Magma:WeaponPartListCollectionDefinition_179 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_59',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek:WeaponPartListCollectionDefinition_184 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_60',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Razorback:WeaponPartListCollectionDefinition_185 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_61',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie:WeaponPartListCollectionDefinition_186 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_62',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine:WeaponPartListCollectionDefinition_187 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_63',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan:WeaponPartListCollectionDefinition_235 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_64',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SG_Torgue_3_Landscaper2:WeaponPartListCollectionDefinition_236 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_65',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker:WeaponPartListCollectionDefinition_237 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_66',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade:WeaponPartListCollectionDefinition_221 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_67',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard:WeaponPartListCollectionDefinition_222 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_68',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_FusionBeam:WeaponPartListCollectionDefinition_223 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_69',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_Thunderfire:WeaponPartListCollectionDefinition_224 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_70',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Laser_Tediore_5_LaserDisker:WeaponPartListCollectionDefinition_225 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_71',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Jakobs_5_LuckCannon:WeaponPartListCollectionDefinition_226 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_72',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander:WeaponPartListCollectionDefinition_234 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_73',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.RL_Tediore_5_KanedasLaser:WeaponPartListCollectionDefinition_227 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_74',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.SG_Jakobs_5_Flayer:WeaponPartListCollectionDefinition_238 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_75',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode:WeaponPartListCollectionDefinition_228 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_76',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Sniper_Old_Hyperion_5_OmniCannon:WeaponPartListCollectionDefinition_229 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_77',
    'level None set GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Enlightenment:WeaponPartListCollectionDefinition_230 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_78',
    'level None set GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Minac:WeaponPartListCollectionDefinition_231 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_79',
    'level None set GD_Ma_Weapons.A_Weapons_Unique.Pistol_Bandit_3_PartyPopper:WeaponPartListCollectionDefinition_232 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_80',
    'level None set GD_Ma_Weapons.A_Weapons_Unique.Pistol_Maliwan_3_HardReboot:WeaponPartListCollectionDefinition_233 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_81',
    'level None set GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun:WeaponPartListCollectionDefinition_202 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_82',
    'level None set GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Fridgia:WeaponPartListCollectionDefinition_207 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_83',
    'level None set GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Frostfire:WeaponPartListCollectionDefinition_209 Accessory2PartData.WeightedParts[0].bDisabled True')
mp.register_str('guaranteed_luneshine_84',
    'level None set GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge:WeaponPartListCollectionDefinition_215 Accessory2PartData.WeightedParts[0].bDisabled True')

# Fix some container drop pools which reference an item (Pool_BuffDrinks_Euphoria)
# which doesn't actually exist, causing that loot possibility to never actually
# get chosen.  We'll replace with Pool_BuffDrinks_HealingRegen.  Most of these could
# happen via a regular `set` statement, but this lets us be much more concise.
for (idx, (classname, propname, loot_idx, attachment_idx)) in enumerate([
        ('GD_Balance_Treasure.ChestGrades.ObjectGrade_DahlEpic', 'DefaultLoot', 4, 11),
        ('GD_Itempools.ListDefs.EpicChestRedLoot', 'LootData', 4, 11),
        ('GD_Ma_ItemPools.ListDefs.EpicChestRedLoot_Marigold', 'LootData', 4, 11),
        ('GD_Itempools.ListDefs.EpicChestHyperionLoot', 'LootData', 3, 11),
        ('GD_Ma_ItemPools.ListDefs.EpicChestHyperionLoot_Marigold', 'LootData', 3, 11),
        ('GD_Meteorites.Balance.ObjectGrade_Meteorite_LootPile_Chest', 'DefaultLoot', 4, 11),
        ]):
    mp.register_str('euphoria_fix_{}'.format(idx),
        'level None set {} {}[{}].ItemAttachments[{}].ItemPool GD_Itempools.BuffDrinkPools.Pool_BuffDrinks_HealingRegen'.format(
            classname,
            propname,
            loot_idx,
            attachment_idx,
            ))

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
        mp.register_str('grenade_{}_{}_0'.format(gm_type, man_num),
            'level None set GD_GrenadeMods.A_Item.GM_{} Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
                gm_type, man_num,
            ))
        mp.register_str('grenade_{}_{}_1'.format(gm_type, man_num),
            'level None set GD_GrenadeMods.A_Item.GM_{}_2_Uncommon Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
                gm_type, man_num,
            ))
        mp.register_str('grenade_{}_{}_2'.format(gm_type, man_num),
            'level None set GD_GrenadeMods.A_Item.GM_{}_3_Rare Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
                gm_type, man_num,
            ))
        mp.register_str('grenade_{}_{}_3'.format(gm_type, man_num),
            'level None set GD_GrenadeMods.A_Item.GM_{}_4_VeryRare Manufacturers[{}].Grades[0].GameStageRequirement.MinGameStage 0'.format(
                gm_type, man_num,
            ))

# Improve Nel's loot
for idx in [15, 16, 17, 18, 19, 20, 21]:
    mp.register_str('nel_drops_{}'.format(idx),
        """level Deadsurface_P set GD_Nel.Population.PawnBalance_Nel DefaultItemPoolList[{}].ItemPool ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear'""".format(idx))

# For the record, the Empyrean Sentinel drops from the various Behavior_SpawnItems_* found
# under GD_FinalBossCorkBig.IOs.IO_LootSpew:BehaviorProviderDefinition_0.  "85" is
# money+moonstone, which I'm ignoring here, but it otherwise drops thusly:
# 
# Non-Raid Drops:
# 
# 2x 81 - GD_Itempools.ListDefs.RaidBossEnemyGunsAndGear
# 1x 84 - GD_Itempools.Runnables.Pool_FinalBoss
#         GD_Itempools.Runnables.Pool_ColZarpedon
#         GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear
# 1x 86 - GD_Itempools.Runnables.Pool_FinalBoss
#         GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear 
#         (+customizations)
# 1x 87 - GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear
# 
# Raid Drops:
# 
# 2x 82 - GD_Itempools.Runnables.Pool_FinalBossRaid
#         (+customizations)
# 1x 83 - GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear
# 1x 88 - GD_Itempools.Runnables.Pool_FinalBossRaid
#         GD_Itempools.Runnables.Pool_ColZarpedon
#         GD_Itempools.ListDefs.RaidBossEnemyGunsAndGear
# 1x 89 - GD_Itempools.ListDefs.UltimateBadassEnemyGunsAndGear

# Tweaks to EOS/SH4D0W-TP End-DLC Loot Shower.  There's a bunch of spawners at
# GD_Ma_Chapter05_Data.IO_Ma_LootShower:BehaviorProviderDefinition_1.Behavior_SpawnItems_*
# which fall into a few categories, which are identical save for the velocities +
# angles which the loot comes out of:
# 
#   144, 148, 150, 154, 156, 158, 160: Money + Moonstones
#   145, 147, 149, 151, 155, 157, 159, 161: One GunsAndGear Drop, 30% chance of purple,
#       40% chance of blue, and 40% chance of green
#   152: One Purple, Two Blues (seemingly only used outside System Shutdown (while farming))
#   153: Legendary (only used during System Shutdown)
#   146: Legendary (only used outside System Shutdown (while farming))
#
# Those pools (at least the main gear pools) can be called more than once, and the actual
# quantity seems to be a bit random (and possibly depends on whether you're in System Shutdown
# or not).  The in-mission drops, based on a small sample size, seem to be reasonably
# consistent, with about 1-3 drops per pool.  Outside of the mission it seems to be a bit more
# volatile (though that could be due to a small sample size), more like 0-4 per pool.  Apart
# from the legendary pools and "152", which only have one drop, as noted above.  Anyway, we're
# getting rid of greens, adding glitches, and adding a bit more money + moonstone.
#
# We're leaving 152 alone, doesn't seem worth the hotfix.  :)

# First up, more money+moonstone:
for num in [144, 148, 150, 154, 156, 158, 160]:
    mp.register_str('eos_drop_{}'.format(num),
        """level Ma_FinalBoss_P set GD_Ma_Chapter05_Data.IO_Ma_LootShower:BehaviorProviderDefinition_1.Behavior_SpawnItems_{} ItemPoolList
        (
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
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone_Cluster', 
                PoolProbability=( 
                    BaseValueConstant=0.500000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone_Cluster', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
        )""".format(num))

# Next: improved general gear drops (though we're acutally going to tweak the
# probabilities a bit here, with a net result of a bit less loot)
for num in [145, 147, 149, 151, 155, 157, 159, 161]:
    mp.register_str('eos_drop_{}'.format(num),
        """level Ma_FinalBoss_P set GD_Ma_Chapter05_Data.IO_Ma_LootShower:BehaviorProviderDefinition_1.Behavior_SpawnItems_{} ItemPoolList
        (
            ( 
                ItemPool=ItemPoolDefinition'GD_Ma_ItemPools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear_Marigold', 
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
                    BaseValueConstant=0.300000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare', 
                PoolProbability=( 
                    BaseValueConstant=0.400000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Ma_ItemPools.WeaponPools.Pool_Weapons_All_Glitch_Marigold', 
                PoolProbability=( 
                    BaseValueConstant=0.200000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
        )""".format(num))

# Change the legendary drops to use our main legendary drop pool rather than
# the "weighted" Marigold one.
for num in [153, 146]:
    mp.register_str('eos_drop_{}'.format(num),
        """level Ma_FinalBoss_P set GD_Ma_Chapter05_Data.IO_Ma_LootShower:BehaviorProviderDefinition_1.Behavior_SpawnItems_{} ItemPoolList
        (
            ( 
                ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
        )""".format(num))

# Altering probabilities in the mutator arena chests (in the Cortex).  There's
# a set of fun little AttributeInitializationDefinition objects which base
# their weights on the difficulty selected by the user.  The stock percentages
# end up looking like this (in percentages, assuming you have a pool with all
# four probabilities - uncommon, rare, veryrare, legendary):
#
#   Torment level 1: 84, 14, 2, 0.09
#   Torment level 2: 77, 19, 4, 0.1
#   Torment level 3: 65, 27, 8, 0.33
#   Torment level 4: 55, 33, 12, 0.55
#   Torment level 5: 37, 43, 20, 1
#   Torment level 6: 19, 51, 28, 2
#   Torment level 7: 0.15, 53, 44, 4
#   Torment level 8: 0.14, 42, 52, 5
#   Torment level 9: 0.13, 33, 61, 6
#
# We're changing that to look like this instead, using a gaussian function as
# our guide (with some custom tweaks to make the more common rarities fall
# off a little faster than they otherwise would):
#
#   Torment level 1: 79, 19, 2, 0.07
#   Torment level 2: 71, 25, 4, 0.2
#   Torment level 3: 61, 32, 7, 0.54
#   Torment level 4: 33, 50, 15, 2
#   Torment level 5: 23, 51, 23, 4
#   Torment level 6: 17, 37, 36, 10
#   Torment level 7: 0.0, 33, 48, 18
#   Torment level 8: 0.0, 23, 49, 28
#   Torment level 9: 0.0, 15, 47, 38

# All these curve + step parameters I'd just played around with until they
# felt more-or-less "right"
def gauss_at(x):
    peak = 50
    center = 50
    std_dev = 25
    exp = -((x-center)**2)/(2*(std_dev**2))
    return peak*(math.e**exp)
start = 75
interval = 24
step = -10
uncommons = []
rares = []
veryrares = []
legendaries = []
for count in range(9):
    if count >= 6:
        uncommons.append(0)
    elif count >= 3:
        uncommons.append(gauss_at(start)/2)
    else:
        uncommons.append(gauss_at(start))

    if count >= 5:
        rares.append(gauss_at(start+(interval*1))*2/3)
    else:
        rares.append(gauss_at(start+(interval*1)))

    veryrares.append(gauss_at(start+(interval*2)))
    legendaries.append(gauss_at(start+(interval*3)))
    start += step

# Now actually set up those hotfixes
for (label, objname, levels) in [
        ('uncommon', 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_2_Uncommon', uncommons),
        ('rare', 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_3_Rare', rares),
        ('veryrare', 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_4_VeryRare', veryrares),
        ('legendary', 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_5_Legendary', legendaries),
        ]:
    for idx, weight in enumerate(levels):
        mp.register_str('mutator_weight_{}_{}'.format(label, idx),
            """level Ma_SubBoss_P set {} ConditionalInitialization.ConditionalExpressionList[{}].BaseValueIfTrue
            (
                BaseValueConstant={},
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000
            )
            """.format(objname, idx, round(weight, 6)))

# Now some hotfixes to improve the actual mutator loot pools themselves
def mutator_pool(label, obj_name, contents):
    items = []
    for (pool, weight, scale) in contents:
        if weight == 2:
            idef = 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_2_Uncommon'
        elif weight == 3:
            idef = 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_3_Rare'
        elif weight == 4:
            idef = 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_4_VeryRare'
        elif weight == 5:
            idef = 'GD_Ma_Mutator.Attributes.Init_TormentLootWeight_5_Legendary'
        else:
            raise Exception('Unknown weight: {}'.format(weight))
        if not scale:
            scale = '1.000000'
        items.append("""( 
                ItmPoolDefinition=ItemPoolDefinition'{}', 
                InvBalanceDefinition=None, 
                Probability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=AttributeInitializationDefinition'{}', 
                    BaseValueScaleConstant={} 
                ), 
                bDropOnDeath=True 
            )""".format(pool, idef, scale))

    mp.register_str('mutator_{}'.format(label),
        """level Ma_SubBoss_P set {} BalancedItems
        (
            {}
        )
        """.format(obj_name, ','.join(items)))

mutator_pool('common_coms', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_ClassMods', [
    ('GD_Itempools.ClassModPools.Pool_ClassMod_02_Uncommon', 2, None),
    ('GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare', 3, None),
    ('GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare', 4, None),
    ])
mutator_pool('common_grenades', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_GrenadeMods', [
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_02_Uncommon', 2, None),
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare', 3, None),
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare', 4, None),
    ])
mutator_pool('common_ozkits', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_MoonItems', [
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_02_Uncommon', 2, None),
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_04_Rare', 3, None),
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_05_VeryRare', 4, None),
    ])
mutator_pool('common_shields', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_Shields', [
    ('GD_Itempools.ShieldPools.Pool_Shields_All_02_Uncommon', 2, None),
    ('GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare', 3, None),
    ('GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare', 4, None),
    ])
mutator_pool('common_launchers', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_Weapons_Launchers', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', 4, None),
    ])
mutator_pool('common_longguns', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_Weapons_LongGuns', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_05_VeryRare', 4, None),
    ])
mutator_pool('common_pistols', 'GD_Ma_Mutator.LootPools.Pool_Mut_CommonChest_Weapons_Pistols', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_02_Uncommon', 2, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', 4, None),
    ])
mutator_pool('red_coms', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_ClassMods', [
    ('GD_Itempools.ClassModPools.Pool_ClassMod_04_Rare', 3, None),
    ('GD_Itempools.ClassModPools.Pool_ClassMod_05_VeryRare', 4, None),
    ('GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary', 5, None),
    ])
mutator_pool('red_grenades', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_GrenadeMods', [
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare', 3, None),
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_05_VeryRare', 4, None),
    ('GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary', 5, None),
    ])
mutator_pool('red_ozkits', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_MoonItems', [
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_04_Rare', 3, None),
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_05_VeryRare', 4, None),
    ('GD_Itempools.MoonItemPools.Pool_MoonItem_06_Legendary', 5, None),
    ])
mutator_pool('red_shields', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Shields', [
    ('GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare', 3, None),
    ('GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare', 4, None),
    ('GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary', 5, None),
    ])
mutator_pool('red_launchers', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_Launchers', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Launchers_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary', 5, None),
    ])
mutator_pool('red_launchers_glitch', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_Launchers_PlusGitch', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Launchers_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary', 5, None),
    ])
mutator_pool('red_longguns', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_LongGuns', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_AssaultRifles_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Shotguns_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_SMG_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Sniper_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Lasers_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_06_Legendary', 5, None),
    ])
mutator_pool('red_longguns_glitch', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_LongGuns_PlusGlitch', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_AssaultRifles_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Shotguns_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_SMG_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Sniper_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary', 5, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Lasers_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_06_Legendary', 5, None),
    ])
mutator_pool('red_pistols', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_Pistols', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Pistols_Glitch_Marigold', 4, '0.5'),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', 5, None),
    ])
mutator_pool('red_pistols_glitch', 'GD_Ma_Mutator.LootPools.Pool_Mut_RedChest_Weapons_Pistols_PlusGlitch', [
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', 3, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', 4, None),
    ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Pistols_Glitch_Marigold', 4, None),
    ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', 5, None),
    ])

# Improve Flameknuckle's Holodome Onslaught drops
for num in [17, 18, 19, 20]:
    mp.register_str('flameknuckle_holodome_drop_{}'.format(num),
        """level Eridian_Slaughter_P set GD_DahlPowersuit_KnuckleRepaired.Population.PawnBalance_DahlSergeantFlameKnuckle DefaultItemPoolList[{}].ItemPool ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare'""".format(num))

# Exhaustive early-game weapon unlocks.  Generated by `part_unlock.py` using
# ft-explorer data.
mp.register_str('part_unlock_0',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_1',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_2',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_3',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_4',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_5',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_6',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_7',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_8',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_9',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_10',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_11',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_12',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_13',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_14',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_15',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_16',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_17',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_18',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_19',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_20',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_21',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_22',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_23',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_24',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_25',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_26',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_27',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_28',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_29',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_30',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_31',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_32',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_33',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_34',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_35',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_36',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_37',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_38',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_39',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_40',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_41',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_42',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_43',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_44',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_45',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_46',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_47',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_48',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_49',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_50',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_51',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_52',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_53',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_54',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_55',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_56',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_57',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_58',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_59',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_60',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_61',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_62',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_63',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_64',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_65',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_66',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_67',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_68',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_69',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_70',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_71',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_72',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_73',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_74',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_75',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_76',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_77',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_78',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_79',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_80',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_81',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_82',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_83',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_84',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_85',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_86',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_87',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_88',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_89',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_90',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_91',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_92',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_93',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_94',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_95',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_96',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_97',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_98',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_99',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_100',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_101',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_102',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_103',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_104',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_105',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_106',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_107',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_108',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_109',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_110',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_111',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_112',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_113',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_114',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_115',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_116',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_117',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_118',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_119',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_120',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_0 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_121',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_0 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_122',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_0 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_123',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_124',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_125',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_126',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_127',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_128',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_129',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_130',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_131',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_132',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_133',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_134',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_135',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_136',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_137',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_138',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_3_Rare:WeaponPartListCollectionDefinition_10 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_139',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_3_Rare:WeaponPartListCollectionDefinition_10 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_140',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_3_Rare:WeaponPartListCollectionDefinition_10 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_141',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe:WeaponPartListCollectionDefinition_11 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_142',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe:WeaponPartListCollectionDefinition_11 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_143',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe:WeaponPartListCollectionDefinition_11 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_144',
    'level None set GD_Co_ToroToroData.A_Weapons_Unique.MW_Co_Probe:WeaponPartListCollectionDefinition_12 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_145',
    'level None set GD_Co_ToroToroData.A_Weapons_Unique.MW_Co_Probe:WeaponPartListCollectionDefinition_12 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_146',
    'level None set GD_Co_ToroToroData.A_Weapons_Unique.MW_Co_Probe:WeaponPartListCollectionDefinition_12 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_147',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_20 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_148',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_20 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_149',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_20 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_150',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_3_Rare:WeaponPartListCollectionDefinition_21 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_151',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_3_Rare:WeaponPartListCollectionDefinition_21 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_152',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_3_Rare:WeaponPartListCollectionDefinition_21 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_153',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_22 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_154',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_22 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_155',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_22 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_156',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom:WeaponPartListCollectionDefinition_23 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_157',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom:WeaponPartListCollectionDefinition_23 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_158',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom:WeaponPartListCollectionDefinition_23 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_159',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_32 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_160',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_32 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_161',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_32 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_162',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_3_Rare:WeaponPartListCollectionDefinition_33 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_163',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_3_Rare:WeaponPartListCollectionDefinition_33 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_164',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_3_Rare:WeaponPartListCollectionDefinition_33 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_165',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_34 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_166',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_34 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_167',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_34 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_168',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier:WeaponPartListCollectionDefinition_35 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_169',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier:WeaponPartListCollectionDefinition_35 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_170',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier:WeaponPartListCollectionDefinition_35 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_171',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_172',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_173',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_174',
    'level None set gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_175',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_176',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_177',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_178',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_179',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_180',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_181',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_182',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_183',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_184',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_185',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_186',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_187',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_188',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_189',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_190',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_191',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_192',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_193',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_194',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_195',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_196',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_197',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_198',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_199',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_200',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_201',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_202',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_203',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_204',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_205',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_206',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_207',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_208',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_209',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_210',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_211',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_212',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_213',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_214',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_215',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_216',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_217',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_218',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_219',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_220',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_221',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_222',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_223',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_224',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_225',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_226',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_227',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_228',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50 ConsolidatedAttributeInitData[8].BaseValueConstant 1')
mp.register_str('part_unlock_229',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50 ConsolidatedAttributeInitData[9].BaseValueConstant 1')
mp.register_str('part_unlock_230',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_231',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_232',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_233',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_234',
    'level None set GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_235',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining:WeaponPartListCollectionDefinition_57 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_236',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining:WeaponPartListCollectionDefinition_57 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_237',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining:WeaponPartListCollectionDefinition_57 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_238',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie:WeaponPartListCollectionDefinition_60 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_239',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie:WeaponPartListCollectionDefinition_60 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_240',
    'level None set GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie:WeaponPartListCollectionDefinition_60 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_241',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_63 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_242',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_63 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_243',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_63 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_244',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_3_Rare:WeaponPartListCollectionDefinition_64 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_245',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_3_Rare:WeaponPartListCollectionDefinition_64 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_246',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_3_Rare:WeaponPartListCollectionDefinition_64 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_247',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_65 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_248',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_65 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_249',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_65 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_250',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom:WeaponPartListCollectionDefinition_66 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_251',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom:WeaponPartListCollectionDefinition_66 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_252',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom:WeaponPartListCollectionDefinition_66 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_253',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_68 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_254',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_68 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_255',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_68 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_256',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_3_Rare:WeaponPartListCollectionDefinition_69 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_257',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_3_Rare:WeaponPartListCollectionDefinition_69 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_258',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_3_Rare:WeaponPartListCollectionDefinition_69 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_259',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_70 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_260',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_70 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_261',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_70 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_262',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_76 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_263',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_76 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_264',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_76 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_265',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_3_Rare:WeaponPartListCollectionDefinition_77 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_266',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_3_Rare:WeaponPartListCollectionDefinition_77 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_267',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_3_Rare:WeaponPartListCollectionDefinition_77 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_268',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_78 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_269',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_78 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_270',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_78 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_271',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol:WeaponPartListCollectionDefinition_79 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_272',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol:WeaponPartListCollectionDefinition_79 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_273',
    'level None set GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol:WeaponPartListCollectionDefinition_79 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_274',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_80 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_275',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_80 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_276',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_80 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_277',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_83 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_278',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_83 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_279',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_83 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_280',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_3_Rare:WeaponPartListCollectionDefinition_84 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_281',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_3_Rare:WeaponPartListCollectionDefinition_84 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_282',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_3_Rare:WeaponPartListCollectionDefinition_84 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_283',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_85 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_284',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_85 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_285',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_85 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_286',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_87 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_287',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_87 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_288',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_87 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_289',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_3_Rare:WeaponPartListCollectionDefinition_88 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_290',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_3_Rare:WeaponPartListCollectionDefinition_88 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_291',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_3_Rare:WeaponPartListCollectionDefinition_88 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_292',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_89 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_293',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_89 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_294',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_89 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_295',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_95 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_296',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_95 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_297',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_95 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_298',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_3_Rare:WeaponPartListCollectionDefinition_96 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_299',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_3_Rare:WeaponPartListCollectionDefinition_96 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_300',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_3_Rare:WeaponPartListCollectionDefinition_96 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_301',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_97 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_302',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_97 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_303',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_97 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_304',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang:WeaponPartListCollectionDefinition_98 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_305',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang:WeaponPartListCollectionDefinition_98 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_306',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang:WeaponPartListCollectionDefinition_98 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_307',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead:WeaponPartListCollectionDefinition_103 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_308',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead:WeaponPartListCollectionDefinition_103 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_309',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead:WeaponPartListCollectionDefinition_103 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_310',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_104 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_311',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_104 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_312',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_104 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_313',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_3_Rare:WeaponPartListCollectionDefinition_105 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_314',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_3_Rare:WeaponPartListCollectionDefinition_105 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_315',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_3_Rare:WeaponPartListCollectionDefinition_105 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_316',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber:WeaponPartListCollectionDefinition_106 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_317',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber:WeaponPartListCollectionDefinition_106 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_318',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber:WeaponPartListCollectionDefinition_106 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_319',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist:WeaponPartListCollectionDefinition_108 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_320',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist:WeaponPartListCollectionDefinition_108 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_321',
    'level None set GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist:WeaponPartListCollectionDefinition_108 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_322',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_110 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_323',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_110 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_324',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_110 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_325',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_3_Rare:WeaponPartListCollectionDefinition_111 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_326',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_3_Rare:WeaponPartListCollectionDefinition_111 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_327',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_3_Rare:WeaponPartListCollectionDefinition_111 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_328',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_112 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_329',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_112 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_330',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_112 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_331',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun:WeaponPartListCollectionDefinition_113 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_332',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun:WeaponPartListCollectionDefinition_113 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_333',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun:WeaponPartListCollectionDefinition_113 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_334',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_114 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_335',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_114 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_336',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_114 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_337',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_115 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_338',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_115 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_339',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_115 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_340',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_116 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_341',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_116 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_342',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_116 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_343',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella:WeaponPartListCollectionDefinition_126 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_344',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella:WeaponPartListCollectionDefinition_126 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_345',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella:WeaponPartListCollectionDefinition_126 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_346',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_129 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_347',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_129 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_348',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_129 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_349',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_130 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_350',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_130 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_351',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_130 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_352',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup:WeaponPartListCollectionDefinition_131 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_353',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup:WeaponPartListCollectionDefinition_131 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_354',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup:WeaponPartListCollectionDefinition_131 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_355',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_132 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_356',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_132 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_357',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_132 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_358',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_3_Rare:WeaponPartListCollectionDefinition_133 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_359',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_3_Rare:WeaponPartListCollectionDefinition_133 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_360',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_3_Rare:WeaponPartListCollectionDefinition_133 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_361',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo:WeaponPartListCollectionDefinition_134 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_362',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo:WeaponPartListCollectionDefinition_134 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_363',
    'level None set GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo:WeaponPartListCollectionDefinition_134 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_364',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_138 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_365',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_138 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_366',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_138 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_367',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_3_Rare:WeaponPartListCollectionDefinition_139 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_368',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_3_Rare:WeaponPartListCollectionDefinition_139 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_369',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_3_Rare:WeaponPartListCollectionDefinition_139 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_370',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_140 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_371',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_140 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_372',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_140 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_373',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent:WeaponPartListCollectionDefinition_141 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_374',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent:WeaponPartListCollectionDefinition_141 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_375',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent:WeaponPartListCollectionDefinition_141 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_376',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_142 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_377',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_142 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_378',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_142 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_379',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_143 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_380',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_143 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_381',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_143 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_382',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_144 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_383',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_144 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_384',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_144 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_385',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_146 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_386',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_146 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_387',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_146 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_388',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_3_Rare:WeaponPartListCollectionDefinition_147 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_389',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_3_Rare:WeaponPartListCollectionDefinition_147 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_390',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_3_Rare:WeaponPartListCollectionDefinition_147 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_391',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_148 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_392',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_148 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_393',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_148 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_394',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_150 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_395',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_150 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_396',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_150 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_397',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_3_Rare:WeaponPartListCollectionDefinition_151 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_398',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_3_Rare:WeaponPartListCollectionDefinition_151 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_399',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_3_Rare:WeaponPartListCollectionDefinition_151 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_400',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_152 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_401',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_152 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_402',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_152 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_403',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF:WeaponPartListCollectionDefinition_153 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_404',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF:WeaponPartListCollectionDefinition_153 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_405',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF:WeaponPartListCollectionDefinition_153 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_406',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_154 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_407',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_154 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_408',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_154 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_409',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_3_Rare:WeaponPartListCollectionDefinition_156 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_410',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_3_Rare:WeaponPartListCollectionDefinition_156 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_411',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_3_Rare:WeaponPartListCollectionDefinition_156 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_412',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder:WeaponPartListCollectionDefinition_157 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_413',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder:WeaponPartListCollectionDefinition_157 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_414',
    'level None set GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder:WeaponPartListCollectionDefinition_157 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_415',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_160 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_416',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_160 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_417',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_160 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_418',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_161 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_419',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_161 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_420',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_161 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_421',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_162 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_422',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_162 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_423',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_162 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_424',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_164 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_425',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_164 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_426',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_164 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_427',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare:WeaponPartListCollectionDefinition_165 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_428',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare:WeaponPartListCollectionDefinition_165 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_429',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare:WeaponPartListCollectionDefinition_165 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_430',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_166 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_431',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_166 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_432',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_166 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_433',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork:WeaponPartListCollectionDefinition_167 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_434',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork:WeaponPartListCollectionDefinition_167 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_435',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork:WeaponPartListCollectionDefinition_167 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_436',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_168 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_437',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_168 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_438',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_168 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_439',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_3_Rare:WeaponPartListCollectionDefinition_169 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_440',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_3_Rare:WeaponPartListCollectionDefinition_169 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_441',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_3_Rare:WeaponPartListCollectionDefinition_169 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_442',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_170 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_443',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_170 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_444',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_170 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_445',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader:WeaponPartListCollectionDefinition_171 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_446',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader:WeaponPartListCollectionDefinition_171 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_447',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader:WeaponPartListCollectionDefinition_171 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_448',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_176 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_449',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_176 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_450',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_176 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_451',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_3_Rare:WeaponPartListCollectionDefinition_177 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_452',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_3_Rare:WeaponPartListCollectionDefinition_177 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_453',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_3_Rare:WeaponPartListCollectionDefinition_177 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_454',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_178 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_455',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_178 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_456',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_178 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_457',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_180 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_458',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_180 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_459',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_180 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_460',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_3_Rare:WeaponPartListCollectionDefinition_181 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_461',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_3_Rare:WeaponPartListCollectionDefinition_181 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_462',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_3_Rare:WeaponPartListCollectionDefinition_181 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_463',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_182 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_464',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_182 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_465',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_182 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_466',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail:WeaponPartListCollectionDefinition_183 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_467',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail:WeaponPartListCollectionDefinition_183 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_468',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail:WeaponPartListCollectionDefinition_183 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_469',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek:WeaponPartListCollectionDefinition_184 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_470',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek:WeaponPartListCollectionDefinition_184 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_471',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek:WeaponPartListCollectionDefinition_184 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_472',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie:WeaponPartListCollectionDefinition_186 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_473',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie:WeaponPartListCollectionDefinition_186 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_474',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie:WeaponPartListCollectionDefinition_186 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_475',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine:WeaponPartListCollectionDefinition_187 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_476',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine:WeaponPartListCollectionDefinition_187 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_477',
    'level None set GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine:WeaponPartListCollectionDefinition_187 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_478',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_188 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_479',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_188 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_480',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_188 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_481',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare:WeaponPartListCollectionDefinition_189 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_482',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare:WeaponPartListCollectionDefinition_189 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_483',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare:WeaponPartListCollectionDefinition_189 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_484',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_190 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_485',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_190 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_486',
    'level None set GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_190 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_487',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_3_Rare:WeaponPartListCollectionDefinition_192 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_488',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_3_Rare:WeaponPartListCollectionDefinition_192 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_489',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_3_Rare:WeaponPartListCollectionDefinition_192 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_490',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_193 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_491',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_193 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_492',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_193 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_493',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_194 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_494',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_194 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_495',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_194 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_496',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_195 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_497',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_195 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_498',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_195 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_499',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_196 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_500',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_196 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_501',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_196 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_502',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_197 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_503',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_197 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_504',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_197 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_505',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_198 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_506',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_198 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_507',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_198 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_508',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_199 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_509',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_199 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_510',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_199 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_511',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_3_Rare:WeaponPartListCollectionDefinition_200 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_512',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_3_Rare:WeaponPartListCollectionDefinition_200 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_513',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_3_Rare:WeaponPartListCollectionDefinition_200 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_514',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_201 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_515',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_201 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_516',
    'level None set GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_201 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_517',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_203 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_518',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_203 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_519',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_203 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_520',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_204 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_521',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_204 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_522',
    'level None set GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_204 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_523',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_206 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_524',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_206 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_525',
    'level None set GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_206 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_526',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_211 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_527',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_211 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_528',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_211 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_529',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_212 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_530',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_212 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_531',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_212 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_532',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_213 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_533',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_213 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_534',
    'level None set GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_213 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_535',
    'level None set GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge:WeaponPartListCollectionDefinition_215 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_536',
    'level None set GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge:WeaponPartListCollectionDefinition_215 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_537',
    'level None set GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge:WeaponPartListCollectionDefinition_215 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_538',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_216 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_539',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_216 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_540',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_216 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_541',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_217 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_542',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_217 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_543',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_217 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_544',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_218 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_545',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_218 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_546',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_218 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_547',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_219 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_548',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_219 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_549',
    'level None set GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_219 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_550',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_551',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_552',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_553',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_554',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_555',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_556',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_557',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_558',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_559',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_560',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_561',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_562',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade:WeaponPartListCollectionDefinition_221 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_563',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade:WeaponPartListCollectionDefinition_221 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_564',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade:WeaponPartListCollectionDefinition_221 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_565',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard:WeaponPartListCollectionDefinition_222 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_566',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard:WeaponPartListCollectionDefinition_222 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_567',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard:WeaponPartListCollectionDefinition_222 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_568',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode:WeaponPartListCollectionDefinition_228 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_569',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode:WeaponPartListCollectionDefinition_228 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_570',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode:WeaponPartListCollectionDefinition_228 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_571',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander:WeaponPartListCollectionDefinition_234 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_572',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander:WeaponPartListCollectionDefinition_234 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_573',
    'level None set GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander:WeaponPartListCollectionDefinition_234 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_574',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan:WeaponPartListCollectionDefinition_235 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_575',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan:WeaponPartListCollectionDefinition_235 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_576',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan:WeaponPartListCollectionDefinition_235 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_577',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker:WeaponPartListCollectionDefinition_237 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_578',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker:WeaponPartListCollectionDefinition_237 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_579',
    'level None set GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker:WeaponPartListCollectionDefinition_237 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_580',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Vladof_6_Glitch:WeaponPartListCollectionDefinition_239 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_581',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Vladof_6_Glitch:WeaponPartListCollectionDefinition_239 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_582',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Vladof_6_Glitch:WeaponPartListCollectionDefinition_239 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_583',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Dahl_6_Glitch:WeaponPartListCollectionDefinition_242 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_584',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Dahl_6_Glitch:WeaponPartListCollectionDefinition_242 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_585',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Dahl_6_Glitch:WeaponPartListCollectionDefinition_242 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_586',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Bandit_6_Glitch:WeaponPartListCollectionDefinition_243 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_587',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Bandit_6_Glitch:WeaponPartListCollectionDefinition_243 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_588',
    'level None set GD_Ma_Weapons.A_Weapons.AR_Bandit_6_Glitch:WeaponPartListCollectionDefinition_243 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_589',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_590',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_591',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_592',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_593',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_594',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_595',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_596',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_597',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_598',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_599',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_600',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_601',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_602',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_603',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_604',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_605',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_606',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_607',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_608',
    'level None set GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_609',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Vladof_6_Glitch:WeaponPartListCollectionDefinition_250 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_610',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Vladof_6_Glitch:WeaponPartListCollectionDefinition_250 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_611',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Vladof_6_Glitch:WeaponPartListCollectionDefinition_250 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_612',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Tediore_6_Glitch:WeaponPartListCollectionDefinition_251 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_613',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Tediore_6_Glitch:WeaponPartListCollectionDefinition_251 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_614',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Tediore_6_Glitch:WeaponPartListCollectionDefinition_251 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_615',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Bandit_6_Glitch:WeaponPartListCollectionDefinition_252 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_616',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Bandit_6_Glitch:WeaponPartListCollectionDefinition_252 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_617',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Bandit_6_Glitch:WeaponPartListCollectionDefinition_252 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_618',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_253 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_619',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_253 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_620',
    'level None set GD_Ma_Weapons.A_Weapons.RL_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_253 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_621',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Dahl_6_Glitch:WeaponPartListCollectionDefinition_254 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_622',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Dahl_6_Glitch:WeaponPartListCollectionDefinition_254 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_623',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Dahl_6_Glitch:WeaponPartListCollectionDefinition_254 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_624',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Bandit_6_Glitch:WeaponPartListCollectionDefinition_255 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_625',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Bandit_6_Glitch:WeaponPartListCollectionDefinition_255 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_626',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Bandit_6_Glitch:WeaponPartListCollectionDefinition_255 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_627',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_257 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_628',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_257 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_629',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_257 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_630',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_258 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_631',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_258 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_632',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_258 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_633',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Tediore_6_Glitch:WeaponPartListCollectionDefinition_259 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_634',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Tediore_6_Glitch:WeaponPartListCollectionDefinition_259 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_635',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Tediore_6_Glitch:WeaponPartListCollectionDefinition_259 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_636',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Vladof_6_Glitch:WeaponPartListCollectionDefinition_261 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_637',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Vladof_6_Glitch:WeaponPartListCollectionDefinition_261 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_638',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Vladof_6_Glitch:WeaponPartListCollectionDefinition_261 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_639',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_262 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_640',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_262 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_641',
    'level None set GD_Ma_Weapons.A_Weapons.Pistol_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_262 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_642',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_263 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_643',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_263 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_644',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_263 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_645',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_264 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_646',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_264 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_647',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_264 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_648',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_265 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_649',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_265 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_650',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_265 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_651',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_268 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_652',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_268 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_653',
    'level None set GD_Ma_Weapons.A_Weapons.SG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_268 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_654',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_269 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_655',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_269 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_656',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_269 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_657',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_270 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_658',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_270 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_659',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_270 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_660',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_271 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_661',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_271 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_662',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_271 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_663',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_272 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_664',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_272 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_665',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_272 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_666',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Dahl_6_Glitch:WeaponPartListCollectionDefinition_273 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_667',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Dahl_6_Glitch:WeaponPartListCollectionDefinition_273 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_668',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Dahl_6_Glitch:WeaponPartListCollectionDefinition_273 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_669',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_274 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_670',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_274 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_671',
    'level None set GD_Ma_Weapons.A_Weapons.SMG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_274 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_672',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_277 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_673',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_277 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_674',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_277 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_675',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Vladof_6_Glitch:WeaponPartListCollectionDefinition_278 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_676',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Vladof_6_Glitch:WeaponPartListCollectionDefinition_278 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_677',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Vladof_6_Glitch:WeaponPartListCollectionDefinition_278 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_678',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_279 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_679',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_279 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_680',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_279 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_681',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch:WeaponPartListCollectionDefinition_280 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_682',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch:WeaponPartListCollectionDefinition_280 ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_683',
    'level None set GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch:WeaponPartListCollectionDefinition_280 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_684',
    'level None set GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace:PartList ConsolidatedAttributeInitData[3].BaseValueConstant 1')
mp.register_str('part_unlock_685',
    'level None set GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_686',
    'level None set GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace:PartList ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_687',
    'level None set GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_688',
    'level None set GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_689',
    'level None set GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:WeaponPartListCollectionDefinition_282 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_690',
    'level None set GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:WeaponPartListCollectionDefinition_282 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_691',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:WeaponPartListCollectionDefinition_285 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_692',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:WeaponPartListCollectionDefinition_285 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_693',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:WeaponPartListCollectionDefinition_285 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_694',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_3_Rare_DahlBarrel:WeaponPartListCollectionDefinition_284 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_695',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_3_Rare_DahlBarrel:WeaponPartListCollectionDefinition_284 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_696',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_3_Rare_DahlBarrel:WeaponPartListCollectionDefinition_284 ConsolidatedAttributeInitData[7].BaseValueConstant 1')
mp.register_str('part_unlock_697',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:PartList ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_698',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:PartList ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_699',
    'level None set GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:PartList ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_700',
    'level None set GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi:WeaponPartListCollectionDefinition_286 ConsolidatedAttributeInitData[4].BaseValueConstant 1')
mp.register_str('part_unlock_701',
    'level None set GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi:WeaponPartListCollectionDefinition_286 ConsolidatedAttributeInitData[5].BaseValueConstant 1')
mp.register_str('part_unlock_702',
    'level None set GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi:WeaponPartListCollectionDefinition_286 ConsolidatedAttributeInitData[6].BaseValueConstant 1')
mp.register_str('part_unlock_703',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_AllParts:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_704',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Enforcer_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_705',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Gladiator_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_706',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Lawbringer_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_707',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Prototype_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_708',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Enforcer:ItemPartListCollectionDefinition_0 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_709',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Enforcer_04_VeryRare:ItemPartListCollectionDefinition_4 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_710',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Gladiator:ItemPartListCollectionDefinition_7 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_711',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Gladiator_04_VeryRare:ItemPartListCollectionDefinition_11 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_712',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Lawbringer:ItemPartListCollectionDefinition_14 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_713',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Lawbringer_04_VeryRare:ItemPartListCollectionDefinition_18 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_714',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Prototype:ItemPartListCollectionDefinition_21 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_715',
    'level None set GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Prototype_04_VeryRare:ItemPartListCollectionDefinition_25 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_716',
    'level None set GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_717',
    'level None set GD_Crocus_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Baroness_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_718',
    'level None set GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness:ItemPartListCollectionDefinition_28 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_719',
    'level None set GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness_04_VeryRare:ItemPartListCollectionDefinition_32 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_720',
    'level None set GD_Crocus_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Baroness:ItemPartListCollectionDefinition_36 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_721',
    'level None set GD_Crocus_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Baroness_04_VeryRare:ItemPartListCollectionDefinition_40 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_722',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Doppel_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_723',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Enforcer_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_724',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Gladiator_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_725',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Lawbringer_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_726',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Prototype_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_727',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Doppel:ItemPartListCollectionDefinition_41 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_728',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Doppel_04_VeryRare:ItemPartListCollectionDefinition_45 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_729',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Enforcer:ItemPartListCollectionDefinition_47 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_730',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Enforcer_04_VeryRare:ItemPartListCollectionDefinition_51 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_731',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Gladiator:ItemPartListCollectionDefinition_53 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_732',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Gladiator_04_VeryRare:ItemPartListCollectionDefinition_57 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_733',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Lawbringer:ItemPartListCollectionDefinition_59 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_734',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Lawbringer_04_VeryRare:ItemPartListCollectionDefinition_63 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_735',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Prototype:ItemPartListCollectionDefinition_65 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_736',
    'level None set GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Prototype_04_VeryRare:ItemPartListCollectionDefinition_69 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_737',
    'level None set GD_Quince_ItemGrades.ClassMods.BalDef_ClassMod_Doppelganger_04_VeryRare:PartList ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_738',
    'level None set GD_Quince_ItemGrades.ClassMods.BalDef_ClassMod_Doppelganger:ItemPartListCollectionDefinition_71 ConsolidatedAttributeInitData[2].BaseValueConstant 1')
mp.register_str('part_unlock_739',
    'level None set GD_Quince_ItemGrades.ClassMods.BalDef_ClassMod_Doppelganger_04_VeryRare:ItemPartListCollectionDefinition_75 ConsolidatedAttributeInitData[2].BaseValueConstant 1')

###
### Generate our quality category strings
###

qualities = {}
for profile in profiles:

    profile.set_balanced_pct_reports('drop_weapon', [
            profile.weapon_base_common,
            profile.weapon_base_uncommon,
            profile.weapon_base_rare,
            profile.weapon_base_veryrare,
            profile.weapon_base_glitch,
            profile.weapon_base_legendary,
            ], fixedlen=True)
    # We're assuming that all items have the same percentages, which at the
    # moment is true.  It's possible that at some point in the future that'll
    # become Not True, and we'll have more work to do.
    profile.set_balanced_pct_reports('drop_items', [
            profile.com_base_common,
            profile.com_base_uncommon,
            profile.com_base_rare,
            profile.com_base_veryrare,
            profile.com_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('treasure_weapon', [
            profile.treasure_base_common,
            profile.treasure_base_uncommon,
            profile.treasure_base_rare,
            profile.treasure_base_veryrare,
            profile.treasure_base_glitch,
            profile.treasure_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('treasure_items', [
            profile.treasure_base_common,
            profile.treasure_base_uncommon,
            profile.treasure_base_rare,
            profile.treasure_base_veryrare,
            profile.treasure_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('epic_weapon', [
            profile.epic_base_uncommon,
            profile.epic_base_rare,
            profile.epic_base_veryrare,
            profile.epic_base_glitch,
            profile.epic_base_legendary,
            ], fixedlen=True)
    profile.set_balanced_pct_reports('epic_items', [
            profile.epic_base_uncommon,
            profile.epic_base_rare,
            profile.epic_base_veryrare,
            profile.epic_base_legendary,
            ], fixedlen=True)
    profile.set_badass_qty_reports('regular', [
            profile.badass_pool_veryrare,
            profile.badass_pool_glitch,
            profile.badass_pool_epicchest,
            ])
    profile.set_badass_qty_reports('super', [
            profile.super_badass_pool_rare,
            profile.super_badass_pool_veryrare,
            profile.super_badass_pool_glitch,
            profile.super_badass_pool_legendary,
            profile.super_badass_pool_epicchest,
            ])
    profile.set_badass_qty_reports('ultimate', [
            profile.ultimate_badass_pool_veryrare_1 + profile.ultimate_badass_pool_veryrare_2,
            profile.ultimate_badass_pool_glitch_1 + profile.ultimate_badass_pool_glitch_2,
            profile.ultimate_badass_pool_legendary_1 + profile.ultimate_badass_pool_legendary_2 + profile.ultimate_badass_pool_legendary_3,
            profile.ultimate_badass_pool_epicchest_1 + profile.ultimate_badass_pool_epicchest_2 + profile.ultimate_badass_pool_epicchest_3,
            ])

    with open('input-file-quality.txt') as df:
        qualities[profile.profile_name] = df.read().format(
                config=profile,
                mp=mp,
                )


###
### Generate our boss unique drop strings
###

boss_drops = {}
for (label, key, unique_pct, rare_pct, holodome_pct) in [
        ('Guaranteed', 'guaranteed', 1, 1, .2),
        ('Very Improved', 'veryimproved', .5, .75, .15),
        ('Improved', 'improved', .33, .60, 0.1),
        ('Slightly Improved', 'slight', .22, .45, .085),
        ('Stock', 'stock', .1, .33, .066),
        ]:

    with open('input-file-droprate.txt', 'r') as df:
        boss_drops[key] = df.read().format(
                section_label='{} ({}% Uniques, {}% Rares, {}% Holodome Uniques)'.format(
                    label, round(unique_pct*100), round(rare_pct*100), round(holodome_pct*100)),
                unique_pct=unique_pct,
                rare_pct=rare_pct,
                holodome_pct=holodome_pct,
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
        base=ConfigBase(),
        drop_quality_excellent=qualities['Excellent'],
        drop_quality_good=qualities['Good'],
        boss_drops_guaranteed=boss_drops['guaranteed'],
        boss_drops_veryimproved=boss_drops['veryimproved'],
        boss_drops_improved=boss_drops['improved'],
        boss_drops_slightimproved=boss_drops['slight'],
        boss_drops_stock=boss_drops['stock'],
        )
mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod to: {}'.format(output_filename))
