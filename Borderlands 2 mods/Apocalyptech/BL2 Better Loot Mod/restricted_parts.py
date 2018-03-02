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
                print('            set {classname} {propertyname} (bEnabled={enabled},WeightedParts={final_weight_text})'.format(
                    classname=cur_partlist,
                    propertyname=data_type,
                    enabled=enabled,
                    final_weight_text=final_weight_text,
                    ))
                print('')
