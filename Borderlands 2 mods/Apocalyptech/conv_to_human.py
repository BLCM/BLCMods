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

import io
import re
import os
import sys
import codecs
import argparse

# Takes input from either a Borderlands mod file (FT or BLCMM format), or from
# the output of an "obj dump <foo>" from Borderlands' console, and converts it into
# a multiline version which is much easier to both parse and edit by humans.  For
# FT and BLCMM files, this *should* result in a file which is very close to my
# own custom mod format, which modprocessor.py uses to create BLCMM files.  As
# this tool is mostly only concerned with making things look Good Enough for
# humans, I'm not taking the time to make it be 100% compatible with modprocessor.py,
# though.
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

def newline(df_out, cur_indent, extra_indent):
    """
    Output a newline, with the appropriate amount of whitespace at the
    beginning of the next line so that our indentation looks good.
    """
    df_out.write("\n")
    df_out.write(cur_indent)
    df_out.write('    '*extra_indent)

def indent(indent_level):
    """
    Returns the appropriate number of spaces for the given indent level
    """
    return ' '*(4*indent_level)

def process_line(line, df_out, indices=False):
    """
    Takes a single line contianing some BL structural data and turn it into
    a nicely-human-formatted multiline statement, writing to df_out
    """

    on_first_line = True
    at_beginning = True
    cur_indent = ''
    extra_indent = 0

    array_indicies = [0]

    for char in line:

        if at_beginning:
            if char == ' ':
                df_out.write(char)
                cur_indent += char
                continue
            else:
                at_beginning = False

        if char == '(':
            this_index = array_indicies[-1]
            array_indicies[-1] += 1
            array_indicies.append(0)
            if on_first_line:
                newline(df_out, cur_indent, extra_indent)
            if indices:
                df_out.write('{} // {}'.format(char, this_index))
            else:
                df_out.write(char)
            extra_indent += 1
            newline(df_out, cur_indent, extra_indent)
            on_first_line = False
        elif char == ')':
            array_indicies.pop()
            if extra_indent > 0:
                extra_indent -= 1
            newline(df_out, cur_indent, extra_indent)
            on_first_line = False
            df_out.write(char)
        elif char == ',':
            df_out.write(char)
            newline(df_out, cur_indent, extra_indent)
            on_first_line = False
        else:
            df_out.write(char)

class Hotfix(object):

    (PATCH, LEVEL, DEMAND) = range(3)

    def __init__(self, hf_type, value_str=None, enabled=True,
            object_name=None, attr_name=None, val_old=None, val_new=None,
            condition=None,
            initial_whitespace=''):
        """
        Construct a hotfix.  There's intended to be two ways to call this - either
        supply `value_str`, which is the native Borderlands value of the hotfix, or
        specify `object_name`, `attr_name`, and `val_new` (and optionally `val_old`)
        """
        self.hf_type = hf_type
        self.enabled = enabled
        if enabled:
            self.enabled_str = ''
        else:
            self.enabled_str = '#'
        self.initial_whitespace = initial_whitespace
        if value_str and value_str != '':
            if self.hf_type == Hotfix.PATCH:
                (object_name, attr_name, val_old, val_new) = value_str.split(',', 3)
                self.prefix = 'patch'
            else:
                (condition, object_name, attr_name, val_old, val_new) = value_str.split(',', 4)
        self.prefix = Hotfix.get_prefix(self.hf_type, condition)
        self.object_name = object_name
        self.attr_name = attr_name
        self.val_old = val_old
        self.val_new = val_new

    @staticmethod
    def get_prefix(hf_type, condition=None):
        if hf_type == Hotfix.LEVEL:
            return 'level {}'.format(condition)
        elif hf_type == Hotfix.DEMAND:
            return 'demand {}'.format(condition)
        else:
            return 'patch'

    def write_human(self, df_out):
        if self.val_old and self.val_old != '':
            process_line("{}{}{} set_cmp {} {} {} {}\n".format(
                    self.initial_whitespace,
                    self.enabled_str,
                    self.prefix,
                    self.object_name,
                    self.attr_name,
                    self.val_old,
                    self.val_new,
                    ), df_out)
        else:
            process_line("{}{}{} set {} {} {}\n".format(
                    self.initial_whitespace,
                    self.enabled_str,
                    self.prefix,
                    self.object_name,
                    self.attr_name,
                    self.val_new,
                    ), df_out)

    @staticmethod
    def check_ft_hotfix(line):
        """
        Checks the given line to see if it's an old-style FT hotfix.  If so, return
        a Hotfix object.  Otherwise returns None
        """
        match = re.match('^(\s*)#<hotfix><key>"Spark(.*?)Entry-.*?"<\/key><value>"(.*?)"</value><(o(n|ff))>\s*$', line)
        if match:
            type_str = match.group(2)
            if type_str == 'Patch':
                type_val = Hotfix.PATCH
            elif type_str == 'LevelPatch':
                type_val = Hotfix.LEVEL
            elif type_str == 'OnDemandPatch':
                type_val = Hotfix.DEMAND
            else:
                raise Exception('Unknown hotfix type string: {}'.format(type_str))
            value_str = match.group(3)
            if match.group(4) == 'on':
                enabled = True
            elif match.group(4) == 'off':
                enabled = False
            else:
                raise Exception('Unknown activation state: {}'.format(match.group(4)))
            return Hotfix(type_val, value_str=value_str, enabled=enabled, initial_whitespace=match.group(1))
        else:
            return None

def process_plain(df_in, df_out, indices=False):
    """
    Process what looks like a plain text file - could be some `obj dump` output
    from console logs, or whatever.
    """

    # Loop through and process
    for line in df_in.readlines():

        stripped = line.lstrip()

        # Attempt to parse any hotfixes
        hf = Hotfix.check_ft_hotfix(line)
        if hf:
            hf.write_human(df_out)

        # If we've got an empty line, just print it out
        elif len(stripped) == 0:
            df_out.write(line)

        # Commented `set` or `set_cmp` commands should get processed
        elif stripped.startswith('#set ') or stripped.startswith('#set_cmp '):
            process_line(line, df_out, indices)

        # Ignore anything else commented
        elif stripped[0] == '#':
            df_out.write(line)

        # Don't write out end-of-file hotfix stuff at all
        elif 'set Transient.SparkServiceConfiguration' in line:
            pass

        # Aaand finally, go ahead and try to process anything else we see.
        else:
            process_line(line, df_out, indices)

def process_ft(df_in, df_out, indices=False):
    """
    Process what looks like a FT file.  Mostly this is identical to the plain
    processing, though we're going to add in an "unknown" file type at the top.
    """

    # We're not going to bother trying to guess the patch type
    print('(type unknown)', file=df_out)

    # Now just do the plain processing
    process_plain(df_in, df_out)

def process_blcmm(df_in, df_out, indices=False):
    """
    Process a file which looks like a BLCMM file.
    """
    file_type = None
    line = df_in.readline()
    while '<body>' not in line:
        match = re.search('type name="(.*?)"', line)
        if match:
            file_type = match.group(1)
        line = df_in.readline()
    if not file_type:
        raise Exception('File type not found in BLCMM header')
    print(file_type, file=df_out)
    in_comments = False
    in_hotfix = ''
    in_mut = False
    mut_start_level = 0
    indent_level = 0
    category_list = []
    line = df_in.readline()
    while '</body>' not in line and '</BLCMM>' not in line:
        if '<category ' in line:
            match = re.search('<category name="(.*?)"( MUT="true")?( locked="true")?>', line)
            if match:
                cat_name = match.group(1)
                mut = match.group(2) and match.group(2) != ''
                lock = match.group(3) and match.group(3) != ''
                if mut:
                    mut_str = '<MUT>'
                    if not in_mut:
                        in_mut = True
                        mut_start_level = len(category_list)
                else:
                    mut_str = ''
                if lock:
                    lock_str = '<lock>'
                else:
                    lock_str = ''
                if in_comments:
                    print('', file=df_out)
                    in_comments = False
                print('{}#<{}>{}{}'.format(
                    indent(indent_level),
                    cat_name,
                    mut_str,
                    lock_str,
                    ), file=df_out)
                print('', file=df_out)
                indent_level += 1
                category_list.append(cat_name)
            else:
                raise Exception('Could not parse category line: {}'.format(line))
        elif '</category>' in line:
            cat_name = category_list.pop()
            if in_mut and len(category_list) == mut_start_level:
                in_mut = False
                mut_start_level = 0
            indent_level -= 1
            if indent_level < 0:
                indent_level = 0
            if in_comments:
                print('', file=df_out)
                in_comments = False
            print('{}#</{}>'.format(
                indent(indent_level),
                cat_name,
                ), file=df_out)
            print('', file=df_out)
        elif '<comment>' in line:
            match = re.search('<comment>(.*)</comment>', line)
            if match:
                in_comments = True
                print('{}{}'.format(
                    indent(indent_level),
                    match.group(1),
                    ))
            else:
                raise Exception('Could not parse comment line: {}'.format(line))
        elif '<hotfix ' in line:
            match = re.search('<hotfix name=".*?"( level="(.*?)")?( package="(.*?)")?>', line)
            if match:
                if match.group(1) and match.group(1) != '':
                    hf_type = Hotfix.LEVEL
                    condition = match.group(2)
                elif match.group(3) and match.group(3) != '':
                    hf_type = Hotfix.DEMAND
                    condition = match.group(4)
                else:
                    hf_type = Hotfix.PATCH
                    condition = None
                in_hotfix = '{} '.format(Hotfix.get_prefix(hf_type, condition))
            else:
                raise Exception('Could not parse hotfix line: {}'.format(line))
        elif '</hotfix>' in line:
            in_hotfix = ''
        elif '<code ' in line:
            match = re.search('<code profiles="(.*?)">(.*?)</code>', line)
            if match:
                # If we're in a MUT category, never explicitly disable anything
                if (in_mut or (match.group(1) and match.group(1) != '')):
                    enabled = True
                    enabled_str = ''
                else:
                    enabled = False
                    enabled_str = '#'
                if in_comments:
                    print('', file=df_out)
                    in_comments = False
                process_line("{}{}{}{}\n".format(
                        indent(indent_level),
                        enabled_str,
                        in_hotfix,
                        match.group(2),
                        ), df_out, indices)
                print('', file=df_out)
            else:
                raise Exception('Could not parse code line: {}'.format(line))
        else:
            raise Exception('Unknown line: {}'.format(line))
        line = df_in.readline()

# Now the interactive code
if __name__ == '__main__':

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
    parser.add_argument('-i', '--indices',
        action='store_true',
        help='Output indicies in arrays (useful in things like BPDs)')
    parser.add_argument('-p', '--prompt',
        action='store_true',
        help='Prompt for text to format in a loop (everything will be STDIN/STDOUT)')
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

    # Process interactively, if told to
    if args.prompt:
        while True:
            sys.stdout.write('input> ')
            sys.stdout.flush()
            idf = io.StringIO(sys.stdin.readline())
            print('')
            try:
                process_plain(idf, sys.stdout, args.indices)
            except Exception as e:
                print('')
                print('Exception: {}'.format(str(e)))
            print('')

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

    # Open our input filehandle, if we have to
    if using_std_input:
        df_in = codecs.getreader('latin1')(sys.stdin.detach())
    else:
        df_in = open(args.input, 'r', encoding='latin1')

    # Read in the entire input file so that we can do stuff like seek() even
    # if it's stdin
    indata = df_in.read()
    if not using_std_input:
        df_in.close()
    df_in = io.StringIO(indata)

    # Open our output filehandle, if we have to
    if using_std_output:
        df_out = sys.stdout
    else:
        df_out = open(args.output, 'w')

    # Figure out what kind of file we're using here.  This is a pretty sledgehammery
    # approach, which may fail on various of the old-style FilterTool files, but
    # should be good enough, especially given that there's really no difference between
    # how we process FT-style files and just plaintext.
    first_line = df_in.readline()
    df_in.seek(0)
    if '<BLCMM' in first_line:
        process_blcmm(df_in, df_out, args.indices)
    elif '#<' in first_line:
        process_ft(df_in, df_out, args.indices)
    else:
        process_plain(df_in, df_out, args.indices)

    # Report, and close output filehandle if needed
    if using_std_output:
        print('Done!', file=sys.stderr)
    else:
        df_out.close()
        print('Wrote output to "{}"'.format(args.output))
