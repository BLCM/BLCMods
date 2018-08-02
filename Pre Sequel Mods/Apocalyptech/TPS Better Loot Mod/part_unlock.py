#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# This generates a bunch of hotfixes to unlock all weapon/item parts (at least those
# contained in *PartListCollectionDefinition objects, via ConsolidatedAttributeInitData
# structures) available from the beginning of the game.  The hotfixes just touch
# the ConsolidatedAttributeInitData structure itself.  Intended to be run from
# ft-explorer's homedir, since we're using that to get some handy structured data for
# the objects we're interested in.
#
# Note that ft-explorer does *not* give us any handy way to retrieve all objects by
# type, so we're actually looping through a couple files and looking for object names
# that way, which is a bit lame, but whatever.

import re
import sys
import lzma
from ftexplorer.data import Data

data = Data('TPS')

filenames = [
        'resources/TPS/dumps/WeaponPartListCollectionDefinition.dump.xz',
        'resources/TPS/dumps/ItemPartListCollectionDefinition.dump.xz',
    ]

part_hotfix_idx = 0
for filename in filenames:
    with lzma.open(filename, 'rt', encoding='latin1') as df:
        for line in df.readlines():
            match = re.match(r"^\*\*\* Property dump for object '\S+ (\S+)' \*\*\*", line)
            if match:
                obj_name = match.group(1)
                struct = data.get_node_by_full_object(obj_name).get_structure()

                if 'ConsolidatedAttributeInitData' not in struct:
                    # Should maybe keep track of which of these doesn't have it...
                    continue

                # Figure out our caid values
                caid = struct['ConsolidatedAttributeInitData']
                caid_values = []
                for caid_val in caid:
                    caid_values.append(float(caid_val['BaseValueConstant']))

                # Now loop through all our items.
                caid_updates = set()
                for key, val in struct.items():
                    if key[-8:] == 'PartData':
                        for part in val['WeightedParts']:
                            min_stage_idx = int(part['MinGameStageIndex'])
                            if caid_values[min_stage_idx] > 1:
                                caid_updates.add(min_stage_idx)

                # Update, if need be!
                if len(caid_updates) > 0:
                    #print('Updating the following in {}:'.format(obj_name))
                    for idx in caid_updates:
                        #print(' * {}: {}'.format(idx, caid_values[idx]))
                        print("hfs.add_level_hotfix('part_unlock_{}', 'PartUnlock',".format(part_hotfix_idx))
                        print("    ',{},ConsolidatedAttributeInitData[{}].BaseValueConstant,,1')".format(obj_name, idx))
                        print('            {{hotfixes:part_unlock_{}}}'.format(part_hotfix_idx), file=sys.stderr)
                        print('', file=sys.stderr)
                        part_hotfix_idx += 1
