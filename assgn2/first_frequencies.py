#!usr/bin/env python3

import sys

freq_table = {}
total_count = 0
for line in sys.stdin:
  first_char = line[0]
  if not first_char in freq_table:
    freq_table[first_char] = 0
  freq_table[first_char] += 1
  total_count += 1

for key in freq_table.keys():
  freq_table[key] = float(freq_table[key])/total_count

print(freq_table)
