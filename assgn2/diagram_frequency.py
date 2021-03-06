#!usr/bin/env python3

import sys
import json

freq_table = {}
total_count = 0
for line in sys.stdin:
  string = line.strip()
  last = None
  for letter in string:
    if last != None:
      current = last + letter
      if not current in freq_table:
        freq_table[current] = 0
      freq_table[current] += 1
      total_count += 1
    last = letter

for key in freq_table.keys():
  freq_table[key] = float(freq_table[key])/total_count

with open("diagram_freq_json", "w") as out:
  json.dump(freq_table, out)
