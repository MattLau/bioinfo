#!usr/bin/env python3

import sys
import json

freq_table = {}
total_count = 0
for line in open("soluble_sequences", "r"):
  string = line.strip()
  for letter in string:
    letter = letter + "S"
    if not letter in freq_table:
      freq_table[letter] = 0
    freq_table[letter] += 1
    total_count += 1

for line in open("transmembrane_sequences", "r"):
  string = line.strip()
  for letter in string:
    letter = letter + "T"
    if not letter in freq_table:
      freq_table[letter] = 0
    freq_table[letter] += 1
    total_count += 1

for key in freq_table.keys():
  freq_table[key] = float(freq_table[key])/total_count

with open("total_freq_json", "w") as out:
  json.dump(freq_table, out)

