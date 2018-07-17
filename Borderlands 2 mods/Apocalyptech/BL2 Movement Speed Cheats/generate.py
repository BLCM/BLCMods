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
### Constants
###

mod_name = 'BL2 Movement Speed Cheats'
mod_version = '1.2.0'
output_filename = '{}.txt'.format(mod_name)

###
### Generation
###

segments = {}

# Loop through a number of control vars
first_profile = True
for (profile_name, profile_desc,
            (ground_speed, air_speed, injured_speed, crouched_pct, jump_z, air_control_pct, ladder_speed)
            ) in [
        ('reasonable', 'Reasonable Improvements', (650,  700,  300, 1,   750, .8, 400)),
        ('extreme',    'Extreme Improvements',    (1000, 1100, 500, 1,   900, .9, 600)),
        ('stock',      'Stock Values',            (440,  500,  150, 0.5, 630, .11, 200))]:

    # Set up a new hotfix object
    hfs = Hotfixes(nameprefix=profile_name.capitalize())

    # Disable everything but the first option, by default
    if first_profile:
        line_prefix = ''
        line_suffix = ''
    else:
        line_prefix = '#'
        line_suffix = '<off>'

    char_segments = {}
    for (name, streaming_obj, player_obj) in [
            ('Axton', 'GD_Soldier_Streaming.Pawn_Soldier', 'GD_Soldier.Character.CharClass_Soldier'),
            ('Gaige', 'GD_Tulip_Mechro_Streaming.Pawn_Mechromancer', 'GD_Tulip_Mechromancer.Character.CharClass_Mechromancer'),
            ('Krieg', 'GD_Lilac_Psycho_Streaming.Pawn_LilacPlayerClass', 'GD_Lilac_PlayerClass.Character.CharClass_LilacPlayerClass'),
            ('Maya', 'GD_Siren_Streaming.Pawn_Siren', 'GD_Siren.Character.CharClass_Siren'),
            ('Salvador', 'GD_Mercenary_Streaming.Pawn_Mercenary', 'GD_Mercenary.Character.CharClass_Mercenary'),
            ('Zero', 'GD_Assassin_Streaming.Pawn_Assassin', 'GD_Assassin.Character.CharClass_Assassin'),
            ]:
        (pkg, shortobj) = streaming_obj.split('.', 1)
        hfs.add_demand_hotfix('{}GroundSpeed'.format(name),
            '{}GroundSpeed'.format(name),
            '{},{},GroundSpeed,,{}'.format(pkg, streaming_obj, ground_speed),
            activated=first_profile)
        hfs.add_demand_hotfix('{}GroundSpeedBaseValue'.format(name),
            '{}GroundSpeedBaseValue'.format(name),
            '{},{},GroundSpeedBaseValue,,{}'.format(pkg, streaming_obj, ground_speed),
            activated=first_profile)
        hfs.add_demand_hotfix('{}AirSpeed'.format(name),
            '{}AirSpeed'.format(name),
            '{},{},AirSpeed,,{}'.format(pkg, streaming_obj, air_speed),
            activated=first_profile)
        hfs.add_demand_hotfix('{}AirSpeedBaseValue'.format(name),
            '{}AirSpeedBaseValue'.format(name),
            '{},{},AirSpeedBaseValue,,{}'.format(pkg, streaming_obj, air_speed),
            activated=first_profile)
        hfs.add_demand_hotfix('{}JumpZ'.format(name),
            '{}JumpZ'.format(name),
            '{},{},JumpZ,,{}'.format(pkg, streaming_obj, jump_z),
            activated=first_profile)
        hfs.add_demand_hotfix('{}JumpZBaseValue'.format(name),
            '{}JumpZBaseValue'.format(name),
            '{},{},JumpZBaseValue,,{}'.format(pkg, streaming_obj, jump_z),
            activated=first_profile)
        hfs.add_demand_hotfix('{}CrouchedPct'.format(name),
            '{}CrouchedPct'.format(name),
            '{},{},CrouchedPct,,{}'.format(pkg, streaming_obj, crouched_pct),
            activated=first_profile)
        segment_fmt = """#<{name}>{line_suffix}

                {line_prefix}# The set statements apply the settings initially{line_suffix}

                {line_prefix}set {player_obj} GroundSpeed {ground_speed}{line_suffix}

                {line_prefix}set {player_obj} AirSpeed {air_speed}{line_suffix}

                {line_prefix}set {player_obj} CrouchedPct {crouched_pct}{line_suffix}

                {line_prefix}set {player_obj} JumpZ {jump_z}{line_suffix}

                {line_prefix}# The hotfixes apply once you respawn or exit FFYL{line_suffix}
                {line_prefix}# (These may be a bit overboard.  Not sure if you need the BaseValue{line_suffix}
                {line_prefix}# ones, or if the BaseValue ones are the only ones you need, etc.){line_suffix}

                {{hotfixes:{name}GroundSpeed}}

                {{hotfixes:{name}GroundSpeedBaseValue}}

                {{hotfixes:{name}AirSpeed}}

                {{hotfixes:{name}AirSpeedBaseValue}}

                {{hotfixes:{name}JumpZ}}

                {{hotfixes:{name}JumpZBaseValue}}

                {{hotfixes:{name}CrouchedPct}}

            #</{name}>""".format(
                name=name,
                line_prefix=line_prefix,
                line_suffix=line_suffix,
                player_obj=player_obj,
                ground_speed=ground_speed,
                air_speed=air_speed,
                crouched_pct=crouched_pct,
                jump_z=jump_z,
                )

        char_segments[name] = segment_fmt.format(hotfixes=hfs)

    segments[profile_name] = """#<{profile_desc}>{line_suffix}

            {axton}

            {gaige}

            {krieg}

            {maya}

            {salvador}

            {zero}

            #<Global Movement Vars>{line_suffix}

                {line_prefix}# These variables aren't player-specific, and don't seem to require hotfixes{line_suffix}
                {line_prefix}# to apply post-death-or-FFYL{line_suffix}

                {line_prefix}set GD_PlayerShared.injured.PlayerInjuredDefinition InjuredMovementSpeed {injured_speed}{line_suffix}

                {line_prefix}set GD_Globals.General.Globals PlayerAirControl {air_control_pct}{line_suffix}

                {line_prefix}set Engine.Pawn LadderSpeed {ladder_speed}{line_suffix}

            #</Global Movement Vars>

        #</{profile_desc}>""".format(
            line_prefix=line_prefix,
            line_suffix=line_suffix,
            profile_desc=profile_desc,
            axton=char_segments['Axton'],
            gaige=char_segments['Gaige'],
            krieg=char_segments['Krieg'],
            maya=char_segments['Maya'],
            salvador=char_segments['Salvador'],
            zero=char_segments['Zero'],
            injured_speed=injured_speed,
            air_control_pct=air_control_pct,
            ladder_speed=ladder_speed,
            )

    first_profile = False

mod_str = """#<{mod_name}>

    # {mod_name} v{mod_version}
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Ups the movement speed of all characters (including while crouched and during
    # FFYL), increases jump height a bit, and provides much more air control.

    #<Movement Speed Buffs (Pick One)><MUT>

        {reasonable}

        {extreme}

        {stock}

    #</Movement Speed Buffs (Pick One)>

#</{mod_name}>""".format(
    mod_name=mod_name,
    mod_version=mod_version,
    reasonable=segments['reasonable'],
    extreme=segments['extreme'],
    stock=segments['stock'],
    )

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
