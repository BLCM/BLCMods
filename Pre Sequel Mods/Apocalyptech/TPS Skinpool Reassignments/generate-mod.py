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
    from ftexplorer.data import Data
except ModuleNotFoundError:
    print('')
    print('****************************************************************')
    print('To run this script, you will need to copy or symlink the')
    print('"ftexplorer" and "resources" dirs from my ft-explorer project so')
    print('they exist here as well.  Sorry for the bother!')
    print('****************************************************************')
    print('')
    sys.exit(1)

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

mod_name = 'TPS Skinpool Reassignments'
mod_version = '1.0.0'
output_filename = '{}.txt'.format(mod_name)

###
### Processing the mod
###

data = Data('TPS')
hfs = Hotfixes()
free_count = 0
prefix = ' '*(2*4)
hotfix_output = []
saved_pools = []

for keyed in sorted(data.get_all_by_type('KeyedItemPoolDefinition')):
    structure = data.get_node_by_full_object(keyed).get_structure()
    for (bi_idx, item) in enumerate(structure['BalancedItems']):
        (junk, pool, junk2) = item['ItmPoolDefinition'].split("'")
        saved_pools.append(pool)
        innerpool = data.get_node_by_full_object(pool).get_structure()
        if len(innerpool['BalancedItems']) != 1:
            raise Exception('Inner pool {} has {} items'.format(pool, len(innerpool['BalancedItems'])))
        (junk, actualcustom, junk2) = innerpool['BalancedItems'][0]['InvBalanceDefinition'].split("'")

        # Hotfix to unlink the intermediate pool
        hf_id = 'unlink_{}'.format(free_count)
        hfs.add_level_hotfix(hf_id, 'TPSSkinpool',
            ',{},BalancedItems[{}].ItmPoolDefinition,,None'.format(
                keyed,
                bi_idx,
                ))
        hotfix_output.append('{}{}'.format(prefix, hfs.get_hotfix_xml(hf_id)))

        # And a hotfix to link to the actual skin/head
        hf_id = 'link_{}'.format(free_count)
        hfs.add_level_hotfix(hf_id, 'TPSSkinpool',
            """,{},BalancedItems[{}].InvBalanceDefinition,,
            InventoryBalanceDefinition'{}'""".format(
                keyed,
                bi_idx,
                actualcustom,
                ))
        hotfix_output.append('{}{}'.format(prefix, hfs.get_hotfix_xml(hf_id)))

        # Increment our counter
        free_count += 1

hotfix_str = "\n\n".join(hotfix_output)

###
### Generate the mod string
###

mod_str = """#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech (based on the BL2 UCP section with the same purpose)
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Frees up {free_count} skin/head pools for use by TPS mods.  This
    # is possible because the default skin/head pools use an effectively
    # unnecessary intermediate pool inbetween the pool that's actually
    # used for drops and the skins/heads themselves.  The BL2 UCP does
    # this and uses the resulting pools for custom boss drops, and
    # other mods do so as well.
    #
    # See https://github.com/BLCM/BLCMods/wiki/TPS-Custom-Skin-and-Head-Pool-Registry

    #<Skinpool Hotfixes>

{hotfix_str}

    #</Skinpool Hotfixes>

#</{mod_name}>""".format(
        mod_name=mod_name,
        mod_version=mod_version,
        free_count=free_count,
        hotfix_str=hotfix_str,
        )

###
### Output to a file.
###

with open(output_filename, 'w') as df:
    df.write(mod_str)
print('Wrote mod file to: {}'.format(output_filename))

###
### Also write out our list of saved pools to stderr, in a
### format we can just copy right to the BLCMods wiki.
###

if False:
    print('Pool Name | Used In', file=sys.stderr)
    print('--- | ---', file=sys.stderr)
    for pool in sorted(saved_pools):
        print('`{}` | '.format(pool), file=sys.stderr)
