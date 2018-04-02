#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:
import re
import sys
from ftexplorer.data import Data

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

# Loops through all the maps via my own ft-explorer data tools to find "trap"
# containers.  This is actually suuuuuper slow 'cause we're uncompressing the
# same file(s) a million times over to read each individual element.  Should
# maybe add some kind of preloading to the ft-explorer data classes.
#
# Anyway, for something which doesn't take ages, use the "stupid" version.

# What to inspect
control = {
        'BL2': [
            ('Arid Nexus - Badlands', 'Stockade_P'),
            ('Arid Nexus - Boneyard', 'Fyrestone_P'),
            ('Bloodshot Ramparts', 'DamTop_P'),
            ('Bloodshot Stronghold', 'Dam_P'),
            ('Bunker', 'Boss_Cliffs_P'),
            ('Caustic Caverns', 'Caverns_P'),
            ('Control Core Angel', 'VOGChamber_P'),
            ('Dust', 'Interlude_P'),
            ('End of the Line', 'TundraTrain_P'),
            ('Eridium Blight', 'Ash_P'),
            ('Fink\'s Slaughterhouse', 'BanditSlaughter_P'),
            ('Fridge', 'Fridge_P'),
            ('Friendship Gulag', 'HypInterlude_P'),
            ('Frostburn Canyon', 'IceCanyon_P'),
            ('Hero\'s Pass', 'FinalBossAscent_P'),
            ('Highlands Outwash', 'Outwash_P'),
            ('Highlands', 'Grass_P'),
            ('Holy Spirits', 'Luckys_P'),
            ('Lynchwood', 'Grass_Lynchwood_P'),
            ('Natural Selection Annex', 'CreatureSlaughter_P'),
            ('Opportunity', 'HyperionCity_P'),
            ('Ore Chasm', 'RobotSlaughter_P'),
            ('Sanctuary (post liftoff)', 'SanctuaryAir_P'),
            ('Sanctuary (pre liftoff)', 'Sanctuary_P'),
            ('Sanctuary Hole', 'Sanctuary_Hole_P'),
            ('Sawtooth Cauldron', 'CraterLake_P'),
            ('Southern Shelf - Bay', 'Cove_P'),
            ('Southern Shelf', 'SouthernShelf_P'),
            ('Southpaw Steam + Power', 'SouthpawFactory_P'),
            ('Terramorphous Peak', 'ThresherRaid_P'),
            ('Thousand Cuts', 'Grass_Cliffs_P'),
            ('Three Horns Divide', 'Ice_P'),
            ('Three Horns Valley', 'Frost_P'),
            ('Tundra Express', 'TundraExpress_P'),
            ('Vault of the Warrior', 'Boss_Volcano_P'),
            ('Wildlife Exploitation Preserve', 'PandoraPark_P'),
            ('Windshear Waste', 'Glacial_P'),
            ('Hayter\'s Folly', 'Orchid_Caves_P'),
            ('Leviathan\'s Lair', 'Orchid_WormBelly_P'),
            ('Magnys Lighthouse', 'Orchid_Spire_P'),
            ('Oasis', 'Orchid_OasisTown_P'),
            ('Rustyards', 'Orchid_ShipGraveyard_P'),
            ('Washburne Refinery', 'Orchid_Refinery_P'),
            ('Wurmwater', 'Orchid_SaltFlats_P'),
            ('Arena (final boss)', 'Iris_DL1_TAS_P'),
            ('Arena', 'Iris_DL1_P'),
            ('Badass Crater Bar', 'Iris_Moxxi_P'),
            ('Badass Crater of Badassitude', 'Iris_Hub_P'),
            ('Beatdown', 'Iris_DL2_P'),
            ('Forge', 'Iris_DL3_P'),
            ('Pyro Pete\'s Bar', 'Iris_DL2_Interior_P'),
            ('Southern Raceway', 'Iris_Hub2_P'),
            ('Ardorton Station', 'Sage_PowerStation_P'),
            ('Candlerakk\'s Crag', 'Sage_Cliffs_P'),
            ('H.S.S. Terminus', 'Sage_HyperionShip_P'),
            ('Hunter\'s Grotto', 'Sage_Underground_P'),
            ('Scylla\'s Grove', 'Sage_RockForest_P'),
            ('Dark Forest', 'Dark_Forest_P'),
            ('Dragon Keep', 'CastleKeep_P'),
            ('Flamerock Refuge', 'Village_P'),
            ('Hatred\'s Shadow', 'CastleExterior_P'),
            ('Immortal Woods', 'Dead_Forest_P'),
            ('Lair of Infinite Agony', 'Dungeon_P'),
            ('Mines of Avarice', 'Mines_P'),
            ('Murderlin\'s Temple', 'TempleSlaughter_P'),
            ('Unassuming Docks', 'Docks_P'),
            ('Winged Storm', 'DungeonRaid_P'),
            ('Raid on Digistruct Peak', 'TestingZone_P'),
            ('Hallowed Hollow', 'Pumpkin_Patch_P'),
            ('Gluttony Gulch', 'Hunger_P'),
            ('Marcus\'s Mercenary Shop', 'Xmas_P'),
            ('Rotgut Distillery', 'Distillery_P'),
            ('Wam Bam Island', 'Easter_P'),
            ],
    }

for game, levelnames in control.items():
    popdefs = {}
    print('Processing {}'.format(game))
    print('==============')
    print('')
    data = Data(game)
    for (english, levelname) in levelnames:
        
        # Get the info on what objects we need to load.
        level_packages = ['{}.TheWorld:PersistentLevel'.format(levelname)]
        node = data.get_node_by_full_object('{}.TheWorld'.format(levelname))
        for childname, child in node.children.items():
            if childname[:14].lower() == 'levelstreaming':
                childstruct = child.get_structure()
                if childstruct['LoadedLevel'] != 'None':
                    level_packages.append(childstruct['LoadedLevel'].split("'", 2)[1])

        # Report
        #print(levelname)
        #for package in level_packages:
        #    print(' * {}'.format(package))
        #print('')

        # Now loop through 'em to get all the population definitions
        traps = set()
        for package in level_packages:
            package_obj = data.get_node_by_full_object(package)
            for childname, child in package_obj.children.items():
                if (childname[:33].lower() == 'willowpopulationopportunitypoint_' or
                        childname[:27].lower() == 'populationopportunitypoint_'):
                    childstruct =  child.get_structure()
                    if childstruct != {}:
                        if 'Trap' in childstruct['PopulationDef']:
                            popdef = childstruct['PopulationDef'].split("'", 2)[1]
                            traps.add(popdef)

        # Report
        if len(traps) > 0:
            print(levelname)
            for popdef in sorted(traps):
                print(' * {}'.format(popdef))
            print('')

    print('')
