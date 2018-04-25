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

mod_name = 'Guaranteed Varkid Evolution'
mod_version = '1.0.2'
output_filename = '{}.txt'.format(mod_name)

###
### Generate hotfixes!
###

hfs = Hotfixes()

for morph in range(1,6):
    hfs.add_level_hotfix('varkid_clear_{}'.format(morph),
        'VarkidMorphClear',
        ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase{},ConditionalInitialization.ConditionalExpressionList,,()'.format(morph))
    hfs.add_level_hotfix('varkid_default_{}'.format(morph),
        'VarkidMorphDefault',
        ',GD_Balance.WeightingPlayerCount.BugmorphCocoon_PerPlayers_Phase{},ConditionalInitialization.DefaultBaseValue.BaseValueConstant,,1.0'.format(morph))

###
### Generate the mod string
###

mod_str = """#<{mod_name}>

    # {mod_name} v{mod_version}
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Guarantees evolution of all varkids, regardless of playthrough or
    # player count.  Leave one alive and you'll get Vermivorous eventually.

    {hotfixes:varkid_clear_1}

    {hotfixes:varkid_clear_2}

    {hotfixes:varkid_clear_3}

    {hotfixes:varkid_clear_4}

    {hotfixes:varkid_clear_5}

    {hotfixes:varkid_default_1}

    {hotfixes:varkid_default_2}

    {hotfixes:varkid_default_3}

    {hotfixes:varkid_default_4}

    {hotfixes:varkid_default_5}

#</{mod_name}>
""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        hotfixes=hfs,
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))
