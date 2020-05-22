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

try:
    from ftexplorer.data import Data
except ModuleNotFoundError:
    print('')
    print('********************************************************************')
    print('To run this script, you will need to copy or symlink the')
    print('"ftexplorer" and "resources" dirs from my ft-explorer project so')
    print('they exist here as well.  Sorry for the bother!')
    print('********************************************************************')
    print('')
    sys.exit(1)

# Control Vars
mod_name = 'TPS Sorted Fast Travel'
mod_version = '1.0.0'
output_filename = '{}.blcm'.format(mod_name)

data = Data('TPS')
ftdefs = data.get_all_by_type('FastTravelStationDefinition')

# Construct the mod
lines = []
lines.append('TPS')
lines.append('#<{}>'.format(mod_name))
lines.append('')
lines.append('    # {} v{}'.format(mod_name, mod_version))
lines.append('    # by Apocalyptech')
lines.append('    # Licensed under Public Domain / CC0 1.0 Universal')
lines.append('    #')
lines.append('    # Sorts the Fast Travel menu alphabetically by default, and removes')
lines.append('    # the prefix "The" from all fast travel names, so they also sort')
lines.append('    # *correctly.*')
lines.append('')
lines.append('    #<Alphabetical By Default>')
lines.append('')
lines.append('        # Many thanks to Our Lord and Savior Gabe Newell for this!')
lines.append('')
lines.append('        set FastTravelStationGFxMovie SortMode 1')
lines.append('')
lines.append('    #</Alphabetical By Default>')
lines.append('')
lines.append('    #<Remove Level Prefixes>')
lines.append('')
for ftdef in ftdefs:
    ft = data.get_struct_by_full_object(ftdef)
    if ft['StationDisplayName'].startswith('The '):
        lines.append('        set {} StationDisplayName {}'.format(
            ftdef,
            ft['StationDisplayName'][4:],
            ))
        lines.append('')
lines.append('    #</Remove Level Prefixes>')
lines.append('')
lines.append('#</{}>'.format(mod_name))

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))
