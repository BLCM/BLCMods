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

    # Custom weapon drop scaling
    weapon_base_common = '8'
    weapon_base_uncommon = '85'
    weapon_base_rare = '65'
    weapon_base_veryrare = '50'
    weapon_base_glitch = '8'
    weapon_base_legendary = '2'

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
    com_base_legendary = '5'

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
    boss_drop_uniques = '1.0'
    boss_drop_rares = '1.0'

    # Drop rates for "regular" treasure chests
    treasure_base_common = '0'
    treasure_base_uncommon = '0'
    treasure_base_rare = '30'
    treasure_base_veryrare = '60'
    treasure_base_glitch = '10'
    treasure_base_legendary = '4'

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = '0'
    epic_base_rare = '0'
    epic_base_veryrare = '1.4'
    epic_base_glitch = '.6'
    epic_base_legendary = '0.2'
    epic_base_legendary_dbl = '0.4'

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = '0'
    epic_glitch_base_rare = '0'
    epic_glitch_base_veryrare = '0.9'
    epic_glitch_base_glitch = '1.1'
    epic_glitch_base_legendary_dbl = '0.5'

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = '0.4'
    badass_pool_glitch = '0.3'
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

    # 2x chance of both kinds of moonstone
    moonstone_drop = '0.1'          # Stock: 0.050000
    moonstone_cluster_drop = '0.05' # Stock: 0.025000

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

class ConfigReasonable(ConfigLootsplosion):
    """
    Alternate config which has slightly-more-reasonable drop rates for stuff
    like legendaries.  Unsurprisingly, most folks find my default values a
    bit excessive.
    """

    profile_name = 'Reasonable Drops'

    # Weapon drops
    weapon_base_common = '32.75'
    weapon_base_uncommon = '35'
    weapon_base_rare = '25'
    weapon_base_veryrare = '5'
    weapon_base_glitch = '2'
    weapon_base_legendary = '0.25'

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
    boss_drop_uniques = '0.5'
    boss_drop_rares = '0.25'

    # Drop rates for "regular" treasure chests
    treasure_base_common = '32.5'
    treasure_base_uncommon = '40'
    treasure_base_rare = '20'
    treasure_base_veryrare = '5'
    treasure_base_glitch = '3'
    treasure_base_legendary = '0.5'

    # Drop rates for "epic" treasure chests
    epic_base_uncommon = '25'
    epic_base_rare = '49'
    epic_base_veryrare = '20'
    epic_base_glitch = '5'
    epic_base_legendary = '1'
    epic_base_legendary_dbl = '2'

    # Drop rates for Glitched Epic treasure chests.  This is basically just
    # the same as regular, but with increased probabilities for Glitch.
    epic_glitch_base_uncommon = '25'
    epic_glitch_base_rare = '49'
    epic_glitch_base_veryrare = '10'
    epic_glitch_base_glitch = '15'
    epic_glitch_base_legendary_dbl = '2'

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = '0.2'
    badass_pool_glitch = '0.15'
    badass_pool_epicchest = '0.1'

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = '1'
    super_badass_pool_veryrare = '0.4'
    super_badass_pool_glitch = '0.15'
    super_badass_pool_legendary = '.03'
    super_badass_pool_epicchest = '1'

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = '1'
    ultimate_badass_pool_veryrare_2 = '0'
    ultimate_badass_pool_glitch_1 = '0.4'
    ultimate_badass_pool_glitch_2 = '0'
    ultimate_badass_pool_legendary_1 = '0.08'
    ultimate_badass_pool_legendary_2 = '0'
    ultimate_badass_pool_legendary_3 = '0'
    ultimate_badass_pool_epicchest_1 = '1'
    ultimate_badass_pool_epicchest_2 = '1'
    ultimate_badass_pool_epicchest_3 = '1'

# The profiles we'll generate
profiles = [
    ConfigLootsplosion(),
    ConfigReasonable(),
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
force_gunsandgear_drop_type = 'GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary'

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

# Remove bias for dropping Pistols in the main game.  Also buffs drop rates
# for snipers, lasers, and launchers, though it does not bring them up to the
# level of pistols/ARs/SMGs/shotguns.  This could be done with a `set`
# statement, but this is more concise.
for (number, rarity) in [
        ('01', 'Common'),
        ('02', 'Uncommon'),
        ('04', 'Rare'),
        ('05', 'VeryRare'),
        ('06', 'Legendary'),
        ]:
    for (idx, (guntype, gunprob)) in enumerate([
            ('Pistol', ConfigLootsplosion.drop_prob_pistol),
            ('AR', ConfigLootsplosion.drop_prob_ar),
            ('SMG', ConfigLootsplosion.drop_prob_smg),
            ('Shotgun', ConfigLootsplosion.drop_prob_shotgun),
            ('Sniper', ConfigLootsplosion.drop_prob_sniper),
            ('Launcher', ConfigLootsplosion.drop_prob_launcher),
            ('Laser', ConfigLootsplosion.drop_prob_laser),
            ]):
        hfs.add_level_hotfix('normalize_weapon_types_{}_{}'.format(rarity, guntype),
            'NormWeap{}{}'.format(rarity, guntype),
            ',GD_Itempools.WeaponPools.Pool_Weapons_All_{}_{},BalancedItems[{}].Probability.BaseValueConstant,,{}'.format(
                number,
                rarity,
                idx,
                gunprob))

# Fix legendary Class Mod pool.  We would usually do this via `set`, but
# some hotfix-like behavior in the character DLCs ends up resetting the
# pool and ignoring any changes we'd made with `set`, so we must hotfix,
# instead.
hfs.add_level_hotfix('legendary_com_fix', 'LegendaryCOMs',
    """,GD_Itempools.ClassModPools.Pool_ClassMod_06_Legendary,BalancedItems,,
    (
        (
            ItmPoolDefinition=None, 
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness_05_Legendary', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Quince_ItemGrades.ClassMods.BalDef_ClassMod_Doppelganger_05_Legendary', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Enforcer_05_Legendary', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Prototype_05_Legendary', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Gladiator_05_Legendary', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Lawbringer_05_Legendary', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness_07_ChroniclerOfElpis', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Doppel_07_Chronicler', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Enforcer_07_Chronicler', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Gladiator_07_Chronicler', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Lawbringer_07_Chronicler', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Prototype_07_Chronicler', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Enforcer_06_EridianVanquisher', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Gladiator_06_EridianVanquisher', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Lawbringer_06_EridianVanquisher', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Prototype_06_EridianVanquisher', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness_06_EridianVanquisher', 
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
            InvBalanceDefinition=InventoryBalanceDefinition'GD_Quince_ItemGrades.ClassMods.BalDef_ClassMod_Doppelganger_06_EridianVanquisher', 
            Probability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None,
                BaseValueScaleConstant=1.000000 
            ), 
            bDropOnDeath=True 
        )
    )
    """)

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

# Locker drop tweaks.  This could be done via `set` but using a hotfix lets us
# be much more concise.
hfs.add_level_hotfix('locker_loot_shield',
    'LockerLoot',
    """,GD_Itempools.ListDefs.StorageLockerLoot,
    LootData[4].ItemAttachments[0].ItemPool,,
    ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare'""")
hfs.add_level_hotfix('locker_loot_grenade',
    'LockerLoot',
    """,GD_Itempools.ListDefs.StorageLockerLoot,
    LootData[5].ItemAttachments[1].ItemPool,,
    ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_04_Rare'""")

# Better Safes
hfs.add_level_hotfix('better_safes', 'BetterSafes',
    """,GD_Balance_Treasure.LootableGrades.ObjectGrade_Safe,DefaultLoot,,
    (
        ( 
            ConfigurationName="Moonstone", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo4" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo3" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Eridium", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone_Cluster', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo4" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo3" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Safe_Cash", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo3" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo4" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.800000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Grenade", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_3_Uncommoner', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.GrenadeModPools.Pool_GrenadeMods_06_Legendary', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Grenade" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Grenades', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Shield" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Grenades', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Shield", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_3_Uncommoner', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Shield" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.MoonItemPools.Pool_MoonItem_06_Legendary', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=0.500000 
                    ), 
                    AttachmentPointName="Grenade" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ) 
            ) 
        ),
        ( 
            ConfigurationName="Pistol", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_3_Uncommoner', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Grenade" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_Repeater', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Shield" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo1" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo2" 
                ), 
                ( 
                    ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1_BIG', 
                    PoolProbability=( 
                        BaseValueConstant=1.000000, 
                        BaseValueAttribute=None, 
                        InitializationDefinition=None, 
                        BaseValueScaleConstant=1.000000 
                    ), 
                    AttachmentPointName="Ammo5" 
                ) 
            ) 
        )
    )
    """)

# Normalization of one of the final boss drop pools
hfs.add_level_hotfix('final_boss_norm_0', 'FinalBossLootNorm',
    ',GD_Itempools.Runnables.Pool_FinalBoss_Head,BalancedItems[0].Probability.InitializationDefinition,,None')
hfs.add_level_hotfix('final_boss_norm_1', 'FinalBossLootNorm',
    ',GD_Itempools.Runnables.Pool_FinalBoss_Head,BalancedItems[1].Probability.InitializationDefinition,,None')
hfs.add_level_hotfix('final_boss_raid_norm_0', 'FinalBossLootNorm',
    ',GD_Itempools.Runnables.Pool_FinalBossRaid_Head,BalancedItems[0].Probability.InitializationDefinition,,None')
hfs.add_level_hotfix('final_boss_raid_norm_1', 'FinalBossLootNorm',
    ',GD_Itempools.Runnables.Pool_FinalBossRaid_Head,BalancedItems[1].Probability.InitializationDefinition,,None')

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

# Unlock rocket launcher ammo at level 1.  It's possible this can be done
# with `set`, but I like being able to cherry-pick what I'm changing

hfs.add_level_hotfix('rocket_vending', 'RocketVending',
    """,GD_ItemGrades.Ammo_Shop.ItemGrade_AmmoShop_RocketLauncher,
    Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage,,1""")

hfs.add_level_hotfix('rocket_drops', 'RocketDrops',
    """,GD_ItemGrades.Ammo.ItemGrade_Ammo_RocketLauncher,
    Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage,,1""")

hfs.add_level_hotfix('grenade_vending', 'GrenadeVending',
    """,GD_ItemGrades.Ammo_Shop.ItemGrade_AmmoShop_Grenade,
    Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage,,1""")

hfs.add_level_hotfix('grenade_drops', 'GrenadeDrops',
    """,GD_ItemGrades.Ammo.ItemGrade_Ammo_Grenade,
    Manufacturers[0].Grades[0].GameStageRequirement.MinGameStage,,1""")

# Nerfs for some enemies' drops which get inappropriately buffed by the rest of this mod.
# (basically just setting them back to their default values, but without reference to
# constants)
hfs.add_level_hotfix('nerf_drop_badass_kraggon', 'NerfDrops',
    """,GD_Cork_Population_EleBeast.Balance.PawnBalance_ElementalSpitterBadass,DefaultItemPoolList[0].PoolProbability,,
    (
        BaseValueConstant=0.100000, 
        BaseValueAttribute=None,
        InitializationDefinition=None, 
        BaseValueScaleConstant=1.000000 
    )
    """)
hfs.add_level_hotfix('nerf_drop_tork_dredger', 'NerfDrops',
    """,GD_Population_Tork.Balance.PawnBalance_TorkDredger,DefaultItemPoolList[0].PoolProbability,,
    (
        BaseValueConstant=0.100000, 
        BaseValueAttribute=None,
        InitializationDefinition=None, 
        BaseValueScaleConstant=0.125000 
    )
    """)
# This one's slightly different - there's a duplicate pool definition, so we're disabling
# one of them entirely.
hfs.add_level_hotfix('nerf_drop_guard_clapdog', 'NerfDrops',
    """,GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_ClapDawg,DefaultItemPoolList[0].PoolProbability,,
    (
        BaseValueConstant=0.000000, 
        BaseValueAttribute=None,
        InitializationDefinition=None, 
        BaseValueScaleConstant=0.000000 
    )
    """)

# Make FlameKnuckle drop from the badass pool on playthrough 1.  UCP has a statement to
# make him drop the Nukem already, so we won't bother with that.
hfs.add_level_hotfix('flameknuckle_badass', 'FlameKnuckleBadass',
    """MoonShotIntro_P,GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlSergeantFlameKnuckle,
    PlayThroughs[0].CustomItemPoolIncludedLists,,
    (
        ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear'
    )
    """)

# Improve Nel's loot
for idx in [15, 16, 17, 18, 19, 20, 21]:
    hfs.add_level_hotfix('nel_drops_{}'.format(idx),
        'NelDrops',
        """Deadsurface_P,
        GD_Nel.Population.PawnBalance_Nel,
        DefaultItemPoolList[{}].ItemPool,,
        ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear'""".format(idx))

# Optional hotfixes which let us generate common pistols, for the mission
# To Arms!, which is otherwise, amusingly, one of the more difficult missions
# when using this mod.

# First up: the three BanditAmmo containers in the dead drop room will convert
# to being ozkit crates, and get moved around a bit

hfs.add_level_hotfix('toarms_banditammo_type_0', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_31,
    PopulationDef,,
    PopulationDefinition'GD_Population_Treasure.Lootables.Crate_Military_OzKitsOnly'""",
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_loc_0', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_31,
    Location,,
    (
        X=-8960,
        Y=10660,
        Z=-948.618042
    )
    """,
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_rot_0', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_31,
    Rotation,,
    (
        Pitch=45,
        Yaw=-33960,
        Roll=94
    )
    """,
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_type_1', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_24,
    PopulationDef,,
    PopulationDefinition'GD_Population_Treasure.Lootables.Crate_Military_OzKitsOnly'""",
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_loc_1', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_24,
    Location,,
    (
        X=-9160,
        Y=10630,
        Z=-948.618042
    )
    """,
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_rot_1', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_24,
    Rotation,,
    (
        Pitch=68, 
        Yaw=-30284, 
        Roll=77 
    )
    """,
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_type_2', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_4,
    PopulationDef,,
    PopulationDefinition'GD_Population_Treasure.Lootables.Crate_Military_OzKitsOnly'""",
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_loc_2', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_4,
    Location,,
    (
        X=-8493,
        Y=10731,
        Z=-948.618042
    )
    """,
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_rot_2', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_4,
    Rotation,,
    (
        Pitch=0, 
        Yaw=14931, 
        Roll=0 
    )
    """,
    activated=False)

# Next: steal one more BanditAmmo container from on top of the Darksiders'
# tower

hfs.add_level_hotfix('toarms_banditammo_type_3', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_146,
    PopulationDef,,
    PopulationDefinition'GD_Population_Treasure.Lootables.Crate_Military_OzKitsOnly'""",
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_loc_3', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_146,
    Location,,
    (
        X=-8443,
        Y=10531,
        Z=-948.618042
    )
    """,
    activated=False)

hfs.add_level_hotfix('toarms_banditammo_rot_3', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_146,
    Rotation,,
    (
        Pitch=0, 
        Yaw=17931, 
        Roll=0 
    )
    """,
    activated=False)

# Next: the original ozkit crates will get switched to being just ordinary
# Crate_Military.

hfs.add_level_hotfix('toarms_ozchange0', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_85,
    PopulationDef,,
    PopulationDefinition'GD_Population_Treasure.Lootables.Crate_Military'""",
    activated=False)

hfs.add_level_hotfix('toarms_ozchange1', 'ToArmsChanges',
    """Moon_P,
    Moon_P.TheWorld:PersistentLevel.WillowPopulationOpportunityPoint_367,
    PopulationDef,,
    PopulationDefinition'GD_Population_Treasure.Lootables.Crate_Military'""",
    activated=False)

# Improve Zarpedon's chest
hfs.add_level_hotfix('zarpedon_stash', 'ZarpedonStash',
    """Wreck_P,
    GD_Balance_Treasure.ChestGradesUnique.Balance_Chest_ZarpedonsStash,
    DefaultLoot[0].ItemAttachments,,
    (
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_CybercColt', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Gun1" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_LongGuns', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Gun2" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Ammo1" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Ammo2" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Ammo3" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_DropAlways', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Ammo4" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Grenade1" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Grenade2" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Grenade3" 
        ), 
        ( 
            ItemPool=ItemPoolDefinition'GD_Itempools.Treasure_ChestPools.Pool_EpicChest_GrenadeMods', 
            PoolProbability=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=None, 
                BaseValueScaleConstant=1.000000 
            ), 
            InvBalanceDefinition=None, 
            AttachmentPointName="Grenade4" 
        ) 
    ) 
    """)

# Nerf Felicity Rampant drops, a bit
hfs.add_level_hotfix('felicity_drop_nerf_0', 'FelicityDropNerf',
    """DahlFactory_Boss,
    GD_ProtoWarBot_CoreBody.Character.AIDef_ProtoWarBot_CoreBody:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_10,
    ItemPoolIncludedLists[0],,
    ItemPoolListDefinition'GD_Itempools.ListDefs.StandardEnemyGunsAndGear'""")
hfs.add_level_hotfix('felicity_drop_nerf_1', 'FelicityDropNerf',
    """DahlFactory_Boss,
    GD_ProtoWarBot_CoreBody.Character.AIDef_ProtoWarBot_CoreBody:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_11,
    ItemPoolIncludedLists,,
    (ItemPoolListDefinition'GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear')""")
hfs.add_level_hotfix('felicity_drop_nerf_2', 'FelicityDropNerf',
    """DahlFactory_Boss,
    GD_ProtoWarBot_CoreBody.Character.AIDef_ProtoWarBot_CoreBody:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_20,
    ItemPoolIncludedLists[0],,
    ItemPoolListDefinition'GD_Itempools.ListDefs.StandardEnemyGunsAndGear'""")
hfs.add_level_hotfix('felicity_drop_nerf_3', 'FelicityDropNerf',
    """DahlFactory_Boss,
    GD_ProtoWarBot_CoreBody.Character.AIDef_ProtoWarBot_CoreBody:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_21,
    ItemPoolIncludedLists,,
    (ItemPoolListDefinition'GD_Itempools.ListDefs.SuperBadassEnemyGunsAndGear')""")

# Improves the "Picking up the Pieces" laser chest a bit.
hfs.add_level_hotfix('laser_chest_0', 'LaserChestBuff',
    """RandDFacility_P,
    GD_Co_Side_PickingUp_Data.ListDefs.WeaponChestLaser,
    LootData[0].ItemAttachments[0].ItemPool,,
    ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare'""")
hfs.add_level_hotfix('laser_chest_1', 'LaserChestBuff',
    """RandDFacility_P,
    GD_Co_Side_PickingUp_Data.ListDefs.WeaponChestLaser,
    LootData[0].ItemAttachments[1].ItemPool,,
    ItemPoolDefinition'GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare'""")

# Exhaustive early-game weapon unlocks.  Generated by `part_unlock.py` using
# ft-explorer data.
hfs.add_level_hotfix('part_unlock_0', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_1', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_2', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_3', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_4', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_5', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_6', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_7', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_8', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_9', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_10', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_11', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_12', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_13', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_14', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_15', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_16', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_17', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_18', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_19', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_20', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_21', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_22', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_23', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_24', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_25', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_26', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_27', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_28', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_29', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_30', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_31', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_32', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_33', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_34', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_35', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_36', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_37', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_38', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_39', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_40', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_41', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_42', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_43', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_44', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_45', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_46', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_47', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_48', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_49', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_50', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_51', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_52', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_53', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_54', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_55', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_56', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_57', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_58', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_59', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_60', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_61', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_62', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_63', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_64', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_65', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_66', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_67', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_68', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_69', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_70', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_71', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_72', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_73', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_74', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_75', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_76', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_77', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_78', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_79', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_80', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_81', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_82', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_83', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_84', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_85', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_86', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_87', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_88', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_89', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_90', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_91', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_92', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_93', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_94', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_95', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_96', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_97', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_98', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_99', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_100', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_101', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_102', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_103', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_104', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_105', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_106', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_107', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_108', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_109', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_110', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_111', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_112', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_113', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_114', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_115', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_116', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_117', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_118', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_119', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_120', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_0,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_121', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_0,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_122', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_0,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_123', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_124', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_125', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_126', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_127', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_5,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_128', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_129', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_130', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_131', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_132', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_3_Rare:WeaponPartListCollectionDefinition_6,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_133', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_134', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_135', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_136', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_137', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_7,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_138', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_3_Rare:WeaponPartListCollectionDefinition_10,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_139', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_3_Rare:WeaponPartListCollectionDefinition_10,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_140', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_3_Rare:WeaponPartListCollectionDefinition_10,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_141', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe:WeaponPartListCollectionDefinition_11,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_142', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe:WeaponPartListCollectionDefinition_11,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_143', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe:WeaponPartListCollectionDefinition_11,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_144', 'PartUnlock',
    ',GD_Co_ToroToroData.A_Weapons_Unique.MW_Co_Probe:WeaponPartListCollectionDefinition_12,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_145', 'PartUnlock',
    ',GD_Co_ToroToroData.A_Weapons_Unique.MW_Co_Probe:WeaponPartListCollectionDefinition_12,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_146', 'PartUnlock',
    ',GD_Co_ToroToroData.A_Weapons_Unique.MW_Co_Probe:WeaponPartListCollectionDefinition_12,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_147', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_20,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_148', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_20,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_149', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_20,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_150', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_3_Rare:WeaponPartListCollectionDefinition_21,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_151', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_3_Rare:WeaponPartListCollectionDefinition_21,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_152', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_3_Rare:WeaponPartListCollectionDefinition_21,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_153', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_22,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_154', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_22,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_155', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_22,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_156', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom:WeaponPartListCollectionDefinition_23,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_157', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom:WeaponPartListCollectionDefinition_23,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_158', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom:WeaponPartListCollectionDefinition_23,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_159', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_32,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_160', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_32,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_161', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_32,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_162', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_3_Rare:WeaponPartListCollectionDefinition_33,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_163', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_3_Rare:WeaponPartListCollectionDefinition_33,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_164', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_3_Rare:WeaponPartListCollectionDefinition_33,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_165', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_34,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_166', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_34,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_167', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_34,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_168', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier:WeaponPartListCollectionDefinition_35,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_169', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier:WeaponPartListCollectionDefinition_35,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_170', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Vladof_5_Shredifier:WeaponPartListCollectionDefinition_35,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_171', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_172', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_173', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_174', 'PartUnlock',
    ',gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_Hail:WeaponPartListCollectionDefinition_37,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_175', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_176', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_177', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_178', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_179', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_40,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_180', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_181', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_182', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_183', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_184', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_3_Rare:WeaponPartListCollectionDefinition_41,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_185', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_186', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_187', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_188', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_189', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_42,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_190', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_191', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_192', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_193', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_194', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_43,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_195', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_196', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_197', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_198', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_199', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_3_Rare:WeaponPartListCollectionDefinition_44,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_200', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_201', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_202', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_203', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_204', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_45,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_205', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_206', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_207', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_208', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_209', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_46,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_210', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_211', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_212', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_213', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_214', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_47,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_215', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_216', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_217', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_218', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_219', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_48,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_220', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_221', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_222', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_223', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_224', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_49,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_225', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_226', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_227', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_228', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50,ConsolidatedAttributeInitData[8].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_229', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_3_Rare:WeaponPartListCollectionDefinition_50,ConsolidatedAttributeInitData[9].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_230', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_231', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_232', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_233', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_234', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_51,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_235', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining:WeaponPartListCollectionDefinition_57,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_236', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining:WeaponPartListCollectionDefinition_57,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_237', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Hyperion_3_Mining:WeaponPartListCollectionDefinition_57,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_238', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie:WeaponPartListCollectionDefinition_60,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_239', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie:WeaponPartListCollectionDefinition_60,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_240', 'PartUnlock',
    ',GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_4_Rosie:WeaponPartListCollectionDefinition_60,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_241', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_63,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_242', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_63,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_243', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_63,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_244', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_3_Rare:WeaponPartListCollectionDefinition_64,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_245', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_3_Rare:WeaponPartListCollectionDefinition_64,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_246', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_3_Rare:WeaponPartListCollectionDefinition_64,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_247', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_65,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_248', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_65,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_249', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_65,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_250', 'PartUnlock',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom:WeaponPartListCollectionDefinition_66,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_251', 'PartUnlock',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom:WeaponPartListCollectionDefinition_66,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_252', 'PartUnlock',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom:WeaponPartListCollectionDefinition_66,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_253', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_68,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_254', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_68,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_255', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_68,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_256', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_3_Rare:WeaponPartListCollectionDefinition_69,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_257', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_3_Rare:WeaponPartListCollectionDefinition_69,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_258', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_3_Rare:WeaponPartListCollectionDefinition_69,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_259', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_70,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_260', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_70,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_261', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_70,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_262', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_76,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_263', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_76,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_264', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_76,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_265', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_3_Rare:WeaponPartListCollectionDefinition_77,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_266', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_3_Rare:WeaponPartListCollectionDefinition_77,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_267', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_3_Rare:WeaponPartListCollectionDefinition_77,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_268', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_78,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_269', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_78,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_270', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_78,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_271', 'PartUnlock',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol:WeaponPartListCollectionDefinition_79,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_272', 'PartUnlock',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol:WeaponPartListCollectionDefinition_79,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_273', 'PartUnlock',
    ',GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol:WeaponPartListCollectionDefinition_79,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_274', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_80,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_275', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_80,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_276', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_80,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_277', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_83,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_278', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_83,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_279', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_83,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_280', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_3_Rare:WeaponPartListCollectionDefinition_84,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_281', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_3_Rare:WeaponPartListCollectionDefinition_84,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_282', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_3_Rare:WeaponPartListCollectionDefinition_84,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_283', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_85,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_284', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_85,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_285', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_85,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_286', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_87,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_287', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_87,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_288', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_87,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_289', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_3_Rare:WeaponPartListCollectionDefinition_88,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_290', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_3_Rare:WeaponPartListCollectionDefinition_88,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_291', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_3_Rare:WeaponPartListCollectionDefinition_88,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_292', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_89,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_293', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_89,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_294', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_89,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_295', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_95,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_296', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_95,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_297', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_95,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_298', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_3_Rare:WeaponPartListCollectionDefinition_96,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_299', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_3_Rare:WeaponPartListCollectionDefinition_96,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_300', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_3_Rare:WeaponPartListCollectionDefinition_96,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_301', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_97,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_302', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_97,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_303', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_97,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_304', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang:WeaponPartListCollectionDefinition_98,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_305', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang:WeaponPartListCollectionDefinition_98,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_306', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang:WeaponPartListCollectionDefinition_98,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_307', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead:WeaponPartListCollectionDefinition_103,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_308', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead:WeaponPartListCollectionDefinition_103,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_309', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensOtherHead:WeaponPartListCollectionDefinition_103,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_310', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_104,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_311', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_104,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_312', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_104,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_313', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_3_Rare:WeaponPartListCollectionDefinition_105,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_314', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_3_Rare:WeaponPartListCollectionDefinition_105,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_315', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_3_Rare:WeaponPartListCollectionDefinition_105,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_316', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber:WeaponPartListCollectionDefinition_106,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_317', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber:WeaponPartListCollectionDefinition_106,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_318', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber:WeaponPartListCollectionDefinition_106,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_319', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist:WeaponPartListCollectionDefinition_108,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_320', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist:WeaponPartListCollectionDefinition_108,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_321', 'PartUnlock',
    ',GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist:WeaponPartListCollectionDefinition_108,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_322', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_110,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_323', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_110,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_324', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_110,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_325', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_3_Rare:WeaponPartListCollectionDefinition_111,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_326', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_3_Rare:WeaponPartListCollectionDefinition_111,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_327', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_3_Rare:WeaponPartListCollectionDefinition_111,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_328', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_112,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_329', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_112,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_330', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_112,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_331', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun:WeaponPartListCollectionDefinition_113,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_332', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun:WeaponPartListCollectionDefinition_113,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_333', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun:WeaponPartListCollectionDefinition_113,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_334', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_114,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_335', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_114,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_336', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_114,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_337', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_115,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_338', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_115,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_339', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_115,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_340', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_116,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_341', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_116,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_342', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_116,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_343', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella:WeaponPartListCollectionDefinition_126,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_344', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella:WeaponPartListCollectionDefinition_126,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_345', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Boganella:WeaponPartListCollectionDefinition_126,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_346', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_129,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_347', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_129,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_348', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_129,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_349', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_130,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_350', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_130,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_351', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_130,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_352', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup:WeaponPartListCollectionDefinition_131,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_353', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup:WeaponPartListCollectionDefinition_131,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_354', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Old_Hyperion_3_Bullpup:WeaponPartListCollectionDefinition_131,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_355', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_132,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_356', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_132,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_357', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_132,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_358', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_3_Rare:WeaponPartListCollectionDefinition_133,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_359', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_3_Rare:WeaponPartListCollectionDefinition_133,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_360', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_3_Rare:WeaponPartListCollectionDefinition_133,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_361', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo:WeaponPartListCollectionDefinition_134,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_362', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo:WeaponPartListCollectionDefinition_134,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_363', 'PartUnlock',
    ',GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo:WeaponPartListCollectionDefinition_134,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_364', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_138,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_365', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_138,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_366', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_138,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_367', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_3_Rare:WeaponPartListCollectionDefinition_139,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_368', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_3_Rare:WeaponPartListCollectionDefinition_139,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_369', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_3_Rare:WeaponPartListCollectionDefinition_139,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_370', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_140,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_371', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_140,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_372', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_140,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_373', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent:WeaponPartListCollectionDefinition_141,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_374', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent:WeaponPartListCollectionDefinition_141,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_375', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Torrent:WeaponPartListCollectionDefinition_141,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_376', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_142,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_377', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_142,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_378', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_142,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_379', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_143,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_380', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_143,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_381', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_3_Rare:WeaponPartListCollectionDefinition_143,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_382', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_144,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_383', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_144,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_384', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_144,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_385', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_146,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_386', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_146,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_387', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_146,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_388', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_3_Rare:WeaponPartListCollectionDefinition_147,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_389', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_3_Rare:WeaponPartListCollectionDefinition_147,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_390', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_3_Rare:WeaponPartListCollectionDefinition_147,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_391', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_148,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_392', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_148,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_393', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_148,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_394', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_150,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_395', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_150,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_396', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon:WeaponPartListCollectionDefinition_150,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_397', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_3_Rare:WeaponPartListCollectionDefinition_151,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_398', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_3_Rare:WeaponPartListCollectionDefinition_151,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_399', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_3_Rare:WeaponPartListCollectionDefinition_151,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_400', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_152,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_401', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_152,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_402', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_152,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_403', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF:WeaponPartListCollectionDefinition_153,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_404', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF:WeaponPartListCollectionDefinition_153,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_405', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_IVF:WeaponPartListCollectionDefinition_153,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_406', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_154,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_407', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_154,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_408', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_154,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_409', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_3_Rare:WeaponPartListCollectionDefinition_156,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_410', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_3_Rare:WeaponPartListCollectionDefinition_156,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_411', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_3_Rare:WeaponPartListCollectionDefinition_156,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_412', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder:WeaponPartListCollectionDefinition_157,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_413', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder:WeaponPartListCollectionDefinition_157,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_414', 'PartUnlock',
    ',GD_Cork_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_MeatGrinder:WeaponPartListCollectionDefinition_157,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_415', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_160,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_416', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_160,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_417', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_160,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_418', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_161,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_419', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_161,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_420', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_161,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_421', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_162,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_422', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_162,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_423', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_162,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_424', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_164,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_425', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_164,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_426', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon:WeaponPartListCollectionDefinition_164,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_427', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare:WeaponPartListCollectionDefinition_165,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_428', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare:WeaponPartListCollectionDefinition_165,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_429', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare:WeaponPartListCollectionDefinition_165,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_430', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_166,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_431', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_166,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_432', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare:WeaponPartListCollectionDefinition_166,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_433', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork:WeaponPartListCollectionDefinition_167,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_434', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork:WeaponPartListCollectionDefinition_167,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_435', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork:WeaponPartListCollectionDefinition_167,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_436', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_168,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_437', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_168,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_438', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_168,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_439', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_3_Rare:WeaponPartListCollectionDefinition_169,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_440', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_3_Rare:WeaponPartListCollectionDefinition_169,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_441', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_3_Rare:WeaponPartListCollectionDefinition_169,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_442', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_170,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_443', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_170,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_444', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_170,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_445', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader:WeaponPartListCollectionDefinition_171,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_446', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader:WeaponPartListCollectionDefinition_171,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_447', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader:WeaponPartListCollectionDefinition_171,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_448', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_176,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_449', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_176,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_450', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_2_Uncommon:WeaponPartListCollectionDefinition_176,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_451', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_3_Rare:WeaponPartListCollectionDefinition_177,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_452', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_3_Rare:WeaponPartListCollectionDefinition_177,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_453', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_3_Rare:WeaponPartListCollectionDefinition_177,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_454', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_178,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_455', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_178,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_456', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_178,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_457', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_180,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_458', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_180,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_459', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_180,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_460', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_3_Rare:WeaponPartListCollectionDefinition_181,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_461', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_3_Rare:WeaponPartListCollectionDefinition_181,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_462', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_3_Rare:WeaponPartListCollectionDefinition_181,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_463', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_182,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_464', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_182,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_465', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_182,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_466', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail:WeaponPartListCollectionDefinition_183,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_467', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail:WeaponPartListCollectionDefinition_183,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_468', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Longnail:WeaponPartListCollectionDefinition_183,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_469', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek:WeaponPartListCollectionDefinition_184,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_470', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek:WeaponPartListCollectionDefinition_184,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_471', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek:WeaponPartListCollectionDefinition_184,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_472', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie:WeaponPartListCollectionDefinition_186,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_473', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie:WeaponPartListCollectionDefinition_186,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_474', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie:WeaponPartListCollectionDefinition_186,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_475', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine:WeaponPartListCollectionDefinition_187,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_476', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine:WeaponPartListCollectionDefinition_187,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_477', 'PartUnlock',
    ',GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine:WeaponPartListCollectionDefinition_187,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_478', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_188,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_479', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_188,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_480', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon:WeaponPartListCollectionDefinition_188,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_481', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare:WeaponPartListCollectionDefinition_189,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_482', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare:WeaponPartListCollectionDefinition_189,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_483', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare:WeaponPartListCollectionDefinition_189,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_484', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_190,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_485', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_190,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_486', 'PartUnlock',
    ',GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_190,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_487', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_3_Rare:WeaponPartListCollectionDefinition_192,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_488', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_3_Rare:WeaponPartListCollectionDefinition_192,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_489', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_3_Rare:WeaponPartListCollectionDefinition_192,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_490', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_193,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_491', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_193,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_492', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_193,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_493', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_194,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_494', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_194,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_495', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_194,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_496', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_195,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_497', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_195,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_498', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_195,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_499', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_196,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_500', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_196,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_501', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_196,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_502', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_197,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_503', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_197,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_504', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_197,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_505', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_198,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_506', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_198,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_507', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_198,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_508', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_199,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_509', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_199,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_510', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon:WeaponPartListCollectionDefinition_199,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_511', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_3_Rare:WeaponPartListCollectionDefinition_200,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_512', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_3_Rare:WeaponPartListCollectionDefinition_200,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_513', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_3_Rare:WeaponPartListCollectionDefinition_200,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_514', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_201,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_515', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_201,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_516', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_201,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_517', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_203,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_518', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_203,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_519', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_203,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_520', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_204,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_521', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_204,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_522', 'PartUnlock',
    ',GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_204,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_523', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_206,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_524', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_206,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_525', 'PartUnlock',
    ',GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_206,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_526', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_211,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_527', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_211,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_528', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_2_Uncommon:WeaponPartListCollectionDefinition_211,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_529', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_212,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_530', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_212,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_531', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_3_Rare:WeaponPartListCollectionDefinition_212,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_532', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_213,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_533', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_213,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_534', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_4_VeryRare:WeaponPartListCollectionDefinition_213,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_535', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge:WeaponPartListCollectionDefinition_215,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_536', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge:WeaponPartListCollectionDefinition_215,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_537', 'PartUnlock',
    ',GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge:WeaponPartListCollectionDefinition_215,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_538', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_216,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_539', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_216,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_540', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare:WeaponPartListCollectionDefinition_216,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_541', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_217,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_542', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_217,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_543', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare:WeaponPartListCollectionDefinition_217,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_544', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_218,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_545', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_218,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_546', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare:WeaponPartListCollectionDefinition_218,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_547', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_219,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_548', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_219,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_549', 'PartUnlock',
    ',GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare:WeaponPartListCollectionDefinition_219,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_550', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_551', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_552', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_553', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_554', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_555', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_556', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_557', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_558', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_559', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_560', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_561', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_562', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade:WeaponPartListCollectionDefinition_221,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_563', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade:WeaponPartListCollectionDefinition_221,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_564', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.AR_Bandit_5_Fusillade:WeaponPartListCollectionDefinition_221,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_565', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard:WeaponPartListCollectionDefinition_222,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_566', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard:WeaponPartListCollectionDefinition_222,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_567', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Laser_Hyperion_5_LongestYard:WeaponPartListCollectionDefinition_222,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_568', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode:WeaponPartListCollectionDefinition_228,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_569', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode:WeaponPartListCollectionDefinition_228,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_570', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.SMG_Hyperion_5_CheatCode:WeaponPartListCollectionDefinition_228,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_571', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander:WeaponPartListCollectionDefinition_234,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_572', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander:WeaponPartListCollectionDefinition_234,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_573', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Expander:WeaponPartListCollectionDefinition_234,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_574', 'PartUnlock',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan:WeaponPartListCollectionDefinition_235,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_575', 'PartUnlock',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan:WeaponPartListCollectionDefinition_235,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_576', 'PartUnlock',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SG_Hyperion_3_CompanyMan:WeaponPartListCollectionDefinition_235,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_577', 'PartUnlock',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker:WeaponPartListCollectionDefinition_237,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_578', 'PartUnlock',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker:WeaponPartListCollectionDefinition_237,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_579', 'PartUnlock',
    ',GD_Cypressure_Weapons.A_Weapons_Unique.SMG_Bandit_3_FastTalker:WeaponPartListCollectionDefinition_237,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_580', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Vladof_6_Glitch:WeaponPartListCollectionDefinition_239,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_581', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Vladof_6_Glitch:WeaponPartListCollectionDefinition_239,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_582', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Vladof_6_Glitch:WeaponPartListCollectionDefinition_239,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_583', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Dahl_6_Glitch:WeaponPartListCollectionDefinition_242,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_584', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Dahl_6_Glitch:WeaponPartListCollectionDefinition_242,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_585', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Dahl_6_Glitch:WeaponPartListCollectionDefinition_242,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_586', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Bandit_6_Glitch:WeaponPartListCollectionDefinition_243,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_587', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Bandit_6_Glitch:WeaponPartListCollectionDefinition_243,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_588', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.AR_Bandit_6_Glitch:WeaponPartListCollectionDefinition_243,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_589', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_590', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_591', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_592', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_593', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_244,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_594', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_595', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_596', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_597', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_598', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_245,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_599', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_600', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_601', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_602', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_603', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch:WeaponPartListCollectionDefinition_246,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_604', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_605', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_606', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_607', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_608', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch:WeaponPartListCollectionDefinition_247,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_609', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Vladof_6_Glitch:WeaponPartListCollectionDefinition_250,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_610', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Vladof_6_Glitch:WeaponPartListCollectionDefinition_250,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_611', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Vladof_6_Glitch:WeaponPartListCollectionDefinition_250,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_612', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Tediore_6_Glitch:WeaponPartListCollectionDefinition_251,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_613', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Tediore_6_Glitch:WeaponPartListCollectionDefinition_251,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_614', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Tediore_6_Glitch:WeaponPartListCollectionDefinition_251,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_615', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Bandit_6_Glitch:WeaponPartListCollectionDefinition_252,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_616', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Bandit_6_Glitch:WeaponPartListCollectionDefinition_252,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_617', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Bandit_6_Glitch:WeaponPartListCollectionDefinition_252,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_618', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_253,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_619', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_253,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_620', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.RL_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_253,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_621', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Dahl_6_Glitch:WeaponPartListCollectionDefinition_254,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_622', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Dahl_6_Glitch:WeaponPartListCollectionDefinition_254,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_623', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Dahl_6_Glitch:WeaponPartListCollectionDefinition_254,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_624', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Bandit_6_Glitch:WeaponPartListCollectionDefinition_255,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_625', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Bandit_6_Glitch:WeaponPartListCollectionDefinition_255,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_626', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Bandit_6_Glitch:WeaponPartListCollectionDefinition_255,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_627', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_257,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_628', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_257,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_629', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_257,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_630', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_258,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_631', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_258,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_632', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_258,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_633', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Tediore_6_Glitch:WeaponPartListCollectionDefinition_259,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_634', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Tediore_6_Glitch:WeaponPartListCollectionDefinition_259,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_635', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Tediore_6_Glitch:WeaponPartListCollectionDefinition_259,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_636', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Vladof_6_Glitch:WeaponPartListCollectionDefinition_261,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_637', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Vladof_6_Glitch:WeaponPartListCollectionDefinition_261,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_638', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Vladof_6_Glitch:WeaponPartListCollectionDefinition_261,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_639', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_262,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_640', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_262,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_641', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Pistol_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_262,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_642', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_263,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_643', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_263,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_644', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_263,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_645', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_264,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_646', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_264,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_647', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_264,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_648', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_265,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_649', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_265,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_650', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_265,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_651', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_268,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_652', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_268,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_653', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_268,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_654', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_269,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_655', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_269,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_656', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_269,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_657', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_270,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_658', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_270,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_659', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Old_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_270,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_660', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_271,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_661', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_271,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_662', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Tediore_6_Glitch:WeaponPartListCollectionDefinition_271,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_663', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_272,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_664', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_272,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_665', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_272,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_666', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Dahl_6_Glitch:WeaponPartListCollectionDefinition_273,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_667', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Dahl_6_Glitch:WeaponPartListCollectionDefinition_273,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_668', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Dahl_6_Glitch:WeaponPartListCollectionDefinition_273,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_669', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_274,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_670', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_274,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_671', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.SMG_Bandit_6_Glitch:WeaponPartListCollectionDefinition_274,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_672', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_277,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_673', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_277,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_674', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Maliwan_6_Glitch:WeaponPartListCollectionDefinition_277,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_675', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Vladof_6_Glitch:WeaponPartListCollectionDefinition_278,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_676', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Vladof_6_Glitch:WeaponPartListCollectionDefinition_278,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_677', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Vladof_6_Glitch:WeaponPartListCollectionDefinition_278,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_678', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_279,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_679', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_279,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_680', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Hyperion_6_Glitch:WeaponPartListCollectionDefinition_279,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_681', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch:WeaponPartListCollectionDefinition_280,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_682', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch:WeaponPartListCollectionDefinition_280,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_683', 'PartUnlock',
    ',GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch:WeaponPartListCollectionDefinition_280,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_684', 'PartUnlock',
    ',GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace:PartList,ConsolidatedAttributeInitData[3].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_685', 'PartUnlock',
    ',GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_686', 'PartUnlock',
    ',GD_Petunia_Weapons.Launchers.RL_Vladof_5_Menace:PartList,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_687', 'PartUnlock',
    ',GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_688', 'PartUnlock',
    ',GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_689', 'PartUnlock',
    ',GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:WeaponPartListCollectionDefinition_282,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_690', 'PartUnlock',
    ',GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr:WeaponPartListCollectionDefinition_282,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_691', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:WeaponPartListCollectionDefinition_285,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_692', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:WeaponPartListCollectionDefinition_285,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_693', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:WeaponPartListCollectionDefinition_285,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_694', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_3_Rare_DahlBarrel:WeaponPartListCollectionDefinition_284,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_695', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_3_Rare_DahlBarrel:WeaponPartListCollectionDefinition_284,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_696', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_3_Rare_DahlBarrel:WeaponPartListCollectionDefinition_284,ConsolidatedAttributeInitData[7].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_697', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:PartList,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_698', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:PartList,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_699', 'PartUnlock',
    ',GD_DahlShared.WeaponBalance.Laser_Dahl_2_Uncommon_DahlBarrel:PartList,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_700', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi:WeaponPartListCollectionDefinition_286,ConsolidatedAttributeInitData[4].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_701', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi:WeaponPartListCollectionDefinition_286,ConsolidatedAttributeInitData[5].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_702', 'PartUnlock',
    ',GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi:WeaponPartListCollectionDefinition_286,ConsolidatedAttributeInitData[6].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_703', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_AllParts:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_704', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Enforcer_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_705', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Gladiator_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_706', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Lawbringer_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_707', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Prototype_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_708', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Enforcer:ItemPartListCollectionDefinition_0,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_709', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Enforcer_04_VeryRare:ItemPartListCollectionDefinition_4,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_710', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Gladiator:ItemPartListCollectionDefinition_7,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_711', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Gladiator_04_VeryRare:ItemPartListCollectionDefinition_11,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_712', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Lawbringer:ItemPartListCollectionDefinition_14,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_713', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Lawbringer_04_VeryRare:ItemPartListCollectionDefinition_18,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_714', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Prototype:ItemPartListCollectionDefinition_21,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_715', 'PartUnlock',
    ',GD_Cork_ItemGrades.ClassMods.BalDef_ClassMod_Prototype_04_VeryRare:ItemPartListCollectionDefinition_25,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_716', 'PartUnlock',
    ',GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_717', 'PartUnlock',
    ',GD_Crocus_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Baroness_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_718', 'PartUnlock',
    ',GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness:ItemPartListCollectionDefinition_28,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_719', 'PartUnlock',
    ',GD_Crocus_ItemGrades.ClassMods.BalDef_ClassMod_Baroness_04_VeryRare:ItemPartListCollectionDefinition_32,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_720', 'PartUnlock',
    ',GD_Crocus_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Baroness:ItemPartListCollectionDefinition_36,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_721', 'PartUnlock',
    ',GD_Crocus_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Baroness_04_VeryRare:ItemPartListCollectionDefinition_40,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_722', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Doppel_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_723', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Enforcer_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_724', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Gladiator_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_725', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Lawbringer_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_726', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Prototype_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_727', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Doppel:ItemPartListCollectionDefinition_41,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_728', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Doppel_04_VeryRare:ItemPartListCollectionDefinition_45,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_729', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Enforcer:ItemPartListCollectionDefinition_47,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_730', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Enforcer_04_VeryRare:ItemPartListCollectionDefinition_51,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_731', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Gladiator:ItemPartListCollectionDefinition_53,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_732', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Gladiator_04_VeryRare:ItemPartListCollectionDefinition_57,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_733', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Lawbringer:ItemPartListCollectionDefinition_59,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_734', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Lawbringer_04_VeryRare:ItemPartListCollectionDefinition_63,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_735', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Prototype:ItemPartListCollectionDefinition_65,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_736', 'PartUnlock',
    ',GD_Petunia_ItemGrades.ClassMods.BalDef_Pet_ClassMod_Prototype_04_VeryRare:ItemPartListCollectionDefinition_69,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_737', 'PartUnlock',
    ',GD_Quince_ItemGrades.ClassMods.BalDef_ClassMod_Doppelganger_04_VeryRare:PartList,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_738', 'PartUnlock',
    ',GD_Quince_ItemGrades.ClassMods.BalDef_ClassMod_Doppelganger:ItemPartListCollectionDefinition_71,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')
hfs.add_level_hotfix('part_unlock_739', 'PartUnlock',
    ',GD_Quince_ItemGrades.ClassMods.BalDef_ClassMod_Doppelganger_04_VeryRare:ItemPartListCollectionDefinition_75,ConsolidatedAttributeInitData[2].BaseValueConstant,,1')

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
points = []
if False:
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
    hfs.add_level_hotfix('moonstonecost', 'moonstonecost',
        ',GD_Balance_Treasure.InteractiveObjects.InteractiveObj_TreasureChest_Moonstone:BehaviorProviderDefinition_1.Behavior_SetUsabilityCost_46,CostAmount,,0')
if False:
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
if False:
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
if False:
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
if False:
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

# Generate
for idx, point in enumerate(points):
    hfs.add_level_hotfix('chestnew{}type'.format(idx), 'chestloc',
        "{},{}_{},PopulationDef,,PopulationDefinition'{}'".format(level, object_base, point, chest_type))
    hfs.add_level_hotfix('chestnew{}x'.format(idx), 'chestloc',
        '{},{}_{},Location.X,,{}'.format(level, object_base, point, x))
    hfs.add_level_hotfix('chestnew{}y'.format(idx), 'chestloc',
        '{},{}_{},Location.Y,,{}'.format(level, object_base, point, cur_y))
    hfs.add_level_hotfix('chestnew{}z'.format(idx), 'chestloc',
        '{},{}_{},Location.Z,,{}'.format(level, object_base, point, z))
    hfs.add_level_hotfix('chestnew{}yaw'.format(idx), 'chestloc',
        '{},{}_{},Rotation.Yaw,,{}'.format(level, object_base, point, yaw))
    cur_y += y_inc

# Badass scavs (at least in the Outlands)
#hfs.add_level_hotfix('badasses0', 'Badass',
#    ',GD_Population_Scavengers.Mixes.PopDef_ScavGroundMix_Outlands,ActorArchetypeList[3].Probability.BaseValueConstant,,500000')
#hfs.add_level_hotfix('badasses1', 'Badass',
#    ',GD_Population_Scavengers.Mixes.PopDef_ScavGroundMix_Outlands,ActorArchetypeList[3].MaxActiveAtOneTime.BaseValueConstant,,500000')

# Chubby Stalkers (these are the only chubby types in TPS, it seems)
#hfs.add_level_hotfix('chubbies1', 'ChubbySpawn',
#    ',GD_Population_Stalker.Mixes.PopDef_StalkerMix_Ambush,ActorArchetypeList[2].Probability.BaseValueConstant,,10000')
#hfs.add_level_hotfix('chubbies2', 'ChubbySpawn',
#    ',GD_Population_Stalker.Mixes.PopDef_StalkerMix_Needle,ActorArchetypeList[1].Probability.BaseValueConstant,,10000')
#hfs.add_level_hotfix('chubbies3', 'ChubbySpawn',
#    ',GD_Population_Stalker.Mixes.PopDef_StalkerMix_Spring,ActorArchetypeList[1].Probability.BaseValueConstant,,10000')

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
