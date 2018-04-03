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

# Given some data dumps, loop through and find out what maps contain which
# trap containers.  This "stupid" version just loops through and uses regex,
# as oppposed to the non-stupid version which uses ft-explorer data, but this
# version has the benefit of being about a million times faster.

import os
import re
import sys
import lzma

cur_level = None
level_traps = {}
files = ['PopulationOpportunityPoint.dump.xz', 'WillowPopulationOpportunityPoint.dump.xz']
for filename in files:
    with lzma.open(filename, 'rt') as df:
        for line in df.readlines():
            match = re.match('.*Property dump for object \'\w+ (\w+)\..*', line)
            if match:
                cur_level = match.group(1).lower()
                if cur_level not in level_traps:
                    level_traps[cur_level] = set()
            else:
                if cur_level:
                    match = re.match('.*PopulationDef=PopulationDefinition\'(.*)\'.*', line)
                    if match:
                        popdef = match.group(1)
                        if 'Trap' in popdef:
                            level_traps[cur_level].add(popdef)

for levelname, traps in sorted(level_traps.items()):
    if len(traps) > 0:
        print(levelname)
        for trap in traps:
            print(' * {}'.format(trap))
        print('')
