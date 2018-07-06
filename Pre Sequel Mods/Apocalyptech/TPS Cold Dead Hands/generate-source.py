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

# Generation for TPS Cold Dead Hands.
# Apologies about the code in here; there's a lot of functions which do
# nearly-identical things strewn about, and some functional duplication
# here and there.  Might not be the nicest to browse through!

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

mod_name = 'TPS Cold Dead Hands'
mod_version = '1.0.0-prerelease'
output_filename = '{}-source.txt'.format(mod_name)

###
### Some constants
###

class BaseConfig(object):
    """
    Basic class to hold config info
    """

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

class OtherConfig(BaseConfig):
    """
    Config which isn't specific to our other drops
    """

    # Some text that we'll put into the main file
    disable_world_sets = None
    disable_world_chest_sets = None

    # Adding things to the legendary pools
    legendary_unique_adds = None
    legendary_uniqueglitch_adds = None

    # Pools used to provide proper weighted equipment drops for bosses.
    # These will be all set via Hotfix, and re-used by enemies in different
    # levels.  That way, we only need as many pools as we have loot-dropping
    # bosses in a single level.
    level_pool_0 = 'GD_CustomItemPools_Marigold.Baroness.MarigoldSkin06'
    level_pool_1 = 'GD_CustomItemPools_Marigold.Doppel.MarigoldSkin06'
    level_pool_2 = 'GD_CustomItemPools_Marigold.Enforcer.MarigoldSkin06'

class DropConfig(BaseConfig):
    """
    Class to hold basic config for drops
    """

    # Base drop probabilities.  These will be altered slightly for the weighted
    # drop pools.
    drop_prob_pistols = 100
    drop_prob_ar = 100
    drop_prob_smg = 100
    drop_prob_shotguns = 100
    drop_prob_snipers = 80
    drop_prob_launchers = 40
    drop_prob_lasers = 80

    # Scale for weighted pools
    weight_scale = 2.5

    # Rarity drop probabilities
    rarity_drop_prob = {
            'guaranteed': {
                    'common': 1,
                    'uncommon': 1,
                    'rare': 1,
                    'veryrare': 1,
                    'glitch': 1,
                    'legendary': 1,
                },
            'variable': {
                    'common': .1,
                    'uncommon': .33,
                    'rare': .66,
                    'veryrare': 1,
                    'glitch': 1,
                    'legendary': 1,
                },
        }

    ###
    ### Statements which'll be filled in later
    ###

    # Rarity pools for regular enemies
    set_rarity_ar = None
    set_rarity_launchers = None
    set_rarity_pistols = None
    set_rarity_shotguns = None
    set_rarity_smg = None
    set_rarity_snipers = None
    set_rarity_lasers = None

    # Equip pools for regular enemies
    set_equip_all = None
    set_equip_all_glitch = None
    set_equip_ar = None
    set_equip_launchers = None
    set_equip_shotguns = None
    set_equip_snipers_glitch = None
    set_equip_only_lasers = None
    set_equip_lasers = None
    set_equip_lasers_glitch = None

    # Shield pool (only need to worry about one pool for these)
    set_shields = None

    # Rarity weight presets that we'll generate
    weight_common = None
    weight_uncommon = None
    weight_rare = None
    weight_veryrare = None
    weight_glitch_normal = None
    weight_glitch_claptastic = None
    weight_legendary = None
    rarity_presets = [
            ('excellent', 'Enemies Have Excellent Gear (Glitch weapons in Main Game)'),
            ('better', 'Enemies Have Better Gear (Glitch weapons in Main Game)'),
            ('stock', 'Enemies Have Roughly Stock Gear (Glitch weapons in Main Game)'),
            ('excellent_noglitch', 'Enemies Have Excellent Gear (Glitch weapons only in Claptastic Voyage)'),
            ('better_noglitch', 'Enemies Have Better Gear (Glitch weapons only in Claptastic Voyage)'),
            ('stock_noglitch', 'Enemies Have Roughly Stock Gear (Glitch weapons only in Claptastic Voyage)'),
        ]
    rarity_drop_prob_presets = [
            ('guaranteed', 'Guaranteed Drops for All Rarities'),
            ('variable', 'Lower Rarities Drop Less Frequently'),
        ]

    # Computed percent equip rates, for reporting to the user in mod comments
    pct_common = None
    pct_uncommon = None
    pct_rare = None
    pct_veryrare = None
    pct_glitch = None
    pct_legendary = None

    # Claptastic Voyage equip rates
    pct_clap_common = None
    pct_clap_uncommon = None
    pct_clap_rare = None
    pct_clap_veryrare = None
    pct_clap_glitch = None
    pct_clap_legendary = None

    # Guardian shield equips
    guardian_dipl = []
    guardian_pt_cipl = []

    # Claptrap Creature shield equips
    clapcreature_dipl = []
    clapcreature_pt_cipl = []

    # Stalker shield equips
    stalker_dipl = []
    
    ###
    ### ... FUNCTIONS??!?
    ###

    def __init__(self, hotfixes):
        self.hotfixes = hotfixes
        self.num_hotfixes = 0

        # Process some non-glitch variants of our rarity
        rarities_to_add = {}
        for (key, weights) in self.rarities.items():
            new_key = '{}_noglitch'.format(key)
            rarities_to_add[new_key] = {}
            for (level, weight) in weights.items():
                if level == 'glitch_normal':
                    rarities_to_add[new_key][level] = 0
                else:
                    rarities_to_add[new_key][level] = weight
        self.rarities.update(rarities_to_add)

    def _single_assignment_hotfix(self, prefix, classname, attribute, pool, level=None):
        """
        A single assignment hotfix.  Convenience function just to avoid repetition.
        Returns the hotfix XML which should be output in the mod file.
        """
        if level is None:
            level = ''
        hotfix_id = '{}_{}'.format(self.hotfix_prefix, self.num_hotfixes)
        self.hotfixes.add_level_hotfix(hotfix_id, 'EnemyDrop',
                "{},{},{},,ItemPoolDefinition'{}'".format(
                    level, classname, attribute, pool))
        self.num_hotfixes += 1
        return '{}{}'.format(prefix, self.hotfixes.get_hotfix(hotfix_id).get_xml())

    def hotfix_assignments(self):
        """
        Returns a string of rendered hotfixes for performing our custom item pool
        assignments.
        """

        retlist = []
        prefix = ' ' * (4*4)

        # The order in which our assignment tuples are specified
        pool_order = [
                self.equip_pool_shields,
                self.equip_pool_all,
                self.equip_pool_ar,
                self.equip_pool_launchers,
                self.equip_pool_shotguns,
                self.equip_pool_snipers,
                self.equip_pool_only_lasers,
                self.equip_pool_lasers,
            ]

        # First, assign enemies using DefaultItemPoolList[x]
        for (pool, classlist) in zip(pool_order, self.enemy_dipl):
            if pool:
                for (dipl_idx, classname) in classlist:
                    retlist.append(self._single_assignment_hotfix(
                        prefix,
                        classname,
                        'DefaultItemPoolList[{}].ItemPool'.format(dipl_idx),
                        pool))

        # Next, enemies using PlayThroughs[x].CustomItemPoolList[y]
        for (pool, classlist) in zip(pool_order, self.enemy_pt_cipl):
            if pool:
                for (pt_idx, cipl_idx, classname) in classlist:
                    retlist.append(self._single_assignment_hotfix(
                        prefix,
                        classname,
                        'PlayThroughs[{}].CustomItemPoolList[{}].ItemPool'.format(
                            pt_idx, cipl_idx),
                        pool))

        # Next, enemies using ItemPoolList[x] in a specific level WillowAIPawn
        for (pool, classlist) in zip(pool_order, self.enemy_level_ipl):
            if pool:
                for (level, ipl_idx, classname) in classlist:
                    retlist.append(self._single_assignment_hotfix(
                        prefix,
                        classname,
                        'ItemPoolList[{}].ItemPool'.format(ipl_idx),
                        pool,
                        level=level))

        # Next, enemies using DefaultLoot[x].ItemAttachments[y]
        for (pool, classlist) in zip(pool_order, self.enemy_dl_ia):
            if pool:
                for (dl_idx, ia_idx, classname) in classlist:
                    retlist.append(self._single_assignment_hotfix(
                        prefix,
                        classname,
                        'DefaultLoot[{}].ItemAttachments[{}].ItemPool'.format(
                            dl_idx, ia_idx),
                        pool))

        # Next, enemies using NewItemPoolList[0]
        for (pool, classlist) in zip(pool_order, self.enemy_nipl):
            if pool:
                for (nipl_idx, classname) in classlist:
                    retlist.append(self._single_assignment_hotfix(
                        prefix,
                        classname,
                        'NewItemPoolList[{}].ItemPool'.format(nipl_idx),
                        pool))

        return "\n\n".join(retlist)

    def _get_pct_chance(self, weight, total):
        chance = weight/total*100
        if chance == 0:
            return '   0'
        elif chance > 1:
            return '{:4d}'.format(round(chance))
        else:
            return '{:4.2f}'.format(round(chance, 2))


    def set_rarity_weights(self, rarity_key):
        rarity = self.rarities[rarity_key]
        self.weight_common = rarity['common']
        self.weight_uncommon = rarity['uncommon']
        self.weight_rare = rarity['rare']
        self.weight_veryrare = rarity['veryrare']
        self.weight_glitch_normal = rarity['glitch_normal']
        self.weight_glitch_claptastic = rarity['glitch_claptastic']
        self.weight_legendary = rarity['legendary']

        total_weight_normal = (self.weight_common + self.weight_uncommon +
                self.weight_rare + self.weight_veryrare +
                self.weight_glitch_normal + self.weight_legendary)

        self.pct_common = self._get_pct_chance(self.weight_common, total_weight_normal)
        self.pct_uncommon = self._get_pct_chance(self.weight_uncommon, total_weight_normal)
        self.pct_rare = self._get_pct_chance(self.weight_rare, total_weight_normal)
        self.pct_veryrare = self._get_pct_chance(self.weight_veryrare, total_weight_normal)
        self.pct_glitch = self._get_pct_chance(self.weight_glitch_normal, total_weight_normal)
        self.pct_legendary = self._get_pct_chance(self.weight_legendary, total_weight_normal)

        total_weight_claptastic = (self.weight_common + self.weight_uncommon +
                self.weight_rare + self.weight_veryrare +
                self.weight_glitch_claptastic + self.weight_legendary)

        self.pct_clap_common = self._get_pct_chance(self.weight_common, total_weight_claptastic)
        self.pct_clap_uncommon = self._get_pct_chance(self.weight_uncommon, total_weight_claptastic)
        self.pct_clap_rare = self._get_pct_chance(self.weight_rare, total_weight_claptastic)
        self.pct_clap_veryrare = self._get_pct_chance(self.weight_veryrare, total_weight_claptastic)
        self.pct_clap_glitch = self._get_pct_chance(self.weight_glitch_claptastic, total_weight_claptastic)
        self.pct_clap_legendary = self._get_pct_chance(self.weight_legendary, total_weight_claptastic)

class Regular(DropConfig):
    """
    Config info for regular enemies
    """

    # Hotfix prefix
    hotfix_prefix = 'reg'

    # Equip weights
    rarities = {
        'excellent': {
            'common': 30,
            'uncommon': 95,
            'rare': 70,
            'veryrare': 40,
            'glitch_normal': 8,
            'glitch_claptastic': 16,
            'legendary': 3,
            },
        'better': {
            'common': 32.75,
            'uncommon': 35,
            'rare': 25,
            'veryrare': 5,
            'glitch_normal': 2,
            'glitch_claptastic': 4,
            'legendary': 0.25,
            },
        'stock': {
            'common': 80,
            'uncommon': 10,
            'rare': 1,
            'veryrare': 0.1,
            'glitch_normal': 0.1,
            'glitch_claptastic': 0.1,
            'legendary': 0.03,
            },
        }

    # Rarity weight pools
    rarity_pool_ar = 'GD_CustomItemPools_Marigold.Gladiator.MarigoldSkin06'
    rarity_pool_launchers = 'GD_CustomItemPools_Marigold.Lawbringer.MarigoldSkin06'
    rarity_pool_pistols = 'GD_CustomItemPools_Marigold.Prototype.MarigoldSkin06'
    rarity_pool_shotguns = 'GD_CustomItemPools_Marigold.Baroness.MarigoldSkin07'
    rarity_pool_smg = 'GD_CustomItemPools_Marigold.Doppel.MarigoldSkin07'
    rarity_pool_snipers = 'GD_CustomItemPools_Marigold.Enforcer.MarigoldSkin07'
    rarity_pool_lasers = 'GD_CustomItemPools_Marigold.Gladiator.MarigoldSkin07'

    # Equip pools (this is where weights are applied)
    equip_pool_shields = 'GD_CustomItemPools_Marigold.Lawbringer.MarigoldSkin07'
    equip_pool_all = 'GD_CustomItemPools_Marigold.Prototype.MarigoldSkin07'
    equip_pool_ar = 'GD_CustomItemPools_Marigold.Baroness.MarigoldSkin11'
    equip_pool_launchers = 'GD_CustomItemPools_Marigold.Doppel.MarigoldSkin11'
    equip_pool_shotguns = 'GD_CustomItemPools_Marigold.Enforcer.MarigoldSkin11'
    equip_pool_snipers = 'GD_CustomItemPools_Marigold.Gladiator.MarigoldSkin11'
    equip_pool_only_lasers = 'GD_CustomItemPools_Marigold.Lawbringer.MarigoldSkin11'
    equip_pool_lasers = 'GD_CustomItemPools_Marigold.Prototype.MarigoldSkin11'

    ###
    ### Enemy changes
    ###

    enemy_dipl = (
            # Shields
            [
                (1, 'GD_ColZ.Population.PawnBalance_ColZ_DahlMarine'),
                (0, 'GD_ColZMech.Population.PawnBalance_ColZMech_DahlFlameMarine'),
                (1, 'GD_ColZMech.Population.PawnBalance_ColZMech_DahlMarine'),
                (1, 'GD_ColZMech.Population.PawnBalance_ColZMech_DahlRocketMarine'),
                (1, 'GD_ColZMech.Population.PawnBalance_ColZMech_DahlScout'),
                (0, 'GD_DahlCombatSuit_Mini.Population.PawnBalance_DahlCombatSuit_Mini'),
                (1, 'GD_DahlMarineMoonshot.Balance.PawnBalance_DahlMarineMoonshot'),
                (2, 'GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlPowersuit_Knuckle'),
                (1, 'GD_DahlRedShirt.Balance.PawnBalance_DahlRedShirt'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_BotRider'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FlyTrap'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecWheelie'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecuritySniper'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_MinacMinion'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_PermFlyTrap'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_RexLoaderMinion'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBot'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureFlight'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureSentry'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureSniper'),
                (1, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_BlackOps'),
                (0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragPsycho'),
                (0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragPsychoMidget'),
                (0, 'GD_Pet_Population_Dahl.Balance.PawnBalance_DahlEternalPowersuit'),
                (0, 'GD_Pet_Population_Dahl.Balance.PawnBalance_DahlEternalPowersuitShield'),
                (0, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlCorrosiveMarine_MercDay'),
                (0, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlFlameMarine_MercDay'),
                (0, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlIceMarine_MercDay'),
                (1, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlMarine_MercDay'),
                (1, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlMedic_MercDay'),
                (1, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlScout_MercDay'),
                (1, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlSergeant_MercDay'),
                (0, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlFlameMarine_Pandoracorn'),
                (1, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlMarine_Pandoracorn'),
                (1, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlMedic_Pandoracorn'),
                (1, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlScout_Pandoracorn'),
                (1, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlSergeant_Pandoracorn'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlCorrosiveMarine'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlEngineer'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlFactory_SecurityBot'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlFactory_SecurityBot_Small'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlFlameMarine'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlIceMarine'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlJetFighterRider'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlLaserMarine'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlMarine'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlMarine_Intro'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlMarine_Intro2'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlMarine_NoProvokeAnim'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlMedic'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlRocketMarine'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlScout'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlSergeant'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlSniper'),
                (0, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlCorrosiveMarine_Pumpkin'),
                (0, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlFlameMarine_Pumpkin'),
                (0, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlIceMarine_Pumpkin'),
                (1, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlMarine_Pumpkin'),
                (1, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlMedic_Pumpkin'),
                (1, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlScout_Pumpkin'),
                (1, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlSergeant_Pumpkin'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderEXPStation'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderGUN'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderJunk'),
                (1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBanditRider'),
                (1, 'GD_ProtoWarBot_GunLoader.Population.PawnBalance_ProtoWarBot_FriendLoader'),
                (1, 'GD_ProtoWarBot_GunLoader.Population.PawnBalance_ProtoWarBot_FriendLoaderYellow'),
                (1, 'GD_ProtoWarBot_GunLoader.Population.PawnBalance_ProtoWarBot_GunLoader'),
            ],
            # All Weapons
            [
                (0, 'GD_ColZ.Population.PawnBalance_ColZ_DahlMarine'),
                (0, 'GD_ColZMech.Population.PawnBalance_ColZMech_DahlMarine'),
                (0, 'GD_DahlMarineMoonshot.Balance.PawnBalance_DahlMarineMoonshot'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot_LowDamage'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_MinacMinion'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_RexLoaderMinion'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBot'),
                (0, 'GD_PLAMember.Balance.PawnBalance_TimPot'),
                (0, 'GD_PLAMember.Balance.PawnBalance_TumPot'),
                (0, 'GD_PLAMember.Population.PawnBalance_TomPot'),
                (0, 'GD_PoopDeck.Population.PawnBalance_PoopDeck'),
                (0, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlMarine_MercDay'),
                (0, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlMedic_MercDay'),
                (0, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlMarine_Pandoracorn'),
                (0, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlMedic_Pandoracorn'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlEngineer'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlJetFighterRider'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlMarine'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlMedic'),
                (0, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlMarine_Pumpkin'),
                (0, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlMedic_Pumpkin'),
                (0, 'GD_Population_Darksiders.Balance.PawnBalance_DarksiderBandit'),
                (0, 'GD_Population_Darksiders.Balance.PawnBalance_LittleDarksiderPsycho'),
                (0, 'GD_ScavAccepterDude.Population.PawnBalance_ScavAccepterDude'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlSergeant'),
                (0, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlSergeant_Pumpkin'),
                (0, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlSergeant_Pandoracorn'),
                (0, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlSergeant_MercDay'),
            ],
            # AR-Weighted
            [
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlFactory_SecurityBot'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlFactory_SecurityBot_Small'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderEXPStation'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderGUN'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderJunk'),
                (0, 'GD_ProtoWarBot_GunLoader.Population.PawnBalance_ProtoWarBot_FriendLoader'),
                (0, 'GD_ProtoWarBot_GunLoader.Population.PawnBalance_ProtoWarBot_FriendLoaderYellow'),
                (0, 'GD_ProtoWarBot_GunLoader.Population.PawnBalance_ProtoWarBot_GunLoader'),
            ],
            # Launchers Only
            [
                (0, 'GD_ColZMech.Population.PawnBalance_ColZMech_DahlRocketMarine'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlRocketMarine'),
            ],
            # Shotguns Only
            [
                (0, 'GD_ColZMech.Population.PawnBalance_ColZMech_DahlScout'),
                (0, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_DahlScout_MercDay'),
                (0, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_DahlScout_Pandoracorn'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlScout'),
                (0, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_DahlScout_Pumpkin'),
                (0, 'GD_Population_Darksiders.Balance.PawnBalance_LittleDarksiderBandit'),
            ],
            # Snipers Only
            [
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecuritySniper'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureSniper'),
                (0, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_BlackOps'),
            ],
            # Lasers Only
            [
                (0, 'GD_ColZ.Population.PawnBalance_ColZ_DahlFanatic'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlFanatic'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlLaserMarine'),
                (0, 'GD_Population_Dahl.Zealots.PawnBalance_DahlZealot'),
                (0, 'GD_Population_Dahl.Zealots.PawnBalance_DahlZealot_Playthrough2'),
            ],
            # Laser-Weighted
            [
                (0, 'GD_DahlRedShirt.Balance.PawnBalance_DahlRedShirt'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_BotRider'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FlyTrap'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_PermFlyTrap'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureFlight'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_DahlMarine_NoProvokeAnim'),
                (0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidgetSpaceman'),
                (0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavFloatingSpaceman'),
                (0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBanditRider'),
            ],
        )

    enemy_pt_cipl = (
            # Shields
            [
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_BotRider'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_BotRider'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_ClapDawgRider'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_ClapDawgRider'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FlyTrap'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FlyTrap'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecWheelie'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecWheelie'),
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot_LowDamage'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot_LowDamage'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecuritySniper'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecuritySniper'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_MinacMinion'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_MinacMinion'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_PermFlyTrap'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_PermFlyTrap'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_RexLoaderMinion'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_RexLoaderMinion'),
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBot'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBot'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureSniper'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureSniper'),
                (0, 1, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_Engineer'),
                (1, 1, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_Engineer'),
                (2, 1, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_Engineer'),
                (0, 0, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_EngineerArms'),
                (1, 0, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_EngineerArms'),
                (2, 0, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_EngineerArms'),
                (0, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBandit'),
                (1, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBandit'),
                (2, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBandit'),
                (0, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBanditMidget'),
                (1, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBanditMidget'),
                (2, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBanditMidget'),
                (1, 1, 'GD_Population_Boils.Balance.PawnBalance_BoilGuard'),
                (0, 0, 'GD_Population_ProtoWarBot.Balance.PawnBalance_ProtoWarBot_ShieldDrone'),
                (1, 0, 'GD_Population_ProtoWarBot.Balance.PawnBalance_ProtoWarBot_ShieldDrone'),
                (1, 0, 'GD_Population_ProtoWarBot.Balance.PawnBalance_RepairDrone'),
                (1, 1, 'GD_Population_Rat.Balance.PawnBalance_HypRatGuard'),
                (1, 1, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavMidget_Bosun'),
                (1, 0, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavPsychoMidget_Bosun'),
                (0, 1, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavengerBandit_Bosun'),
                (1, 1, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavengerBandit_Bosun'),
                (1, 0, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavengerPsycho_Bosun'),
                (1, 1, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavMidget_Mercday'),
                (0, 1, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Jetpack_MercDay'),
                (1, 1, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Jetpack_MercDay'),
                (0, 1, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Mercday'),
                (1, 1, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Mercday'),
                (1, 0, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerPsycho_Mercday'),
                (1, 1, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidget'),
                (1, 2, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidgetSpaceman'),
                (1, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavPsychoMidget'),
                (0, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_OutlawRider'),
                (1, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_OutlawRider'),
                (0, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavCombatSpaceman'),
                (1, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavCombatSpaceman'),
                (0, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavFloatingSpaceman'),
                (1, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavFloatingSpaceman'),
                (1, 2, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavNomad'),
                (1, 1, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavMidget_Pandoracorn'),
                (0, 1, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Jetpack_Pandoracorn'),
                (1, 1, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Jetpack_Pandoracorn'),
                (0, 1, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Pandoracorn'),
                (1, 1, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Pandoracorn'),
                (1, 0, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerPsycho_Pandoracorn'),
                (0, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavEliteBandit'),
                (1, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavEliteBandit'),
                (0, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavEliteBandit_Jetpack'),
                (1, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavEliteBandit_Jetpack'),
                (0, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavPowerSuitRider'),
                (1, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavPowerSuitRider'),
                (0, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit'),
                (1, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit'),
                (0, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit_Jetpack'),
                (1, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit_Jetpack'),
                (1, 0, 'GD_Population_Scavengers.Balance.Psychos.PawnBalance_ScavengerPsycho'),
                (1, 1, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavMidget_Pumpkin'),
                (0, 1, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Jetpack_Pumpkin'),
                (1, 1, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Jetpack_Pumpkin'),
                (0, 1, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Pumpkin'),
                (1, 1, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Pumpkin'),
                (1, 0, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerPsycho_Pumpkin'),
                (1, 1, 'GD_ScavBanditMidget_Rider.Population.PawnBalance_ScavMidget_Rider'),
            ],
            # All Weapons
            [
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_BotRider'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_BotRider'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot'),
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot_LowDamage'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecurityBot_LowDamage'),
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_MinacMinion'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_MinacMinion'),
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_RexLoaderMinion'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_RexLoaderMinion'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBot'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBot'),
                (0, 0, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_Engineer'),
                (1, 0, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_Engineer'),
                (2, 0, 'GD_Ma_Pop_Engineer.Balance.PawnBalance_Engineer'),
                (0, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBadassBandit'),
                (1, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBadassBandit'),
                (2, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBadassBandit'),
                (0, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBandit'),
                (1, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBandit'),
                (2, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBandit'),
                (0, 0, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavMidget_Bosun'),
                (0, 0, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavengerBandit_Bosun'),
                (1, 0, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavengerBandit_Bosun'),
                (0, 0, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavMidget_Mercday'),
                (0, 0, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Jetpack_MercDay'),
                (1, 0, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Jetpack_MercDay'),
                (0, 0, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Mercday'),
                (1, 0, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Mercday'),
                (0, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidget'),
                (0, 0, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavMidget_Pandoracorn'),
                (0, 0, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Jetpack_Pandoracorn'),
                (1, 0, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Jetpack_Pandoracorn'),
                (0, 0, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Pandoracorn'),
                (1, 0, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Pandoracorn'),
                (0, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavEliteBandit'),
                (1, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavEliteBandit'),
                (0, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavEliteBandit_Jetpack'),
                (1, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavEliteBandit_Jetpack'),
                (0, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavPowerSuitRider'),
                (1, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavPowerSuitRider'),
                (0, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit'),
                (1, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit'),
                (0, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit_Jetpack'),
                (1, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit_Jetpack'),
                (0, 0, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavMidget_Pumpkin'),
                (0, 0, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Jetpack_Pumpkin'),
                (1, 0, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Jetpack_Pumpkin'),
                (0, 0, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Pumpkin'),
                (1, 0, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Pumpkin'),
                (0, 0, 'GD_ScavBanditMidget_Rider.Population.PawnBalance_ScavMidget_Rider'),
            ],
            # AR-Weighted
            [
                (0, 0, 'GD_Population_Boils.Balance.PawnBalance_BoilGuard'),
                (1, 0, 'GD_Population_Boils.Balance.PawnBalance_BoilGuard'),
                (0, 0, 'GD_Population_Rat.Balance.PawnBalance_HypRatGuard'),
                (1, 0, 'GD_Population_Rat.Balance.PawnBalance_HypRatGuard'),
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
                (0, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBanditMidget'),
                (1, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBanditMidget'),
                (2, 0, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBanditMidget'),
            ],
            # Snipers Only
            [
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecuritySniper'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_InsecuritySniper'),
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureSniper'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureSniper'),
            ],
            # Lasers Only
            [
                (0, 0, 'GD_Population_Dahl.Zealots.PawnBalance_DahlZealot'),
                (0, 0, 'GD_Population_Dahl.Zealots.PawnBalance_DahlZealot_Playthrough2'),
            ],
            # Laser-Weighted
            [
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FlyTrap'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FlyTrap'),
                (1, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_PermFlyTrap'),
                (2, 1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_PermFlyTrap'),
                (1, 0, 'GD_Population_Scavengers.Balance.Bosun.PawnBalance_ScavMidget_Bosun'),
                (1, 0, 'GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavMidget_Mercday'),
                (1, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidget'),
                (0, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidgetSpaceman'),
                (1, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidgetSpaceman'),
                (0, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_OutlawRider'),
                (1, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_OutlawRider'),
                (1, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavCombatSpaceman'),
                (0, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavFloatingSpaceman'),
                (1, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavFloatingSpaceman'),
                (0, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavNomad'),
                (1, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavNomad'),
                (1, 0, 'GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavMidget_Pandoracorn'),
                (1, 0, 'GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavMidget_Pumpkin'),
                (1, 0, 'GD_ScavBanditMidget_Rider.Population.PawnBalance_ScavMidget_Rider'),
            ],
        )

    enemy_level_ipl = (
            # Shields
            [
            ],
            # All Weapons
            [
            ],
            # AR-Weighted
            [
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
            ],
            # Snipers Only
            [
            ],
            # Lasers Only
            [
            ],
            # Laser-Weighted
            [
            ],
        )

    enemy_dl_ia = (
            # Shields
            [
            ],
            # All Weapons
            [
            ],
            # AR-Weighted
            [
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
            ],
            # Snipers Only
            [
            ],
            # Lasers Only
            [
            ],
            # Laser-Weighted
            [
            ],
        )

    enemy_nipl = (
            # Shields
            [
            ],
            # All Weapons
            [
            ],
            # AR-Weighted
            [
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
            ],
            # Snipers Only
            [
            ],
            # Lasers Only
            [
            ],
            # Laser-Weighted
            [
            ],
        )

    # Guardian shield equips
    guardian_dipl = [
            (0, 'GD_FinalBossCorkBig.Population.PawnBalance_FBCBig_Guardian_Cheru'),
            (0, 'GD_FinalBossCorkBig.Population.PawnBalance_FBCBig_Guardian_Spectre'),
            (1, 'GD_FinalBossCorkBig.Population.PawnBalance_FBCBig_Sera_Guardian'),
            (0, 'GD_MetaGuardian.Population.PawnBalance_Meta_Guardian_Cheru'),
            (0, 'GD_Population_Eridian_Opha.AIPawn_Bal.PawnBalance_Opha_Heavy'),
            (0, 'GD_Population_Eridian_Opha.AIPawn_Bal.PawnBalance_Opha_Normal'),
            (0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Cheru'),
            (0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Reaper'),
            (0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Spectre'),
            (0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Wraith_CorrosiveShock'),
            (0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Wraith_FireIce'),
            (0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Wraith_IceFire'),
            (0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Wraith_ShockCorrosive'),
            (0, 'GD_Population_Guardians.Opha.Balance.PawnBalance_Virtuous_Opha'),
            (1, 'GD_Population_Guardians.Sera.Balance.PawnBalance_Arch_Guardian'),
            (1, 'GD_Population_Guardians.Sera.Balance.PawnBalance_Dominant_Guardian'),
            (1, 'GD_Population_Guardians.Sera.Balance.PawnBalance_Guardian_Principal_CorrosiveShock'),
            (1, 'GD_Population_Guardians.Sera.Balance.PawnBalance_Guardian_Principal_FireIce'),
            (0, 'GD_Population_Guardians.Sera.Balance.PawnBalance_Guardian_Principal_IceFire'),
            (1, 'GD_Population_Guardians.Sera.Balance.PawnBalance_Guardian_Principal_ShockCorrosive'),
            (1, 'GD_Population_Guardians.Sera.Balance.PawnBalance_Sera_Guardian'),
        ]
    guardian_pt_cipl = [
            (1, 0, 'GD_FinalBossCorkBig.Population.PawnBalance_FBCBig_Guardian_Cheru'),
            (2, 0, 'GD_FinalBossCorkBig.Population.PawnBalance_FBCBig_Guardian_Cheru'),
            (1, 0, 'GD_FinalBossCorkBig.Population.PawnBalance_FBCBig_Guardian_Spectre'),
            (1, 0, 'GD_MetaGuardian.Population.PawnBalance_Meta_Guardian_Cheru'),
            (2, 0, 'GD_MetaGuardian.Population.PawnBalance_Meta_Guardian_Cheru'),
            (1, 0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Cheru'),
            (2, 0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Cheru'),
            (1, 0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Reaper'),
            (1, 0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Spectre'),
            (1, 0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Wraith_CorrosiveShock'),
            (1, 0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Wraith_FireIce'),
            (1, 0, 'GD_Population_Guardians.Cheru.Balance.PawnBalance_Guardian_Wraith_ShockCorrosive'),
        ]

    # Claptrap Creature shield equips
    clapcreature_dipl = [
            (0, 'GD_Ma_Pop_BossFights.Balance.PawnBalance_VoltronTrapHealBug'),
            (0, 'GD_Ma_Pop_Glitches.Balance.PawnBalance_Glitch'),
        ]
    clapcreature_pt_cipl = [
            (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_ClapDawg'),
            (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_ClapDawg'),
            (1, 0, 'GD_Ma_Pop_Glitches.Balance.PawnBalance_RecurringGlitch'),
            (2, 0, 'GD_Ma_Pop_Glitches.Balance.PawnBalance_RecurringGlitch'),
            (1, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_MiniVirus'),
            (2, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_MiniVirus'),
            (0, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_Virus'),
            (1, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_Virus'),
            (2, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_Virus'),
            (0, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_VirusLauncher'),
            (1, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_VirusLauncher'),
            (2, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_VirusLauncher'),
            (1, 0, 'GD_Marigold_Pop_Bugs.Balance.PawnBalance_Bug'),
            (2, 0, 'GD_Marigold_Pop_Bugs.Balance.PawnBalance_Bug'),
        ]

    # Stalker shield equips
    stalker_dipl = [
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerAmbush'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerNeedle'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerSpring'),
        ]

class Badass(DropConfig):
    """
    Config info for badass enemies
    """

    # Hotfix prefix
    hotfix_prefix = 'badass'

    # Equip weights
    rarities = {
        'excellent': {
            'common': 0,
            'uncommon': 0,
            'rare': 50,
            'veryrare': 60,
            'glitch_normal': 40,
            'glitch_claptastic': 70,
            'legendary': 8,
            },
        'better': {
            'common': 0,
            'uncommon': 25,
            'rare': 49,
            'veryrare': 15,
            'glitch_normal': 8,
            'glitch_claptastic': 16,
            'legendary': 1,
            },
        # There's really not such a thing as a "stock" badass pool we could
        # base these weights on, so we're sort of just making it up.
        'stock': {
            'common': 0,
            'uncommon': 40,
            'rare': 30,
            'veryrare': 8,
            'glitch_normal': 3,
            'glitch_claptastic': 6,
            'legendary': 0.25,
            },
        }

    # Rarity weight pools
    rarity_pool_ar = 'GD_CustomItemPools_Marigold.Baroness.MarigoldSkin12'
    rarity_pool_launchers = 'GD_CustomItemPools_Marigold.Doppel.MarigoldSkin12'
    rarity_pool_pistols = 'GD_CustomItemPools_Marigold.Enforcer.MarigoldSkin12'
    rarity_pool_shotguns = 'GD_CustomItemPools_Marigold.Gladiator.MarigoldSkin12'
    rarity_pool_smg = 'GD_CustomItemPools_Marigold.Lawbringer.MarigoldSkin12'
    rarity_pool_snipers = 'GD_CustomItemPools_Marigold.Prototype.MarigoldSkin12'
    rarity_pool_lasers = 'GD_CustomItemPools_Marigold.Baroness.MarigoldSkin13'

    # Equip pools (this is where weights are applied)
    equip_pool_shields = 'GD_CustomItemPools_Marigold.Doppel.MarigoldSkin13'
    equip_pool_all = 'GD_CustomItemPools_Marigold.Enforcer.MarigoldSkin13'
    equip_pool_ar = 'GD_CustomItemPools_Marigold.Gladiator.MarigoldSkin13'
    equip_pool_launchers = None
    equip_pool_shotguns = 'GD_CustomItemPools_Marigold.Lawbringer.MarigoldSkin13'
    equip_pool_snipers = None
    equip_pool_only_lasers = None
    equip_pool_lasers = 'GD_CustomItemPools_Marigold.Prototype.MarigoldSkin13'

    ###
    ### Enemy changes
    ###

    enemy_dipl = (
            # Shields
            [
                (0, 'GD_ColZ.Population.PawnBalance_ColZ'),
                (0, 'GD_ColZMech.Population.PawnBalance_ColZMech'),
                (1, 'GD_Cork_DontGetCocky_Data.Balance.PawnBalance_DanZando'),
                (0, 'GD_Cork_Eradicate_Data.BalanceDefs.PawnBalance_Clap_L3K'),
                (0, 'GD_DahlCombatSuit_Felicity.Population.PawnBalance_DahlCombatSuit_Felicity'),
                (1, 'GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlSergeantFlameKnuckle'),
                (0, 'GD_DahlPowersuit_KnuckleRepaired.Population.PawnBalance_DahlPowersuit_KnuckleRepaired'),
                (0, 'GD_DahlRedShirtPowersuit.Balance.PawnBalance_DahlRedShirtPowersuit'),
                (0, 'GD_DrongoBones.Balance.PawnBalance_DrongoBones'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_CleanupRuntime'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FireWall'),
                (1, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBadass'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.Uniques.PawnBalance_Despair'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.Uniques.PawnBalance_SH4D0W-TP-Part1'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.Uniques.PawnBalance_SelfLoathing'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.Uniques.PawnBalance_ShadowClone'),
                (0, 'GD_Ma_Pop_Trojan.Balance.Uniques.PawnBalance_Trojan_Shame'),
                (0, 'GD_Ma_Pop_Worm.Balance.PawnBalance_CodeWorm'),
                (2, 'GD_Ma_Pop_Worm.Balance.PawnBalance_EarWorm'),
                (2, 'GD_Ma_Sponx.Balance.Balance_Ma_Sponx'),
                (0, 'GD_MeatHead.Balance.PawnBalance_MeatHead'),
                (1, 'GD_Population_Boils.Balance.PawnBalance_Eghood'),
                (1, 'GD_Population_Boils.Balance.PawnBalance_Eghood_MercDay'),
                (1, 'GD_Population_Boils.Balance.PawnBalance_Eghood_Pandoracorn'),
                (1, 'GD_Population_Boils.Balance.PawnBalance_Eghood_Pumpkin'),
                (1, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_BadassDahlMarine_MercDay'),
                (1, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_BadassDahlMarine_Pandoracorn'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_BadassDahlMarine'),
                (1, 'GD_Population_Dahl.Balance.PawnBalance_DahlMarine_CentralTerm'),
                (1, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_BadassDahlMarine_Pumpkin'),
                (1, 'GD_Population_Darksiders.Balance.PawnBalance_DarksiderBadassBandit'),
                (0, 'GD_Population_Darksiders.Balance.PawnBalance_DarksiderBadassPsycho'),
                (1, 'GD_Population_Darksiders.Balance.PawnBalance_LittleDarksiderBadassBandit'),
                (1, 'GD_Population_Rat.Balance.PawnBalance_Lazlo'),
                (1, 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift'),
                (1, 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_MercDay'),
                (1, 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_Pandoracorn'),
                (1, 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_Pumpkin'),
                (0, 'GD_TimberLogwood.Balance.PawnBalance_TimberLogwood'),
            ],
            # All Weapons
            [
                (0, 'GD_Bruce.Population.Bal_Bruce'),
                (0, 'GD_Population_Darksiders.Balance.PawnBalance_DarksiderBadassBandit'),
                (0, 'GD_Population_Darksiders.Balance.PawnBalance_LittleDarksiderBadassBandit'),
                (0, 'GD_Squat.Population.PawnBalance_Squat'),
                (0, 'GD_Population_Dahl.Balance.PawnBalance_BadassDahlMarine'),
                (0, 'GD_Population_Dahl.Balance.Pumpkin.PawnBalance_BadassDahlMarine_Pumpkin'),
                (0, 'GD_Population_Dahl.Balance.Pandoracorn.PawnBalance_BadassDahlMarine_Pandoracorn'),
                (0, 'GD_Population_Dahl.Balance.MercDay.PawnBalance_BadassDahlMarine_MercDay'),
            ],
            # AR-Weighted
            [
                (0, 'GD_Population_Scavengers.Uniques.PawnBalance_Ned'),
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
                (0, 'GD_Population_Boils.Balance.PawnBalance_Eghood'),
                (0, 'GD_Population_Boils.Balance.PawnBalance_Eghood_MercDay'),
                (0, 'GD_Population_Boils.Balance.PawnBalance_Eghood_Pandoracorn'),
                (0, 'GD_Population_Boils.Balance.PawnBalance_Eghood_Pumpkin'),
                (2, 'GD_TimberLogwood.Balance.PawnBalance_TimberLogwood'),
            ],
            # Snipers Only
            [
            ],
            # Lasers Only
            [
            ],
            # Laser-Weighted
            [
                (0, 'GD_Cork_DontGetCocky_Data.Balance.PawnBalance_DanZando'),
                (1, 'GD_DrongoBones.Balance.PawnBalance_DrongoBones'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_CleanupRuntime'),
                (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBadass'),
                (0, 'GD_Population_Scavengers.Uniques.PawnBalance_Kelly'),
            ],
        )

    enemy_pt_cipl = (
            # Shields
            [
                (1, 2, 'GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlSergeantFlameKnuckle'),
                (1, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FireWall'),
                (2, 0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_FireWall'),
                (0, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBadassBandit'),
                (1, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBadassBandit'),
                (2, 1, 'GD_Marigold_Pop_Fragmented.Balance.PawnBalance_FragBadassBandit'),
                (1, 1, 'GD_Population_Boils.Balance.PawnBalance_BoilBadass'),
                (0, 1, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassBanditMidget'),
                (1, 1, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassBanditMidget'),
                (0, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassPsychoMidget'),
                (1, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassPsychoMidget'),
                (0, 1, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassSpacemanMidget'),
                (1, 1, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassSpacemanMidget'),
                (0, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_BadassSpaceman'),
                (1, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_BadassSpaceman'),
                (0, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker'),
                (1, 1, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker'),
                (0, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBadassBandit'),
                (1, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBadassBandit'),
                (0, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBadassBandit_Jetpack'),
                (1, 1, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBadassBandit_Jetpack'),
                (0, 0, 'GD_Population_Scavengers.Balance.Psychos.PawnBalance_ScavBadassPsycho'),
                (1, 0, 'GD_Population_Scavengers.Balance.Psychos.PawnBalance_ScavBadassPsycho'),
            ],
            # All Weapons
            [
                (0, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassBanditMidget'),
                (1, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassBanditMidget'),
                (0, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassSpacemanMidget'),
                (1, 0, 'GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavBadassSpacemanMidget'),
                (0, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavCombatSpaceman'),
                (0, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBadassBandit'),
                (1, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBadassBandit'),
                (0, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBadassBandit_Jetpack'),
                (1, 0, 'GD_Population_Scavengers.Balance.PawnBalance_ScavBadassBandit_Jetpack'),
            ],
            # AR-Weighted
            [
                (1, 0, 'GD_Population_Boils.Balance.PawnBalance_BoilBadass'),
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
            ],
            # Snipers Only
            [
            ],
            # Lasers Only
            [
            ],
            # Laser-Weighted
            [
                (0, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker'),
                (1, 0, 'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker'),
            ],
        )

    enemy_level_ipl = (
            # Shields
            [
            ],
            # All Weapons
            [
            ],
            # AR-Weighted
            [
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
            ],
            # Snipers Only
            [
            ],
            # Lasers Only
            [
            ],
            # Laser-Weighted
            [
            ],
        )

    enemy_dl_ia = (
            # Shields
            [
            ],
            # All Weapons
            [
            ],
            # AR-Weighted
            [
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
            ],
            # Snipers Only
            [
            ],
            # Lasers Only
            [
            ],
            # Laser-Weighted
            [
            ],
        )

    enemy_nipl = (
            # Shields
            [
            ],
            # All Weapons
            [
            ],
            # AR-Weighted
            [
            ],
            # Launchers Only
            [
            ],
            # Shotguns Only
            [
            ],
            # Snipers Only
            [
            ],
            # Lasers Only
            [
            ],
            # Laser-Weighted
            [
            ],
        )

    # Guardian shield equips
    guardian_dipl = [
            (0, 'GD_Pet_Population_Guardians.Balance.PawnBalance_GuardianPondor'),
            (0, 'GD_Population_Eridian_Opha.AIPawn_Bal.PawnBalance_Opha_BadAss'),
            (0, 'GD_Population_Eridian_OphaBoss.AIPawn_Bal.PawnBalance_OphaBoss'),
        ]
    guardian_pt_cipl = [
        ]

    # Claptrap Creature shield equips
    clapcreature_dipl = [
            (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_BadassClapDawg'),
            (0, 'GD_Ma_Pop_ClaptrapForces.Balance.PawnBalance_VeryInsecureBadassClapDawg'),
            (0, 'GD_Ma_Pop_Glitches.Balance.PawnBalance_BadassGlitch'),
            (0, 'GD_Ma_Pop_Glitches.Balance.PawnBalance_SolidGlitch'),
            (0, 'GD_Ma_Pop_Trojan.Balance.PawnBalance_Trojan'),
            (1, 'GD_Marigold_Pop_Bugs.Balance.PawnBalance_BadassBug'),
        ]
    clapcreature_pt_cipl = [
            (1, 0, 'GD_Ma_Pop_Trojan.Balance.PawnBalance_Trojan'),
            (2, 0, 'GD_Ma_Pop_Trojan.Balance.PawnBalance_Trojan'),
            (0, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_BadassVirus'),
            (1, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_BadassVirus'),
            (2, 0, 'GD_Ma_Pop_Virus.Balance.PawnBalance_BadassVirus'),
        ]

    # Stalker shield equips
    stalker_dipl = [
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerBadass'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_StalkerChubby'),
            (0, 'GD_Population_Stalker.Balance.PawnBalance_Stalker_RnD'),
            (0, 'GD_Population_Stalker.Balance.Unique.PawnBalance_StalkerRabid'),
        ]

###
### Convenience functions
###

def get_balanced_items(items):
    """
    Returns a string containing a BalancedItems array with the given `items`.
    Each element of the list `items` should be a tuple, the first element
    being the itempool class name, the second being the weight of that
    item, and the third (optional) being an `invbalance` (or None).  If `None`,
    the item will be put into the ItmPoolDefinition attribute - otherwise it
    will be put into the InvBalanceDefinition attribute, with the given
    `invbalance` string as the type of object being linked to (most commonly
    either WeaponBalanceDefinition or InventoryBalanceDefinition).  An
    optional fourth element will be the BaseValueScaleConstant of the item,
    which will default to 1, otherwise.  An optional *fifth* element can be
    specified to determine whether or not the item/pool will be Actually
    Dropped.
    """
    bal_items = []
    new_items = []
    for item in items:
        if len(item) == 2:
            new_items.append((item[0], item[1], None, 1, True))
        elif len(item) == 3:
            new_items.append((item[0], item[1], item[2], 1, True))
        elif len(item) == 4:
            new_items.append((item[0], item[1], item[2], item[3], True))
        else:
            new_items.append((item[0], item[1], item[2], item[3], item[4]))
    for (classname, weight, invbalance, scale, item_drop) in new_items:
        if classname:
            if invbalance:
                itmpool = 'None'
                invbal = "{}'{}'".format(invbalance, classname)
            else:
                itmpool = "ItemPoolDefinition'{}'".format(classname)
                invbal = 'None'
        else:
            itmpool = 'None'
            invbal = 'None'
        if item_drop:
            drop_string = 'True'
        else:
            drop_string = 'False'
        bal_items.append("""
            (
                ItmPoolDefinition={},
                InvBalanceDefinition={},
                Probability=(
                    BaseValueConstant={},
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant={}
                ),
                bDropOnDeath={}
            )
            """.format(itmpool, invbal, weight, round(scale, 6), drop_string))
    return '({})'.format(','.join(bal_items))

def get_balanced_set(objectname, items):
    """
    Returns a regular "set" command to set `objectname`'s BalancedItems
    attribute to an array with the specified `items`.  The bulk of the
    work here is done in `get_balanced_items()`.
    """
    return "set {} BalancedItems\n{}".format(objectname,
            get_balanced_items(items))

def disable_balanced_drop(prefix, pool, item_num):
    """
    Disables an item in a pool's BalancedItems array.  Rather than actually
    disabling or deleting, we're going to redirect to the locker items pool,
    so that the other drop weights in the pool aren't changed.  The player
    will just see slightly more ammo/health/eridium instead.  Returns a list
    of XMLish strings to add to the mod file.
    """
    global hfs
    to_pool = 'GD_Itempools.LootablePools.Pool_Locker_Items_CashAndAmmo'
    hotfix_id_itmpool = 'disable_balanced_itmpool_{}'.format(hfs.num_hotfixes())
    hotfix_id_invbal = 'disable_balanced_invbal_{}'.format(hfs.num_hotfixes())
    hfs.add_level_hotfix(hotfix_id_itmpool,
        'DisableBalanced',
        ",{},BalancedItems[{}].ItmPoolDefinition,,ItemPoolDefinition'{}'".format(
            pool, item_num, to_pool))
    hfs.add_level_hotfix(hotfix_id_invbal,
        'DisableBalanced',
        ',{},BalancedItems[{}].InvBalanceDefinition,,None'.format(
            pool, item_num))
    return [
            '{}{}'.format(prefix, hfs.get_hotfix(hotfix_id_itmpool).get_xml()),
            '{}{}'.format(prefix, hfs.get_hotfix(hotfix_id_invbal).get_xml()),
        ]

def set_dipl_item_pool(hotfix_name, classname, index, pool,
        level=None, activated=True):
    """
    Sets an entire DefaultItemPoolList entry on the given `classname`, at
    the given `index`, to point towards the pool `pool`.  Will be done with
    a hotfix with the ID `hotfix_name`, optionally in the level `level`.
    To disable (for inclusion into a MUT category, for instance), pass
    `activated`=`False`.
    """
    if level is None:
        level = ''
    hfs.add_level_hotfix(hotfix_name, 'DIPLItemPool',
        """{},{},DefaultItemPoolList[{}],,
        (
            ItemPool=ItemPoolDefinition'{}',
            PoolProbability=(
                BaseValueConstant=1,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1
            )
        )""".format(level, classname, index, pool),
        activated=activated)

def set_pt_cipl_item_pool(hotfix_name, classname, pt_index, cipl_index,
        pool, level=None, activated=True):
    """
    Sets an entire PlayThroughs[x].CustomItemPoolList entry on the given
    `classname`, at the given playthrough index `pt_index` and CIPL index
    `cipl_index`, to point towards the pool `pool`.  Will be done with
    a hotfix with the ID `hotfix_name`, optionally in the level `level`.
    To disable (for inclusion into a MUT category, for instance), pass
    `activated`=`False`.
    """
    if level is None:
        level = ''
    hfs.add_level_hotfix(hotfix_name, 'PTCIPLItemPool',
        """{},{},PlayThroughs[{}].CustomItemPoolList[{}],,
        (
            ItemPool=ItemPoolDefinition'{}',
            PoolProbability=(
                BaseValueConstant=1,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1
            )
        )""".format(level, classname, pt_index, cipl_index, pool),
        activated=activated)

def set_generic_item_prob(hotfix_name, classname, attribute,
        level=None, prob=None, activated=True):
    """
    Sets a probability in the given `classname`, on the attribute `attribute`.
    Will do so via a hotfix with the name `hotfix_name`.  If `prob` is not
    specified, the item will be disabled (ie: given a zero probability).
    Otherwise, pass `1` for the prob (or any other percentage you want).
    To disable the hotfix by default (for inclusion in a MUT, for instance),
    pass `activated`=`False`.
    """
    global hfs
    if level is None:
        level = ''
    if prob is None:
        prob = 0
    hfs.add_level_hotfix(hotfix_name, 'Disable',
        """{},{},{},,
        (
            BaseValueConstant={},
            BaseValueAttribute=None,
            InitializationDefinition=None,
            BaseValueScaleConstant=1
        )""".format(level, classname, attribute, prob),
        activated=activated)

def set_bi_item_pool(hotfix_name, classname, index, item,
        level=None, prob=None, activated=True, invbalance=None):
    """
    Sets an entire BalancedItem structure
    """
    global hfs
    if level is None:
        level = ''
    if prob is None:
        prob = 1
    if invbalance:
        itmpool = 'None'
        invbal = "{}'{}'".format(invbalance, item)
    else:
        itmpool = "ItemPoolDefinition'{}'".format(item)
        invbal = 'None'
    hfs.add_level_hotfix(hotfix_name, 'SetBIItem',
        """{},{},BalancedItems[{}],,
        (
            ItmPoolDefinition={},
            InvBalanceDefinition={},
            Probability=(
                BaseValueConstant={},
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant=1
            ),
            bDropOnDeath=True
        )""".format(level, classname, index, itmpool, invbal, prob),
        activated=activated)

def set_bi_item_prob(hotfix_name, classname, index, level=None,
        prob=None, activated=True):
    """
    Sets a BalancedItems probability.
    """
    set_generic_item_prob(hotfix_name, classname,
        'BalancedItems[{}].Probability'.format(index),
        level=level,
        prob=prob,
        activated=activated)

def set_dipl_item_prob(hotfix_name, classname, index, level=None,
        prob=None, activated=True):
    """
    Sets a DefaultItemPoolList probability.
    """
    set_generic_item_prob(hotfix_name, classname,
        'DefaultItemPoolList[{}].PoolProbability'.format(index),
        level=level,
        prob=prob,
        activated=activated)

def set_pt_cipl_item_prob(hotfix_name, classname,
        pt_index, poollist_index, level=None, prob=None, activated=True):
    """
    Sets a PlayThroughs[x].CustomItemPoolList probability in the given
    `classname`, at the playthrough index `pt_index` and CustomItemPoolList
    index `poollist_index`.
    """
    set_generic_item_prob(hotfix_name, classname,
        'PlayThroughs[{}].CustomItemPoolList[{}].PoolProbability'.format(
            pt_index, poollist_index),
        level=level,
        prob=prob,
        activated=activated)

def set_ld_item_weight(hotfix_name, classname, index, level=None,
        weight=None, activated=True):
    """
    Sets a LootData item weight.
    """
    set_generic_item_prob(hotfix_name, classname,
        'LootData[{}].PoolProbability'.format(index),
        level=level,
        prob=weight,
        activated=activated)

def set_ld_ia_item_pool(hotfix_name, classname, pool, ld_index, ia_index,
        point=None, level=None, activated=True, main_attr='LootData'):
    """
    Sets an `ItemPool` pool inside a `LootData[x].ItemAttachments[y]` structure,
    inside the class `classname`, LootData index `ld_index`, and ItemAttachments
    index `ia_index`.  Will use the hotfix name `hotfix_name`.  `activated` is
    a boolean describing if the hotfix will be active or not.  If `level` is passed
    in, the hotfix will only be active for the given level.  If `point` is passed
    in, we will additionally create another hotfix (with the name suffixed with
    "_point") which sets the attachment point for the newly-defined pool.  To
    use a different top-level attribute than `LootData`, pass in `main_attr`.
    """
    global hfs
    if not level:
        level = 'None'
    hfs.add_level_hotfix(hotfix_name, 'LDIAPool',
        """{level},
        {classname},
        {main_attr}[{ld_index}].ItemAttachments[{ia_index}].ItemPool,,
        ItemPoolDefinition'{pool}'""".format(
            level=level,
            classname=classname,
            main_attr=main_attr,
            ld_index=ld_index,
            ia_index=ia_index,
            pool=pool),
        activated=activated)
    if point:
        hfs.add_level_hotfix('{}_point'.format(hotfix_name),
            'LDIAPoolPoint',
            """{level},
            {classname},
            {main_attr}[{ld_index}].ItemAttachments[{ia_index}].AttachmentPointName,,
            {point}""".format(
                level=level,
                classname=classname,
                main_attr=main_attr,
                ld_index=ld_index,
                ia_index=ia_index,
                point='"{}"'.format(point)),
            activated=activated)

def set_dl_ia_item_pool(hotfix_name, classname, pool, ld_index, ia_index,
        point=None, level=None, activated=True):
    """
    Sets an `ItemPool` pool inside a `DefaultLoot[x].ItemAttachments[y]` structure.
    """
    set_ld_ia_item_pool(hotfix_name, classname, pool, ld_index, ia_index,
        point=point, level=level, activated=activated, main_attr='DefaultLoot')

def setup_boss_pool(hotfix_id, level, pool, default_gear, unique_gear, activated=True):
    """
    Sets up our specified `pool` using the given `hotfix_id`, active in the
    level `level`.  The "default" ItemPool which the boss ordinarily draws from
    is specified by `default_gear`, and the pool's unique gear in a list of
    `unique_gear`, each element of which should be a tuple with three elements:
        1) The unique pool to drop from / gear to drop.
        2) The percent chance of dropping this pool/gear
        3) If this is an item, the InvBalanceDefinition type of the item.
    If the total of all the percent chances in `unique_gear` is greater than
    1, the `default_gear` will never actually be dropped.  To disable this
    hotfix (for inclusion in a MUT, for instance) pass `activated`=`False`.
    `default_gear` may also be a tuple, with the following elements:
        1) The pool to drop from / gear to drop.
        2) If this is an item, the InvBalanceDefinition type of the item.
    """
    global hfs
    total_unique = 0
    bal_items_tuples = []
    for (unique, pct, baldef) in unique_gear:
        total_unique += pct
        bal_items_tuples.append((unique, round(pct, 6), baldef))
    if level:
        level_str = level
    else:
        level_str = ''
    if default_gear and total_unique < 1:
        try:
            (default_name, default_baldef) = default_gear
            bal_items_tuples.append((default_name, round(1 - total_unique, 6), default_baldef))
        except ValueError:
            bal_items_tuples.append((default_gear, round(1 - total_unique, 6), None))
    hfs.add_level_hotfix(hotfix_id, 'BossPool',
        '{},{},BalancedItems,,{}'.format(
            level_str,
            pool,
            get_balanced_items(bal_items_tuples)),
        activated=activated)

###
### Code to generate the mod
###

hfs = Hotfixes()
regular = Regular(hfs)
badass = Badass(hfs)
other = OtherConfig()

# Get rid of global world drops.
prefix = ' '*(4*5)
drop_disables = []
drop_chest_disables = []
for (pool, index) in [
        ('GD_Itempools.GeneralItemPools.Pool_Gear', 0),
        ('GD_Itempools.GeneralItemPools.Pool_GunsAndGear', 0),
        ('GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne', 0),
        ('GD_Itempools.GeneralItemPools.Pool_GunsAndGear', 1),
        ('GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne', 1),
        ('GD_Itempools.GeneralItemPools.Pool_Items_Small', 1),
        ('GD_Ma_ItemPools.GeneralItemPools.Pool_GunsAndGear_Marigold', 0),
        ('GD_Ma_ItemPools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne_Marigold', 0),
        ('GD_Ma_ItemPools.GeneralItemPools.Pool_GunsAndGear_Marigold', 1),
        ('GD_Ma_ItemPools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne_Marigold', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_01_Common', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_01_Common', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_02_Uncommon', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_02_Uncommon', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_02_UncommonsRaid', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_02_UncommonsRaid', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_RaresRaid', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_RaresRaid', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedLasers', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedLasers', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedLasers', 2),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedLaunchers', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedLaunchers', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedLaunchers', 2),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedPistols', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedPistols', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedPistols', 2),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedRifles', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedRifles', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedRifles', 2),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedShotguns', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedShotguns', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedShotguns', 2),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedSMGs', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedSMGs', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedSMGs', 2),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedSniper', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedSniper', 1),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedSniper', 2),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedShields', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_WeightedShields', 1),
        ]:
    drop_disables.extend(disable_balanced_drop(prefix, pool, index))
other.disable_world_sets = "\n\n".join(drop_disables)

# A separate set of hotfixes for chests, so they can be easily toggled in FT/BLCMM
prefix = ' '*(4*5)
for (pool, index) in [
        # The Pool_GunsAndGear_06_Legendary_Moonstone pool doesn't seem to be actually
        # used anywhere, but whatever.
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary_Moonstone', 0),
        ('GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary_Moonstone', 1),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear', 1),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear', 2),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear', 3),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear', 4),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items', 0),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items', 1),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items', 2),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items', 3),
        ('GD_Ma_ItemPools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear_Marigold', 1),
        ('GD_Ma_ItemPools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear_Marigold', 2),
        ('GD_Ma_ItemPools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear_Marigold', 3),
        ('GD_Ma_ItemPools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear_Marigold', 4),
        ('GD_Ma_ItemPools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear_Marigold', 7),
        ]:
    drop_chest_disables.extend(disable_balanced_drop(prefix, pool, index))
other.disable_world_chest_sets = "\n\n".join(drop_chest_disables)

# Moonstone chests cost Eridium to open up, and paying 40E to get a couple bucks
# and some shotgun ammo is needlessly cruel.  :)  So, completely disable those
# options so that Moonstone chests always contain gear.
hfs.add_level_hotfix('moonstone_disable_0', 'MoonstoneDisable',
    """,
    GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary_Moonstone,
    BalancedItems[0].Probability,,
    (
        BaseValueConstant=0,
        BaseValueAttribute=None, 
        InitializationDefinition=None,
        BaseValueScaleConstant=0
    )""")
hfs.add_level_hotfix('moonstone_disable_1', 'MoonstoneDisable',
    """,
    GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary_Moonstone,
    BalancedItems[1].Probability,,
    (
        BaseValueConstant=0,
        BaseValueAttribute=None, 
        InitializationDefinition=None,
        BaseValueScaleConstant=0
    )""")

# Configure rarity pools
prefix = ' '*(4*4)
claptastic_levels = [
        'Ma_LeftCluster_P',
        'Ma_RightCluster_P',
        'Ma_SubBoss_P',
        'Ma_Deck13_P',
        'Ma_FinalBoss_P',
        'Ma_Motherboard_P',
        'Ma_Nexus_P',
        'Ma_Subconscious_P',
    ]
rarity_sections = {}
line_prefix = ''
line_suffix = ''
hotfix_activated = True
for (rarity_key, rarity_label) in DropConfig.rarity_presets:

    hotfix_list = []
    for config in [regular, badass]:

        config.set_rarity_weights(rarity_key)

        config.set_rarity_ar = get_balanced_set(
            config.rarity_pool_ar,
            [
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_01_Common', config.weight_common, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_01_Common', config.weight_common, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_02_Uncommon', config.weight_uncommon, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_02_Uncommon', config.weight_uncommon, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', config.weight_rare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', config.weight_rare, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', config.weight_veryrare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', config.weight_veryrare, None, 1, False),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_AssaultRifles_Glitch_Marigold', config.weight_glitch_normal, None, 1, True),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_AssaultRifles_Glitch_Marigold', config.weight_glitch_normal, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary', config.weight_legendary, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary', config.weight_legendary, None, 1, False),
            ])

        config.set_rarity_launchers = get_balanced_set(
            config.rarity_pool_launchers,
            [
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_01_Common', config.weight_common, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_01_Common', config.weight_common, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_02_Uncommon', config.weight_uncommon, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_02_Uncommon', config.weight_uncommon, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', config.weight_rare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', config.weight_rare, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', config.weight_veryrare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', config.weight_veryrare, None, 1, False),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Launchers_Glitch_Marigold', config.weight_glitch_normal, None, 1, True),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Launchers_Glitch_Marigold', config.weight_glitch_normal, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary', config.weight_legendary, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary', config.weight_legendary, None, 1, False),
            ])

        config.set_rarity_pistols = get_balanced_set(
            config.rarity_pool_pistols,
            [
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common', config.weight_common, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common', config.weight_common, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_02_Uncommon', config.weight_uncommon, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_02_Uncommon', config.weight_uncommon, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', config.weight_rare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', config.weight_rare, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', config.weight_veryrare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', config.weight_veryrare, None, 1, False),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Pistols_Glitch_Marigold', config.weight_glitch_normal, None, 1, True),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Pistols_Glitch_Marigold', config.weight_glitch_normal, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', config.weight_legendary, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', config.weight_legendary, None, 1, False),
            ])

        config.set_rarity_smg = get_balanced_set(
            config.rarity_pool_smg,
            [
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_01_Common', config.weight_common, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_01_Common', config.weight_common, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_02_Uncommon', config.weight_uncommon, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_02_Uncommon', config.weight_uncommon, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', config.weight_rare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', config.weight_rare, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', config.weight_veryrare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', config.weight_veryrare, None, 1, False),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_SMG_Glitch_Marigold', config.weight_glitch_normal, None, 1, True),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_SMG_Glitch_Marigold', config.weight_glitch_normal, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary', config.weight_legendary, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary', config.weight_legendary, None, 1, False),
            ])

        config.set_rarity_shotguns = get_balanced_set(
            config.rarity_pool_shotguns,
            [
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_01_Common', config.weight_common, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_01_Common', config.weight_common, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_02_Uncommon', config.weight_uncommon, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_02_Uncommon', config.weight_uncommon, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', config.weight_rare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', config.weight_rare, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', config.weight_veryrare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', config.weight_veryrare, None, 1, False),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Shotguns_Glitch_Marigold', config.weight_glitch_normal, None, 1, True),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Shotguns_Glitch_Marigold', config.weight_glitch_normal, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary', config.weight_legendary, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary', config.weight_legendary, None, 1, False),
            ])

        config.set_rarity_snipers = get_balanced_set(
            config.rarity_pool_snipers,
            [
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_01_Common', config.weight_common, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_01_Common', config.weight_common, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_02_Uncommon', config.weight_uncommon, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_02_Uncommon', config.weight_uncommon, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', config.weight_rare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', config.weight_rare, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', config.weight_veryrare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', config.weight_veryrare, None, 1, False),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Sniper_Glitch_Marigold', config.weight_glitch_normal, None, 1, True),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Sniper_Glitch_Marigold', config.weight_glitch_normal, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary', config.weight_legendary, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary', config.weight_legendary, None, 1, False),
            ])

        config.set_rarity_lasers = get_balanced_set(
            config.rarity_pool_lasers,
            [
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_01_Common', config.weight_common, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_01_Common', config.weight_common, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_02_Uncommon', config.weight_uncommon, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_02_Uncommon', config.weight_uncommon, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare', config.weight_rare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_04_Rare', config.weight_rare, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_05_VeryRare', config.weight_veryrare, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_05_VeryRare', config.weight_veryrare, None, 1, False),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Lasers_Glitch_Marigold', config.weight_glitch_normal, None, 1, True),
                ('GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Lasers_Glitch_Marigold', config.weight_glitch_normal, None, 1, False),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_06_Legendary', config.weight_legendary, None, 1, True),
                ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_06_Legendary', config.weight_legendary, None, 1, False),
            ])

        # Shield pool (rarity + equip in one, since we don't need to make two choices)
        # Also, to support easier shields in the intro level (so that it's not too hard) we're using
        # a global level hotfix here, instead of a set.  Then we can easily override for the intro
        # level.

        hotfix_id = 'shield_equip_pool_{}_{}'.format(rarity_key, config.hotfix_prefix)
        hfs.add_level_hotfix(hotfix_id, 'ShieldEquipPool',
                ',{},BalancedItems,,{}'.format(
                    config.equip_pool_shields,
                    get_balanced_items([
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_01_Common', config.weight_common, None, 1, True),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_01_Common', config.weight_common, None, 1, False),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_02_Uncommon', config.weight_uncommon, None, 1, True),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_02_Uncommon', config.weight_uncommon, None, 1, False),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare', config.weight_rare, None, 1, True),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare', config.weight_rare, None, 1, False),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare', config.weight_veryrare, None, 1, True),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare', config.weight_veryrare, None, 1, False),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary', config.weight_legendary, None, 1, True),
                            ('GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary', config.weight_legendary, None, 1, False),
                        ])),
                    activated=hotfix_activated)
        config.set_shields = hfs.get_hotfix_xml(hotfix_id)

        # We save ourselves having to use a bunch more loot pools than necessary
        # by using hotfixes to dynamically change the weights depending on if we're
        # in a Claptastic Voyage map or not.  We set up a "base" hotfix which fires
        # on all levels, and then a whole bunch of level-specific ones to fire
        # afterwards on Claptastic Voyage levels.

        rarity_hfs = Hotfixes(nameprefix='Apoc{}{}RarityFix'.format(
            config.hotfix_prefix.capitalize(), rarity_key.capitalize()))
        glitch_indexes = [8, 9]
        for pool in [
                config.rarity_pool_ar,
                config.rarity_pool_launchers,
                config.rarity_pool_pistols,
                config.rarity_pool_smg,
                config.rarity_pool_shotguns,
                config.rarity_pool_snipers,
                config.rarity_pool_lasers,
                ]:
            for idx in glitch_indexes:
                hfs_id = 'rarity_{}'.format(len(rarity_hfs.hotfixes))
                rarity_hfs.add_level_hotfix(hfs_id, 'Set',
                    ',{},BalancedItems[{}].Probability.BaseValueConstant,,{}'.format(
                        pool, idx, config.weight_glitch_normal),
                    activated=hotfix_activated)
                hotfix_list.append('{}{}'.format(prefix, rarity_hfs.get_hotfix_xml(hfs_id)))
            for level in claptastic_levels:
                for idx in glitch_indexes:
                    hfs_id = 'rarity_{}'.format(len(rarity_hfs.hotfixes))
                    rarity_hfs.add_level_hotfix(hfs_id, 'Set',
                        '{},{},BalancedItems[{}].Probability.BaseValueConstant,,{}'.format(
                            level, pool, idx, config.weight_glitch_claptastic),
                        activated=hotfix_activated)
                    hotfix_list.append('{}{}'.format(prefix, rarity_hfs.get_hotfix_xml(hfs_id)))

    # Join up our claptastic support hotfixes
    claptastic_support_str = "\n\n".join(hotfix_list)

    # The first level in the game has some special Dahl marines who have a limited
    # equipment set.  We're customizing the three pools which are used to all have
    # the same stuff.  We allow for a wider range of equipment, but we're restricting
    # it to blue and lower (and blue has a decreased chance).  Note that even though
    # the pool names say "Pistol", the DahlIntro one already allows for lasers as well.
    hotfix_list = []
    for (idx, pool) in enumerate([
            'GD_ItempoolsEnemyUse.WeaponPools.Pool_Weapons_Pistols_EnemyUse',
            'GD_ItempoolsEnemyUse.WeaponPools.Pool_Weapons_Pistols_EnemyUse_DahlIntro',
            'GD_ItempoolsEnemyUse.WeaponPools.Pool_Weapons_Pistols_EnemyUse_Intro',
            ]):
        hfs_id = 'intro_{}'.format(idx)
        rarity_hfs.add_level_hotfix(hfs_id, 'IntroPools',
            'MoonShotIntro_P,{},BalancedItems,,{}'.format(
                pool,
                get_balanced_items([
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common', regular.weight_common, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common', regular.weight_common, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_02_Uncommon', regular.weight_uncommon, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_02_Uncommon', regular.weight_uncommon, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', regular.weight_rare/2, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', regular.weight_rare/2, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_01_Common', regular.weight_common, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_01_Common', regular.weight_common, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_02_Uncommon', regular.weight_uncommon, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_02_Uncommon', regular.weight_uncommon, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', regular.weight_rare/2, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', regular.weight_rare/2, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_01_Common', regular.weight_common, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_01_Common', regular.weight_common, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_02_Uncommon', regular.weight_uncommon, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_02_Uncommon', regular.weight_uncommon, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', regular.weight_rare/2, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', regular.weight_rare/2, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_01_Common', regular.weight_common, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_01_Common', regular.weight_common, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_02_Uncommon', regular.weight_uncommon, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_02_Uncommon', regular.weight_uncommon, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_01_Common', regular.weight_common, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_01_Common', regular.weight_common, None, 1, False),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_02_Uncommon', regular.weight_uncommon, None, 1, True),
                        ('GD_Itempools.WeaponPools.Pool_Weapons_Lasers_02_Uncommon', regular.weight_uncommon, None, 1, False),
                    ])),
                activated=hotfix_activated)
        hotfix_list.append('{}{}'.format(prefix, rarity_hfs.get_hotfix_xml(hfs_id)))

    # Also nerf our shield equip pool during the intro - with "excellent" rarity
    # presets it becomes a pretty difficult fight.  Purple shields and all.  Also
    # note that we must specifically exclude Turtle/Juggernaut shields from here.
    # The health scaling of the early-game Dahl troops is such that even white-rarity
    # Turtle shields will make them literally unkillable, which in addition to being
    # annoying, breaks the intro game sequence.
    hfs_id = 'intro_shield_equip_pool_{}'.format(rarity_key)
    other_scale = .6
    rarity_hfs.add_level_hotfix(hfs_id, 'IntroShieldEquipPool',
            'MoonShotIntro_P,{},BalancedItems,,{}'.format(
                regular.equip_pool_shields,
                get_balanced_items([
                        ('GD_Itempools.ShieldPools.Pool_Shields_Standard_01_Common', regular.weight_common, None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Standard_01_Common', regular.weight_common, None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Standard_02_Uncommon', regular.weight_uncommon, None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Standard_02_Uncommon', regular.weight_uncommon, None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Standard_04_Rare', regular.weight_rare/2, None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Standard_04_Rare', regular.weight_rare/2, None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Absorption_01_Common', round(regular.weight_common*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Absorption_01_Common', round(regular.weight_common*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Absorption_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Absorption_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Booster_01_Common', round(regular.weight_common*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Booster_01_Common', round(regular.weight_common*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Booster_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Booster_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Chimera_01_Common', round(regular.weight_common*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Chimera_01_Common', round(regular.weight_common*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Chimera_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Chimera_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Impact_01_Common', round(regular.weight_common*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Impact_01_Common', round(regular.weight_common*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Impact_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Impact_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_NovaShields_All_01_Common', round(regular.weight_common*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_NovaShields_All_01_Common', round(regular.weight_common*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_NovaShields_All_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_NovaShields_All_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Roid_01_Common', round(regular.weight_common*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Roid_01_Common', round(regular.weight_common*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Roid_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_Roid_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_SpikeShields_All_01_Common', round(regular.weight_common*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_SpikeShields_All_01_Common', round(regular.weight_common*other_scale, 6), None, 1, False),
                        ('GD_Itempools.ShieldPools.Pool_Shields_SpikeShields_All_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, True),
                        ('GD_Itempools.ShieldPools.Pool_Shields_SpikeShields_All_02_Uncommon', round(regular.weight_uncommon*other_scale, 6), None, 1, False),
                    ])),
                activated=hotfix_activated)
    hotfix_list.append('{}{}'.format(prefix, rarity_hfs.get_hotfix_xml(hfs_id)))

    # Join up our intro pool hotfixes
    intro_pool_support_str = "\n\n".join(hotfix_list)

    # Dahl snipers have their own equip pool which restricts them to only Dahl
    # sniper rifles (with Hyperion barrel, apparently).  We'll widen that up a bit
    # to allow *any* Dahl sniper (and use our regular weight, as well)

    for (idx, weight) in enumerate([
            regular.weight_common,
            regular.weight_common,
            regular.weight_uncommon,
            regular.weight_uncommon,
            regular.weight_rare,
            regular.weight_rare,
            regular.weight_veryrare,
            regular.weight_veryrare,
            regular.weight_glitch_normal,
            regular.weight_glitch_normal,
            regular.weight_legendary/2,
            regular.weight_legendary/2,
            regular.weight_legendary/2,
            ]):
        rarity_hfs.add_level_hotfix('dahl_sniper_activate_{}'.format(idx),
                'DahlSniperActivatePool{}'.format(rarity_key.capitalize()),
                ',{},BalancedItems[{}].Probability.BaseValueConstant,,{}'.format(
                    'GD_DahlSniper.WeaponPools.Pool_Weapons_HypSniper_EnemyUse_NoScheduling',
                    idx,
                    weight),
                activated=hotfix_activated)

    # Now construct the rarity section

    with open('input-file-rarity.txt', 'r') as df:
        rarity_sections[rarity_key] = df.read().format(
                section_label=rarity_label,
                line_prefix=line_prefix,
                line_suffix=line_suffix,
                regular=regular,
                badass=badass,
                claptastic_support_str=claptastic_support_str,
                intro_pool_support_str=intro_pool_support_str,
                hotfixes=rarity_hfs,
                )

    line_prefix = '#'
    line_suffix = '<off>'
    hotfix_activated = False

# Configure the drop percentages per rarity level
rarity_drop_prob_sections = {}
prefix = ' '*(4*4)
line_prefix = ''
line_suffix = ''
hotfix_activated = True
for (rarity_key, rarity_label) in DropConfig.rarity_drop_prob_presets:
    drop_prob_hfs = Hotfixes(nameprefix='ApocRarityDropProb{}'.format(rarity_key.capitalize()))
    hotfix_list = []
    for config in [regular, badass]:
        rarity_drop_prob = config.rarity_drop_prob[rarity_key]
        (T_GUN, T_SHIELD, T_DAHLINTRO, T_DAHLINTROSHIELD) = range(4)
        for (pooldesc, pool, pooltype, has_regular, has_badass, level) in [
                ('ar', config.rarity_pool_ar, T_GUN, True, True, ''),
                ('launchers', config.rarity_pool_launchers, T_GUN, True, True, ''),
                ('pistols', config.rarity_pool_pistols, T_GUN, True, True, ''),
                ('smg', config.rarity_pool_smg, T_GUN, True, True, ''),
                ('shotguns', config.rarity_pool_shotguns, T_GUN, True, True, ''),
                ('snipers', config.rarity_pool_snipers, T_GUN, True, True, ''),
                ('lasers', config.rarity_pool_lasers, T_GUN, True, True, ''),
                ('shields', config.equip_pool_shields, T_SHIELD, True, True, ''),
                ('dahl0', 'GD_ItempoolsEnemyUse.WeaponPools.Pool_Weapons_Pistols_EnemyUse', T_DAHLINTRO, True, False, 'MoonShotIntro_P'),
                ('dahl1', 'GD_ItempoolsEnemyUse.WeaponPools.Pool_Weapons_Pistols_EnemyUse_DahlIntro', T_DAHLINTRO, True, False, 'MoonShotIntro_P'),
                ('dahl2', 'GD_ItempoolsEnemyUse.WeaponPools.Pool_Weapons_Pistols_EnemyUse_Intro', T_DAHLINTRO, True, False, 'MoonShotIntro_P'),
                ('dahl3', regular.equip_pool_shields, T_DAHLINTROSHIELD, True, False, 'MoonShotIntro_P'),
                ('dahl4', 'GD_DahlSniper.WeaponPools.Pool_Weapons_HypSniper_EnemyUse_NoScheduling', T_GUN, True, False, ''),
                ]:
            if config.hotfix_prefix == 'reg' and not has_regular:
                continue
            if config.hotfix_prefix == 'badass' and not has_badass:
                continue
            if pool:
                if pooltype == T_GUN:
                    rarities = ['common', 'uncommon', 'rare', 'veryrare', 'glitch', 'legendary']
                elif pooltype == T_SHIELD:
                    rarities = ['common', 'uncommon', 'rare', 'veryrare', 'legendary']
                elif pooltype == T_DAHLINTRO:
                    rarities = ['common', 'uncommon', 'rare']*3 + ['common', 'uncommon']*2
                elif pooltype == T_DAHLINTROSHIELD:
                    rarities = ['common', 'uncommon', 'rare'] + ['common', 'uncommon']*7
                else:
                    raise Exception('Unknown pool type: {}'.format(pooltype))
                for (idx, rarity) in enumerate(rarities):
                    prob_val = rarity_drop_prob[rarity]
                    
                    # Make Dahl Intro pools drop a bit more frequently than usual
                    if pooltype == T_DAHLINTRO or pooltype == T_DAHLINTROSHIELD:
                        prob_val = (prob_val*3 + 1)/4

                    hotfix_id = 'rarity_drop_prob_{}_{}_{}_{}'.format(config.hotfix_prefix, pooldesc, rarity, len(hotfix_list))
                    drop_prob_hfs.add_level_hotfix(hotfix_id, 'Idx',
                            '{},{},BalancedItems[{}].Probability.BaseValueScaleConstant,,{}'.format(
                                level, pool, idx*2, round(prob_val, 6)
                                ),
                            activated=hotfix_activated)
                    hotfix_list.append('{}{}'.format(prefix, drop_prob_hfs.get_hotfix_xml(hotfix_id)))
                    hotfix_id = 'rarity_drop_prob_{}_{}_{}_{}'.format(config.hotfix_prefix, pooldesc, rarity, len(hotfix_list))
                    drop_prob_hfs.add_level_hotfix(hotfix_id, 'Idx',
                            '{},{},BalancedItems[{}].Probability.BaseValueScaleConstant,,{}'.format(
                                level, pool, (idx*2)+1, round(1-prob_val, 6)
                                ),
                            activated=hotfix_activated)
                    hotfix_list.append('{}{}'.format(prefix, drop_prob_hfs.get_hotfix_xml(hotfix_id)))

    # Now construct the rarity section

    with open('input-file-droppct.txt', 'r') as df:
        rarity_drop_prob_sections[rarity_key] = df.read().format(
                section_label=rarity_label,
                line_prefix=line_prefix,
                line_suffix=line_suffix,
                pct_common=round(regular.rarity_drop_prob[rarity_key]['common']*100),
                pct_uncommon=round(regular.rarity_drop_prob[rarity_key]['uncommon']*100),
                pct_rare=round(regular.rarity_drop_prob[rarity_key]['rare']*100),
                pct_veryrare=round(regular.rarity_drop_prob[rarity_key]['veryrare']*100),
                pct_glitch=round(regular.rarity_drop_prob[rarity_key]['glitch']*100),
                pct_legendary=round(regular.rarity_drop_prob[rarity_key]['legendary']*100),
                drop_prob_hotfixes="\n\n".join(hotfix_list),
                )

    line_prefix = '#'
    line_suffix = '<off>'
    hotfix_activated = False

# Configure the gun type probabilities
for config in [regular, badass]:

    # Configure Equip pools

    config.set_equip_all = get_balanced_set(
        config.equip_pool_all,
        [
            (config.rarity_pool_pistols, config.drop_prob_pistols),
            (config.rarity_pool_ar, config.drop_prob_ar),
            (config.rarity_pool_smg, config.drop_prob_smg),
            (config.rarity_pool_shotguns, config.drop_prob_shotguns),
            (config.rarity_pool_snipers, config.drop_prob_snipers),
            (config.rarity_pool_launchers, config.drop_prob_launchers, None, 0),
            (config.rarity_pool_lasers, config.drop_prob_lasers),
        ])

    config.set_equip_ar = get_balanced_set(
        config.equip_pool_ar,
        [
            (config.rarity_pool_pistols, config.drop_prob_pistols),
            (config.rarity_pool_ar, config.drop_prob_ar*config.weight_scale),
            (config.rarity_pool_smg, config.drop_prob_smg),
            (config.rarity_pool_shotguns, config.drop_prob_shotguns),
            (config.rarity_pool_snipers, config.drop_prob_snipers),
            (config.rarity_pool_launchers, config.drop_prob_launchers, None, 0),
            (config.rarity_pool_lasers, config.drop_prob_lasers),
        ])

    if config.equip_pool_launchers:
        config.set_equip_launchers = get_balanced_set(
            config.equip_pool_launchers,
            [
                (config.rarity_pool_launchers, 1),
            ])

    config.set_equip_shotguns = get_balanced_set(
        config.equip_pool_shotguns,
        [
            (config.rarity_pool_shotguns, 1),
        ])

    if config.equip_pool_snipers:
        config.set_equip_snipers = get_balanced_set(
            config.equip_pool_snipers,
            [
                (config.rarity_pool_snipers, 1),
            ])

    if config.equip_pool_only_lasers:
        config.set_equip_only_lasers = get_balanced_set(
            config.equip_pool_only_lasers,
            [
                (config.rarity_pool_lasers, 1),
            ])

    config.set_equip_lasers = get_balanced_set(
        config.equip_pool_lasers,
        [
            (config.rarity_pool_pistols, config.drop_prob_pistols),
            (config.rarity_pool_ar, config.drop_prob_ar),
            (config.rarity_pool_smg, config.drop_prob_smg),
            (config.rarity_pool_shotguns, config.drop_prob_shotguns),
            (config.rarity_pool_snipers, config.drop_prob_snipers),
            (config.rarity_pool_launchers, config.drop_prob_launchers, None, 0),
            (config.rarity_pool_lasers, config.drop_prob_lasers*config.weight_scale),
        ])

    # Hotfixes to enable rocket launchers for all our general-purpose pools.
    for (pooltype, pool) in [
            ('all', config.equip_pool_all),
            ('ar', config.equip_pool_ar),
            ('lasers', config.equip_pool_lasers),
            ]:
        hfs.add_level_hotfix('rocket_enable_{}_{}'.format(config.hotfix_prefix, pooltype),
                'RocketEnable',
                ',{},BalancedItems[5].Probability.BaseValueScaleConstant,,1'.format(pool))
        hfs.add_level_hotfix('rocket_disable_{}_{}'.format(config.hotfix_prefix, pooltype),
                'RocketDisable',
                ',{},BalancedItems[5].Probability.BaseValueScaleConstant,,0'.format(pool),
                activated=False)

# Legendary Pool management
unique_hotfixes = []
uniqueglitch_hotfixes = []
for (guntype, legendaries, uniques, uniqueglitches) in [
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
                'GD_Cork_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Moxxis_Probe',
                'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Bandit_3_PartyPopper',
                'GD_Ma_Weapons.A_Weapons_Unique.Pistol_Maliwan_3_HardReboot',
                'GD_Petunia_Weapons.Pistols.Pistol_Hyperion_3_T4sr',
            ],
            [
                # Unique Glitches
            ],
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
        ),
        ]:

    # First set up a hotfix for the base pool initialization
    initial_pool = []
    for legendary in legendaries:
        initial_pool.append((legendary, 1, 'WeaponBalanceDefinition'))
    for i in range(len(uniques) + len(uniqueglitches)):
        initial_pool.append((None, 0))
    hfs.add_level_hotfix('weapon_pool_clear_{}'.format(guntype.lower()),
        'WeaponPoolClear{}'.format(guntype),
        """,GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary,
        BalancedItems,,{}""".format(
            guntype,
            get_balanced_items(initial_pool),
            ))  

    # Hotfixes to add uniques
    for (idx, unique) in enumerate(uniques):
        hotfix_id = 'unique_weap_add_{}_{}'.format(guntype.lower(), idx)
        unique_hotfixes.append(hotfix_id)
        hfs.add_level_hotfix(hotfix_id,
            'WeaponUniqueAdd{}'.format(guntype),
            """,GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary,
            BalancedItems[{}],,
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
        hotfix_id = 'uniqueglitch_weap_add_{}_{}'.format(guntype.lower(), idx)
        uniqueglitch_hotfixes.append(hotfix_id)
        hfs.add_level_hotfix(hotfix_id,
            'WeaponUniqueGlitchAdd{}'.format(guntype),
            """,GD_Itempools.WeaponPools.Pool_Weapons_{}_06_Legendary,
            BalancedItems[{}],,
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

other.legendary_unique_adds = "\n\n".join(
        ['{}{}'.format(' '*(4*3), hfs.get_hotfix(hotfix_id).get_xml()) for hotfix_id in unique_hotfixes]
    )

other.legendary_uniqueglitch_adds = "\n\n".join(
        ['{}{}'.format(' '*(4*3), hfs.get_hotfix(hotfix_id).get_xml()) for hotfix_id in uniqueglitch_hotfixes]
    )


# Legendary shield pool configuration.  Doing this a bit differently since there's
# not nearly as many shields to handle as weapons.

shields = {
    'GD_Itempools.ShieldPools.Pool_Shields_Booster_06_Legendary': [
        ('asteroidbelt', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_AsteroidBelt'),
        ('slammer', 2, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_MoxxisSlammer'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_Chimera_06_Legendary': [
        ('haymaker', 1, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_Haymaker'),
        ('m0rq', 2, 'GD_Ma_Shields.A_Item_Legendary.ItemGrade_Gear_Shield_Chimera_05_M0RQ'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_Juggernaut_06_Legendary': [
        ('shieldofages', 1, 'GD_Ma_Shields.A_Item_Unique.ItemGrade_Gear_Shield_Juggernaut_03_ShieldOfAges'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_NovaShields_All_06_Legendary': [
        ('sunshine', 3, 'GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Starburst'),
        ('rapidrelease', 4, 'GD_Cork_Shields.A_Item_Custom.ItemGrade_Shield_RapidRelease'),
        ],
    'GD_Itempools.ShieldPools.Pool_Shields_Standard_06_Legendary': [
        ('naught', 1, 'GD_Ma_Shields.A_Item_Unique.ItemGrade_Gear_Shield_Naught'),
        ],
    }
for (pool, shieldlist) in shields.items():
    for (label, index, shieldname) in shieldlist:
        set_bi_item_pool('shield_{}'.format(label),
            pool,
            index,
            shieldname,
            invbalance='InventoryBalanceDefinition')

# Dahl Sniper poool setup
hfs.add_level_hotfix('dahl_sniper_setup', 'DahlSniperPool',
        ',{},BalancedItems,,{}'.format(
            'GD_DahlSniper.WeaponPools.Pool_Weapons_HypSniper_EnemyUse_NoScheduling',
            get_balanced_items([
                    ('GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl', regular.rarities['stock']['common'], 'WeaponBalanceDefinition', 1, True),
                    ('GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl', regular.rarities['stock']['common'], 'WeaponBalanceDefinition', 1, False),
                    ('GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon', regular.rarities['stock']['uncommon'], 'WeaponBalanceDefinition', 1, True),
                    ('GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon', regular.rarities['stock']['uncommon'], 'WeaponBalanceDefinition', 1, False),
                    ('GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare', regular.rarities['stock']['rare'], 'WeaponBalanceDefinition', 1, True),
                    ('GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare', regular.rarities['stock']['rare'], 'WeaponBalanceDefinition', 1, False),
                    ('GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare', regular.rarities['stock']['veryrare'], 'WeaponBalanceDefinition', 1, True),
                    ('GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare', regular.rarities['stock']['veryrare'], 'WeaponBalanceDefinition', 1, False),
                    ('GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch', regular.rarities['stock']['glitch_normal'], 'WeaponBalanceDefinition', 1, True),
                    ('GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch', regular.rarities['stock']['glitch_normal'], 'WeaponBalanceDefinition', 1, False),
                    ('GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork', regular.rarities['stock']['legendary']/2, 'WeaponBalanceDefinition', 1, True),
                    ('GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork', regular.rarities['stock']['legendary']/2, 'WeaponBalanceDefinition', 1, False),
                    ('GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek', regular.rarities['stock']['legendary']/2, 'WeaponBalanceDefinition', 0),
                ])))

hfs.add_level_hotfix('dahl_sniper_unique', 'DahlSniperPool',
        ',{},BalancedItems[12].Probability.BaseValueScaleConstant,,1'.format(
            'GD_DahlSniper.WeaponPools.Pool_Weapons_HypSniper_EnemyUse_NoScheduling'))

# No extra shields (dummy statement)
hfs.add_level_hotfix('moreshields_dummy', 'MoreShields',
        'MoreShieldsDummy_P,GD_MoreShieldsDummy,DummyAttribute,1,1',
        activated=False)

# Add a chance of shields to early-game enemies so that there's a reasonable
# chance of getting shield drops (would be very thin on the ground, otherwise)
moreshields_real_list = []
prefix = ' '*(4*4)

# First up: enemies with a CIPL on PT[0] without any shield entry
for (pool, chance) in [
        ('GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavMidget_Mercday', .2),
        ('GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidget', .2),
        ('GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavMidget_Pandoracorn', .2),
        ('GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavMidget_Pumpkin', .2),
        ('GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavMidgetSpaceman', .3),
        ('GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavNomad', .3),
        ]:
    hotfix_id = 'more_shields_{}'.format(len(moreshields_real_list))
    hfs.add_level_hotfix(hotfix_id, 'MoreShields',
            """,{},PlayThroughs[0].CustomItemPoolList,,
            +(
                ItemPool=ItemPoolDefinition'{}',
                PoolProbability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant={}
                )
            )
            """.format(
                pool,
                regular.equip_pool_shields,
                chance))
    moreshields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(hotfix_id)))

# Next: enemies without DIPL or CIPL at all (populate CIPL)
for (pool, chance) in [
        ('GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerPsycho_Mercday', .2),
        ('GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerPsycho_Pandoracorn', .2),
        ('GD_Population_Scavengers.Balance.Psychos.PawnBalance_ScavengerPsycho', .2),
        ('GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerPsycho_Pumpkin', .2),
        ('GD_Population_Scavengers.Balance.Midgets.PawnBalance_ScavPsychoMidget', .33),
        ('GD_Population_Darksiders.Balance.PawnBalance_DarksiderPsycho', .1),
        ]:
    hotfix_id = 'more_shields_{}'.format(len(moreshields_real_list))
    hfs.add_level_hotfix(hotfix_id, 'MoreShields',
            """,{},PlayThroughs[0].CustomItemPoolList,,
            (
                (
                    ItemPool=ItemPoolDefinition'{}',
                    PoolProbability=(
                        BaseValueConstant=1,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant={}
                    )
                )
            )
            """.format(
                pool,
                regular.equip_pool_shields,
                chance))
    moreshields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(hotfix_id)))

# Next: enemies with a CIPL on PT[0] which already has a shield entry (but is typically set to 0)
for (pool, cipl_idx, chance) in [
        ('GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Jetpack_MercDay', 1, .1),
        ('GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Jetpack_Pandoracorn', 1, .1),
        ('GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Jetpack_Pumpkin', 1, .1),
        ('GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit_Jetpack', 1, .1),
        ('GD_Population_Scavengers.Balance.MercDay.PawnBalance_ScavengerBandit_Mercday', 1, .1),
        ('GD_Population_Scavengers.Balance.Pandoracorn.PawnBalance_ScavengerBandit_Pandoracorn', 1, .1),
        ('GD_Population_Scavengers.Balance.PawnBalance_ScavengerBandit', 1, .1),
        ('GD_Population_Scavengers.Balance.Pumpkin.PawnBalance_ScavengerBandit_Pumpkin', 1, .1),
        ]:
    hotfix_id = 'more_shields_{}'.format(len(moreshields_real_list))
    hfs.add_level_hotfix(hotfix_id, 'MoreShields',
            """,{},PlayThroughs[0].CustomItemPoolList[{}].PoolProbability,,
            (
                BaseValueConstant=1,
                BaseValueAttribute=None,
                InitializationDefinition=None,
                BaseValueScaleConstant={}
            )
            """.format(pool, cipl_idx, chance))
    moreshields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(hotfix_id)))

# Finally: enemies with a DIPL which doesn't have shields
for (pool, chance) in [
        ('GD_Population_Darksiders.Balance.PawnBalance_DarksiderBandit', .1),
        ('GD_Population_Darksiders.Balance.PawnBalance_LittleDarksiderBandit', .1),
        ('GD_Population_Darksiders.Balance.PawnBalance_LittleDarksiderPsycho', .1),
        ]:
    hotfix_id = 'more_shields_{}'.format(len(moreshields_real_list))
    hfs.add_level_hotfix(hotfix_id, 'MoreShields',
            """,{},DefaultItemPoolList,,
            +(
                ItemPool=ItemPoolDefinition'{}',
                PoolProbability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant={}
                )
            )
            """.format(
                pool,
                regular.equip_pool_shields,
                chance))
    moreshields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(hotfix_id)))

# Vanilla Stalker shield hotfixes (dummy statement)
hfs.add_level_hotfix('stalker_dummy', 'StalkerShields',
        'StalkerDummy_P,GD_StalkerDummy,DummyAttribute,1,1')

# "Real" Stalker shield hotfixes
stalker_shields_real_list = []
prefix = ' '*(4*3)
for config in [regular, badass]:
    for (idx, (dipl_idx, popdef)) in enumerate(config.stalker_dipl):
        stalker_id = 'real_stalker_{}_{}'.format(config.hotfix_prefix, idx)
        hfs.add_level_hotfix(stalker_id, 'StalkerShields',
            ",{},DefaultItemPoolList[{}].ItemPool,,ItemPoolDefinition'{}'".format(
                popdef, dipl_idx, config.equip_pool_shields,
                ),
            activated=False)
        stalker_shields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(stalker_id)))

# Vanilla Guardian shield hotfixes (dummy statement)
hfs.add_level_hotfix('guardian_dummy', 'GuardianShields',
        'GuardianDummy_P,GD_GuardianDummy,DummyAttribute,1,1')

# "Real" Guardian shield hotfixes
guardian_shields_real_list = []
prefix = ' '*(4*3)
for config in [regular, badass]:
    for (idx, (dipl_idx, popdef)) in enumerate(config.guardian_dipl):
        guardian_id = 'real_guardian_{}_{}'.format(config.hotfix_prefix, idx)
        hfs.add_level_hotfix(guardian_id, 'GuardianShields',
            ",{},DefaultItemPoolList[{}].ItemPool,,ItemPoolDefinition'{}'".format(
                popdef, dipl_idx, config.equip_pool_shields,
                ),
            activated=False)
        guardian_shields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(guardian_id)))
    for (idx, (pt_idx, cipl_idx, popdef)) in enumerate(config.guardian_pt_cipl):
        guardian_id = 'real_guardian_pt_{}_{}'.format(config.hotfix_prefix, idx)
        hfs.add_level_hotfix(guardian_id, 'GuardianShields',
            ",{},PlayThroughs[{}].CustomItemPoolList[{}].ItemPool,,ItemPoolDefinition'{}'".format(
                popdef, pt_idx, cipl_idx, config.equip_pool_shields,
                ),
            activated=False)
        guardian_shields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(guardian_id)))

# Vanilla ClaptasticCreature shield hotfixes (dummy statement)
hfs.add_level_hotfix('clapcreature_dummy', 'ClaptasticCreatureShields',
        'ClaptasticCreatureDummy_P,GD_ClaptasticCreatureDummy,DummyAttribute,1,1')

# "Real" ClaptasticCreature shield hotfixes
clapcreature_shields_real_list = []
prefix = ' '*(4*3)
for config in [regular, badass]:
    for (idx, (dipl_idx, popdef)) in enumerate(config.clapcreature_dipl):
        clapcreature_id = 'real_clapcreature_{}_{}'.format(config.hotfix_prefix, idx)
        hfs.add_level_hotfix(clapcreature_id, 'ClaptasticCreatureShields',
            ",{},DefaultItemPoolList[{}].ItemPool,,ItemPoolDefinition'{}'".format(
                popdef, dipl_idx, config.equip_pool_shields,
                ),
            activated=False)
        clapcreature_shields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(clapcreature_id)))
    for (idx, (pt_idx, cipl_idx, popdef)) in enumerate(config.clapcreature_pt_cipl):
        clapcreature_id = 'real_clapcreature_pt_{}_{}'.format(config.hotfix_prefix, idx)
        hfs.add_level_hotfix(clapcreature_id, 'ClaptasticCreatureShields',
            ",{},PlayThroughs[{}].CustomItemPoolList[{}].ItemPool,,ItemPoolDefinition'{}'".format(
                popdef, pt_idx, cipl_idx, config.equip_pool_shields,
                ),
            activated=False)
        clapcreature_shields_real_list.append('{}{}'.format(prefix, hfs.get_hotfix_xml(clapcreature_id)))

# Remove weapons+shields from lockers
set_ld_ia_item_pool('lockers_0', 'GD_Itempools.ListDefs.StorageLockerLoot',
        'GD_Itempools.LootablePools.Pool_Locker_Items_CashAndAmmo', 3, 0,
        point='Ammo1')
set_ld_ia_item_pool('lockers_1', 'GD_Itempools.ListDefs.StorageLockerLoot',
        'GD_Itempools.LootablePools.Pool_Locker_Items_CashAndAmmo', 4, 0,
        point='Ammo1')
set_ld_ia_item_pool('lockers_2', 'GD_Itempools.ListDefs.StorageLockerLoot',
        'GD_Itempools.LootablePools.Pool_Locker_Items_CashAndAmmo', 5, 0,
        point='Ammo1')
hfs.add_level_hotfix('lockers_3', 'LockerNerf',
        """,
        GD_Itempools.ListDefs.StorageLockerLoot,
        LootData[5].ItemAttachments[1].PoolProbability.BaseValueConstant,,
        0""")

# Remove weapons+shields from cardboard boxes
set_dl_ia_item_pool('cardboard_0',
        'GD_Balance_Treasure.LootableGrades.ObjectGrade_Cardboard_Box',
        'GD_Itempools.LootablePools.Pool_Locker_Items_CashAndAmmo', 1, 0,
        point='Ammo1')

# Remove guns from dumpsters
hfs.add_level_hotfix('dumpsters_0', 'Dumpster',
        """,GD_Itempools.LootablePools.Pool_Dumpster_Guns,BalancedItems,,
        (
            (
                ItmPoolDefinition=ItemPoolDefinition'GD_Itempools.LootablePools.Pool_Locker_Items_CashAndAmmo',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant=1,
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=False
            )
        )""")

# Remove guns from bandit coolers
set_dl_ia_item_pool('cooler_0',
        'GD_Balance_Treasure.LootableGrades.ObjectGrade_Bandit_Cooler',
        'GD_Itempools.LootablePools.Pool_Locker_Items_CashAndAmmo', 4, 0,
        point='Ammo1')

# Remove guns from safes (this is actually taken from my Better Loot safe
# definition, and improves the safes in general).
hfs.add_level_hotfix('safes_0', 'BetterSafes',
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
            ConfigurationName="MoonItem", 
            LootGameStageVarianceFormula=None, 
            Weight=( 
                BaseValueConstant=1.000000, 
                BaseValueAttribute=None, 
                InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_3_Uncommoner', 
                BaseValueScaleConstant=1.000000 
            ), 
            ItemAttachments=( 
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
        )
    )
    """)

# Nerf vendors
hfs.add_level_hotfix('vendor_nerf_0', 'VendorNerf',
        """,
        GD_ItemPools_Shop.Items.Shoppool_Weapons_FlatChance,
        Quantity.BaseValueConstant,,
        2""")
hfs.add_level_hotfix('vendor_nerf_1', 'VendorNerf',
        """,
        GD_ItemPools_Shop.HealthShop.HealthShop_Items,
        Quantity.BaseValueConstant,,
        2""")
hfs.add_level_hotfix('vendor_nerf_2', 'VendorNerf',
        """,
        GD_ItemPools_Shop.WeaponPools.Shoppool_IOTD_WeaponMachine,
        Quantity.BaseValueConstant,,
        0""")
set_bi_item_prob('vendor_nerf_3', 'GD_ItemPools_Shop.HealthShop.HealthShop_FeaturedItem', 0)
set_bi_item_prob('vendor_nerf_4', 'GD_ItemPools_Shop.HealthShop.HealthShop_FeaturedItem', 1)
set_bi_item_prob('vendor_nerf_5', 'GD_ItemPools_Shop.HealthShop.HealthShop_FeaturedItem', 2)
set_bi_item_prob('vendor_nerf_6', 'GD_ItemPools_Shop.HealthShop.HealthShop_FeaturedItem', 3)

# Badass Outlaw pool tweaks.  They have their own equip pool which splits it
# 80% lasers, 20% launchers.  We'll go ahead and keep that split, and just
# redirect the weapon pools to our own custom-weighted ones.
hfs.add_level_hotfix('badass_outlaw_equip_0', 'BadassOutlawEquip',
        """,
        GD_BadassSpaceman.ItemPool.ItemPool_BadassOutlaw,
        BalancedItems[0].ItmPoolDefinition,,
        ItemPoolDefinition'{}'
        """.format(badass.rarity_pool_lasers))
hfs.add_level_hotfix('badass_outlaw_equip_1', 'BadassOutlawEquip',
        """,
        GD_BadassSpaceman.ItemPool.ItemPool_BadassOutlaw,
        BalancedItems[1].ItmPoolDefinition,,
        ItemPoolDefinition'{}'
        """.format(badass.rarity_pool_launchers))

# Flame Knuckle pool tweaks.  Revert UCP 2.0's changes and normalize all the drops,
# regardless of playthrough, to drop from the "Default" pools.  Also, we're going
# to force "regular" shields instead of badass, given the early-game nature of
# Flame Knuckle.  Also also, prevent the powersuit version from dropping a weapon.
hfs.add_level_hotfix('flameknuckle_pool_0', 'FlameKnucklePool',
        """MoonShotIntro_P,
        GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlPowersuit_Knuckle,
        DefaultItemPoolList[1].PoolProbability.BaseValueConstant,,0""")
hfs.add_level_hotfix('flameknuckle_pool_1', 'FlameKnucklePool',
        """MoonShotIntro_P,
        GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlSergeantFlameKnuckle,
        PlayThroughs[0].CustomItemPoolIncludedLists,,()""")
hfs.add_level_hotfix('flameknuckle_pool_2', 'FlameKnucklePool',
        """MoonShotIntro_P,
        GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlSergeantFlameKnuckle,
        PlayThroughs[0].CustomItemPoolList,,()""")
hfs.add_level_hotfix('flameknuckle_pool_3', 'FlameKnucklePool',
        """MoonShotIntro_P,
        GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlSergeantFlameKnuckle,
        PlayThroughs[1].CustomItemPoolIncludedLists,,()""")
hfs.add_level_hotfix('flameknuckle_pool_4', 'FlameKnucklePool',
        """MoonShotIntro_P,
        GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlSergeantFlameKnuckle,
        PlayThroughs[1].CustomItemPoolList,,()""")
hfs.add_level_hotfix('flameknuckle_pool_5', 'FlameKnucklePool',
        """MoonShotIntro_P,
        GD_DahlPowersuit_Knuckle.Population.PawnBalance_DahlSergeantFlameKnuckle,
        DefaultItemPoolList,,
        (
            ( 
                ItemPool=ItemPoolDefinition'GD_DahlPowersuit_Knuckle.WeaponPools.Pool_Weapons_KnuckleLaser_EnemyUse', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'{}', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1or2', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1or2', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1or2', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1or2', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1or2', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1or2', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Money_1or2', 
                PoolProbability=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Money', 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone', 
                PoolProbability=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Money', 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone_Cluster', 
                PoolProbability=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Money', 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All', 
                PoolProbability=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health', 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Health_All', 
                PoolProbability=( 
                    BaseValueConstant=0.000000, 
                    BaseValueAttribute=AttributeDefinition'GD_Itempools.DropWeights.DropODDS_Health', 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_NeedOnly', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer', 
                    BaseValueScaleConstant=0.500000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_NeedOnly', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=AttributeInitializationDefinition'GD_Balance.WeightingPlayerCount.AmmoDrops_PerPlayer', 
                    BaseValueScaleConstant=0.500000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_Emergency', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'GD_Itempools.AmmoAndResourcePools.Pool_Ammo_All_Emergency', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
        )""".format(regular.equip_pool_shields))

# Flame Knuckle (Holodome) pool tweaks.  UCP doesn't touch this, but the pool
# definitions are weird anyway, so we're going to normalize them.  Cut out most
# of the obviously-intended-for-early-game drops, make sure we're using our
# own badass pool for shields, and drop the same stuff regardless of playthrough.
hfs.add_level_hotfix('flameknuckle_holodome_pool_0', 'FlameKnuckleHolodomePool',
        """Eridian_Slaughter_P,
        GD_DahlPowersuit_KnuckleRepaired.Population.PawnBalance_DahlSergeantFlameKnuckle,
        PlayThroughs[1].CustomItemPoolIncludedLists,,()""")
hfs.add_level_hotfix('flameknuckle_holodome_pool_1', 'FlameKnuckleHolodomePool',
        """Eridian_Slaughter_P,
        GD_DahlPowersuit_KnuckleRepaired.Population.PawnBalance_DahlSergeantFlameKnuckle,
        PlayThroughs[1].CustomItemPoolList,,()""")
hfs.add_level_hotfix('flameknuckle_holodome_pool_2', 'FlameKnuckleHolodomePool',
        """Eridian_Slaughter_P,
        GD_DahlPowersuit_KnuckleRepaired.Population.PawnBalance_DahlSergeantFlameKnuckle,
        DefaultItemPoolIncludedLists,,
        (ItemPoolListDefinition'GD_Itempools.ListDefs.BadassEnemyGunsAndGear')""")
hfs.add_level_hotfix('flameknuckle_holodome_pool_3', 'FlameKnuckleHolodomePool',
        """Eridian_Slaughter_P,
        GD_DahlPowersuit_KnuckleRepaired.Population.PawnBalance_DahlSergeantFlameKnuckle,
        DefaultItemPoolList,,
        (
            ( 
                ItemPool=ItemPoolDefinition'GD_DahlPowersuit_Knuckle.WeaponPools.Pool_Weapons_KnuckleLaser_EnemyUse', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            ),
            (
                ItemPool=ItemPoolDefinition'{}', 
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
        )
        """.format(badass.equip_pool_shields))

# Corporal Bob - remove weapon-equip pool, since he doesn't actually use it.
set_dipl_item_prob('corporal_bob_pool_0',
        'GD_Population_Dahl.Balance.PawnBalance_DahlMarine_CentralTerm',
        0,
        level='CentralTerminal_P')

# Lost Legion Eternal - remove their ascension drop, since we can't guarantee
# that it will be the same as what they use (and in fact is all but guaranteed
# *not* to be).
hfs.add_level_hotfix('lost_legion_eternal_0', 'LostLegionEternal',
        """,
        GD_DahlFanatic.Character.AIDef_DahlFanatic:AIBehaviorProviderDefinition_0.Behavior_SpawnItems_0,
        ItemPoolList[0].PoolProbability.BaseValueConstant,,
        0""")

# Save our current hotfixes
orig_hfs = hfs

# Set up Boss/Miniboss unique drops.
boss_drops = {}
line_prefix = ''
line_suffix = ''
hotfix_activated = True
for (label, key, unique_pct, rare_pct) in [
        ('Guaranteed', 'guaranteed', 1, 1),
        ('Very Improved', 'veryimproved', .5, .75),
        ('Improved', 'improved', .33, .60),
        ('Slightly Improved', 'slight', .22, .45),
        ('Stock Equip', 'stock', .1, .33),
        ]:

    # Set up a new hotfixes object so we don't have to fiddle with hotfix IDs
    hfs = Hotfixes(nameprefix='ApocBoss{}'.format(key.capitalize()))

    # Flame Knuckle (MoonShotIntro_P, using own pool)
    # Also using "Regular" pool for lasers, since the intro's already a bit tough.

    for (idx, (level, default_pool)) in enumerate([
            ('MoonShotIntro_P', regular.equip_pool_only_lasers),
            ('Eridian_Slaughter_P', badass.equip_pool_lasers),
            ]):
        setup_boss_pool('flameknuckle_use_pool_{}'.format(idx),
                level,
                'GD_DahlPowersuit_Knuckle.WeaponPools.Pool_Weapons_KnuckleLaser_EnemyUse',
                default_pool,
                [
                    ('GD_Itempools.Runnables.Pool_FlameKnuckle', rare_pct, None),
                ],
                activated=hotfix_activated)

    # Deadlift Weapon (Deadsurface_P, using own pool)
    # UCP adds Min Min Lighter, so we'll swap back and forth between that and Vandergraffen
    # Make sure to retain at least a 50% chance of spawning the Vandergraffen

    minmin_pct = min(rare_pct, .5)
    setup_boss_pool('deadlift_pool_0', 'Deadsurface_P',
            'GD_SpacemanDeadlift.WeaponPools.Pool_Weapons_Deadlift_Shocklaser',
            ('GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Tediore_3_Vandergraffen', 'WeaponBalanceDefinition'),
            [
                ('GD_Cork_Weap_Lasers.A_Weapons_Legendary.Laser_Tediore_5_Tesla', minmin_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    for (hotfix_id, popdef) in [
            ('base', 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift'),
            ('mercday', 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_MercDay'),
            ('pandoracorn', 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_Pandoracorn'),
            ('pumpkin', 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_Pumpkin'),
            ]:

        set_dipl_item_prob('deadlift_pool_{}_1'.format(hotfix_id),
                popdef,
                2,
                level='Deadsurface_P',
                activated=hotfix_activated)

    # Deadlift Shield, though only in PT2+ (Deadsurface_P pool 0)

    setup_boss_pool('deadlift_pool_2', 'Deadsurface_P', other.level_pool_0,
            badass.equip_pool_shields,
            [
                ('GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryShock', rare_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    for (hotfix_id, popdef) in [
            ('base', 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift'),
            ('mercday', 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_MercDay'),
            ('pandoracorn', 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_Pandoracorn'),
            ('pumpkin', 'GD_SpacemanDeadlift.Population.PawnBalance_SpacemanDeadlift_Pumpkin'),
            ]:

        hfs.add_level_hotfix('deadlift_pool_{}_3'.format(hotfix_id),
                'DeadliftShieldSecondPT',
                """
                Deadsurface_P,
                {},
                PlayThroughs[1].CustomItemPoolList,,
                (
                    ( 
                        ItemPool=ItemPoolDefinition'GD_SpacemanDeadlift.WeaponPools.Pool_Weapons_Deadlift_Shocklaser', 
                        PoolProbability=( 
                            BaseValueConstant=1.000000, 
                            BaseValueAttribute=None, 
                            InitializationDefinition=None, 
                            BaseValueScaleConstant=1.000000 
                        ) 
                    ),
                    (
                        ItemPool=ItemPoolDefinition'{}', 
                        PoolProbability=( 
                            BaseValueConstant=1.000000, 
                            BaseValueAttribute=None, 
                            InitializationDefinition=None, 
                            BaseValueScaleConstant=1.000000 
                        ) 
                    )
                )
                """.format(popdef, other.level_pool_0),
                activated=hotfix_activated)

    # Nel Shield (Deadsurface_P pool 1)

    setup_boss_pool('nel_pool_0', 'Deadsurface_P', other.level_pool_1,
            badass.equip_pool_shields,
            [
                ('GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryShock', rare_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    hfs.add_level_hotfix('nel_pool_1', 'NelKalaShield',
            """
            DeadSurface_P,
            GD_Nel.Population.PawnBalance_Nel,
            DefaultItemPoolList,,
            +(
                ItemPool=ItemPoolDefinition'{}',
                PoolProbability=( 
                    BaseValueConstant=1.000000, 
                    BaseValueAttribute=None, 
                    InitializationDefinition=None, 
                    BaseValueScaleConstant=1.000000 
                ) 
            )
            """.format(other.level_pool_1),
            activated=hotfix_activated)

    # Nel - disable specific weapon drops.

    for num in range(15, 22):

        set_dipl_item_prob('nel_pool_disable_{}'.format(num),
                'GD_Nel.Population.PawnBalance_Nel',
                num,
                level='Deadsurface_P',
                activated=hotfix_activated)

    # Oscar Shield (Moon_P, using the pool UCP uses, to cut back on the number of pools we need)
    # Oscar doesn't define a DefaultItemPoolList by default, so for compatibility
    # with UCP, we're just redefining it entirely.

    setup_boss_pool('oscar_pool_0', 'Moon_P', 'GD_Itempools.Runnables.Pool_ScavBadassMidget',
            badass.equip_pool_shields,
            [
                ('GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_05_Legendary', rare_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    hfs.add_level_hotfix('oscar_pool_1', 'OscarShields',
            """Moon_P,
            GD_Population_Scavengers.Balance.Psychos.PawnBalance_ScavSuicidePsycho_Oscar,
            DefaultItemPoolList,,
            (
                (
                    ItemPool=ItemPoolDefinition'GD_Itempools.Runnables.Pool_ScavBadassMidget',
                    PoolProbability=(
                        BaseValueConstant=1.000000,
                        BaseValueAttribute=None,
                        InitializationDefinition=None,
                        BaseValueScaleConstant=1.000000
                    )
                )
            )
            """,
            activated=hotfix_activated)

    # Magma Rivers (Moon_P pool 0)
    # Also fixing up the UCP loot pool to exclude the Magma

    setup_boss_pool('magmarivers_pool_0', 'Moon_P', other.level_pool_0,
            badass.equip_pool_all,
            [
                ('GD_Cork_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Magma', rare_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('magmarivers_pool_1',
            'GD_Population_Darksiders.Balance.PawnBalance_LittleDarksiderBadassBandit',
            0,
            other.level_pool_0,
            level='Moon_P',
            activated=hotfix_activated)

    set_bi_item_prob('magmarivers_pool_2',
            'GD_Itempools.Runnables.Pool_Maureen',
            1,
            level='Moon_P',
            activated=hotfix_activated)

    # Fair Dinkum (Moon_P pool 1)
    # Also fixing up the UCP loot pool to exclude Cradle

    setup_boss_pool('fairdinkum_pool_0', 'Moon_P', other.level_pool_1,
            badass.equip_pool_shields,
            [
                ('GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_05_Legendary', rare_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('fairdinkum_pool_1',
            'GD_Population_Darksiders.Balance.PawnBalance_DarksiderBadassPsycho',
            0,
            other.level_pool_1,
            level='Moon_P',
            activated=hotfix_activated)

    set_bi_item_prob('fairdinkum_pool_2',
            'GD_Itempools.Runnables.Pool_BadassDarksiderPsycho',
            1,
            level='Moon_P',
            activated=hotfix_activated)

    # Wally Wrong (Moon_P pool 2)

    setup_boss_pool('wallywrong_pool_0', 'Moon_P', other.level_pool_2,
            badass.equip_pool_all,
            [
                ('GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun', rare_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('wallywrong_pool_1',
            'GD_Population_Darksiders.Balance.PawnBalance_DarksiderBadassBandit',
            0,
            other.level_pool_2,
            level='Moon_P',
            activated=hotfix_activated)

    set_bi_item_prob('wallywrong_pool_2',
            'GD_Itempools.Runnables.Pool_BadassDarksiderBandit',
            1,
            level='Moon_P',
            activated=hotfix_activated)

    # Swagman (various levels, using own pool)

    setup_boss_pool('swagman_pool_0', None,
            'GD_Itempools.Runnables.Pool_ScavBadassSpacemanMidget',
            badass.equip_pool_lasers,
            [
                ('GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_WetWeek', rare_pct, 'WeaponBalanceDefinition'),
                ('GD_Cork_Weap_SniperRifles.A_Weapons_Unique.Sniper_Vladof_3_TheMachine', rare_pct, 'WeaponBalanceDefinition'),
                ('GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_JackOCannon', rare_pct, 'WeaponBalanceDefinition'),
                ('GD_Cork_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_Boomacorn', rare_pct, 'WeaponBalanceDefinition'),
                ('gd_cork_weap_assaultrifle.A_Weapons_Unique.AR_Vladof_3_OldPainful', rare_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_pt_cipl_item_pool('swagman_pool_1',
            'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker',
            0, 0,
            'GD_Itempools.Runnables.Pool_ScavBadassSpacemanMidget',
            activated=hotfix_activated)

    set_pt_cipl_item_pool('swagman_pool_2',
            'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker',
            1, 0,
            'GD_Itempools.Runnables.Pool_ScavBadassSpacemanMidget',
            activated=hotfix_activated)

    set_pt_cipl_item_prob('swagman_pool_3',
            'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker',
            0, 2,
            activated=hotfix_activated)

    set_pt_cipl_item_prob('swagman_pool_4',
            'GD_Population_Scavengers.Balance.Outlaws.PawnBalance_ScavWastelandWalker',
            1, 2,
            activated=hotfix_activated)

    # Bruce Weapons (ComFacility_P pool 0)

    setup_boss_pool('bruce_pool_0', 'ComFacility_P', other.level_pool_0,
            badass.equip_pool_all,
            [
                ('GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun', unique_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('bruce_pool_1',
            'GD_Bruce.Population.Bal_Bruce',
            0,
            other.level_pool_0,
            level='ComFacility_P',
            activated=hotfix_activated)

    # Bruce Shields (ComFacility_P, using own pool)

    setup_boss_pool('bruce_pool_2', 'ComFacility_P',
            'GD_Itempools.Runnables.Pool_Bruce',
            badass.equip_pool_shields,
            [
                ('GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Supernova', rare_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('bruce_pool_3',
            'GD_Bruce.Population.Bal_Bruce',
            1,
            'GD_Itempools.Runnables.Pool_Bruce',
            level='ComFacility_P',
            activated=hotfix_activated)

    # Red Weapon (ComFacility_P, using own pool)

    setup_boss_pool('red_pool_0', 'ComFacility_P',
            'GD_Itempools.Runnables.Pool_Red_Rare',
            badass.equip_pool_ar,
            [
                ('GD_Cork_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom', rare_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('red_pool_1',
            'GD_Population_Scavengers.Uniques.PawnBalance_Ned',
            0,
            'GD_Itempools.Runnables.Pool_Red_Rare',
            level='ComFacility_P',
            activated=hotfix_activated)

    # Red Shield (ComFacility_P pool 1)

    setup_boss_pool('red_pool_2', 'ComFacility_P', other.level_pool_1,
            badass.equip_pool_shields,
            [
                ('GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_05_Legendary', rare_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('red_pool_3',
            'GD_Population_Scavengers.Uniques.PawnBalance_Ned',
            2,
            other.level_pool_1,
            level='ComFacility_P',
            activated=hotfix_activated)

    # Belly Weapon (ComFacility_P, using own pool)

    setup_boss_pool('belly_pool_0', 'ComFacility_P',
            'GD_Itempools.Runnables.Pool_Belly',
            badass.equip_pool_lasers,
            [
                ('GD_Cork_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker', unique_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('belly_pool_1',
            'GD_Population_Scavengers.Uniques.PawnBalance_Kelly',
            0,
            'GD_Itempools.Runnables.Pool_Belly',
            level='ComFacility_P',
            activated=hotfix_activated)

    # Belly Shield (ComFacility_P pool 2)

    setup_boss_pool('belly_pool_2', 'ComFacility_P', other.level_pool_2,
            badass.equip_pool_shields,
            [
                ('GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_05_Legendary', unique_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('belly_pool_3',
            'GD_Population_Scavengers.Uniques.PawnBalance_Kelly',
            1,
            other.level_pool_2,
            level='ComFacility_P',
            activated=hotfix_activated)

    # Drongo Bones (Outlands_P2 pool 0)

    setup_boss_pool('drongobones_pool_0', 'Outlands_P2', other.level_pool_0,
            badass.equip_pool_lasers,
            [
                ('GD_Cork_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch', unique_pct, 'WeaponBalanceDefinition'),
                ('GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie', unique_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('drongobones_pool_1',
            'GD_DrongoBones.Balance.PawnBalance_DrongoBones',
            1,
            other.level_pool_0,
            level='Outlands_P2',
            activated=hotfix_activated)

    set_dipl_item_prob('drongobones_pool_2',
            'GD_DrongoBones.Balance.PawnBalance_DrongoBones',
            2,
            level='Outlands_P2',
            activated=hotfix_activated)

    # Lazlo (InnerHull_P, using own pool)

    setup_boss_pool('lazlo_pool_0', 'InnerHull_P',
            'GD_Lazlo.ItemPools.Pool_Lazlo_Freezeasy_EnemyUse',
            None,
            [
                ('GD_Cork_Weap_Lasers.A_Weapons_Unique.Laser_Maliwan_3_Blizzard', 1, 'WeaponBalanceDefinition'),
                ('GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Shooterang', 1, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_prob('lazlo_pool_1',
            'GD_Population_Rat.Balance.PawnBalance_Lazlo',
            2,
            level='InnerHull_P',
            activated=hotfix_activated)

    # Eghood (InnerHull_P pool 0)

    setup_boss_pool('eghood_pool_0', 'InnerHull_P', other.level_pool_0,
            badass.equip_pool_shotguns,
            [
                ('GD_Cork_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Blowfly', unique_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('eghood_pool_1',
            'GD_Population_Boils.Balance.PawnBalance_Eghood',
            0,
            other.level_pool_0,
            level='InnerHull_P',
            activated=hotfix_activated)

    setup_boss_pool('eghood_pool_2', 'InnerHull_P',
            'GD_Itempools.Runnables.Pool_Eghood',
            None,
            [
                ('GD_GrenadeMods.A_Item_Legendary.GM_Leech', 1, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    # Lost Legion Courier (Laser_P pool 0)
    # This is actually our own addition - making him equip/drop a Major Tom.  The
    # Powersuit Noob already does that, but the powersuit doesn't actually USE a
    # real weapon, so I wanted to give it the opporuntity to do so.

    setup_boss_pool('courier_pool_0', 'Laser_P', other.level_pool_0,
            regular.equip_pool_lasers,
            [
                ('gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom', unique_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('courier_pool_1',
            'GD_DahlRedShirt.Balance.PawnBalance_DahlRedShirt',
            0,
            other.level_pool_0,
            level='Laser_P',
            activated=hotfix_activated)

    # Lost Legion Powersuit Noob shield (Laser_P pool 1)
    # Also tweak the runnables to just have the Major Tom

    setup_boss_pool('powersuit_noob_pool_0', 'Laser_P', other.level_pool_1,
            badass.equip_pool_shields,
            [
                ('GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_ShootingStar', unique_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('powersuit_noob_pool_1',
            'GD_DahlRedShirtPowersuit.Balance.PawnBalance_DahlRedShirtPowersuit',
            0,
            other.level_pool_1,
            level='Laser_P',
            activated=hotfix_activated)

    setup_boss_pool('powersuit_noob_pool_2', 'Laser_P',
            'GD_Itempools.Runnables.Pool_RedShirt',
            None,
            [
                ('gd_cork_weap_assaultrifle.A_Weapons_Legendary.AR_Dahl_5_MajorTom', 1, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    # Shadow-TP weapon (Ma_SubBoss_P, using own pool)

    setup_boss_pool('shadowtrap_pool_0', 'Ma_SubBoss_P',
            'GD_Ma_SH4D0W-TP.ItemPool.ItemPool_ShadowTrapBlaster',
            'GD_Ma_ItemPools.WeaponPools.Pool_Weapons_Lasers_Glitch_Marigold',
            [
                ('GD_Ma_Weapons.A_Weapons_Legendary.Laser_Tediore_5_LaserDisker', unique_pct, 'WeaponBalanceDefinition'),
            ],
            activated=hotfix_activated)

    # Shadow-TP shield (Ma_SubBoss_P pool 0)

    setup_boss_pool('shadowtrap_pool_1', 'Ma_SubBoss_P', other.level_pool_0,
            badass.equip_pool_shields,
            [
                ('GD_Ma_Shields.A_Item_Legendary.ItemGrade_Gear_Shield_Impact_05_Rerouter', unique_pct, 'InventoryBalanceDefinition'),
            ],
            activated=hotfix_activated)

    set_dipl_item_pool('shadowtrap_pool_2',
            'GD_Ma_Pop_ClaptrapForces.Balance.Uniques.PawnBalance_SH4D0W-TP-Part1',
            0,
            other.level_pool_0,
            level='Ma_SubBoss_P',
            activated=hotfix_activated)

    set_dipl_item_prob('shadowtrap_pool_3',
            'GD_Ma_Pop_ClaptrapForces.Balance.Uniques.PawnBalance_SH4D0W-TP-Part1',
            3,
            level='Ma_SubBoss_P',
            activated=hotfix_activated)

    # Generate the section string
    with open('input-file-bosses.txt', 'r') as df:
        boss_drops[key] = df.read().format(
                boss_label='{} ({}% Uniques, {}% Rares)'.format(
                    label, round(unique_pct*100), round(rare_pct*100)),
                line_prefix=line_prefix,
                line_suffix=line_suffix,
                hotfixes=hfs,
                regular=regular,
                badass=badass,
                other=other,
                unique_pct=unique_pct,
                rare_pct=rare_pct,
                )

    line_prefix = '#'
    line_suffix = '<off>'
    hotfix_activated = False

# Load in skinpool settings
with open('input-file-skinpools.txt') as df:
    skinpool_setup = df.read()

###
### Generate the mod string
###

with open('input-file-mod.txt') as df:
    mod_str = df.read().format(
        mod_name=mod_name,
        mod_version=mod_version,
        hotfixes=orig_hfs,
        regular=regular,
        badass=badass,
        other=other,
        rarity_excellent=rarity_sections['excellent'],
        rarity_better=rarity_sections['better'],
        rarity_stock=rarity_sections['stock'],
        rarity_noglitch_excellent=rarity_sections['excellent_noglitch'],
        rarity_noglitch_better=rarity_sections['better_noglitch'],
        rarity_noglitch_stock=rarity_sections['stock_noglitch'],
        rarity_drop_prob_guaranteed=rarity_drop_prob_sections['guaranteed'],
        rarity_drop_prob_variable=rarity_drop_prob_sections['variable'],
        boss_drops_guaranteed=boss_drops['guaranteed'],
        boss_drops_veryimproved=boss_drops['veryimproved'],
        boss_drops_improved=boss_drops['improved'],
        boss_drops_slightimproved=boss_drops['slight'],
        boss_drops_stock=boss_drops['stock'],
        more_shields_real="\n\n".join(moreshields_real_list),
        stalker_shields_real="\n\n".join(stalker_shields_real_list),
        guardian_shields_real="\n\n".join(guardian_shields_real_list),
        clapcreature_shields_real="\n\n".join(clapcreature_shields_real_list),
        skinpool_setup=skinpool_setup,
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
