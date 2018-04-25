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

mod_name = 'TPS Movement Speed Cheats'
mod_version = '1.0.1'
output_filename = '{}.txt'.format(mod_name)

# Control vars
ground_speed = 1000     # (stock: 440)
air_speed = 1100        # (stock: 500)
injured_speed = 500     # (stock: 150)
crouched_pct = 1        # (stock: 0.5)
jump_z = 900            # (stock: 630)
air_control_pct = .9    # (stock: 0.05)

###
### Hotfix object to store all our hotfixes
###

hfs = Hotfixes()

char_segments = {}
for (name, streaming_obj, player_obj) in [
        ('Athena', 'GD_Gladiator_Streaming.Pawn_Gladiator', 'GD_Gladiator.Character.CharClass_Gladiator'),
        ('Aurelia', 'Crocus_Baroness_Streaming.Pawn_Baroness', 'Crocus_Baroness.Character.CharClass_Baroness'),
        ('Fragtrap', 'GD_Prototype_Streaming.Pawn_Prototype', 'GD_Prototype.Character.CharClass_Prototype'),
        ('Jack', 'Quince_Doppel_Streaming.Pawn_Doppelganger', 'Quince_Doppel.Character.charclass_doppelganger'),
        ('Nisha', 'GD_Lawbringer_Streaming.Pawn_Lawbringer', 'GD_Lawbringer.Character.CharClass_Lawbringer'),
        ('Wilhelm', 'GD_Enforcer_Streaming.Pawn_Enforcer', 'GD_Enforcer.Character.CharClass_Enforcer'),
        ]:
    (pkg, shortobj) = streaming_obj.split('.', 1)
    hfs.add_demand_hotfix('{}GroundSpeed'.format(name),
        '{}GroundSpeed'.format(name),
        '{},{},GroundSpeed,,{}'.format(pkg, streaming_obj, ground_speed))
    hfs.add_demand_hotfix('{}GroundSpeedBaseValue'.format(name),
        '{}GroundSpeedBaseValue'.format(name),
        '{},{},GroundSpeedBaseValue,,{}'.format(pkg, streaming_obj, ground_speed))
    hfs.add_demand_hotfix('{}AirSpeed'.format(name),
        '{}AirSpeed'.format(name),
        '{},{},AirSpeed,,{}'.format(pkg, streaming_obj, air_speed))
    hfs.add_demand_hotfix('{}AirSpeedBaseValue'.format(name),
        '{}AirSpeedBaseValue'.format(name),
        '{},{},AirSpeedBaseValue,,{}'.format(pkg, streaming_obj, air_speed))
    hfs.add_demand_hotfix('{}JumpZ'.format(name),
        '{}JumpZ'.format(name),
        '{},{},JumpZ,,{}'.format(pkg, streaming_obj, jump_z))
    hfs.add_demand_hotfix('{}JumpZBaseValue'.format(name),
        '{}JumpZBaseValue'.format(name),
        '{},{},JumpZBaseValue,,{}'.format(pkg, streaming_obj, jump_z))
    hfs.add_demand_hotfix('{}CrouchedPct'.format(name),
        '{}CrouchedPct'.format(name),
        '{},{},CrouchedPct,,{}'.format(pkg, streaming_obj, crouched_pct))
    segment_fmt = """#<{name}>

        # The set statements apply the settings initially

        set {player_obj} GroundSpeed {ground_speed}

        set {player_obj} AirSpeed {air_speed}

        set {player_obj} CrouchedPct {crouched_pct}

        set {player_obj} JumpZ {jump_z}

        # The hotfixes apply once you respawn or exit FFYL
        # (These may be a bit overboard.  Not sure if you need the BaseValue
        # ones, or if the BaseValue ones are the only ones you need, etc.)

        {{hotfixes:{name}GroundSpeed}}

        {{hotfixes:{name}GroundSpeedBaseValue}}

        {{hotfixes:{name}AirSpeed}}

        {{hotfixes:{name}AirSpeedBaseValue}}

        {{hotfixes:{name}JumpZ}}

        {{hotfixes:{name}JumpZBaseValue}}

        {{hotfixes:{name}CrouchedPct}}

    #</{name}>""".format(name=name,
        player_obj=player_obj,
        ground_speed=ground_speed,
        air_speed=air_speed,
        crouched_pct=crouched_pct,
        jump_z=jump_z,
        )
    char_segments[name] = segment_fmt.format(hotfixes=hfs)

loot_str = """#<{mod_name}>

    # {mod_name} v{mod_version}
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Ups the movement speed of all characters (including while crouched and during
    # FFYL), increases jump height a bit, and provides much more air control.

    {athena}

    {aurelia}

    {fragtrap}

    {jack}

    {nisha}

    {wilhelm}

    #<Global Movement Vars>

        # These variables aren't player-specific, and don't seem to require hotfixes
        # to apply post-death-or-FFYL

        set GD_PlayerShared.injured.PlayerInjuredDefinition InjuredMovementSpeed {injured_speed}

        set GD_Globals.General.Globals PlayerAirControl {air_control_pct}

    #</Global Movement Vars>

#</{mod_name}>""".format(
    mod_name=mod_name,
    mod_version=mod_version,
    athena=char_segments['Athena'],
    aurelia=char_segments['Aurelia'],
    fragtrap=char_segments['Fragtrap'],
    jack=char_segments['Jack'],
    nisha=char_segments['Nisha'],
    wilhelm=char_segments['Wilhelm'],
    injured_speed=injured_speed,
    air_control_pct=air_control_pct,
    )

with open(output_filename, 'w') as df:
    df.write(loot_str)
print('Wrote mod file to: {}'.format(output_filename))
