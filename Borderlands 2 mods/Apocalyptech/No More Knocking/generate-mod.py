#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2019, CJ Kucera
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
import random

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

# Control Vars
mod_name = 'No More Knocking'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

level_perches = {
        ('Badass Crater Bar', 'Iris_Moxxi_P'): [
            'Iris_Moxxi_P.TheWorld:PersistentLevel.Perch_17',
            ],
        ('Flamerock Refuge', 'Village_P'): [
            'Village_Dynamic.TheWorld:PersistentLevel.Perch_52',
            ],
        ('Holy Spirits', 'Luckys_P'): [
            'Luckys_Dynamic.TheWorld:PersistentLevel.Perch_29',
            ],
        ('Sanctuary (Air)', 'SanctuaryAir_P'): [
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_11',
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_113',
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_126',
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_133',
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_151',
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_177',
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_182',
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_47',
            'SanctuaryAir_Combat.TheWorld:PersistentLevel.Perch_66',
            'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Perch_73',
            ],
        ('Sanctuary (Ground)', 'Sanctuary_P'): [
            'Sanctuary_Combat.TheWorld:PersistentLevel.Perch_11',
            'Sanctuary_Combat.TheWorld:PersistentLevel.Perch_113',
            'Sanctuary_Combat.TheWorld:PersistentLevel.Perch_126',
            'Sanctuary_Combat.TheWorld:PersistentLevel.Perch_133',
            'Sanctuary_Combat.TheWorld:PersistentLevel.Perch_151',
            'Sanctuary_Combat.TheWorld:PersistentLevel.Perch_182',
            'Sanctuary_Combat.TheWorld:PersistentLevel.Perch_47',
            'Sanctuary_Combat.TheWorld:PersistentLevel.Perch_66',
            'Sanctuary_Dynamic.TheWorld:PersistentLevel.Perch_73',
            ],
        ('Southern Shelf', 'SouthernShelf_P'): [
            'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Perch_102',
            'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Perch_37',
            ],
        }

alternate_perchdefs = [
        ('Arms Crossed', 'GD_NPCShared.Perches.Perch_NPC_ArmsCrossed'),
        ('Hands on Hips', 'GD_NPCShared.Perches.Perch_NPC_HandsOnHips'),
        ('Kick Ground', 'GD_NPCShared.Perches.Perch_NPC_KickGround'),
        ('Look at Ground', 'GD_NPCShared.Perches.Perch_NPC_LookAtGround'),
        ('Look Intently', 'GD_NPCShared.Perches.Perch_NPC_LookIntently'),
        ]

# Construct the mod
lines = []
lines.append('BL2')
lines.append('#<{}>'.format(mod_name))
lines.append('')
lines.append('    # {} v{}'.format(mod_name, mod_version))
lines.append('    # by Apocalyptech')
lines.append('    # Licensed under Public Domain / CC0 1.0 Universal')
lines.append('    #')
lines.append('    # Prevents NPCs from banging/knocking on walls, mostly in Sanctuary')
lines.append('    # but also in every other map where this behavior is found in the game')
lines.append('')
lines.append('    #<Choose Alternate NPC Stance><mut>')
lines.append('')

# First, provide a "random" option
lines.append('        #<Mixed-up Behaviors>')
lines.append('')
lines.append('            # This mixes up the Perches so that the idle behaviors will be a bit')
lines.append("            # more unpredictable.  It's not random -- the same locations will always")
lines.append('            # get the same behaviors, but it should mix things up a bit.')
lines.append('')
for ((mapname, maplevel), perches) in level_perches.items():
    lines.append('            #<{}>'.format(mapname))
    lines.append('')
    for perch in perches:
        lines.append("                level {} set {} PerchDef PerchDefinition'{}'".format(
            maplevel,
            perch,
            random.choice(alternate_perchdefs)[1],
            ))
        lines.append('')
    lines.append('            #</{}>'.format(mapname))
    lines.append('')
lines.append('        #</Mixed-up Behavior>')
lines.append('')
for (perch_desc, perchdef) in alternate_perchdefs:
    lines.append('        #<{}>'.format(perch_desc))
    lines.append('')
    for ((mapname, maplevel), perches) in level_perches.items():
        lines.append('            #<{}>'.format(mapname))
        lines.append('')
        for perch in perches:
            lines.append("                level {} set {} PerchDef PerchDefinition'{}'".format(
                maplevel,
                perch,
                perchdef,
                ))
            lines.append('')
        lines.append('            #</{}>'.format(mapname))
        lines.append('')
    lines.append('        #</{}>'.format(perch_desc))
    lines.append('')
lines.append('    #</Choose Alternate NPC Stance><mut>')
lines.append('')
lines.append('#</{}>'.format(mod_name))

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))
