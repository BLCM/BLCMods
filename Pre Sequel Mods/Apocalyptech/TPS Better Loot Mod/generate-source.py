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

mod_name = 'TPS Better Loot Mod'
mod_version = '1.0.0 (prerelease)'
variant_ucp = 'UCP Compat'
variant_offline = 'Standalone Offline'

###
### Where we get our mod data from
###

input_filename = 'mod-input-file.txt'

###
### Hotfix object to store all our hotfixes
###

hfs = Hotfixes(include_gearbox_patches=True, game='tps')

###
### Variables which control drop rates and stuff like that
###

class ConfigBase(object):
    """
    Class to hold all our weights, and other vars which alter the probabilities of
    various things dropping.  Derive from this class to actually define the
    values.
    """

    def filename(self, mod_name, variant_name):
        """
        Constructs our filename
        """
        return '{} ({}) - {}-source.txt'.format(
                mod_name,
                self.profile_name,
                variant_name,
            )

    def __format__(self, formatstr):
        """
        A bit of magic so that we can use our values in format strings
        """
        attr = getattr(self, formatstr)
        if type(attr) == str:
            return attr
        else:
            return attr()

###
### Config classes which define the actual contstants that we use
### for things like drop weights, etc.
###

class ConfigLootsplosion(ConfigBase):
    """
    This is our default config, which I personally find quite pleasant.
    Many folks will consider this a bit too OP/Extreme.
    """

    profile_name = 'Lootsplosion'

    # Just some convenience vars
    one = '1.000000'
    zero = '0.000000'

    # Custom weapon drop scaling
    weapon_base_common = '8'
    weapon_base_uncommon = '85'
    weapon_base_rare = '65'
    weapon_base_veryrare = '50'
    weapon_base_glitch = '15'
    weapon_base_legendary = '3'

    # Custom ozkit drop scaling (identical to weapons)
    ozkit_base_common = weapon_base_common
    ozkit_base_uncommon = weapon_base_uncommon
    ozkit_base_rare = weapon_base_rare
    ozkit_base_veryrare = weapon_base_veryrare
    ozkit_base_legendary = weapon_base_legendary

    # Custom COM drop scaling (identical to weapons, apart from an additional Alignment COM pool)
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

    # Custom relic drop scaling
    relic_base_rare = '1.0'
    relic_base_veryrare = '2.0'

    # Drop rates for "regular" treasure chests
    treasure_base_common = zero
    treasure_base_uncommon = zero
    treasure_base_rare = '20'
    treasure_base_veryrare = '60'
    treasure_base_glitch = '30'
    treasure_base_legendary = '5'

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = zero
    epic_base_rare = zero
    epic_base_veryrare = '1.2'
    epic_base_glitch = '.8'
    epic_base_legendary = '0.3'
    epic_base_legendary_dbl = '0.6'

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = '0.4'
    badass_pool_glitch = '0.4'
    badass_pool_epicchest = '0.1'

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = '1'
    super_badass_pool_veryrare = '1'
    super_badass_pool_glitch = '1'
    super_badass_pool_legendary = '1'
    super_badass_pool_epicchest = '1'

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = '1'
    ultimate_badass_pool_veryrare_2 = '0.5'
    ultimate_badass_pool_glitch_1 = '1'
    ultimate_badass_pool_glitch_2 = '0.5'
    ultimate_badass_pool_legendary_1 = '1'
    ultimate_badass_pool_legendary_2 = '0.5'
    ultimate_badass_pool_legendary_3 = '0.25'
    ultimate_badass_pool_epicchest_1 = '1'
    ultimate_badass_pool_epicchest_2 = '0.5'
    ultimate_badass_pool_epicchest_3 = '0.5'

    # Unique drop quantities.  Some of these are pretty high in my "default"
    # configuration, so putting them here lets me override them in the other
    # configs, easily.
    quantity_chubby = '4'
    quantity_terra = '7'
    quantity_vermivorous = '5'
    quantity_warrior = '8'
    quantity_hyperius_legendary = '7'
    quantity_hyperius_seraph = '4'
    quantity_gee_seraph = '4'
    quantity_gee_legendary = '6'

    # Voracidous quantities have to be done slightly differently, because both
    # Dexiduous and Voracidous use the same Seraph and Legendary pools for their
    # unique drops, but Dexi calls it multiple times, whereas Vorac just calls
    # it the once (by default).  So upping the quantity for Vorac makes Dexi's
    # drops totally ludicrous.  So instead, we're just gonna specify the pool
    # multiple times in Vorac's ItemPool.  This is lame, but should let both
    # of them coexist.
    voracidous_drop_seraph_1 = '1'
    voracidous_drop_seraph_2 = '1'
    voracidous_drop_seraph_3 = '1'
    voracidous_drop_seraph_4 = '1'
    voracidous_drop_legendary_1 = '1'
    voracidous_drop_legendary_2 = '1'
    voracidous_drop_legendary_3 = '1'
    voracidous_drop_legendary_4 = '1'

    # 2x chance of both kinds of moonstone
    moonstone_drop = '0.1'          # Stock: 0.050000
    moonstone_cluster_drop = '0.05' # Stock: 0.025000

    # Gun Type drop weights.  Note that because these values are going into
    # our hotfix object, these variables *cannot* be successfully overridden
    # in an extending class.
    drop_prob_pistol = 100
    drop_prob_ar = 100
    drop_prob_smg = 100
    drop_prob_shotgun = 100
    drop_prob_sniper = 80
    drop_prob_launcher = 40

# The profiles we'll generate
profiles = [
    ConfigLootsplosion(),
    ]

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

# Some alternate vars from a mutually-exclusive area - merely improve
# the drop rate, rather than making it 100%
loot_drop_chance_1p_alt = '0.170000'    # Stock: 0.085000
loot_drop_chance_2p_alt = '0.140000'    # Stock: 0.070000
loot_drop_chance_3p_alt = '0.120000'    # Stock: 0.060000
loot_drop_chance_4p_alt = '0.100000'    # Stock: 0.050000

# Force Pool_GunsAndGear to always drop the specified pool, if `force_gunsandgear_drop`
# is True.  Useful for testing out how individual pools are behaving.
force_gunsandgear_drop = False
force_gunsandgear_drop_type = 'GD_Itempools.WeaponPools.Pool_Weapons_All'

# Force Pool_GunsAndGear to always drop the specified item, if
# `force_gunsandgear_specific` is True.  Useful for seeing what exactly an
# item is.  `force_gunsandgear_specific` will override `force_gunsandgear_drop`,
# if both are set to True.
force_gunsandgear_specific = False
force_gunsandgear_specific_classtype = 'WeaponBalanceDefinition'
#force_gunsandgear_specific_classtype = 'InventoryBalanceDefinition'
force_gunsandgear_specific_names = [
    'GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr',
    'GD_Petunia_Weapons.Snipers.Sniper_Jakobs_3_Plunkett',
    ]

###
### Hotfixes; these are handled a little differently than everything
### else.
###

# Guaranteed Luneshine for Unique/Legendary weapons.  This is generated
# automatically by `gen_guaranteed_luneshine.py`.  Note that removing the
# "None" Luneshine attachment entirely would result in vanilla guns being
# removed from inventory, if loaded with this mod active, but we're okay
# if we just set `bDisabled` to `True`.
hfs.add_level_hotfix('guaranteed_luneshine_0',
    'GuaranteedLuneshine',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom:WeaponPartListCollectionDefinition_23,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_1',
    'GuaranteedLuneshine',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBreaker:WeaponPartListCollectionDefinition_27,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_2',
    'GuaranteedLuneshine',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Torgue_5_KerBoom:WeaponPartListCollectionDefinition_31,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_3',
    'GuaranteedLuneshine',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier:WeaponPartListCollectionDefinition_35,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_4',
    'GuaranteedLuneshine',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Jakobs_3_Wallop:WeaponPartListCollectionDefinition_36,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_5',
    'GuaranteedLuneshine',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_6',
    'GuaranteedLuneshine',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_IceScream:WeaponPartListCollectionDefinition_38,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_7',
    'GuaranteedLuneshine',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful:WeaponPartListCollectionDefinition_39,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_8',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_Ricochet:WeaponPartListCollectionDefinition_52,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_9',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Old_Hyperion_5_Excalibastard:WeaponPartListCollectionDefinition_53,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_10',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Tediore_5_Tesla:WeaponPartListCollectionDefinition_54,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_11',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Dahl_3_Firestarta:WeaponPartListCollectionDefinition_56,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_12',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining:WeaponPartListCollectionDefinition_57,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_13',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_Blizzard:WeaponPartListCollectionDefinition_58,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_14',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_VibraPulse:WeaponPartListCollectionDefinition_59,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_15',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Egun:WeaponPartListCollectionDefinition_8,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_16',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie:WeaponPartListCollectionDefinition_60,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_17',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_SavorySideSaber:WeaponPartListCollectionDefinition_61,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_18',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Tediore_3_Vandergraffen:WeaponPartListCollectionDefinition_62,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_19',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom:WeaponPartListCollectionDefinition_66,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_20',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_Thingy:WeaponPartListCollectionDefinition_67,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_21',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Cryophobia:WeaponPartListCollectionDefinition_71,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_22',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem:WeaponPartListCollectionDefinition_75,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_23',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol:WeaponPartListCollectionDefinition_79,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_24',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Tediore_3_Rocketeer:WeaponPartListCollectionDefinition_81,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_25',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer:WeaponPartListCollectionDefinition_82,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_26',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Zim:WeaponPartListCollectionDefinition_86,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_27',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Blowfly:WeaponPartListCollectionDefinition_90,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_28',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie:WeaponPartListCollectionDefinition_94,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_29',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang:WeaponPartListCollectionDefinition_98,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_30',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_88Fragnum:WeaponPartListCollectionDefinition_102,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_31',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead:WeaponPartListCollectionDefinition_103,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_32',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber:WeaponPartListCollectionDefinition_106,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_33',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Globber:WeaponPartListCollectionDefinition_107,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_34',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist:WeaponPartListCollectionDefinition_108,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_35',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Smasher:WeaponPartListCollectionDefinition_109,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_36',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe:WeaponPartListCollectionDefinition_11,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_37',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent:WeaponPartListCollectionDefinition_141,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_38',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch:WeaponPartListCollectionDefinition_145,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_39',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire:WeaponPartListCollectionDefinition_149,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_40',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF:WeaponPartListCollectionDefinition_153,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_41',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder:WeaponPartListCollectionDefinition_157,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_42',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch:WeaponPartListCollectionDefinition_158,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_43',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch:WeaponPartListCollectionDefinition_159,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_44',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun:WeaponPartListCollectionDefinition_113,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_45',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall:WeaponPartListCollectionDefinition_117,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_46',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker:WeaponPartListCollectionDefinition_121,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_47',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker:WeaponPartListCollectionDefinition_125,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_48',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella:WeaponPartListCollectionDefinition_126,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_49',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Moonface:WeaponPartListCollectionDefinition_128,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_50',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup:WeaponPartListCollectionDefinition_131,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_51',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo:WeaponPartListCollectionDefinition_134,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_52',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon:WeaponPartListCollectionDefinition_135,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_53',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Torguemada:WeaponPartListCollectionDefinition_136,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_54',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Wombat:WeaponPartListCollectionDefinition_137,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_55',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork:WeaponPartListCollectionDefinition_167,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_56',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader:WeaponPartListCollectionDefinition_171,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_57',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher:WeaponPartListCollectionDefinition_175,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_58',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Magma:WeaponPartListCollectionDefinition_179,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_59',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek:WeaponPartListCollectionDefinition_184,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_60',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Razorback:WeaponPartListCollectionDefinition_185,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_61',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie:WeaponPartListCollectionDefinition_186,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_62',
    'GuaranteedLuneshine',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine:WeaponPartListCollectionDefinition_187,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_63',
    'GuaranteedLuneshine',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan:WeaponPartListCollectionDefinition_235,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_64',
    'GuaranteedLuneshine',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SG_Torgue_3_Landscaper2:WeaponPartListCollectionDefinition_236,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_65',
    'GuaranteedLuneshine',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker:WeaponPartListCollectionDefinition_237,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_66',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade:WeaponPartListCollectionDefinition_221,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_67',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard:WeaponPartListCollectionDefinition_222,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_68',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_FusionBeam:WeaponPartListCollectionDefinition_223,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_69',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Laser_Maliwan_5_Thunderfire:WeaponPartListCollectionDefinition_224,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_70',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Laser_Tediore_5_LaserDisker:WeaponPartListCollectionDefinition_225,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_71',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Jakobs_5_LuckCannon:WeaponPartListCollectionDefinition_226,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_72',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander:WeaponPartListCollectionDefinition_234,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_73',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.RL_Tediore_5_KanedasLaser:WeaponPartListCollectionDefinition_227,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_74',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.SG_Jakobs_5_Flayer:WeaponPartListCollectionDefinition_238,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_75',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode:WeaponPartListCollectionDefinition_228,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_76',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Sniper_Old_Hyperion_5_OmniCannon:WeaponPartListCollectionDefinition_229,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_77',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Enlightenment:WeaponPartListCollectionDefinition_230,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_78',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Unique.Laser_Maliwan_3_Minac:WeaponPartListCollectionDefinition_231,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_79',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Unique.Pistol_Bandit_3_PartyPopper:WeaponPartListCollectionDefinition_232,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_80',
    'GuaranteedLuneshine',
    ',GD_Ma_Weapons.A_Weapons_Unique.Pistol_Maliwan_3_HardReboot:WeaponPartListCollectionDefinition_233,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_81',
    'GuaranteedLuneshine',
    ',GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun:WeaponPartListCollectionDefinition_202,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_82',
    'GuaranteedLuneshine',
    ',GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Fridgia:WeaponPartListCollectionDefinition_207,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_83',
    'GuaranteedLuneshine',
    ',GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Frostfire:WeaponPartListCollectionDefinition_209,Accessory2PartData.WeightedParts[0].bDisabled,,True')
hfs.add_level_hotfix('guaranteed_luneshine_84',
    'GuaranteedLuneshine',
    ',GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge:WeaponPartListCollectionDefinition_215,Accessory2PartData.WeightedParts[0].bDisabled,,True')

# Adds Luneshine to some unique weapons which didn't have them,
# previously.  This too is autogenerated by `gen_guaranteed_luneshine.py`,
# though I've since edited it slightly to handle the one launcher
# properly.
hfs.add_level_hotfix('luneshine_override_0',
    'LuneshineOverride',
    """,GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace:PartList,Accessory2PartData,,
    (
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
    )""")

for idx, partlist in enumerate([
        'GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Dahl_5_ZX1:PartList',
        'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_CyberColt:PartList',
        'GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Old_Hyperion_BlackSnake:WeaponPartListCollectionDefinition_163',
        'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn:PartList',
        'GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_TooScoops:PartList',
        'GD_Cypressure_Weapons.A_Weapons_Unique.AR_Bandit_3_BossNova:PartList',
        'GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:WeaponPartListCollectionDefinition_282',
        'GD_Petunia_Weapons.SMGs.SMG_Tediore_3_Boxxy:PartList',
        'GD_Petunia_Weapons.Shotguns.SG_Tediore_3_PartyLine:PartList',
        'GD_Petunia_Weapons.Snipers.Sniper_Jakobs_3_Plunkett:WeaponPartListCollectionDefinition_283',
        ]):
    hfs.add_level_hotfix('luneshine_override_{}'.format(idx+1),
        'LuneshineOverride',
        """,{},Accessory2PartData,,
        (
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
        )
        """.format(partlist))

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
    hfs.add_level_hotfix('euphoria_fix_{}'.format(idx),
        'EuphoriaChestFix',
        ',{},{}[{}].ItemAttachments[{}].ItemPool,,GD_Itempools.BuffDrinkPools.Pool_BuffDrinks_HealingRegen'.format(
            classname,
            propname,
            loot_idx,
            attachment_idx,
            ))

###
### Testing hotfixes, not really intended to be used for real.  These
### aren't referenced in the body of the mod, so they'll only activate
### on the standalone version.
###

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
    hfs.add_level_hotfix('cjtestingclear{}'.format(idx), 'cjtestclear',
        ",{},DefaultIncludedLootLists,,()".format(container))
    hfs.add_level_hotfix('cjtestingset{}'.format(idx), 'cjtestset',
        """,{container},DefaultLoot,,
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
#hfs.add_level_hotfix('cjtestmeteor', 'meteor', ",GD_Meteorites.Projectiles.Projectile_Meteorite:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_123.PopulationFactoryPopulationDefinition_1,PopulationDef,,PopulationDefinition'GD_Meteorites.Population.Pop_Meteorite_LootPile_Chest'")
#hfs.add_level_hotfix('cjtestmeteor2', 'meteor', ",GD_Meteorites.Projectiles.Projectile_Meteorite:BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_124.PopulationFactoryPopulationDefinition_0,PopulationDef,,PopulationDefinition'GD_Meteorites.Population.Pop_Meteorite_LootPile_Chest'")

# Chest Overload
#cur_y = 29010
#yaw = '8192'
#chest_type = 'GD_Population_Treasure.TreasureChests.EpicChest_Dahl_Respawning'
#for idx, point in enumerate([31, 32, 33, 34, 35, 36, 37, 20, 22, 24, 25, 26]):
#    hfs.add_level_hotfix('moonstonenew{}type'.format(idx),
#        'mooonstoneloc',
#        "DahlFactory_Boss,DahlFactory_BossDynamic.TheWorld:PersistentLevel.PopulationOpportunityPoint_{},PopulationDef,,PopulationDefinition'{}'".format(point, chest_type))
#    hfs.add_level_hotfix('moonstonenew{}x'.format(idx),
#        'mooonstoneloc',
#        'DahlFactory_Boss,DahlFactory_BossDynamic.TheWorld:PersistentLevel.PopulationOpportunityPoint_{},Location.X,,-16778'.format(point))
#    hfs.add_level_hotfix('moonstonenew{}y'.format(idx),
#        'mooonstoneloc',
#        'DahlFactory_Boss,DahlFactory_BossDynamic.TheWorld:PersistentLevel.PopulationOpportunityPoint_{},Location.Y,,{}'.format(point, cur_y))
#    hfs.add_level_hotfix('moonstonenew{}z'.format(idx),
#        'mooonstoneloc',
#        'DahlFactory_Boss,DahlFactory_BossDynamic.TheWorld:PersistentLevel.PopulationOpportunityPoint_{},Location.Z,,5920'.format(point))
#    hfs.add_level_hotfix('moonstonenew{}yaw'.format(idx),
#        'mooonstoneloc',
#        'DahlFactory_Boss,DahlFactory_BossDynamic.TheWorld:PersistentLevel.PopulationOpportunityPoint_{},Rotation.Yaw,,{}'.format(point, yaw))
#    cur_y += 200

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

###
### Everything below this point is constructing the actual patch file
###

# Process our forced GunsAndGear drop
gunsandgear_drop_str = ''
if force_gunsandgear_specific:
    specific_bits = []
    for specific_name in force_gunsandgear_specific_names:
        specific_bits.append("""            (
                ItmPoolDefinition=None,
                InvBalanceDefinition={force_gunsandgear_specific_classtype}'{specific_name}',
                Probability=(
                    BaseValueConstant=1.000000,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )""".format(
                force_gunsandgear_specific_classtype=force_gunsandgear_specific_classtype,
                specific_name=specific_name,
                ))
    specific_pool_contents = ",\n".join(specific_bits)

    if len(force_gunsandgear_specific_names) == 1:
        desc_string = force_gunsandgear_specific_names[0]
    else:
        desc_string = '{} (and others)'.format(force_gunsandgear_specific_names[0])

    gunsandgear_drop_str = """
    #<Force GunsAndGearDrop to {desc_string}>

        # Forces the GunsAndGear drop pool to always drop {desc_string}
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
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1.000000
                ),
                bDropOnDeath=True
            )
        )

        set {force_gunsandgear_drop_type} BalancedItems
        (
{specific_pool_contents}
        )

    #</Force GunsAndGearDrop to {desc_string}>
    """.format(
        desc_string=desc_string,
        force_gunsandgear_drop_type=force_gunsandgear_drop_type,
        specific_pool_contents=specific_pool_contents,
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
drop_chance_str_source = """

        #<{adjective} Enemy Loot Drop Chance{drop_wording}>

            {drop_comment}# Gives {description} chance to drop loot from enemies.{drop_off}
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

        #</{adjective} Enemy Loot Drop Chance{drop_wording}>"""

drop_quantity_str_source = """
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

    #</Extreme Enemy Loot Drop Quantity{drop_wording}>"""

# Guaranteed drop chance string
test_drop_chance_guaranteed_str = drop_chance_str_source.format(
        adjective='Guaranteed',
        description='a 100%',
        drop_comment=drop_comment,
        drop_off=drop_off,
        drop_wording=drop_wording,
        loot_drop_chance_1p=loot_drop_chance_1p,
        loot_drop_chance_2p=loot_drop_chance_2p,
        loot_drop_chance_3p=loot_drop_chance_3p,
        loot_drop_chance_4p=loot_drop_chance_4p,
    )

# Merely improved drop chance string
test_drop_chance_improved_str = drop_chance_str_source.format(
        adjective='Improved',
        description='a doubled',
        drop_comment='#',
        drop_off='    <off>',
        drop_wording=' (disabled by default)',
        loot_drop_chance_1p=loot_drop_chance_1p_alt,
        loot_drop_chance_2p=loot_drop_chance_2p_alt,
        loot_drop_chance_3p=loot_drop_chance_3p_alt,
        loot_drop_chance_4p=loot_drop_chance_4p_alt,
    )

# Concatenate our drop chance stanzas in one mutually-exclusive folder
test_drop_chance_str = """
    #<Enemy Loot Drop Chance Modification (choose one){drop_wording}><MUT>
{test_drop_chance_guaranteed_str}
{test_drop_chance_improved_str}

    #</Enemy Loot Drop Chance Modification (choose one){drop_wording}>
""".format(
        drop_wording=drop_wording,
        test_drop_chance_guaranteed_str=test_drop_chance_guaranteed_str,
        test_drop_chance_improved_str=test_drop_chance_improved_str,
    )

# Test drop quantity string
test_drop_quantity_str = drop_quantity_str_source.format(
        drop_comment=drop_comment,
        drop_off=drop_off,
        drop_wording=drop_wording,
        loot_drop_quantity=loot_drop_quantity,
    )

# Now read in our main input file
with open(input_filename, 'r') as df:
    loot_str = df.read()

# Loop through our profiles and generate the files
for profile in profiles:

    # Write our UCP-compatible version
    with open(profile.filename(mod_name, variant_ucp), 'w') as df:
        df.write(loot_str.format(
            mod_name=mod_name,
            mod_version=mod_version,
            variant_name=variant_ucp,
            config=profile,
            hotfixes=hfs,
            hotfix_gearbox_base='',
            hotfix_transient_defs='',
            gunsandgear_drop_str=gunsandgear_drop_str,
            test_drop_chance_str=test_drop_chance_str,
            test_drop_quantity_str=test_drop_quantity_str,
            ))
    print('Wrote UCP-compatible ({}) mod file to: {}'.format(
        profile.profile_name,
        profile.filename(mod_name, variant_ucp),
        ))

    # Write to a standalone offline file
    with open(profile.filename(mod_name, variant_offline), 'w') as df:
        df.write(loot_str.format(
            mod_name=mod_name,
            mod_version=mod_version,
            variant_name=variant_offline,
            config=profile,
            hotfixes=hfs,
            hotfix_gearbox_base=hfs.get_gearbox_hotfix_xml(),
            hotfix_transient_defs=hfs.get_transient_defs(offline=True),
            gunsandgear_drop_str=gunsandgear_drop_str,
            test_drop_chance_str=test_drop_chance_str,
            test_drop_quantity_str=test_drop_quantity_str,
            ))
    print('Wrote standalone offline ({}) mod file to: {}'.format(
        profile.profile_name,
        profile.filename(mod_name, variant_offline),
        ))
