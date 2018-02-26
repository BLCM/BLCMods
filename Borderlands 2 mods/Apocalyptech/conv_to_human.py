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

# Takes input from either a Borderlands mod file, or from the output
# of an "obj dump <foo>" from Borderlands' console, and converts it into
# a multiline version which is much easier to both parse and edit by humans.
#
# For instance, a file with a line like the following:
#
# BalancedItems(0)=(ItmPoolDefinition=None,InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Vitality_Rare',Probability=(BaseValueConstant=1.000000,BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000),bDropOnDeath=True)
#
# ... would be converted to this:
#
#     BalancedItems(
#         0
#     )=(
#         ItmPoolDefinition=None,
#         InvBalanceDefinition=InventoryBalanceDefinition'GD_Artifacts.A_Item.A_Vitality_Rare',
#         Probability=(
#             BaseValueConstant=1.000000,
#             BaseValueAttribute=None,
#             InitializationDefinition=None,
#             BaseValueScaleConstant=1.000000
#         ),
#         bDropOnDeath=True
#     )
#
# By default both the source and the output files will be stdin/stdout, but
# you can specify filenames instead.
#
# This utility does not actually understand hotfix-style modding, but should
# theoretically leave those statements alone.

parser = argparse.ArgumentParser(
    description='Converts single-line Borderlands mod/console statements to multiline',
    epilog='By default, both input and output files are stdin/stdout, but arbitrary '
        'filenames can be used instead.  Substitute "-" for either to continue to use '
        'stdin/stdout, if required.  Ignores any commented lines in the file.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
parser.add_argument('-f', '--force',
    action='store_true',
    help='Force overwriting the output file')
parser.add_argument('input',
    nargs='?',
    help='Input filename; specify "-" for STDIN',
    default='-',
    )
parser.add_argument('output',
    nargs='?',
    help='Output filename; specify "-" for STDOUT',
    default='-',
    )
args = parser.parse_args()

# Check our input
if args.input == '-':
    using_std_input = True
else:
    using_std_input = False
    if not os.path.exists(args.input):
        print('File "{}" does not exist!'.format(args.input), file=sys.stderr)
        sys.exit(1)

# Check our output
if args.output == '-':
    using_std_output = True
else:
    using_std_output = False
    if os.path.exists(args.output) and not args.force:
        if using_std_input:
            print('ERROR: Output file "{}" already exists, but we can\'t ask for overwrite')
            print('confirmation because STDIN is being used for the input file.  Specify')
            print('-f or --force to force this overwrite.')
            sys.exit(3)
        user_resp = input('File "{}" exists already.  Overwrite it? [y|N] >'.format(args.output))
        if len(user_resp) > 0 and user_resp[0].lower() == 'y':
            print('Continuing...')
        else:
            print('Exiting!')
            sys.exit(2)

# Now continue on!

def newline():
    """
    Output a newline, with the appropriate amount of whitespace at the
    beginning of the next line so that our indentation looks good.
    """
    global df_out
    global cur_indent
    global extra_indent
    df_out.write("\n")
    df_out.write(cur_indent)
    df_out.write('    '*extra_indent)

# Open our input filehandle, if we have to
if using_std_input:
    df_in = sys.stdin
else:
    df_in = open(args.input, 'r')

# Open our output filehandle, if we have to
if using_std_output:
    df_out = sys.stdout
else:
    df_out = open(args.output, 'w')

# Now loop through and process
for line in df_in.readlines():

    if len(line.lstrip()) > 0 and line.lstrip()[0] == '#':
        df_out.write(line)

    elif '<hotfix>' in line or 'SparkServiceConfiguration' in line:
        df_out.write(line)

    else:
        at_beginning = True
        cur_indent = ''
        extra_indent = 0

        for char in line:

            if at_beginning:
                if char == ' ':
                    df_out.write(char)
                    cur_indent += char
                    continue
                else:
                    at_beginning = False

            if char == '(':
                df_out.write(char)
                extra_indent += 1
                newline()
            elif char == ')':
                if extra_indent > 0:
                    extra_indent -= 1
                newline()
                df_out.write(char)
            elif char == ',':
                df_out.write(char)
                newline()
            else:
                df_out.write(char)

# Close input filehandle if needed
if not using_std_input:
    df_in.close()

# Report, and close output filehandle if needed
if using_std_output:
    print('Done!', file=sys.stderr)
else:
    df_out.close()
    print('Wrote output to "{}"'.format(args.output))

