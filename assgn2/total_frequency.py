#!usr/bin/env python3

import sys

freq_table = {}
total_count = 0
for line in sys.stdin:
  string = line.strip()
  for letter in string:
    if not letter in freq_table:
      freq_table[letter] = 0
    freq_table[letter] += 1
    total_count += 1

for key in freq_table.keys():
  freq_table[key] = float(freq_table[key])/total_count
print(freq_table)
