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

# Takes the "Resource - InventoryPartListCollectionDefinition.txt" file from
# FilterTool's internal resources dir, and generates a list of `set` commands
# to remove gamestage/level requirements from all parts for everything found
# in the file which isn't already set to level 0 or 1.  This is overkill, and
# includes some properties we don't even actually need, but whatever.
#
# I apologize for how awful the code is - this is super hacky.

import re
import sys

# These are classes which aren't available immediately, and so need a
# hotfix in order to be set properly.  This list was just constructed
# by trying everything out with `set` first and grabbing the list of
# what failed via B2's launch.log.
need_hotfix = set([
    'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin:ItemPartListCollectionDefinition_28',
    'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer:ItemPartListCollectionDefinition_29',
    'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc:ItemPartListCollectionDefinition_30',
    'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho:ItemPartListCollectionDefinition_31',
    'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren:ItemPartListCollectionDefinition_32',
    'GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier:ItemPartListCollectionDefinition_33',
    'GD_Aster_RaidWeapons.Pistols.Aster_Seraph_Stinger_Balance:WeaponPartListCollectionDefinition_225',
    'GD_Aster_RaidWeapons.Shotguns.Aster_Seraph_Omen_Balance:WeaponPartListCollectionDefinition_224',
    'GD_Aster_Weapons.AssaultRifles.AR_Bandit_4_Quartz:WeaponPartListCollectionDefinition_231',
    'GD_Aster_Weapons.AssaultRifles.AR_Dahl_4_Emerald:WeaponPartListCollectionDefinition_232',
    'GD_Aster_Weapons.AssaultRifles.AR_Vladof_4_Garnet:WeaponPartListCollectionDefinition_233',
    'GD_Aster_Weapons.Pistols.Pistol_Bandit_4_Quartz:WeaponPartListCollectionDefinition_235',
    'GD_Aster_Weapons.Pistols.Pistol_Dahl_4_Emerald:WeaponPartListCollectionDefinition_237',
    'GD_Aster_Weapons.Pistols.Pistol_Hyperion_4_Diamond:WeaponPartListCollectionDefinition_241',
    'GD_Aster_Weapons.Pistols.Pistol_Maliwan_4_Aquamarine:WeaponPartListCollectionDefinition_239',
    'GD_Aster_Weapons.Pistols.Pistol_Tediore_4_CubicZerconia:WeaponPartListCollectionDefinition_236',
    'GD_Aster_Weapons.Pistols.Pistol_Vladof_4_Garnet:WeaponPartListCollectionDefinition_238',
    'GD_Aster_Weapons.Shotguns.SG_Bandit_4_Quartz:WeaponPartListCollectionDefinition_242',
    'GD_Aster_Weapons.Shotguns.SG_Hyperion_4_Diamond:WeaponPartListCollectionDefinition_245',
    'GD_Aster_Weapons.Shotguns.SG_Tediore_4_CubicZerconia:WeaponPartListCollectionDefinition_243',
    'GD_Aster_Weapons.SMGs.SMG_Bandit_3_Orc:WeaponPartListCollectionDefinition_258',
    'GD_Aster_Weapons.SMGs.SMG_Bandit_4_Quartz:WeaponPartListCollectionDefinition_246',
    'GD_Aster_Weapons.SMGs.SMG_Dahl_4_Emerald:WeaponPartListCollectionDefinition_248',
    'GD_Aster_Weapons.SMGs.SMG_Hyperion_4_Diamond:WeaponPartListCollectionDefinition_250',
    'GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit:WeaponPartListCollectionDefinition_223',
    'GD_Aster_Weapons.SMGs.SMG_Maliwan_4_Aquamarine:WeaponPartListCollectionDefinition_249',
    'GD_Aster_Weapons.SMGs.SMG_Tediore_4_CubicZerconia:WeaponPartListCollectionDefinition_247',
    'GD_Aster_Weapons.Snipers.SR_Dahl_4_Emerald:WeaponPartListCollectionDefinition_251',
    'GD_Aster_Weapons.Snipers.SR_Hyperion_4_Diamond:WeaponPartListCollectionDefinition_255',
    'GD_Aster_Weapons.Snipers.SR_Vladof_4_Garnet:WeaponPartListCollectionDefinition_252',
    'GD_Gladiolus_Weapons.AssaultRifle.AR_Dahl_6_Bearcat:WeaponPartListCollectionDefinition_262',
    'GD_Gladiolus_Weapons.Pistol.Pistol_Vladof_6_Stalker:WeaponPartListCollectionDefinition_260',
    'GD_Gladiolus_Weapons.Shotgun.SG_Hyperion_6_Butcher:WeaponPartListCollectionDefinition_264',
    'GD_Gladiolus_Weapons.SMG.SMG_Tediore_6_Avenger:WeaponPartListCollectionDefinition_263',
    'GD_Iris_ItemPools.BalDefs.BalDef_ClassMod_Torgue_Common:ItemPartListCollectionDefinition_39',
    'GD_Iris_Weapons.AssaultRifles.AR_Vladof_3_Kitten:WeaponPartListCollectionDefinition_272',
    'GD_Iris_Weapons.Shotguns.SG_Hyperion_3_SlowHand:WeaponPartListCollectionDefinition_267',
    'GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_04_VeryRare:ItemPartListCollectionDefinition_44',
    'GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho:ItemPartListCollectionDefinition_40',
    'GD_Lobelia_Weapons.Pistol.Pistol_Maliwan_6_Wanderlust:WeaponPartListCollectionDefinition_274',
    'GD_Orchid_BossWeapons.AssaultRifle.AR_Vladof_3_Rapier:WeaponPartListCollectionDefinition_289',
    'GD_Orchid_BossWeapons.Shotgun.SG_Bandit_3_JollyRoger:WeaponPartListCollectionDefinition_290',
    'GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk:WeaponPartListCollectionDefinition_292',
    'GD_Orchid_BossWeapons.SniperRifles.Sniper_Maliwan_3_Pimpernel:WeaponPartListCollectionDefinition_293',
    'GD_Orchid_RaidWeapons.Shotgun.Spitter.Orchid_Seraph_Spitter_Balance:WeaponPartListCollectionDefinition_283',
    'GD_Orchid_RaidWeapons.SMG.Actualizer.Orchid_Seraph_Actualizer_Balance:WeaponPartListCollectionDefinition_284',
    'GD_Orchid_RaidWeapons.SMG.Tattler.Orchid_Seraph_Tattler_Balance:WeaponPartListCollectionDefinition_282',
    'GD_Orchid_RaidWeapons.sniper.Patriot.Orchid_Seraph_Patriot_Balance:WeaponPartListCollectionDefinition_286',
    'GD_Sage_RaidWeapons.AssaultRifle.Sage_Seraph_LeadStorm_Balance:WeaponPartListCollectionDefinition_298',
    'GD_Sage_RaidWeapons.Shotgun.Sage_Seraph_Interfacer_Balance:WeaponPartListCollectionDefinition_297',
    'GD_Sage_Weapons.AssaultRifle.AR_Bandit_3_Chopper:WeaponPartListCollectionDefinition_303',
    'GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_04_VeryRare:ItemPartListCollectionDefinition_52',
    'GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer:ItemPartListCollectionDefinition_48',
    ])

class Re(object):
    """
    Class to allow us to use a Perl-like regex-comparison idiom
    such as:

    if $line =~ /(foo)/ { ... }
    elsif $line =~ /(bar)/ { ... }
    elsif $line =~ /(baz)/ { ... }

    Taken from http://stackoverflow.com/questions/597476/how-to-concisely-cascade-through-multiple-regex-statements-in-python
    """

    def __init__(self):
        self.last_match = None

    def match(self, regex, text):
        self.last_match = re.match(regex, text)
        return self.last_match

    def search(self, regex, text):
        self.last_match = re.search(regex, text)
        return self.last_match

hotfix_count = 0
myre = Re()
with open('Resource - InventoryPartListCollectionDefinition.txt', 'r') as df:
    cur_partlist = None
    for line in df.readlines():

        if myre.search("Property dump for object '.*PartListCollectionDefinition (.*)'", line):
            cur_partlist = myre.last_match.group(1)

        elif myre.match('^\s*(.*?)=(.*WeightedParts.*)$', line):

            if not cur_partlist:
                raise Exception("Found some parts but we're not in a partlist def")
            data_type = myre.last_match.group(1)
            data_value = myre.last_match.group(2)

            # Grab just WeightedParts
            match = myre.match('^\(bEnabled=(\w+),WeightedParts=(.*)\)$', data_value)
            if not match:
                raise Exception("Didn't find the structure we expected")
            enabled = match.group(1)
            weighted_parts = match.group(2)

            # Weed out some stuff we don't care about
            if enabled == 'False':
                continue
            if weighted_parts == '':
                continue

            # Pull apart WeightedParts; if we see commas in inner paren statements,
            # just bloody change 'em to pipes.  For the dataset we care about, at
            # the moment I'd like to just be able to split the thing on top-level
            # commas
            part_defs = []
            weighted_parts = weighted_parts[1:-1]
            cur_level = 0
            cur_part_txt = []
            for char in weighted_parts:
                if char == '(':
                    cur_level += 1
                    if cur_level == 1:
                        cur_part_txt = []
                    else:
                        cur_part_txt.append(char)
                elif char == ')':
                    cur_level -= 1
                    if cur_level == 0:
                        part_defs.append(''.join(cur_part_txt))
                    else:
                        cur_part_txt.append(char)
                elif char == ',':
                    if cur_level > 1:
                        cur_part_txt.append('|')
                    else:
                        cur_part_txt.append(char)
                else:
                    cur_part_txt.append(char)

            # Now create a dict
            parts = []
            weights = set()
            need_set = False
            for (idx, part_def) in enumerate(part_defs):
                part_dict = {}
                for item in part_def.split(','):
                    (key, val) = item.split('=', 1)
                    part_dict[key] = val.replace('|', ',')
                if 'MinGameStageIndex' not in part_dict:
                    raise Exception("Expected MinGameStageIndex but didn't find it: {}".format(weighted_parts))
                weights.add(part_dict['DefaultWeightIndex'])
                parts.append(part_dict)

                # Find out if we need to do anything
                if int(part_dict['MinGameStageIndex']) > 1:
                    need_set = True
                    part_dict['MinGameStageIndex'] = '0'

            # Reporting on which partlists don't weight all parts equally
            #if len(weights) > 1:
            #    print('{} {} Weights: {}'.format(cur_partlist, data_type, len(weights)), file=sys.stderr)

            # Create a `set` statement to remove all game stage requirements
            if need_set:
                final_weight_text = '(({}))'.format('),('.join(','.join(['{}={}'.format(key, val) for (key, val) in part_dict.items()]) for part_dict in parts))
                if cur_partlist in need_hotfix:
                    print('            {{hotfixes:part_early_game_fix_{}}}'.format(hotfix_count))

                    # Also output our hotfix-generation code on stderr
                    print("hfs.add_level_hotfix('part_early_game_fix_{idx}', 'PartEarlyGameFix', \",{classname},{propertyname}.WeightedParts,,{final_weight_text}\")".format(
                        idx=hotfix_count,
                        classname=cur_partlist,
                        propertyname=data_type,
                        final_weight_text=final_weight_text,
                        ), file=sys.stderr)

                    hotfix_count += 1
                else:
                    print('            set {classname} {propertyname} (bEnabled={enabled},WeightedParts={final_weight_text})'.format(
                        classname=cur_partlist,
                        propertyname=data_type,
                        enabled=enabled,
                        final_weight_text=final_weight_text,
                        ))
                print('')
