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
    weapon_scale_common = '8'
    weapon_scale_uncommon = '85'
    weapon_scale_rare = '65'
    weapon_scale_veryrare = '50'
    weapon_scale_alien = '30'
    weapon_scale_legendary = '3'
    weapon_scale_iris_cobra = '1'

    # Custom COM drop scaling (identical to weapons, apart from an additional Alignment COM pool)
    cm_scale_common = weapon_scale_common
    cm_scale_uncommon = weapon_scale_uncommon
    cm_scale_rare = weapon_scale_rare
    cm_scale_veryrare = weapon_scale_veryrare
    cm_scale_alignment = '30'
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
    treasure_scale_common = zero
    treasure_scale_uncommon = zero
    treasure_scale_rare = '20'
    treasure_scale_veryrare = '60'
    treasure_scale_alien = '30'
    treasure_scale_legendary = '5'

    # Drop rates for "epic" treasure chests
    epic_scale_common = zero
    epic_scale_uncommon = zero
    epic_scale_rare = zero
    epic_scale_veryrare = '1'
    epic_scale_alien = '1'
    epic_scale_legendary = '0.3'
    epic_scale_legendary_dbl = '0.6'

    # Badass pool probabilities (NOTE: these are *not* weights)
    badass_pool_veryrare = '0.4'
    badass_pool_alien = '0.4'
    badass_pool_epicchest = '0.1'

    # Super Badass pool probabilities (NOTE: these are *not* weights)
    super_badass_pool_rare = '1'
    super_badass_pool_veryrare = '1'
    super_badass_pool_alien = '1'
    super_badass_pool_legendary = '1'
    super_badass_pool_epicchest = '1'

    # Ultimate Badass pool probabilities (NOTE: these are *not* weights)
    ultimate_badass_pool_veryrare_1 = '1'
    ultimate_badass_pool_veryrare_2 = '0.5'
    ultimate_badass_pool_alien_1 = '1'
    ultimate_badass_pool_alien_2 = '0.5'
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

    # Drop rates within the "very high roll" pools of dice chests
    dice_vhigh_veryrare = '1'
    dice_vhigh_alien = '1'
    dice_vhigh_legendary = '0.5'

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
force_gunsandgear_drop_type = 'GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary'

# Force Pool_GunsAndGear to always drop the specified item, if
# `force_gunsandgear_specific` is True.  Useful for seeing what exactly an
# item is.  `force_gunsandgear_specific` will override `force_gunsandgear_drop`,
# if both are set to True.
force_gunsandgear_specific = False
#force_gunsandgear_specific_classtype = 'WeaponBalanceDefinition'
force_gunsandgear_specific_classtype = 'InventoryBalanceDefinition'
force_gunsandgear_specific_name = 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_05_Legendary'

###
### Hotfixes; these are handled a little differently than everything
### else.
###


###
### Testing hotfixes, not really intended to be used for real.  These
### aren't referenced in the body of the mod, so they'll only activate
### on the standalone version.
###

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
                InvBalanceDefinition={force_gunsandgear_specific_classtype}'{force_gunsandgear_specific_name}',
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
        force_gunsandgear_specific_classtype=force_gunsandgear_specific_classtype,
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
