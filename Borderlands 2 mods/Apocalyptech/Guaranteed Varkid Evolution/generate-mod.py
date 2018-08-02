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

# Python script to generate my Guaranteed Varkid Evolution Mod.

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

mod_name = 'Guaranteed Varkid Evolution'
mod_version = '1.1.0'
output_filename = '{}.blcm'.format(mod_name)

###
### Generate hotfixes!
###

for morph in range(1,6):
    mp.register_str('varkid_clear_{}'.format(morph),
        'level None set GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase{} ConditionalInitialization.ConditionalExpressionList ()'.format(morph))
    mp.register_str('varkid_default_{}'.format(morph),
        'level None set GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase{} ConditionalInitialization.DefaultBaseValue.BaseValueConstant 1.0'.format(morph))

###
### Generate the mod string
###

mod_str = """BL2
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Guarantees evolution of all varkids, regardless of playthrough or
    # player count.  Leave one alive and you'll get Vermivorous eventually.

    {mp:varkid_clear_1}

    {mp:varkid_clear_2}

    {mp:varkid_clear_3}

    {mp:varkid_clear_4}

    {mp:varkid_clear_5}

    {mp:varkid_default_1}

    {mp:varkid_default_2}

    {mp:varkid_default_3}

    {mp:varkid_default_4}

    {mp:varkid_default_5}

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        mp=mp,
        )

###
### Output to a file.
###

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
