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

mod_name = 'BL2 Cold Dead Hands'
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

    disable_world_sets = None

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

    # Scale for weighted pools
    weight_scale = 2.5

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

    # Equip pools for regular enemies
    set_equip_all = None
    set_equip_ar = None
    set_equip_launchers = None
    set_equip_pistols = None
    set_equip_shotguns = None
    set_equip_smg = None
    set_equip_snipers = None
    set_equip_only_shotguns = None

    # Shield pool (only need to worry about one pool for these)
    set_shields = None
    
    ###
    ### ... FUNCTIONS??!?
    ###

    def __init__(self, hotfixes):
        self.hotfixes = hotfixes
        self.num_hotfixes = 0

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
        prefix = ' ' * (4*3)

        # The order in which our assignment tuples are specified
        pool_order = [
                self.equip_pool_ar,
                self.equip_pool_pistols,
                self.equip_pool_shotguns,
                self.equip_pool_smg,
                self.equip_pool_all,
                self.equip_pool_launchers,
                self.equip_pool_snipers,
                self.equip_pool_only_shotguns,
                self.pool_shields,
            ]

        # First, assign enemies using DefaultItemPoolList[x]
        for (pool, classlist) in zip(pool_order, self.enemy_dipl):
            for (dipl_idx, classname) in classlist:
                retlist.append(self._single_assignment_hotfix(
                    prefix,
                    classname,
                    'DefaultItemPoolList[{}].ItemPool'.format(dipl_idx),
                    pool))

        # Next, enemies using PlayThroughs[x].CustomItemPoolList[y]
        for (pool, classlist) in zip(pool_order, self.enemy_pt_cipl):
            for (pt_idx, cipl_idx, classname) in classlist:
                retlist.append(self._single_assignment_hotfix(
                    prefix,
                    classname,
                    'PlayThroughs[{}].CustomItemPoolList[{}].ItemPool'.format(
                        pt_idx, cipl_idx),
                    pool))

        # Next, enemies using ItemPoolList[x] in a specific level WillowAIPawn
        for (pool, classlist) in zip(pool_order, self.enemy_level_ipl):
            for (level, ipl_idx, classname) in classlist:
                retlist.append(self._single_assignment_hotfix(
                    prefix,
                    classname,
                    'ItemPoolList[{}].ItemPool'.format(ipl_idx),
                    pool,
                    level=level))

        # Next, enemies using DefaultLoot[x].ItemAttachments[y]
        for (pool, classlist) in zip(pool_order, self.enemy_dl_ia):
            for (dl_idx, ia_idx, classname) in classlist:
                retlist.append(self._single_assignment_hotfix(
                    prefix,
                    classname,
                    'DefaultLoot[{}].ItemAttachments[{}].ItemPool'.format(
                        dl_idx, ia_idx),
                    pool))

        # Next, enemies using NewItemPoolList[0]
        for (pool, classlist) in zip(pool_order, self.enemy_nipl):
            for (nipl_idx, classname) in classlist:
                retlist.append(self._single_assignment_hotfix(
                    prefix,
                    classname,
                    'NewItemPoolList[{}].ItemPool'.format(nipl_idx),
                    pool))

        return "\n\n".join(retlist)

class Regular(DropConfig):
    """
    Config info for regular enemies
    """

    # Hotfix prefix
    hotfix_prefix = 'reg'

    # Equip weights
    weight_common = 20
    weight_uncommon = 85
    weight_rare = 65
    weight_veryrare = 40
    weight_alien = 20
    weight_legendary = 1

    # Rarity weight pools
    rarity_pool_ar = 'GD_CustomItemPools_MainGame.Soldier.TorgueUncommon'
    rarity_pool_launchers = 'GD_CustomItemPools_Lilac.Psycho.TorgueUncommon'
    rarity_pool_pistols = 'GD_CustomItemPools_MainGame.Mercenary.TorgueUncommon'
    rarity_pool_shotguns = 'GD_CustomItemPools_tulip.Mechro.TorgueUncommon'
    rarity_pool_smg = 'GD_CustomItemPools_MainGame.Siren.TorgueUncommon'
    rarity_pool_snipers = 'GD_CustomItemPools_MainGame.Assassin.TorgueUncommon'

    # Equip pools (this is where gun type weights are applied)
    equip_pool_all = 'GD_CustomItemPools_allium.Mechro.AlliumTGSkins'
    equip_pool_ar = 'GD_CustomItemPools_MainGame.Soldier.VladofUncommon'
    equip_pool_launchers = 'GD_CustomItemPools_Lilac.Psycho.VladofUncommon'
    equip_pool_pistols = 'GD_CustomItemPools_MainGame.Mercenary.VladofUncommon'
    equip_pool_shotguns = 'GD_CustomItemPools_tulip.Mechro.VladofUncommon'
    equip_pool_smg = 'GD_CustomItemPools_MainGame.Siren.VladofUncommon'
    equip_pool_snipers = 'GD_CustomItemPools_MainGame.Assassin.VladofUncommon'
    equip_pool_only_shotguns = 'GD_CustomItemPools_allium.Assassin.AlliumXmasSkins'

    # Shield pool
    pool_shields = 'GD_CustomItemPools_allium.Mechro.AlliumXmasSkins'

    ###
    ### Enemy changes
    ###

    enemy_dipl = (
            # ARs
            [
                (0, 'GD_Allium_LootMidget_LoaderJET.Balance.PawnBalance_LootMidget_LoaderJETAllium'),
                (0, 'GD_Allium_LootMidgetLoaderBUL.Balance.PawnBalance_LootMidget_LoaderBULAllium'),
                (0, 'GD_HolidayLoader.Balance.PawnBalance_HolidayLoader'),
                (0, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_MissionPlaceholder'),
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_BikeRiderMarauder'),
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_RaidBikeMarauder'),
                (0, 'GD_Iris_Population_Loader.Balance.Iris_PawnBalance_LoaderGUN'),
                (0, 'GD_Iris_Population_Rat.Balance.Iris_PawnBalance_RatTunnel'),
                (0, 'GD_Orchid_Hovercraft.AI.PawnBalance_Hovercraft_Rider'),
                (0, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderGUN'),
                (0, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderJunk'),
                (0, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderPirate'),
                (0, 'GD_Orchid_Pop_Loader.Disabled.Balance.PawnBalance_Orchid_LoaderGUN_Disabled'),
                (0, 'GD_Orchid_Pop_Loader.Disabled.Balance.PawnBalance_Orchid_LoaderJunk_Disabled'),
                (0, 'GD_Orchid_Pop_PirateRadioGuy.PawnBalance_Orchid_PirateRadioGuy'),
                (0, 'GD_Population_Goliath.Balance.PawnBalance_GoliathOneArm'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderGUN'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderJET'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderGUN'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderGUN_HealthCashAmmoOnly'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderJunk'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_TundraPatrol'),
                (1, 'GD_Population_Midget.Balance.PawnBalance_MidgetNomad'),
                (0, 'GD_RatGrunt_Digi.Population.PawnBalance_RatGrunt_Digi'),
                (0, 'GD_Sage_Pop_Loader.Balance.PawnBalance_Sage_LoaderGUN'),
                (0, 'GD_Population_Goliath.Balance.PawnBalance_Goliath'),
                (0, 'GD_Population_Goliath.Balance.PawnBalance_GoliathLootGoon'),
                (0, 'GD_Aster_Pop_Dwarves.Balance.PawnBalance_Dwarfzerker'),
                (0, 'GD_Aster_Pop_Dwarves.Balance.PawnBalance_Dwarfzerker_Minus2'),
                (0, 'GD_Aster_Pop_Dwarves.Balance.PawnBalance_Dwarfzerker_StandStill'),
                (0, 'GD_Aster_Pop_Orcs.Balance.PawnBalance_Orczerker'),
            ],
            # Pistols
            [
                (1, 'GD_Orchid_Hovercraft.AI.PawnBalance_Hovercraft_Rider'),
                (0, 'GD_Orchid_SM_JockoLegUp_Data.PawnBalance_Orchid_PiratePegLeg'),
                (0, 'GD_ResistanceFighter.Population.BD_ResistanceFighter_Pistol'), # Sure, make Sanctuary a bit more colorful
                (0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderIntro'),
                (0, 'GD_Population_Midget.Balance.PawnBalance_MidgetGoliath'),
            ],
            # Shotguns
            [
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_Bike'),
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_GrinderBike'),
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_RaidBike'),
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_RaidGrinderBike'),
                (0, 'GD_Iris_Population_Bruiser.Balance.Iris_PawnBalance_BikerBruiser'),
                (1, 'GD_Iris_Population_Marauder.Balance.Iris_PawnBalance_SullyTheStabber'),
                (0, 'GD_Iris_Population_Midget.Balance.Iris_PawnBalance_BikerMidget'),
                (0, 'GD_Nast_Hodunk_Grunt.Balance.PawnBalance_Nast_HodunkGrunt'),
                (0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateGrenadier'),
                (0, 'GD_Population_Goliath.Balance.PawnBalance_Juggernaught'),
                (0, 'GD_Population_Goliath.Balance.Unique.PawnBalance_DiggerGoliath'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_HodunkGrunt'),
            ],
            # SMGs
            [
                (0, 'GD_Iris_Population_Loader.Balance.Iris_PawnBalance_LoaderJET'),
                (0, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_ScarlettMarauder'),
                (0, 'GD_Population_Engineer.Balance.PawnBalance_EngyArms_FreeWilly_Skag'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderJET'),
                (0, 'GD_Population_Midget.Balance.PawnBalance_MidgetRat'),
                (0, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf1'),
                (0, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf2'),
                (0, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf3'),
                (0, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf4'),
                (0, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf5'),
                (0, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf6'),
                (0, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf7'),
                (0, 'GD_Sage_Pop_Natives.Balance.PawnBalance_Native_Soldier'),
                (1, 'GD_Nast_BadassJunkLoader.Population.PawnBalance_BadassJunkLoader'),
                (0, 'GD_Nast_Native_Soldier.Population.PawnBalance_Nast_Native_Soldier'),
                (0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMarauderSMG'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_ZafordGrunt'),
                (0, 'GD_Nast_Zaford_Grunt.Balance.PawnBalance_Nast_ZafordGroomsman'),
                (0, 'GD_Nast_Zaford_Grunt.Balance.PawnBalance_Nast_ZafordGrunt'),
                (0, 'GD_Nast_Zaford_Grunt.Balance.PawnBalance_Nast_ZafordKnife'),
            ],
            # All
            [
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_BikeRiderMidget'),
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_RaidBikeMidget'),
                (0, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_BigBiker'),
                (0, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_Biker'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderSGT'),
                (0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMarauder'),
            ],
            # Launchers
            [
                (1, 'GD_ButcherBoss3.Balance.PawnBalance_ButcherBoss3'),
                (0, 'GD_Iris_Population_Goliath.Balance.Iris_PawnBalance_ArenaGoliath'),
                (0, 'GD_Iris_Population_Loader.Balance.Iris_PawnBalance_LoaderRPG'),
                (0, 'GD_Iris_Population_MotorMama.Balance.Iris_PawnBalance_MotorMamaBike'),
                (0, 'GD_Orchid_Pop_Deserters.Deserter3.PawnBalance_Orchid_Deserter3'),
                (0, 'GD_Population_Goliath.Balance.PawnBalance_GoliathBlaster'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderRPG'),
                (0, 'GD_Population_Nomad.Balance.PawnBalance_Nomad_Rocket'),
            ],
            # Snipers
            [
                (0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateHunter'),
                (0, 'GD_Population_Engineer.Balance.PawnBalance_BlackOps'),
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
                (1, 'GD_Allium_LootMidget_LoaderJET.Balance.PawnBalance_LootMidget_LoaderJETAllium'),
                (1, 'GD_Allium_LootMidgetLoaderBUL.Balance.PawnBalance_LootMidget_LoaderBULAllium'),
                (1, 'GD_HolidayLoader.Balance.PawnBalance_HolidayLoader'),
                (2, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_BigBiker'),
                (2, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_Biker'),
                (1, 'GD_Iris_Population_Goliath.Balance.Iris_PawnBalance_ArenaGoliath'),
                (0, 'GD_Iris_Population_Loader.Balance.Iris_PawnBalance_LoaderPWR'),
                (1, 'GD_Nast_Hodunk_Grunt.Balance.PawnBalance_Nast_HodunkGrunt'),
                (3, 'GD_Nast_Zaford_Grunt.Balance.PawnBalance_Nast_ZafordGroomsman'),
                (3, 'GD_Nast_Zaford_Grunt.Balance.PawnBalance_Nast_ZafordGrunt'),
                (3, 'GD_Nast_Zaford_Grunt.Balance.PawnBalance_Nast_ZafordKnife'),
                (3, 'GD_Orchid_Hovercraft.AI.PawnBalance_Hovercraft_Rider'),
                (0, 'GD_Orchid_Pop_BubblesLilSis.Balance.PawnBalance_Orchid_Bubbles'),
                (1, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderBUL'),
                (0, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderEXP'),
                (1, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderGUN'),
                (1, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderHOT'),
                (1, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderJunk'),
                (1, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderPirate'),
                (0, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderPWR'),
                (1, 'GD_Orchid_Pop_PirateRadioGuy.PawnBalance_Orchid_PirateRadioGuy'),
                (1, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateHunter'),
                (1, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMarauder'),
                (1, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_ScarlettMarauder'),
                (0, 'GD_Population_Constructor.Balance.Unique.PawnBalance_Constructor_1340'),
                (1, 'GD_Population_Engineer.Balance.PawnBalance_BlackOps'),
                (0, 'GD_Population_Engineer.Balance.Unique.PawnBalance_RequisitionOfficer'),
                (1, 'GD_Population_Goliath.Balance.PawnBalance_Juggernaught'),
                (1, 'GD_Population_Jack.Balance.PawnBalance_JackClone'),
                (1, 'GD_Population_Jack.Balance.PawnBalance_JackCloneMelee_Shield'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderBUL'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderEXP'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderGUN'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderHOT'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderION'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderJET'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderPWR'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_BunkerLoaderWAR'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderBUL'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderEXP'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderGUN'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderGUN_HealthCashAmmoOnly'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderHOT'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderION'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderION_HealthCashAmmoOnly'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderJET'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderJunk'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderLWT'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderPWR'),
                (2, 'GD_Population_Loader.Balance.PawnBalance_LoaderRPG'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderSGT'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderWAR'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderWAR_HealthCashAmmoOnly'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderWAR_Overlooked'),
                (1, 'GD_Population_Loader.Balance.Unique.JackFight.PawnBalance_LoaderBUL_JackFight'),
                (0, 'GD_Population_Loader.Balance.Unique.JackFight.PawnBalance_LoaderEXP_JackFight'),
                (1, 'GD_Population_Loader.Balance.Unique.JackFight.PawnBalance_LoaderGUN_JackFight'),
                (1, 'GD_Population_Marauder.Balance.Unique.PawnBalance_Ep13_Roland'),
                (1, 'GD_Population_Marauder.Balance.Unique.PawnBalance_Ep6_Roland'),
                (1, 'GD_Population_Marauder.Balance.Unique.PawnBalance_HodunkGrunt'),
                (3, 'GD_Population_Marauder.Balance.Unique.PawnBalance_ZafordGrunt'),
                (0, 'GD_Population_Midget.Balance.PawnBalance_MidgetNomad'),
                (1, 'GD_Population_Midget.Balance.PawnBalance_MidgetRat'),
                (1, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf1'),
                (1, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf2'),
                (1, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf3'),
                (1, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf4'),
                (1, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf5'),
                (1, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf6'),
                (1, 'GD_Population_Midget.Balance.Unique.PawnBalance_LaneyDwarf7'),
                (1, 'GD_Population_Nomad.Balance.PawnBalance_Nomad_Rocket'),
                (0, 'GD_Population_Psycho.Balance.Unique.PawnBalance_Undertaker'),
                (0, 'GD_Population_Rat.Balance.PawnBalance_RatPlague'),
                (0, 'GD_Psycho_Digi.Population.PawnBalance_Psycho_Digi'),
                (0, 'GD_PsychoMidget_Digi.Population.PawnBalance_PsychoMidget_Digi'),
                (1, 'GD_RatGrunt_Digi.Population.PawnBalance_RatGrunt_Digi'),
                (0, 'GD_Sage_Pop_Loader.Balance.PawnBalance_Sage_LoaderEXP'),
                (1, 'GD_Sage_Pop_Loader.Balance.PawnBalance_Sage_LoaderGUN'),
                (1, 'GD_Sage_Pop_Loader.Balance.PawnBalance_Sage_LoaderION'),
            ],
        )

    enemy_pt_cipl = (
            # ARs
            [
                (0, 1, 'GD_Allium_Butcher_Midget.Balance.PawnBalance_ButcherMidget'),
                (1, 1, 'GD_Allium_Butcher_Midget.Balance.PawnBalance_ButcherMidget'),
                (2, 1, 'GD_Allium_Butcher_Midget.Balance.PawnBalance_ButcherMidget'),
                (0, 0, 'GD_Iris_Population_RaidPete.Balance.PawnBalance_Iris_RaidPete_SewerPipeRat'),
                (1, 0, 'GD_Iris_Population_Rat.Balance.Iris_PawnBalance_RatTunnel'),
                (0, 0, 'GD_Population_Engineer.Balance.PawnBalance_HyperionSoldier'),
                (1, 0, 'GD_Population_Engineer.Balance.PawnBalance_HyperionSoldier'),
                (0, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderRider'),
                (1, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderRider'),
                (0, 0, 'GD_Population_Marauder.Balance.PawnBalance_Scavenger'),
                (1, 1, 'GD_Population_Midget.Balance.PawnBalance_MidgetNomad'),
                (0, 0, 'GD_Population_Nomad.Balance.PawnBalance_Nomad'),
                (1, 0, 'GD_Population_Nomad.Balance.PawnBalance_Nomad'),
                (1, 0, 'GD_Population_Nomad.Balance.PawnBalance_NomadPyro'),
                (0, 0, 'GD_Population_Nomad.Balance.PawnBalance_NomadShieldwMidget'),
                (1, 0, 'GD_Population_Nomad.Balance.PawnBalance_NomadShieldwMidget'),
                (0, 0, 'GD_Population_Nomad.Balance.PawnBalance_NomadShock'),
                (1, 0, 'GD_Population_Nomad.Balance.PawnBalance_NomadShock'),
                (0, 0, 'GD_Population_Rat.Balance.PawnBalance_RatRider'),
                (0, 0, 'GD_Population_Rat.Balance.PawnBalance_RatTunnel'),
                (1, 0, 'GD_Population_Rat.Balance.PawnBalance_RatTunnel'),
                (0, 0, 'GD_Allium_GoliathSnow.Balance.PawnBalance_GoliathSnow'),
                (0, 0, 'GD_Allium_MarauderKitchen.Balance.PawnBalance_MarauderKitchen'),
                (1, 0, 'GD_Allium_MarauderKitchen.Balance.PawnBalance_MarauderKitchen'),
                (2, 0, 'GD_Allium_MarauderKitchen.Balance.PawnBalance_MarauderKitchen'),
                (0, 0, 'GD_Allium_MarauderSnow.Balance.PawnBalance_MarauderSnow'),
                (1, 0, 'GD_Allium_MarauderSnow.Balance.PawnBalance_MarauderSnow'),
                (2, 0, 'GD_Allium_MarauderSnow.Balance.PawnBalance_MarauderSnow'),
                (0, 0, 'GD_Nomad_Digi.Population.PawnBalance_Nomad_Digi'),
            ],
            # Pistols
            [
                (0, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderGrunt'),
            ],
            # Shotguns
            [
                (1, 0, 'GD_Iris_Population_Bruiser.Balance.Iris_PawnBalance_BikerBruiser'),
                (1, 0, 'GD_Iris_Population_Midget.Balance.Iris_PawnBalance_BikerMidget'),
                (0, 0, 'GD_Population_Bruiser.Balance.PawnBalance_Bruiser'),
                (1, 0, 'GD_Population_Bruiser.Balance.PawnBalance_Bruiser'),
                (0, 0, 'GD_Population_Bruiser.Balance.PawnBalance_Bruiser_LilithIntro'),
                (1, 0, 'GD_Population_Bruiser.Balance.PawnBalance_Bruiser_LilithIntro'),
                (0, 0, 'GD_Population_Engineer.Balance.PawnBalance_HyperionInfiltrator'),
                (1, 0, 'GD_Population_Engineer.Balance.PawnBalance_HyperionInfiltrator'),
                (0, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderElite'),
                (1, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderElite'),
                (1, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderGrunt'),
                (0, 0, 'GD_Population_Nomad.Balance.PawnBalance_Nomad_Taskmaster'),
                (1, 0, 'GD_Population_Nomad.Balance.PawnBalance_Nomad_Taskmaster'),
            ],
            # SMGs
            [
                (0, 0, 'GD_Population_Engineer.Balance.PawnBalance_Engineer'),
                (1, 0, 'GD_Population_Engineer.Balance.PawnBalance_Engineer'),
                (0, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderPsycho'),
                (1, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderPsycho'),
                (0, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderRegular'),
                (1, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderRegular'),
                (1, 0, 'GD_Population_Midget.Balance.PawnBalance_MidgetRat'),
                (0, 0, 'GD_Population_Rat.Balance.Unique.PawnBalance_ProspectorRat'),
                (1, 0, 'GD_Population_Rat.Balance.Unique.PawnBalance_ProspectorRat'),
                (0, 0, 'GD_MarauderRegular_Digi.Population.PawnBalance_MarauderRegular_Digi'),
                (0, 0, 'GD_Pop_HallowSkeleton.Balance.PawnBalance_BanditFireSkeleton'),
                (1, 0, 'GD_Pop_HallowSkeleton.Balance.PawnBalance_BanditFireSkeleton'),
                (2, 0, 'GD_Pop_HallowSkeleton.Balance.PawnBalance_BanditFireSkeleton'),
                (0, 0, 'GD_Pop_HallowSkeleton.Balance.PawnBalance_BanditHallowSkeleton'),
                (1, 0, 'GD_Pop_HallowSkeleton.Balance.PawnBalance_BanditHallowSkeleton'),
                (2, 0, 'GD_Pop_HallowSkeleton.Balance.PawnBalance_BanditHallowSkeleton'),
                (0, 1, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMarauderSMG'),
            ],
            # All
            [
                (1, 0, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_BigBiker'),
                (1, 0, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_Biker'),
                (1, 1, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMarauder'),
            ],
            # Launchers
            [
                (0, 0, 'GD_Population_Engineer.Balance.PawnBalance_HyperionHawk'),
                (1, 0, 'GD_Population_Engineer.Balance.PawnBalance_HyperionHawk'),
            ],
            # Snipers
            [
            ],
            # Only Shotguns
            [
                (0, 0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMidgetShotgun'),
                (1, 0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMidgetShotgun'),
                (0, 0, 'GD_Population_Midget.Balance.PawnBalance_MidgetShotgun'),
                (1, 0, 'GD_Population_Midget.Balance.PawnBalance_MidgetShotgun'),
            ],
            # Shields
            [
                (0, 0, 'GD_Allium_Butcher_Midget.Balance.PawnBalance_ButcherMidget'),
                (1, 0, 'GD_Allium_Butcher_Midget.Balance.PawnBalance_ButcherMidget'),
                (2, 0, 'GD_Allium_Butcher_Midget.Balance.PawnBalance_ButcherMidget'),
                (0, 1, 'GD_Allium_GoliathSnow.Balance.PawnBalance_GoliathSnow'),
                (0, 1, 'GD_Allium_MarauderKitchen.Balance.PawnBalance_MarauderKitchen'),
                (1, 1, 'GD_Allium_MarauderKitchen.Balance.PawnBalance_MarauderKitchen'),
                (2, 1, 'GD_Allium_MarauderKitchen.Balance.PawnBalance_MarauderKitchen'),
                (0, 1, 'GD_Allium_MarauderSnow.Balance.PawnBalance_MarauderSnow'),
                (1, 1, 'GD_Allium_MarauderSnow.Balance.PawnBalance_MarauderSnow'),
                (2, 1, 'GD_Allium_MarauderSnow.Balance.PawnBalance_MarauderSnow'),
                (0, 0, 'GD_Allium_PsychoKitchen.Balance.PawnBalance_PsychoKitchen'),
                (1, 0, 'GD_Allium_PsychoKitchen.Balance.PawnBalance_PsychoKitchen'),
                (2, 0, 'GD_Allium_PsychoKitchen.Balance.PawnBalance_PsychoKitchen'),
                (0, 0, 'GD_Allium_PsychoSnow.Balance.PawnBalance_PsychoSnow'),
                (1, 0, 'GD_Allium_PsychoSnow.Balance.PawnBalance_PsychoSnow'),
                (2, 0, 'GD_Allium_PsychoSnow.Balance.PawnBalance_PsychoSnow'),
                (0, 0, 'GD_Allium_PsychoSnow_Midget.Balance.PawnBalance_PsychoSnow_Midget'),
                (1, 0, 'GD_Allium_PsychoSnow_Midget.Balance.PawnBalance_PsychoSnow_Midget'),
                (2, 0, 'GD_Allium_PsychoSnow_Midget.Balance.PawnBalance_PsychoSnow_Midget'),
                (0, 0, 'GD_Butcher.Balance.PawnBalance_Butcher'),
                (1, 0, 'GD_Butcher.Balance.PawnBalance_Butcher'),
                (2, 0, 'GD_Butcher.Balance.PawnBalance_Butcher'),
                (1, 0, 'GD_HodunkPsycho.Balance.PawnBalance_HodunkPsycho'),
                (2, 0, 'GD_HodunkPsycho.Balance.PawnBalance_HodunkPsycho'),
                (1, 2, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_BigBiker'),
                (1, 2, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_Biker'),
                (1, 0, 'GD_Iris_Population_Engineer.Balance.Iris_PawnBalance_EngineerArms'),
                (1, 0, 'GD_Iris_Population_Engineer.Balance.Iris_PawnBalance_EngineerArmsNoJump'),
                (0, 1, 'GD_MarauderRegular_Digi.Population.PawnBalance_MarauderRegular_Digi'),
                (0, 1, 'GD_Nomad_Digi.Population.PawnBalance_Nomad_Digi'),
                (0, 0, 'GD_Nomad_HMG_Digi.Population.PawnBalance_Nomad_HMG_Digi'),
                (1, 0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMarauder'),
                (1, 0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMarauderSMG'),
                (0, 2, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMidgetShotgun'),
                (1, 2, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateMidgetShotgun'),
                (1, 0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PiratePsycho'),
                (1, 0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PiratePsychoMidget'),
                (0, 0, 'GD_Population_Constructor.Balance.PawnBalance_Constructor'),
                (1, 0, 'GD_Population_Constructor.Balance.PawnBalance_Constructor'),
                (0, 0, 'GD_Population_Constructor.Balance.Unique.PawnBalance_ConstructorWillhelm'),
                (1, 0, 'GD_Population_Constructor.Balance.Unique.PawnBalance_ConstructorWillhelm'),
                (0, 1, 'GD_Population_Engineer.Balance.PawnBalance_Engineer'),
                (1, 1, 'GD_Population_Engineer.Balance.PawnBalance_Engineer'),
                (0, 0, 'GD_Population_Engineer.Balance.PawnBalance_EngineerArms'),
                (1, 0, 'GD_Population_Engineer.Balance.PawnBalance_EngineerArms'),
                (0, 1, 'GD_Population_Engineer.Balance.PawnBalance_HyperionHawk'),
                (1, 1, 'GD_Population_Engineer.Balance.PawnBalance_HyperionHawk'),
                (0, 1, 'GD_Population_Engineer.Balance.PawnBalance_HyperionInfiltrator'),
                (1, 1, 'GD_Population_Engineer.Balance.PawnBalance_HyperionInfiltrator'),
                (0, 1, 'GD_Population_Engineer.Balance.PawnBalance_HyperionSoldier'),
                (1, 1, 'GD_Population_Engineer.Balance.PawnBalance_HyperionSoldier'),
                (0, 0, 'GD_Population_Goliath.Balance.PawnBalance_GoliathCorrosive'),
                (1, 0, 'GD_Population_Goliath.Balance.PawnBalance_GoliathCorrosive'),
                (0, 1, 'GD_Population_Goliath.Balance.PawnBalance_GoliathTurret'),
                (1, 1, 'GD_Population_Goliath.Balance.PawnBalance_GoliathTurret'),
                (0, 2, 'GD_Population_Marauder.Balance.PawnBalance_MarauderElite'),
                (1, 2, 'GD_Population_Marauder.Balance.PawnBalance_MarauderElite'),
                (0, 1, 'GD_Population_Marauder.Balance.PawnBalance_MarauderGrunt'),
                (1, 1, 'GD_Population_Marauder.Balance.PawnBalance_MarauderGrunt'),
                (0, 2, 'GD_Population_Marauder.Balance.PawnBalance_MarauderPsycho'),
                (1, 2, 'GD_Population_Marauder.Balance.PawnBalance_MarauderPsycho'),
                (0, 1, 'GD_Population_Marauder.Balance.PawnBalance_MarauderRegular'),
                (1, 1, 'GD_Population_Marauder.Balance.PawnBalance_MarauderRegular'),
                (0, 1, 'GD_Population_Marauder.Balance.PawnBalance_MarauderRider'),
                (1, 1, 'GD_Population_Marauder.Balance.PawnBalance_MarauderRider'),
                (0, 2, 'GD_Population_Marauder.Balance.PawnBalance_Scavenger'),
                (1, 0, 'GD_Population_Midget.Balance.PawnBalance_FlamingMidget'),
                (1, 0, 'GD_Population_Midget.Balance.PawnBalance_MidgetNomad'),
                (1, 1, 'GD_Population_Midget.Balance.PawnBalance_MidgetRat'),
                (0, 2, 'GD_Population_Midget.Balance.PawnBalance_MidgetShotgun'),
                (1, 2, 'GD_Population_Midget.Balance.PawnBalance_MidgetShotgun'),
                (1, 0, 'GD_Population_Midget.Balance.PawnBalance_MidgetSuicide'),
                (1, 0, 'GD_Population_Midget.Balance.PawnBalance_PsychoMidget'),
                (0, 1, 'GD_Population_Nomad.Balance.PawnBalance_Nomad'),
                (1, 1, 'GD_Population_Nomad.Balance.PawnBalance_Nomad'),
                (0, 1, 'GD_Population_Nomad.Balance.PawnBalance_Nomad_Ambush'),
                (0, 1, 'GD_Population_Nomad.Balance.PawnBalance_Nomad_Taskmaster'),
                (1, 1, 'GD_Population_Nomad.Balance.PawnBalance_Nomad_Taskmaster'),
                (0, 1, 'GD_Population_Nomad.Balance.PawnBalance_NomadPyro'),
                (1, 1, 'GD_Population_Nomad.Balance.PawnBalance_NomadPyro'),
                (0, 1, 'GD_Population_Nomad.Balance.PawnBalance_NomadShieldwMidget'),
                (1, 1, 'GD_Population_Nomad.Balance.PawnBalance_NomadShieldwMidget'),
                (0, 1, 'GD_Population_Nomad.Balance.PawnBalance_NomadShock'),
                (1, 1, 'GD_Population_Nomad.Balance.PawnBalance_NomadShock'),
                (1, 0, 'GD_Population_Psycho.Balance.PawnBalance_Psycho'),
                (1, 0, 'GD_Population_Psycho.Balance.PawnBalance_PsychoBurning'),
                (1, 0, 'GD_Population_Psycho.Balance.PawnBalance_PsychoSlag'),
                (1, 0, 'GD_Population_Psycho.Balance.PawnBalance_PsychoSnow'),
                (1, 1, 'GD_Population_Psycho.Balance.PawnBalance_PsychoSuicide'),
                (0, 0, 'GD_Population_Rat.Balance.PawnBalance_RatLab'),
                (1, 0, 'GD_Population_Rat.Balance.PawnBalance_RatLab'),
                (0, 0, 'GD_Population_Rat.Balance.PawnBalance_RatThief'),
                (1, 0, 'GD_Population_Rat.Balance.PawnBalance_RatThief'),
                (1, 1, 'GD_Population_Rat.Balance.PawnBalance_RatTunnel'),
                (0, 1, 'GD_Population_Rat.Balance.Unique.PawnBalance_ProspectorRat'),
                (1, 1, 'GD_Population_Rat.Balance.Unique.PawnBalance_ProspectorRat'),
                (1, 0, 'GD_PsychoMidget_Digi.Population.PawnBalance_PsychoMidget_Digi'),
                (0, 0, 'GD_RatChef.Balance.PawnBalance_RatChef'),
                (0, 0, 'GD_RatLab_Digi.Population.PawnBalance_RatLab_Digi'),
                (1, 0, 'GD_RatLab_Digi.Population.PawnBalance_RatLab_Digi'),
            ],
        )

    enemy_level_ipl = (
            # ARs
            [
                ('Dam_P', 8, 'dam_p.TheWorld:PersistentLevel.WillowAIPawn_20'),
                ('Damtop_P', 8, 'damtop_p.TheWorld:PersistentLevel.WillowAIPawn_19'),
                ('Fridge_P', 8, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_178'),
                ('Fridge_P', 8, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_179'),
                ('Fridge_P', 8, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_180'),
                ('Fridge_P', 8, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_181'),
                ('Fridge_P', 8, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_229'),
                ('icecanyon_p', 8, 'icecanyon_p.TheWorld:PersistentLevel.WillowAIPawn_72'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_102'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_105'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_108'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_362'),
                ('Orchid_Refinery_P', 8, 'Orchid_Refinery_P.TheWorld:PersistentLevel.WillowAIPawn_224'),
            ],
            # Pistols
            [
            ],
            # Shotguns
            [
                ('Grass_Cliffs_P', 7, 'Grass_Cliffs_P.TheWorld:PersistentLevel.WillowAIPawn_253'),
                ('Interlude_P', 8, 'Interlude_P.TheWorld:PersistentLevel.WillowAIPawn_12'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_101'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_109'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_111'),
                ('Orchid_ShipGraveyard_P', 7, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_200'),
                ('Orchid_ShipGraveyard_P', 7, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_203'),
                ('Orchid_ShipGraveyard_P', 7, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_248'),
            ],
            # SMGs
            [
                ('dam_p', 7, 'dam_p.TheWorld:PersistentLevel.WillowAIPawn_23'),
                ('damtop_p', 7, 'damtop_p.TheWorld:PersistentLevel.WillowAIPawn_17'),
                ('Fridge_P', 8, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_182'),
                ('Grass_Cliffs_P', 8, 'Grass_Cliffs_P.TheWorld:PersistentLevel.WillowAIPawn_208'),
                ('Grass_Cliffs_P', 8, 'Grass_Cliffs_P.TheWorld:PersistentLevel.WillowAIPawn_254'),
                ('SouthpawFactory_P', 7, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_161'),
                ('SouthpawFactory_P', 7, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_162'),
                ('SouthpawFactory_P', 7, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_163'),
                ('SouthpawFactory_P', 7, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_164'),
                ('SouthpawFactory_P', 7, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_210'),
                ('SouthpawFactory_P', 7, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_211'),
                ('SouthpawFactory_P', 7, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_295'),
                ('Orchid_ShipGraveyard_P', 9, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_199'),
                ('Orchid_ShipGraveyard_P', 9, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_201'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_232'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_233'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_234'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_236'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_238'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_240'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_242'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_244'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_245'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_246'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_11'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_12'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_14'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_17'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_19'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_21'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_23'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_7'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_8'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_9'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_187'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_188'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_189'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_191'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_193'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_195'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_197'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_199'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_200'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_184'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_185'),
                ('Luckys_P', 7, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_182'),
            ],
            # All
            [
                ('Iris_DL2_Interior_P', 7, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_106'),
                ('Iris_DL2_Interior_P', 7, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_363'),
                ('Orchid_SaltFlats_P', 9, 'Orchid_SaltFlats_P.TheWorld:PersistentLevel.WillowAIPawn_230'),
            ],
            # Launchers
            [
            ],
            # Snipers
            [
                ('Orchid_SaltFlats_P', 8, 'Orchid_SaltFlats_P.TheWorld:PersistentLevel.WillowAIPawn_228'),
                ('Orchid_SaltFlats_P', 8, 'Orchid_SaltFlats_P.TheWorld:PersistentLevel.WillowAIPawn_229'),
                ('Orchid_ShipGraveyard_P', 8, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_202'),
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
                ('dam_p', 9, 'dam_p.TheWorld:PersistentLevel.WillowAIPawn_20'),
                ('dam_p', 8, 'dam_p.TheWorld:PersistentLevel.WillowAIPawn_22'),
                ('dam_p', 9, 'dam_p.TheWorld:PersistentLevel.WillowAIPawn_23'),
                ('damtop_p', 9, 'damtop_p.TheWorld:PersistentLevel.WillowAIPawn_17'),
                ('damtop_p', 8, 'damtop_p.TheWorld:PersistentLevel.WillowAIPawn_18'),
                ('damtop_p', 9, 'damtop_p.TheWorld:PersistentLevel.WillowAIPawn_19'),
                ('Fridge_P', 9, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_178'),
                ('Fridge_P', 9, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_179'),
                ('Fridge_P', 9, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_180'),
                ('Fridge_P', 9, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_182'),
                ('Fridge_P', 8, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_227'),
                ('Fridge_P', 9, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_229'),
                ('Grass_Cliffs_P', 9, 'Grass_Cliffs_P.TheWorld:PersistentLevel.WillowAIPawn_208'),
                ('Grass_Cliffs_P', 9, 'Grass_Cliffs_P.TheWorld:PersistentLevel.WillowAIPawn_253'),
                ('Grass_Cliffs_P', 9, 'Grass_Cliffs_P.TheWorld:PersistentLevel.WillowAIPawn_254'),
                ('icecanyon_p', 8, 'icecanyon_p.TheWorld:PersistentLevel.WillowAIPawn_71'),
                ('icecanyon_p', 9, 'icecanyon_p.TheWorld:PersistentLevel.WillowAIPawn_72'),
                ('Interlude_P', 9, 'Interlude_P.TheWorld:PersistentLevel.WillowAIPawn_12'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_104'),
                ('Iris_DL2_Interior_P', 9, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_106'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_107'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_110'),
                ('Iris_DL2_Interior_P', 9, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_363'),
                ('Iris_DL2_Interior_P', 8, 'Iris_DL2_Interior_P.TheWorld:PersistentLevel.WillowAIPawn_364'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_11'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_12'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_14'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_17'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_182'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_184'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_185'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_187'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_188'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_189'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_19'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_191'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_193'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_195'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_197'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_199'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_200'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_21'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_23'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_232'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_233'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_234'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_236'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_238'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_240'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_242'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_244'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_245'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_246'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_7'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_8'),
                ('Luckys_P', 10, 'Luckys_P.TheWorld:PersistentLevel.WillowAIPawn_9'),
                ('Orchid_SaltFlats_P', 9, 'Orchid_SaltFlats_P.TheWorld:PersistentLevel.WillowAIPawn_228'),
                ('Orchid_SaltFlats_P', 9, 'Orchid_SaltFlats_P.TheWorld:PersistentLevel.WillowAIPawn_229'),
                ('Orchid_SaltFlats_P', 8, 'Orchid_SaltFlats_P.TheWorld:PersistentLevel.WillowAIPawn_230'),
                ('Orchid_SaltFlats_P', 8, 'Orchid_SaltFlats_P.TheWorld:PersistentLevel.WillowAIPawn_231'),
                ('Orchid_SaltFlats_P', 8, 'Orchid_SaltFlats_P.TheWorld:PersistentLevel.WillowAIPawn_277'),
                ('Orchid_ShipGraveyard_P', 8, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_199'),
                ('Orchid_ShipGraveyard_P', 8, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_201'),
                ('Orchid_ShipGraveyard_P', 9, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_202'),
                ('Orchid_ShipGraveyard_P', 9, 'Orchid_ShipGraveyard_P.TheWorld:PersistentLevel.WillowAIPawn_203'),
                ('SouthpawFactory_P', 9, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_161'),
                ('SouthpawFactory_P', 9, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_162'),
                ('SouthpawFactory_P', 9, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_163'),
                ('SouthpawFactory_P', 9, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_164'),
                ('SouthpawFactory_P', 9, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_210'),
                ('SouthpawFactory_P', 9, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_211'),
                ('SouthpawFactory_P', 9, 'SouthpawFactory_P.TheWorld:PersistentLevel.WillowAIPawn_295'),
                ('TundraTrain_P', 12, 'TundraTrain_P.TheWorld:PersistentLevel.WillowAIPawn_40'),
                ('TundraTrain_P', 12, 'TundraTrain_P.TheWorld:PersistentLevel.WillowAIPawn_41'),
                ('icecanyon_p', 9, 'icecanyon_p.TheWorld:PersistentLevel.WillowAIPawn_69'),
                ('icecanyon_p', 9, 'icecanyon_p.TheWorld:PersistentLevel.WillowAIPawn_70'),
            ],
        )

    enemy_dl_ia = (
            # ARs
            [
                (0, 0, 'GD_Episode06Data.BalanceDefs.BD_Ep6_RolandGunOnGround'),
            ],
            # Pistols
            [
            ],
            # Shotguns
            [
            ],
            # SMGs
            [
            ],
            # "All but Launchers"
            [
            ],
            # Launchers
            [
            ],
            # Snipers
            [
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
            ],
        )

    enemy_nipl = (
            # ARs
            [
            ],
            # Pistols
            [
            ],
            # Shotguns
            [
            ],
            # SMGs
            [
            ],
            # All
            [
                (0, 'GD_Sage_ClaptrapWorshipper.Character.AIDef_Sage_ClaptrapWorshiper:AIBehaviorProviderDefinition_0.Behavior_AIChangeInventory_29'),
            ],
            # Launchers
            [
            ],
            # Snipers
            [
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
            ],
        )

class Badass(DropConfig):
    """
    Config info for badass enemies
    """

    # Hotfix prefix
    hotfix_prefix = 'badass'

    # Equip weights
    weight_common = 0
    weight_uncommon = 0
    weight_rare = 35
    weight_veryrare = 60
    weight_alien = 55
    weight_legendary = 10

    # Rarity weight pools
    rarity_pool_ar = 'GD_CustomItemPools_MainGame.Soldier.TorgueEpic'
    rarity_pool_launchers = 'GD_CustomItemPools_Lilac.Psycho.TorgueEpic'
    rarity_pool_pistols = 'GD_CustomItemPools_MainGame.Mercenary.TorgueEpic'
    rarity_pool_shotguns = 'GD_CustomItemPools_tulip.Mechro.TorgueEpic'
    rarity_pool_smg = 'GD_CustomItemPools_MainGame.Siren.TorgueEpic'
    rarity_pool_snipers = 'GD_CustomItemPools_MainGame.Assassin.TorgueEpic'

    # Equip pools (this is where gun type weights are applied)
    equip_pool_all = 'GD_CustomItemPools_allium.Mechro.AlliumTGHeads'
    equip_pool_ar = 'GD_CustomItemPools_MainGame.Soldier.VladofEpic'
    equip_pool_launchers = 'GD_CustomItemPools_Lilac.Psycho.VladofEpic'
    equip_pool_pistols = 'GD_CustomItemPools_MainGame.Mercenary.VladofEpic'
    equip_pool_shotguns = 'GD_CustomItemPools_tulip.Mechro.VladofEpic'
    equip_pool_smg = 'GD_CustomItemPools_MainGame.Siren.VladofEpic'
    equip_pool_snipers = 'GD_CustomItemPools_MainGame.Assassin.VladofEpic'
    equip_pool_only_shotguns = 'GD_CustomItemPools_allium.Assassin.AlliumXmasHeads'

    # Shield pool
    pool_shields = 'GD_CustomItemPools_allium.Mechro.AlliumXmasHeads'

    ###
    ### Enemy changes
    ###

    enemy_dipl = (
            # ARs
            [
                (0, 'GD_BoneHead_v3.Population.PawnBalance_BoneHead_V3'),
                (0, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_BikerBadass'),
                (0, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_Hamlock'),
                (0, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_JohnnyAbs'),
                (0, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_TonyGlutes'),
                (0, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_SayFaceTroll'),
                (0, 'GD_Iris_Population_Loader.Balance.Iris_PawnBalance_LoaderBadass'),
                (0, 'GD_Orchid_Pop_Deserters.Deserter1.PawnBalance_Orchid_Deserter1'),
                (0, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderBadass'),
                (0, 'GD_Orchid_Pop_Pervbot.PawnBalance_Orchid_Pervbot'),
                (0, 'GD_Orchid_Pop_Sandman.Balance.PawnBalance_Orchid_Sandman'),
                (0, 'GD_Orchid_Pop_Sandman.Balance.PawnBalance_Orchid_Sandman_Solo'),
                (0, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_PirateHenchman2'),
                (0, 'GD_Population_Bruiser.Balance.PawnBalance_Bruiser_Muscles'),
                (0, 'GD_Population_Engineer.Balance.Unique.PawnBalance_DJHyperion'),
                (0, 'GD_Population_Engineer.Balance.Unique.PawnBalance_Gettle'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderBadass'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderBadass_HealthCashAmmoOnly'),
                (0, 'GD_Population_Loader.Balance.Unique.PawnBalance_BoneHead2'),
                (0, 'GD_Population_Loader.Balance.Unique.PawnBalance_PinocchioBot'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_Ep13_Roland'), # sure, why not?
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_Jimmy'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_CombatEngineer'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_Goliath'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_LoaderGUN'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_LoaderJET'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_Marauder'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_Nomad'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_Rat'),
                (0, 'GD_Population_Nomad.Balance.Unique.PawnBalance_Prospector'),
                (0, 'GD_Population_Rat.Balance.Unique.PawnBalance_RatEasterEgg'),
                (0, 'GD_Population_Sheriff.Balance.PawnBalance_Deputy'),
                (0, 'GD_Population_Sheriff.Balance.PawnBalance_Marshal'),
                (0, 'GD_MarauderBadass_Digi.Population.PawnBalance_MarauderBadass_Digi'),
            ],
            # Pistols
            [
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_BrningRedneck'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_JimboRiding'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_Mobley'),
                (0, 'GD_Population_Rat.Balance.Unique.PawnBalance_Dan'),
                (0, 'GD_Population_Rat.Balance.Unique.PawnBalance_Laney'),
                (0, 'GD_Population_Rat.Balance.Unique.PawnBalance_Lee'),
                (0, 'GD_Population_Rat.Balance.Unique.PawnBalance_Mick'),
                (0, 'GD_Population_Rat.Balance.Unique.PawnBalance_Ralph'),
            ],
            # Shotguns
            [
                (1, 'GD_Assassin2_Digi.Population.PawnBalance_Assassin2_Digi'),
                (0, 'GD_Assassin4_Digi.Population.PawnBalance_Assassin4_Digi'),
                (0, 'GD_ButcherBoss.Balance.PawnBalance_ButcherBoss'),
                (0, 'GD_Orchid_Pop_Sandman.Balance.PawnBalance_Orchid_Sandman_MarauderMaster'),
                (0, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_PirateHenchman'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_TectorHodunk_Combat'),
                (1, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_Jimmy'),
                (1, 'GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2'),
                (0, 'GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4'),
                (0, 'GD_Population_Rat.Balance.Unique.PawnBalance_Mortar'),
                (0, 'GD_Z1_InMemoriamData.Balance.PawnBalance_Boll'),
            ],
            # SMGs
            [
                (0, 'GD_Assassin1_Digi.Population.PawnBalance_Assassin1_Digi'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1'),
                (0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_MickZaford_Combat'),
                (0, 'GD_Population_Midget.Balance.PawnBalance_MidgetBadass'),
            ],
            # All
            [
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_BikeRiderMarauderBadass'),
                (0, 'GD_Iris_Population_BikeRider.Balance.PawnBalance_Iris_RaidBikeMarauderBadass'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderGuard'),
            ],
            # Launchers
            [
                (0, 'GD_Population_Goliath.Balance.Unique.PawnBalance_SmashHead'),
                (0, 'GD_Population_Nomad.Balance.Unique.PawnBalance_MadMike'),
            ],
            # Snipers
            [
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
                (2, 'GD_Z1_InMemoriamData.Balance.PawnBalance_Boll'),
                (2, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_BikerBadass'),
                (1, 'GD_Assassin1_Digi.Population.PawnBalance_Assassin1_Digi'),
                (0, 'GD_Assassin2_Digi.Population.PawnBalance_Assassin2_Digi'),
                (0, 'GD_Assassin3_Digi.Population.PawnBalance_Assassin3_Digi'),
                (1, 'GD_Assassin4_Digi.Population.PawnBalance_Assassin4_Digi'),
                (2, 'GD_BoneHead_v3.Population.PawnBalance_BoneHead_V3'),
                (0, 'GD_ButcherBoss2.Balance.PawnBalance_ButcherBoss2'),
                (0, 'GD_ButcherBoss3.Balance.PawnBalance_ButcherBoss3'),
                (0, 'GD_LoaderUltimateBadass_Digi.Population.PawnBalance_LoaderUltimateBadass_Digi'),
                (1, 'GD_MarauderBadass_Digi.Population.PawnBalance_MarauderBadass_Digi'),
                (1, 'GD_MrMercy_Digi.Balance.PawnBalance_MrMercy_Digi'),
                (1, 'GD_Orchid_Pop_Loader.Balance.PawnBalance_OrchidLoaderBadass'),
                (0, 'GD_Orchid_Pop_Sandman.Balance.PawnBalance_Orchid_BigSleep'),
                (1, 'GD_Orchid_Pop_Sandman.Balance.PawnBalance_Orchid_Sandman_Solo'),
                (1, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_PirateHenchman'),
                (1, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_PirateHenchman2'),
                (1, 'GD_Population_Engineer.Balance.Unique.PawnBalance_DJHyperion'),
                (1, 'GD_Population_Engineer.Balance.Unique.PawnBalance_Gettle'),
                (1, 'GD_Population_Engineer.Balance.Unique.PawnBalance_Leprechaun'),
                (1, 'GD_Population_Goliath.Balance.PawnBalance_GoliathLootGoon'),
                (1, 'GD_Population_Jack.Balance.PawnBalance_JacksBodyDouble'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderBadass'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderBadass_HealthCashAmmoOnly'),
                (1, 'GD_Population_Loader.Balance.PawnBalance_LoaderGuard'),
                (0, 'GD_Population_Loader.Balance.PawnBalance_LoaderSuperBadass'),
                (0, 'GD_Population_Loader.Balance.Unique.PawnBalance_LoaderWAR_1340'),
                (1, 'GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1'),
                (2, 'GD_Population_Marauder.Balance.Unique.PawnBalance_MickZaford_Combat'),
                (1, 'GD_Population_Marauder.Balance.Unique.PawnBalance_Mobley'),
                (2, 'GD_Population_Marauder.Balance.Unique.PawnBalance_TectorHodunk_Combat'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_Engineer'),
                (1, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_LoaderGUN'),
                (1, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_LoaderJET'),
                (0, 'GD_Population_Midget.Balance.LootMidget.PawnBalance_LootMidget_LoaderWAR'),
                (0, 'GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2'),
                (1, 'GD_Population_Nomad.Balance.Unique.PawnBalance_Flynt'),
                (1, 'GD_Population_Nomad.Balance.Unique.PawnBalance_MadMike'),
                (1, 'GD_Population_Nomad.Balance.Unique.PawnBalance_MrMercy'),
                (1, 'GD_Population_Nomad.Balance.Unique.PawnBalance_Prospector'),
                (0, 'GD_Population_Psycho.Balance.Unique.PawnBalance_Assassin3'),
                (0, 'GD_Population_Psycho.Balance.Unique.PawnBalance_IncineratorVanya_Combat'),
                (0, 'GD_Population_Psycho.Balance.Unique.PawnBalance_RakkMan'),
                (1, 'GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4'),
                (1, 'GD_Population_Rat.Balance.Unique.PawnBalance_Dan'),
                (1, 'GD_Population_Rat.Balance.Unique.PawnBalance_Laney'),
                (1, 'GD_Population_Rat.Balance.Unique.PawnBalance_Lee'),
                (1, 'GD_Population_Rat.Balance.Unique.PawnBalance_Mick'),
                (1, 'GD_Population_Rat.Balance.Unique.PawnBalance_Mortar'),
                (1, 'GD_Population_Rat.Balance.Unique.PawnBalance_Ralph'),
                (1, 'GD_Population_Rat.Balance.Unique.PawnBalance_RatEasterEgg'),
                (1, 'GD_Population_Sheriff.Balance.PawnBalance_Deputy'),
                (1, 'GD_Population_Sheriff.Balance.PawnBalance_Sheriff'),
                (0, 'GD_PsychoBadass_Digi.Population.PawnBalance_PsychoBadass_Digi'),

                # Bosses follow - I'm actually not sure if we want to be doing these or not.
                (2, 'GD_Iris_Population_MotorMama.Balance.Iris_PawnBalance_MotorMama'),
                (1, 'GD_Iris_Population_PyroPete.Balance.Iris_PawnBalance_Pyro_Pete'),
                (0, 'GD_Aster_Pop_Wizards.Balance.PawnBalance_JackWarlock_Demon'),
                (0, 'GD_Aster_Pop_Wizards.Balance.PawnBalance_JackWarlock_DemonFall'),
                (0, 'GD_Aster_Pop_Wizards.Balance.PawnBalance_JackWarlock_MirrorImage'),
                (0, 'GD_Aster_Pop_Wizards.Balance.PawnBalance_JackWarlock_Phase2'),
                (0, 'GD_Iris_Population_PistonBoss.Balance.Iris_PawnBalance_PistonBoss'),
                (0, 'GD_Iris_Population_RaidPete.Balance.Iris_PawnBalance_RaidPete'),
                (0, 'GD_Orchid_Pop_LoaderBoss.Balance.PawnBalance_Orchid_LoaderBoss'),
                (0, 'GD_Population_Jack.Balance.PawnBalance_Jack'),
                (0, 'GD_Population_Loader.Balance.Unique.PawnBalance_LoaderGiant'),
                (0, 'GD_Population_Loader.Balance.Unique.PawnBalance_Willhelm'),
                (0, 'GD_Sage_Raid_BeastMaster.Population.Balance_Sage_Raid_BeastMaster'),
            ],
        )

    enemy_pt_cipl = (
            # ARs
            [
                (0, 0, 'GD_Allium_Badass_SnowMarauder.Balance.PawnBalance_Badass_SnowMarauder'),
                (1, 0, 'GD_Allium_Badass_SnowMarauder.Balance.PawnBalance_Badass_SnowMarauder'),
                (2, 0, 'GD_Allium_Badass_SnowMarauder.Balance.PawnBalance_Badass_SnowMarauder'),
                (0, 0, 'GD_CraterMale.Balance.PawnBalance_CraterMale'),
                (1, 0, 'GD_CraterMale.Balance.PawnBalance_CraterMale'),
                (0, 0, 'GD_EngineerMale.Balance.PawnBalance_EngineerMale'),
                (1, 0, 'GD_EngineerMale.Balance.PawnBalance_EngineerMale'),
                (1, 0, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_BikerBadass'),
                (1, 0, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_Hamlock'),
                (1, 0, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_JohnnyAbs'),
                (1, 0, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_TonyGlutes'),
                (1, 0, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_SayFaceTroll'),
                (0, 0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateCaptain'),
                (1, 0, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateCaptain'),
                (1, 0, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_PirateHenchman'),
                (1, 0, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_PirateHenchman2'),
                (0, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderBadass'),
                (1, 0, 'GD_Population_Marauder.Balance.PawnBalance_MarauderBadass'),
                (0, 0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_ShirtlessMan'),
                (1, 0, 'GD_Population_Marauder.Balance.Unique.PawnBalance_ShirtlessMan'),
                (0, 0, 'GD_Population_Nomad.Balance.PawnBalance_Nomad_Ambush'),
                (0, 0, 'GD_Population_Nomad.Balance.PawnBalance_NomadBadass'),
                (1, 0, 'GD_Population_Nomad.Balance.PawnBalance_NomadBadass'),
                (0, 0, 'GD_CraterFemale.Balance.PawnBalance_CraterFemale'),
                (1, 0, 'GD_CraterFemale.Balance.PawnBalance_CraterFemale'),
                (0, 0, 'GD_HodunkBadass.Balance.PawnBalance_HodunkBadass'),
                (1, 0, 'GD_HodunkBadass.Balance.PawnBalance_HodunkBadass'),
                (2, 0, 'GD_HodunkBadass.Balance.PawnBalance_HodunkBadass'),
                (0, 0, 'GD_RaiderFemale.Balance.PawnBalance_RaiderFemale'),
                (0, 0, 'GD_RaiderMale.Balance.PawnBalance_RaiderMale'),
                (0, 0, 'GD_ZafordBadass.Balance.PawnBalance_ZafordBadass'),
                (1, 0, 'GD_ZafordBadass.Balance.PawnBalance_ZafordBadass'),
                (2, 0, 'GD_ZafordBadass.Balance.PawnBalance_ZafordBadass'),
            ],
            # Pistols
            [
                (0, 0, 'GD_Lynchwood_Male.Balance.PawnBalance_Lynchwood_Male'),
                (1, 0, 'GD_Lynchwood_Male.Balance.PawnBalance_Lynchwood_Male'),
            ],
            # Shotguns
            [
                (0, 0, 'GD_Population_Nomad.Balance.PawnBalance_BadMaw'),
                (1, 0, 'GD_Population_Nomad.Balance.PawnBalance_BadMaw'),
            ],
            # SMGs
            [
                (0, 0, 'GD_Sage_Pop_DrNakayama.Balance.PawnBalance_Sage_DrNakayama'), # he needs all the help he can get
            ],
            # All
            [
            ],
            # Launchers
            [
            ],
            # Snipers
            [
                (0, 0, 'GD_Lynchwood_Female.Balance.PawnBalance_Lynchwood_Female'),
                (1, 0, 'GD_Lynchwood_Female.Balance.PawnBalance_Lynchwood_Female'),
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
                (0, 1, 'GD_HodunkBadass.Balance.PawnBalance_HodunkBadass'),
                (1, 1, 'GD_HodunkBadass.Balance.PawnBalance_HodunkBadass'),
                (2, 1, 'GD_HodunkBadass.Balance.PawnBalance_HodunkBadass'),
                (1, 1, 'GD_Iris_Population_Biker.Balance.Iris_PawnBalance_BikerBadass'),
                (1, 1, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_Hamlock'),
                (1, 1, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_JohnnyAbs'),
                (1, 1, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_BB_TonyGlutes'),
                (1, 1, 'GD_Iris_Population_Biker.Balance.Unique.Iris_PawnBalance_SayFaceTroll'),
                (0, 1, 'GD_Population_Marauder.Balance.PawnBalance_MarauderBadass'),
                (1, 1, 'GD_Population_Marauder.Balance.PawnBalance_MarauderBadass'),
                (0, 0, 'GD_Population_Psycho.Balance.Unique.PawnBalance_SavageLee'),
                (1, 0, 'GD_Population_Psycho.Balance.Unique.PawnBalance_SavageLee'),
                (0, 0, 'GD_SandFemale.Balance.PawnBalance_SandFemale'),
                (0, 1, 'GD_ZafordBadass.Balance.PawnBalance_ZafordBadass'),
                (1, 1, 'GD_ZafordBadass.Balance.PawnBalance_ZafordBadass'),
                (2, 1, 'GD_ZafordBadass.Balance.PawnBalance_ZafordBadass'),
                (0, 1, 'GD_Allium_Badass_SnowMarauder.Balance.PawnBalance_Badass_SnowMarauder'),
                (1, 1, 'GD_Allium_Badass_SnowMarauder.Balance.PawnBalance_Badass_SnowMarauder'),
                (2, 1, 'GD_Allium_Badass_SnowMarauder.Balance.PawnBalance_Badass_SnowMarauder'),
                (1, 1, 'GD_CraterFemale.Balance.PawnBalance_CraterFemale'),
                (1, 1, 'GD_CraterMale.Balance.PawnBalance_CraterMale'),
                (0, 1, 'GD_EngineeFemale.Balance.PawnBalance_EngineerFemale'),
                (1, 1, 'GD_EngineeFemale.Balance.PawnBalance_EngineerFemale'),
                (0, 1, 'GD_EngineerMale.Balance.PawnBalance_EngineerMale'),
                (1, 1, 'GD_EngineerMale.Balance.PawnBalance_EngineerMale'),
                (1, 0, 'GD_FleshripperFemale.Balance.PawnBalance_FleshripperFemale'),
                (1, 0, 'GD_FleshripperMale.Balance.PawnBalance_FleshripperMale'),
                (0, 0, 'GD_GoliathGroom.Population.PawnBalance_GoliathGroom'),
                (0, 0, 'GD_GoliathGroom.Population.PawnBalance_GoliathGroomRaid'),
                (1, 0, 'GD_IncineratorFemale.Balance.PawnBalance_IncineratorFemale'),
                (1, 0, 'GD_IncineratorMale.Balance.PawnBalance_IncineratorMale'),
                (1, 1, 'GD_Lynchwood_Female.Balance.PawnBalance_Lynchwood_Female'),
                (1, 1, 'GD_Lynchwood_Male.Balance.PawnBalance_Lynchwood_Male'),
                (1, 0, 'GD_Orchid_Pop_Deserters.Deserter1.PawnBalance_Orchid_Deserter1'),
                (1, 0, 'GD_Orchid_Pop_Deserters.Deserter2.PawnBalance_Orchid_Deserter2'),
                (0, 1, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateCaptain'),
                (1, 1, 'GD_Orchid_Pop_Pirates.Balance.PawnBalance_Orchid_PirateCaptain'),
                (1, 2, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_PirateHenchman'), # technically this fixes a bug!
                (1, 2, 'GD_Orchid_Pop_ScarlettCrew.Balance.PawnBalance_Orchid_PirateHenchman2'), # this also fixes a bug!
                (0, 0, 'GD_Population_Constructor.Balance.PawnBalance_ConstructorBadass'),
                (1, 0, 'GD_Population_Constructor.Balance.PawnBalance_ConstructorBadass'),
                (0, 1, 'GD_Population_Marauder.Balance.Unique.PawnBalance_ShirtlessMan'),
                (1, 1, 'GD_Population_Marauder.Balance.Unique.PawnBalance_ShirtlessMan'),
                (1, 0, 'GD_Population_Midget.Balance.Unique.PawnBalance_Midge'),
                (0, 1, 'GD_Population_Nomad.Balance.PawnBalance_BadMaw'),
                (1, 1, 'GD_Population_Nomad.Balance.PawnBalance_BadMaw'),
                (0, 1, 'GD_Population_Nomad.Balance.PawnBalance_NomadBadass'),
                (1, 1, 'GD_Population_Nomad.Balance.PawnBalance_NomadBadass'),
                (1, 0, 'GD_Population_Psycho.Balance.PawnBalance_PsychoBadass'),
                (1, 0, 'GD_Population_Psycho.Balance.Unique.PawnBalance_ProspectorPsycho'),
                (0, 1, 'GD_RaiderFemale.Balance.PawnBalance_RaiderFemale'),
                (0, 1, 'GD_RaiderMale.Balance.PawnBalance_RaiderMale'),
                (0, 1, 'GD_Sage_Pop_DrNakayama.Balance.PawnBalance_Sage_DrNakayama'), # again, let's give him all the help we can
                (0, 0, 'GD_SandMale.Balance.PawnBalance_SandMale'),
            ],
        )

    enemy_level_ipl = (
            # ARs
            [
                ('Ash_P', 8, 'Ash_P.TheWorld:PersistentLevel.WillowAIPawn_3'),
                ('Ash_P', 8, 'Ash_P.TheWorld:PersistentLevel.WillowAIPawn_47'),
                ('Damtop_P', 12, 'damtop_p.TheWorld:PersistentLevel.WillowAIPawn_20'),
                ('Grass_Lynchwood_P', 8, 'Grass_Lynchwood_P.TheWorld:PersistentLevel.WillowAIPawn_0'),
                ('Grass_Lynchwood_P', 8, 'Grass_Lynchwood_P.TheWorld:PersistentLevel.WillowAIPawn_2'),
                ('Grass_Lynchwood_P', 8, 'Grass_Lynchwood_P.TheWorld:PersistentLevel.WillowAIPawn_86'),
                ('Grass_Lynchwood_P', 8, 'Grass_Lynchwood_P.TheWorld:PersistentLevel.WillowAIPawn_87'),
                ('Grass_Lynchwood_P', 8, 'Grass_Lynchwood_P.TheWorld:PersistentLevel.WillowAIPawn_89'),
                ('Grass_Lynchwood_P', 8, 'Grass_Lynchwood_P.TheWorld:PersistentLevel.WillowAIPawn_90'),
                ('icecanyon_p', 8, 'icecanyon_p.TheWorld:PersistentLevel.WillowAIPawn_69'),
                ('icecanyon_p', 8, 'icecanyon_p.TheWorld:PersistentLevel.WillowAIPawn_70'),
            ],
            # Pistols
            [
            ],
            # Shotguns
            [
                ('Grass_Lynchwood_P', 8, 'Grass_Lynchwood_P.TheWorld:PersistentLevel.WillowAIPawn_91'),
            ],
            # SMGs
            [
            ],
            # All
            [
            ],
            # Launchers
            [
            ],
            # Snipers
            [
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
                ('damtop_p', 13, 'damtop_p.TheWorld:PersistentLevel.WillowAIPawn_20'),
                ('Fridge_P', 12, 'Fridge_P.TheWorld:PersistentLevel.WillowAIPawn_228'),
            ],
        )

    enemy_dl_ia = (
            # ARs
            [
            ],
            # Pistols
            [
            ],
            # Shotguns
            [
            ],
            # SMGs
            [
            ],
            # All
            [
            ],
            # Launchers
            [
            ],
            # Snipers
            [
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
            ],
        )

    enemy_nipl = (
            # ARs
            [
            ],
            # Pistols
            [
            ],
            # Shotguns
            [
                (0, 'GD_Nast_Native_Soldier.Anims.Anim_Soldier_Warcry:BehaviorProviderDefinition_0.Behavior_AIChangeInventory_3'),
                (0, 'GD_Native_Soldier.Anims.Anim_Soldier_Warcry:BehaviorProviderDefinition_0.Behavior_AIChangeInventory_211'),
            ],
            # SMGs
            [
                (0, 'GD_Nast_Native_Soldier.Anims.Anim_Soldier_Warcry:BehaviorProviderDefinition_0.Behavior_AIChangeInventory_2'),
                (0, 'GD_Native_Soldier.Anims.Anim_Soldier_Warcry:BehaviorProviderDefinition_0.Behavior_AIChangeInventory_212'),
            ],
            # All
            [
            ],
            # Launchers
            [
            ],
            # Snipers
            [
            ],
            # Only Shotguns
            [
            ],
            # Shields
            [
            ],
        )

###
### Convenience functions
###

def get_balanced_items(items):
    """
    Returns a string containing a BalancedItems array with the given `items`.
    Each element of the list `items` should be a tuple, the first element
    being the itempool class name, and the second being the weight of that
    item.
    """
    bal_items = []
    for (classname, weight) in items:
        bal_items.append("""
            (
                ItmPoolDefinition=ItemPoolDefinition'{}',
                InvBalanceDefinition=None,
                Probability=(
                    BaseValueConstant={},
                    BaseValueAttribute=None,
                    InitializationDefinition=None,
                    BaseValueScaleConstant=1
                ),
                bDropOnDeath=True
            )
            """.format(classname, weight))
    return '({})'.format(','.join(bal_items))

def get_balanced_set(objectname, items):
    """
    Returns a regular "set" command to set `objectname`'s BalancedItems
    attribute to an array with the specified `items`.  The bulk of the
    work here is done in `get_balanced_items()`
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

def set_generic_item_prob(hotfix_name, classname, attribute,
        level=None, prob=None):
    """
    Sets a probability in the given `classname`, on the attribute `attribute`.
    Will do so via a hotfix with the name `hotfix_name`.  If `prob` is not
    specified, the item will be disabled (ie: given a zero probability).
    Otherwise, pass `1` for the prob (or any other percentage you want).
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
        )""".format(level, classname, attribute, prob))

def set_bi_item_prob(hotfix_name, classname, index, level=None, prob=None):
    """
    Sets a BalancedItems probability.
    """
    set_generic_item_prob(hotfix_name, classname,
        'BalancedItems[{}].Probability'.format(index),
        level=level,
        prob=prob)

def set_dipl_item_prob(hotfix_name, classname, index, level=None, prob=None):
    """
    Sets a DefaultItemPoolList probability.
    """
    set_generic_item_prob(hotfix_name, classname,
        'DefaultItemPoolList[{}].PoolProbability'.format(index),
        level=level,
        prob=prob)

def set_pt_cipl_item_prob(hotfix_name, classname,
        pt_index, poollist_index, level=None, prob=None):
    """
    Sets a PlayThroughs[x].CustomItemPoolList probability in the given
    `classname`, at the playthrough index `pt_index` and CustomItemPoolList
    index `poollist_index`.
    """
    set_generic_item_prob(hotfix_name, classname,
        'PlayThroughs[{}].CustomItemPoolList[{}].PoolProbability'.format(
            pt_index, poollist_index),
        level=level,
        prob=prob)

###
### Code to generate the mod
###

hfs = Hotfixes()
regular = Regular(hfs)
badass = Badass(hfs)
other = OtherConfig()

# Get rid of global world drops.
prefix = ' '*(4*2)
drop_disables = []
for (pool, index) in [
        ('GD_Itempools.GeneralItemPools.Pool_Gear', 0),
        ('GD_Itempools.GeneralItemPools.Pool_GunsAndGear', 0),
        ('GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne', 0),
        ('GD_Itempools.GeneralItemPools.Pool_GunsAndGear', 1),
        ('GD_Itempools.GeneralItemPools.Pool_GunsAndGearDropNumPlayersPlusOne', 1),
        ('GD_Itempools.GeneralItemPools.Pool_Items_Small', 1),
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
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear', 1),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear', 2),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear', 3),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Weapons_GunsAndGear', 4),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items', 0),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items', 1),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items', 2),
        ('GD_Itempools.Treasure_ChestPools.Pool_EpicChest_Items', 3),
        ('GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Items', 0),
        ('GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Items', 1),
        ('GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Items', 2),
        ('GD_Itempools.Treasure_ChestPools.Pool_WeaponChest_Items', 3),
        # BL2 Better Loot would require clearing out index 4 of Pool_WeaponChest_Items, too.
        ('GD_Itempools.EarlyGame.Pool_Knuckledragger_Pistol', 0),
        ('GD_Itempools.EarlyGame.Pool_Knuckledragger_Pistol_P2_P3', 0),
        ('GD_Itempools.EarlyGame.Pool_Knuckledragger_Pistol_P4', 0),
        ]:
    drop_disables.extend(disable_balanced_drop(prefix, pool, index))
other.disable_world_sets = "\n\n".join(drop_disables)

# Configure the loot pools that we'll use to equip regular + badass enemies.  There's one
# pool which determines the rarities, and another which determines the gun type probabilities
for config in [regular, badass]:

    # Configure rarity pools

    config.set_rarity_ar = get_balanced_set(
        config.rarity_pool_ar,
        [
            ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_01_Common', config.weight_common),
            ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_02_Uncommon', config.weight_uncommon),
            ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_04_Rare', config.weight_rare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare', config.weight_veryrare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_05_VeryRare_Alien', config.weight_alien),
            ('GD_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_06_Legendary', config.weight_legendary),
        ])

    config.set_rarity_launchers = get_balanced_set(
        config.rarity_pool_launchers,
        [
            ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_01_Common', config.weight_common),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_02_Uncommon', config.weight_uncommon),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_04_Rare', config.weight_rare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare', config.weight_veryrare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_05_VeryRare_Alien', config.weight_alien),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Launchers_06_Legendary', config.weight_legendary),
        ])

    config.set_rarity_pistols = get_balanced_set(
        config.rarity_pool_pistols,
        [
            ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_01_Common', config.weight_common),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_02_Uncommon', config.weight_uncommon),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_04_Rare', config.weight_rare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare', config.weight_veryrare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_05_VeryRare_Alien', config.weight_alien),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Pistols_06_Legendary', config.weight_legendary),
        ])

    config.set_rarity_smg = get_balanced_set(
        config.rarity_pool_smg,
        [
            ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_01_Common', config.weight_common),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_02_Uncommon', config.weight_uncommon),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_04_Rare', config.weight_rare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare', config.weight_veryrare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_05_VeryRare_Alien', config.weight_alien),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SMG_06_Legendary', config.weight_legendary),
        ])

    config.set_rarity_shotguns = get_balanced_set(
        config.rarity_pool_shotguns,
        [
            ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_01_Common', config.weight_common),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_02_Uncommon', config.weight_uncommon),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_04_Rare', config.weight_rare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare', config.weight_veryrare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_05_VeryRare_Alien', config.weight_alien),
            ('GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_06_Legendary', config.weight_legendary),
        ])

    config.set_rarity_snipers = get_balanced_set(
        config.rarity_pool_snipers,
        [
            ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_01_Common', config.weight_common),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_02_Uncommon', config.weight_uncommon),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_04_Rare', config.weight_rare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare', config.weight_veryrare),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_05_VeryRare_Alien', config.weight_alien),
            ('GD_Itempools.WeaponPools.Pool_Weapons_SniperRifles_06_Legendary', config.weight_legendary),
        ])

    # Shield pool (rarity + equip in one, since we don't need to make two choices)

    config.set_shields = get_balanced_set(
        config.pool_shields,
        [
            ('GD_Itempools.ShieldPools.Pool_Shields_All_01_Common', config.weight_common),
            ('GD_Itempools.ShieldPools.Pool_Shields_All_02_Uncommon', config.weight_uncommon),
            ('GD_Itempools.ShieldPools.Pool_Shields_All_04_Rare', config.weight_rare),
            ('GD_Itempools.ShieldPools.Pool_Shields_All_05_VeryRare', config.weight_veryrare),
            ('GD_Itempools.ShieldPools.Pool_Shields_All_06_Legendary', config.weight_legendary),
        ])

    # Configure Equip pools

    config.set_equip_all = get_balanced_set(
        config.equip_pool_all,
        [
            (config.rarity_pool_pistols, config.drop_prob_pistols),
            (config.rarity_pool_ar, config.drop_prob_ar),
            (config.rarity_pool_smg, config.drop_prob_smg),
            (config.rarity_pool_shotguns, config.drop_prob_shotguns),
            (config.rarity_pool_snipers, config.drop_prob_snipers),
            (config.rarity_pool_launchers, config.drop_prob_launchers),
        ])

    config.set_equip_ar = get_balanced_set(
        config.equip_pool_ar,
        [
            (config.rarity_pool_pistols, config.drop_prob_pistols),
            (config.rarity_pool_ar, config.drop_prob_ar*config.weight_scale),
            (config.rarity_pool_smg, config.drop_prob_smg),
            (config.rarity_pool_shotguns, config.drop_prob_shotguns),
            (config.rarity_pool_snipers, config.drop_prob_snipers),
            (config.rarity_pool_launchers, config.drop_prob_launchers),
        ])

    config.set_equip_pistols = get_balanced_set(
        config.equip_pool_pistols,
        [
            (config.rarity_pool_pistols, config.drop_prob_pistols*config.weight_scale),
            (config.rarity_pool_ar, config.drop_prob_ar),
            (config.rarity_pool_smg, config.drop_prob_smg),
            (config.rarity_pool_shotguns, config.drop_prob_shotguns),
            (config.rarity_pool_snipers, config.drop_prob_snipers),
            (config.rarity_pool_launchers, config.drop_prob_launchers),
        ])

    config.set_equip_shotguns = get_balanced_set(
        config.equip_pool_shotguns,
        [
            (config.rarity_pool_pistols, config.drop_prob_pistols),
            (config.rarity_pool_ar, config.drop_prob_ar),
            (config.rarity_pool_smg, config.drop_prob_smg),
            (config.rarity_pool_shotguns, config.drop_prob_shotguns*config.weight_scale),
            (config.rarity_pool_snipers, config.drop_prob_snipers),
            (config.rarity_pool_launchers, config.drop_prob_launchers),
        ])

    config.set_equip_smg = get_balanced_set(
        config.equip_pool_smg,
        [
            (config.rarity_pool_pistols, config.drop_prob_pistols),
            (config.rarity_pool_ar, config.drop_prob_ar),
            (config.rarity_pool_smg, config.drop_prob_smg*config.weight_scale),
            (config.rarity_pool_shotguns, config.drop_prob_shotguns),
            (config.rarity_pool_snipers, config.drop_prob_snipers),
            (config.rarity_pool_launchers, config.drop_prob_launchers),
        ])

    config.set_equip_launchers = get_balanced_set(
        config.equip_pool_launchers,
        [
            (config.rarity_pool_launchers, 1),
        ])

    config.set_equip_snipers = get_balanced_set(
        config.equip_pool_snipers,
        [
            (config.rarity_pool_snipers, 1),
        ])

    config.set_equip_only_shotguns = get_balanced_set(
        config.equip_pool_only_shotguns,
        [
            (config.rarity_pool_shotguns, 1),
        ])

# Improve "medical mystery" pool (used in a couple of places, actually)
hfs.add_level_hotfix('medicalmystery', 'MedicalMystery',
    """,GD_ItempoolsEnemyUse.Turrets.MedicalMystery_AlienGun,
    BalancedItems,,{}""".format(get_balanced_items([
        ('GD_Itempools.WeaponPools.Pool_Weapons_All_05_VeryRare_Alien', 1),
    ])))

# NoBeard's Stinkpot drop
hfs.add_level_hotfix('nobeard_stinkpot_0', 'NoBeardStinkpot',
    """Orchid_OasisTown_P,
    GD_Orchid_ItemPoolsEnemyUse.WeaponPools.Pool_Weapons_EnemyUse_NoBeardStinkpot,
    BalancedItems[0].InvBalanceDefinition,,
    WeaponBalanceDefinition'GD_Orchid_BossWeapons.AssaultRifle.AR_Jakobs_3_Stinkpot'""")
hfs.add_level_hotfix('nobeard_stinkpot_1', 'NoBeardStinkpot',
    """Orchid_OasisTown_P,
    GD_Orchid_ItemPoolsEnemyUse.WeaponPools.Pool_Weapons_EnemyUse_NoBeardStinkpot,
    BalancedItems[0].bDropOnDeath,,
    True""")

# Midge-mong uses a KerBlaster.  The rider is a generic Badass Midget, but fortunately
# no other Badass Midgets can spawn in Cove_P.  So just fiddle with the pools via
# hotfix and we're good to go.

hfs.add_level_hotfix('midgemong_kerblaster', 'Midge',
    """Cove_P,
    GD_Population_Midget.Balance.PawnBalance_MidgetBadass,
    DefaultItemPoolList[0].ItemPool,,
    ItemPoolDefinition'GD_Itempools.Runnables.Pool_WarMong'""")

hfs.add_level_hotfix('midgemong_clean_pool', 'Midge',
    """Cove_P,
    GD_Population_PrimalBeast.Balance.Unique.PawnBalance_PrimalBeast_Warmong,
    DefaultItemPoolList,,
    ()""")

# Captain Flynt - use the drop pool for equipping

set_dipl_item_prob('flynt_pool_0',
    'GD_Population_Nomad.Balance.Unique.PawnBalance_Flynt',
    0,
    level='SouthernShelf_P')
set_dipl_item_prob('flynt_pool_1',
    'GD_Population_Nomad.Balance.Unique.PawnBalance_Flynt',
    3,
    level='SouthernShelf_P')
set_dipl_item_prob('flynt_pool_2',
    'GD_Population_Nomad.Balance.Unique.PawnBalance_Flynt',
    2,
    level='SouthernShelf_P',
    prob=1)

# Bad Maw - UCP adds Deliverance, so use that.

set_pt_cipl_item_prob('badmaw_pool_0',
    'GD_Population_Nomad.Balance.PawnBalance_BadMaw',
    0, 0,
    level='Frost_P')

set_pt_cipl_item_prob('badmaw_pool_1',
    'GD_Population_Nomad.Balance.PawnBalance_BadMaw',
    1, 0,
    level='Frost_P')

# Assassin Common

set_bi_item_prob('assassin_pool_0',
    'GD_Itempools.Runnables.Pool_FourAssassins',
    0,
    level='SouthpawFactory_P')

# Assassin Wot

set_dipl_item_prob('wot_pool_0',
    'GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1',
    0,
    level='SouthpawFactory_P')

set_dipl_item_prob('wot_pool_1',
    'GD_Population_Marauder.Balance.Unique.PawnBalance_Assassin1',
    2,
    level='SouthpawFactory_P',
    prob=1)

# Assassin Oney

set_dipl_item_prob('oney_pool_0',
    'GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2',
    1,
    level='SouthpawFactory_P')

set_dipl_item_prob('oney_pool_1',
    'GD_Population_Nomad.Balance.Unique.PawnBalance_Assassin2',
    3,
    level='SouthpawFactory_P',
    prob=1)

# Assassin Rouf

set_dipl_item_prob('rouf_pool_0',
    'GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4',
    0,
    level='SouthpawFactory_P')

set_dipl_item_prob('rouf_pool_1',
    'GD_Population_Rat.Balance.Unique.PawnBalance_Assassin4',
    2,
    level='SouthpawFactory_P',
    prob=1)

###
### Generate the mod string
###

with open('mod-input-file.txt') as df:
    mod_str = df.read().format(
        mod_name=mod_name,
        mod_version=mod_version,
        hotfixes=hfs,
        regular=regular,
        badass=badass,
        other=other,
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
