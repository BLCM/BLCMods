#!/usr/bin/env python3
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

import os
import sys
import argparse

# Takes a source text file containing "expanded", easy-to-edit-by-hand-in-a-text-editor
# Borderlands mod definitions, and compresses them into a destination text file
# containing single "set" lines that are actually usable by Borderlands.
#
# For instance, the following could be a command in the easily-editable file:
#
#     set GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary BalancedItems
#     (
#         (
#             ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_07_LegendaryPlusPearl',
#             InvBalanceDefinition=None,
#             Probability=(
#                 BaseValueConstant=1.000000,
#                 BaseValueAttribute=None,
#                 InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',
#                 BaseValueScaleConstant=2.000000
#             ),
#             bDropOnDeath=True
#         )
#     )
#
# ... running this against the source file will generate the following:
#
#    set GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary BalancedItems ((ItmPoolDefinition=ItemPoolDefinition'GD_Gladiolus_Itempools.WeaponPools.Pool_Weapons_AssaultRifles_07_LegendaryPlusPearl',InvBalanceDefinition=None,Probability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=AttributeInitializationDefinition'GD_Balance.Weighting.Weight_1_Common',BaseValueScaleConstant=2.000000),bDropOnDeath=True))
#
# Note that this does NOT process "hotfix" type patches at all; it's only good
# for "set" style commands.
#
# The "source" filename used is expected to have a suffix of "-source.txt", and
# the utility will write to the same filename minus that suffix.  You can pass
# in either the destination or the source file and the utility will understand
# what to do with either.

parser = argparse.ArgumentParser(
    description='Converts human-editable Borderlands mod files into proper mod format',
    epilog='The source filename must have a suffix of "-source.txt", and the '
        'destination filename will have the same name minus that suffix.  The '
        '"filename" argument can be either the source or destination filename, '
        'and the utility should figure out what to do from there.'
    )
parser.add_argument('-f', '--force',
    action='store_true',
    help='Force overwriting the destination file')
parser.add_argument('filename', nargs=1)
args = parser.parse_args()

input_file = args.filename[0]
if input_file[-11:] == '-source.txt':
    source_file = input_file
    dest_file = input_file[:-11]
else:
    source_file = '{}-source.txt'.format(input_file)
    dest_file = input_file
print('Chosen source filename: {}'.format(source_file))
print('Chosen destination filename: {}'.format(dest_file))

# Check to make sure our source file exists
if not os.path.exists(source_file):
    print('File "{}" does not exist!'.format(source_file))
    sys.exit(1)

# Ask to overwrite if the dest file exists and we're not forcing
if os.path.exists(dest_file) and not args.force:
    user_resp = input('File "{}" exists already.  Overwrite it? [y|N] >'.format(dest_file))
    if len(user_resp) > 0 and user_resp[0].lower() == 'y':
        print('Continuing...')
    else:
        print('Exiting!')
        sys.exit(2)

# Now do the processing
print('Writing to "{}"'.format(dest_file))
with open(source_file, 'r') as df:
    with open(dest_file, 'w') as odf:
        in_set = False
        set_list = []
        for (linenum, line) in enumerate(df.readlines()):
            if in_set:
                line = line.strip()
                if line == '':
                    odf.write(''.join(set_list))
                    odf.write("\n\n")
                    in_set = False
                elif line[:4] == 'set ' or line[0] == '#':
                    raise Exception('Input file line {}: "set" statements should have an empty line after the end'.format(linenum))
                else:
                    set_list.append(line)
            elif line.lstrip()[:4] == 'set ' or line.lstrip()[:5] == '#set ':
                set_list = ['{} '.format(line.rstrip())]
                in_set = True
            else:
                odf.write(line)
        if in_set:
            odf.write(''.join(set_list))
            odf.write("\n\n")

# Report that we're done
print('Done!')
