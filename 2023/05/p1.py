# from ACutils.utils import read_input_to_list_of_strings

# from typing import List, Tuple, Dict

# def contains_any_letters(s: str):
#     return any(c.isalpha() for c in s)

# def get_full_map(input: List[str]) -> Dict[str, List[Tuple[int, int, int]]]:
#     result = {}
#     current_map = ""
#     for line in input:
#         if not line:
#             current_map = ""
#             continue
#         if contains_any_letters(line):
#             current_map = line.split(' ')[0]
#             continue
#         numbers = line.split(' ')
#         try:
#             result[current_map].append((int(numbers[0]), int(numbers[1]), int(numbers[2])))
#         except KeyError:
#             result[current_map] = [(int(numbers[0]), int(numbers[1]), int(numbers[2]))]
#     return result

# def get_this_map(inp: List[Tuple[int, int, int]]) -> Dict[int, int]:
#     for mapping in inp:

# def main():
#     input = read_input_to_list_of_strings("test.txt")
#     seeds = [int(seed) for seed in input[0].split(' ')[1:]]
#     #print(seeds)

#     the_map = get_full_map(input)
#    # print(the_map)
#     result = []
#     for seed in seeds:
#         print("Seed ", seed, end="")
#         tmp = seed
#         for map_name, map_list in the_map.items():
#             for mapping in map_list:
#                 if tmp not in range(mapping[1], mapping[1] + mapping[2]):
#                     print("map_name ", map_name, end="")
#                     continue
#                 diff = tmp - mapping[1]
#                 tmp = mapping[0] + diff
#                 print("map_name ", map_name, end="")

#         result.append(tmp)
    
#     print(result)
#     print("result: {}".format(min(result)))


# main()


import sys
import re
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

class Function:
  def __init__(self, S):
    lines = S.split('\n')[1:] # throw away name
    # dst src sz
    self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    #print(self.tuples)
  def apply_one(self, x: int) -> int:
    for (dst, src, sz) in self.tuples:
      if src<=x<src+sz:
        return x+dst-src
    return x

  # list of [start, end) ranges
  def apply_range(self, R):
    A = []
    for (dest, src, sz) in self.tuples:
      src_end = src+sz
      NR = []
      while R:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = R.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,src))
        inter = (max(st, src), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          NR.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-src+dest, inter[1]-src+dest))
        if after[1]>after[0]:
          NR.append(after)
      R = NR
    return A+R

Fs = [Function(s) for s in others]

def f(R, o):
  A = []
  for line in o:
    dest,src,sz = [int(x) for x in line.split()]
    src_end = src+sz

P1 = []
for x in seed:
  for f in Fs:
    x = f.apply_one(x)
  P1.append(x)
print(min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R = [(st, st+sz)]
  for f in Fs:
    R = f.apply_range(R)
  #print(len(R))
  P2.append(min(R)[0])
print(min(P2))