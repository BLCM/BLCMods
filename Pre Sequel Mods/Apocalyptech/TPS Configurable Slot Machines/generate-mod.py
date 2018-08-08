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

# Python script to generate my TPS Configurable Slot Machines mod

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

mod_name = 'TPS Configurable Slot Machines'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

def get_balanced_report(items):
    """
    Convenience method to generate some percentages based on weights, for
    reporting back to the user.
    """
    to_ret = []
    total = sum(items)
    for item in items:
        pct = item / total * 100
        if pct == 0:
            to_ret.append('0')
        elif pct < 1:
            to_ret.append(str(round(pct, 2)))
        elif pct < 10:
            to_ret.append(str(round(pct, 1)))
        else:
            to_ret.append(str(round(pct)))

        if to_ret[-1].endswith('.00'):
            to_ret[-1] = to_ret[-1][:-3]
        elif to_ret[-1].endswith('.0'):
            to_ret[-1] = to_ret[-1][:-2]

    return tuple(to_ret)

###
### Start generating the mod
###

mod_list = []
mod_list.append("""TPS
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Allows you to configure the base game's slot machines, of the sort in Concordia.
    # The default configuration is identical to the stock slot machines - you must choose
    # some options to actually have any changes take effect.
    #
    # Keep in mind that increasing the frequency of one kind of item can end up impacting
    # the frequencies of other items.  Categories with "Quality" in the title should keep
    # the frequencies the same.
    #
    # Also note that if you're in developer mode in BLCMM v1.1.6, most of this mod will
    # complain that things will be overwritten by the game -- that's actually an error on
    # BLCMM's part, and should hopefully be fixed by v1.1.7.

    #<Mod Setup><lock>

        # These are some statements which are required for some of the later statements
        # to work properly.

        level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0 BehaviorSequences[1].BehaviorData2[4].LinkedVariables.ArrayIndexAndLength 0

        level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0 BehaviorSequences[1].BehaviorData2[42].LinkedVariables.ArrayIndexAndLength 0

        level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0 BehaviorSequences[1].BehaviorData2[97].LinkedVariables.ArrayIndexAndLength 0

        level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0 BehaviorSequences[1].BehaviorData2[102].LinkedVariables.ArrayIndexAndLength 0

        level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0 BehaviorSequences[1].BehaviorData2[126].LinkedVariables.ArrayIndexAndLength 0

    #</Mod Setup>""".format(mod_name=mod_name, mod_version=mod_version))

###
### Weapon Quality
###

mod_list.append('#<Weapons>')
mod_list.append('#<Weapon Quality><MUT>')
for (label, white, green, blue, purple, orange) in [
        ('Stock Quality', 40, 30, 3, 0.3, 0.03),
        ('Improved Quality', 26, 35, 10, 2.3, 0.35),
        ('Better Quality', 11, 33, 22, 5.5, 1.1),
        ('Excellent Quality', 5.1, 15, 30, 20, 2.5),
        ]:
    (white_pct,
            green_pct,
            blue_pct,
            purple_pct,
            orange_pct) = get_balanced_report([
                white,
                green,
                blue,
                purple,
                orange
                ])
    mod_list.append("""
        #<{label}>

            #     White: {white_pct}%
            #     Green: {green_pct}%
            #      Blue: {blue_pct}%
            #    Purple: {purple_pct}%
            # Legendary: {orange_pct}%

            #<Statements>

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[0] {white}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[1] {green}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[2] {blue}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[3] {purple}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[4] {orange}

            #</Statements>
            
        #</{label}>
        """.format(
                label=label,
                white=white, white_pct=white_pct,
                green=green, green_pct=green_pct,
                blue=blue, blue_pct=blue_pct,
                purple=purple, purple_pct=purple_pct,
                orange=orange, orange_pct=orange_pct,
                ))
mod_list.append('#</Weapon Quality>')

###
### Weapon Types
###

mod_list.append('#<Weapon Type Distribution><MUT>')
for (label, pistol, longw, launcher) in [
        ('Stock Type Distribution', 0.3, 1, 0.07),
        ('Totally Even Distribution', 10, 40, 10),
        ]:
    (pistol_pct,
            long_pct,
            launcher_pct) = get_balanced_report([
                pistol,
                longw,
                launcher,
                ])
    mod_list.append("""
        #<{label}>

            #               Pistols: {pistol_pct}%
            # AR/Shotgun/SMG/Sniper: {long_pct}%
            #             Launchers: {launcher_pct}%

            #<Statements>

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_154 Conditions[0] {pistol}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_154 Conditions[1] {longw}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_154 Conditions[2] {launcher}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_156 Conditions[0] {pistol}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_156 Conditions[1] {longw}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_156 Conditions[2] {launcher}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_158 Conditions[0] {pistol}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_158 Conditions[1] {longw}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_158 Conditions[2] {launcher}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_159 Conditions[0] {pistol}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_159 Conditions[1] {longw}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_159 Conditions[2] {launcher}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_160 Conditions[0] {pistol}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_160 Conditions[1] {longw}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_160 Conditions[2] {launcher}

            #</Statements>

        #</{label}>
        """.format(
                label=label,
                pistol=pistol, pistol_pct=pistol_pct,
                longw=longw, long_pct=long_pct,
                launcher=launcher, launcher_pct=launcher_pct,
                ))

mod_list.append('#</Weapon Types>')
mod_list.append('#</Weapons>')

###
### Money Quality
###

mod_list.append('#<Money>')
mod_list.append('#<Money Quality><MUT>')
for (label, one, two, three) in [
        ('Stock Quality', 1, 0.25, 0.1),
        ('Improved Quality', 49, 35, 16),
        ('Better Quality', 33, 33, 33),
        ('Excellent Quality', 10, 30, 60),
        ]:
    (one_pct,
            two_pct,
            three_pct) = get_balanced_report([
                one,
                two,
                three,
                ])
    mod_list.append("""
        #<{label}>

            # 1x Money: {one_pct}%
            # 2x Money: {two_pct}%
            # 3x Money: {three_pct}%

            #<Statements>

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_157 Conditions[0] {one}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_157 Conditions[1] {two}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_157 Conditions[2] {three}

            #</Statements>
            
        #</{label}>
        """.format(
                label=label,
                one=one, one_pct=one_pct,
                two=two, two_pct=two_pct,
                three=three, three_pct=three_pct,
                ))
mod_list.append('#</Money Quality>')

###
### Money Frequency
###

mod_list.append('#<Money Frequency><MUT>')
for (label, weight) in [
        ('Stock Drops', 50),
        ('Doubled Money Drops', 100),
        ('Halved Money Drops', 25),
        ('No Money Drops', 0),
        ]:
    mod_list.append("""
        #<{label}>

            level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[8] {weight}

        #</{label}>
        """.format(
                label=label,
                weight=weight,
                ))

mod_list.append('#</Money Frequency>')
mod_list.append('#</Money>')

###
### Moonstone
###

mod_list.append('#<Moonstone>')
mod_list.append('#<Moonstone Quality + Frequency><MUT>')
for (label, one, two, three) in [
        ('Stock Quality and Frequency', 5, 1.5, 0.45),
        ('Stock Quality, Doubled Frequency', 10, 3, 0.9),
        ('Better Quality, Stock Frequency', 2.3, 2.3, 2.3),
        ('Better Quality, Doubled Frequency', 4.6, 4.6, 4.6),
        ('Excellent Quality, Stock Frequency', 1.3, 2.3, 3.4),
        ('Excellent Quality, Doubled Frequency', 2.6, 4.6, 6.8),
        ]:
    (one_pct,
            two_pct,
            three_pct) = get_balanced_report([
                one,
                two,
                three,
                ])
    mod_list.append("""
        #<{label}>

            # Quality chances:
            #
            #    4x Moonstone: {one_pct}%
            #    8x Moonstone: {two_pct}%
            #         Jackpot: {three_pct}%

            #<Statements>

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[5] {one}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[6] {two}

                level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[7] {three}

            #</Statements>

        #</{label}>
        """.format(
            label=label,
            one=one, one_pct=one_pct,
            two=two, two_pct=two_pct,
            three=three, three_pct=three_pct,
            ))
mod_list.append('#</Moonstone Quality + Frequency>')

###
### Moonstone Jackpot Reward
###

mod_list.append('#<Moonstone Jackpot Reward><MUT>')
for (label, pool) in [
        ('Stock Reward (45 Moonstones)', 'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone_Cluster'),
        ('Probably-Intended Reward (12 Moonstones)', 'GD_Itempools.AmmoAndResourcePools.Pool_Moonstone'),
        ]:
    mod_list.append("""
        #<{label}>

            level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_SpawnItems_528 ItemPoolList[0].ItemPool ItemPoolDefinition'{pool}'

        #</{label}>
        """.format(label=label, pool=pool))

mod_list.append('#</Moonstone Jackpot Reward')

mod_list.append('#</Moonstone>')

###
### Skin Frequency
###

mod_list.append('#<Skin Frequency><MUT>')
for (label, weight) in [
        ('Stock Drops', 10),
        ('Doubled Skin Drops', 20),
        ('Halved Skin Drops', 5),
        ('No Skin Drops', 0),
        ]:
    mod_list.append("""
        #<{label}>

            level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[10] {weight}

        #</{label}>
        """.format(
                label=label,
                weight=weight,
                ))

mod_list.append('#</Skin Frequency>')

###
### Grenade Frequency
###

mod_list.append('#<Grenade Frequency><MUT>')
for (label, weight) in [
        ('Stock Drops', 15),
        ('Doubled Grenade Drops', 30),
        ('Halved Grenade Drops', 7.5),
        ('No Grenade Drops', 0),
        ]:
    mod_list.append("""
        #<{label}>

            level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[9] {weight}

        #</{label}>
        """.format(
                label=label,
                weight=weight,
                ))

mod_list.append('#</Grenade Frequency>')

###
### Nothing Frequency
###

mod_list.append('#<No Reward Frequency><MUT>')
for (label, weight) in [
        ('Stock Weight', 40),
        ('Doubled No-Reward Freqency', 80),
        ('Halved No-Reward Frequency', 20),
        ('Always Get Reward', 0),
        ]:
    mod_list.append("""
        #<{label}>

            level None set GD_SlotMachine.SlotMachine:BehaviorProviderDefinition_0.Behavior_RandomBranch_155 Conditions[11] {weight}

        #</{label}>
        """.format(
                label=label,
                weight=weight,
                ))

mod_list.append('#</No Reward Frequency>')

###
### Finish off the mod
###

mod_list.append('#</{}>'.format(mod_name))

###
### Output to a file.
###

mp.human_str_to_blcm_filename("\n\n".join(mod_list), output_filename)
print('Wrote mod file to: {}'.format(output_filename))
