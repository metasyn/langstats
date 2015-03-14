#!/bin/python
# xander johnson @metasyn

import json
import re

# read in data
with open('./ethnologue.txt', 'r') as f:
	data = f.readlines()
f.close()

children = []
for line in data[1:]:
	lang_dict={}
	splits = line.split('(')
	lang_dict["name"] = splits[0].strip()
	lang_dict["size"] = splits[1][:-2]
	children.append(lang_dict)

flare = {
	"name": "flare",
	"children": children
}

with open('numlangs.json', 'wb') as fp:
	json.dump(flare, fp)

with open('./stats.txt', 'r') as f:
	stats = f.readlines()
f.close()

regex = ur"""
(?P<num>\d+)?
\s+
(?P<family>[a-z\-A-Z]+)
\,?\s
(?P<variety>[^\[]+\s?)?
\s?
(?:\[)
(?P<code>\w+)
(?:\])
\t
(?P<location>[a-zA-Z]+\s?[a-zA-Z]+)
\t
(?P<total_countries>\d+)
\s+
(?P<speakers>[\d\.\,]+)
"""

main={}
for line in stats:
	stats_extract = re.findall(regex, line, re.X)
	for n in range(len(stats_extract[0])):
		main[n]=stats_extract[n]