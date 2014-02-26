#!usr/bin/env python3

import json
import sys

with open("first_freq_json") as f:
  init_model = json.load(f)
with open("diagram_freq_json") as f:
  trans_model = json.load(f)
with open("total_freq_json") as f:
  emission_model = json.load(f)

START = 'START'
states = ["S", "T"]

def new_map():
  return {}

def replace(var):
  if var == "S":
    return "s"
  return "t"

for seq in sys.stdin:
  seq = seq.rstrip()
  assert(len(seq) >= 1)
  v = []
  pointer = []
  v.append(new_map())
  v[0][START] = 1

  v.append(new_map())
  last = seq[0]
  for s in states:
    current = last+s
    v[-1][current] = emission_model[current]*init_model[s]

  print(v)

  for obs in seq[1:]:
    v.append(new_map())
    pointer.append(new_map())
    for s in states:
      current = obs+s
      v[-1][current] = 0
      for (key, value) in v[-2].items():
        compare = emission_model[current]*value*trans_model[s+key[1]]
        if compare > v[-1][current]:
          v[-1][current] = compare
          pointer[-1][current] = key

  currentMax = 0
  currentMaxKey = None
  for (key, value) in v[-1].items():
    if value > currentMax:
      currentMax = value
      currentMaxKey = key

  MLS = currentMaxKey[0]+replace(currentMaxKey[1])
  for i in range(len(pointer)-1, -1, -1):
    nextKey = pointer[i][currentMaxKey]
    MLS = nextKey[0]+replace(nextKey[1]) + MLS
    currentMaxKey = nextKey
  print(" ".join(seq))
  print(MLS,"\n")

