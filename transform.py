#!/usr/bin/env python
# coding: utf-8

import re
import json

match_table = {}
with open("mapping_table.json") as json_file:
    match_table = json.load(json_file)

# the dict
map_table = lambda x: match_table[x] if x in match_table.keys() else x 

# the map function
maps = lambda s: ''.join(x for x in map(map_table,s))

import re
with open('new_array30.dict.yaml', 'w') as f:
    # read
    with open("array30.dict.yaml") as data:
        for idx, row in enumerate(data.readlines()):
            # start from col 13
            if idx >= 13:
                split = row.split("\t")
                
                f.write("%s\t%s" % (split[0], maps(split[1]) ) )
            else:
                f.write(row)

