#!/usr/bin/python3

from itertools import combinations
from j import xy

def pm(m, l):
  for i in range(0, l):
    print(m[i])

xy = xy.split("\n")

for i in range(0, len(xy)):
  t = xy[i].split(",")
  xy[i] = [int(t[0]), int(t[1])]

# Generate meshgrid (no duplicated pairs like [0,1]-[1,0] and same index pairs [0,0])
lst = [] #[[0, 1], 0]
for i, j in combinations(range(len(xy)), 2):
  lst.append([[i, j], 0])

# Generate area
'''
..............
..AAAAA#...#.. (7,1)
..AAAAAA......
..#AAAA#...... (2,3)
..............    --> 6 * 3
..#......#....
..............
.........#.#..
..............
'''

for i in range(0, len(lst)):
  # Skip if x or y the same, to small rectangle
  if ( xy[lst[i][0][0]][0] == xy[lst[i][0][1]][0] or xy[lst[i][0][0]][1] == xy[lst[i][0][1]][1] ):
    continue
  # Calc area
  a = (abs(xy[lst[i][0][0]][0] - xy[lst[i][0][1]][0]) + 1) * ( abs( xy[lst[i][0][0]][1] - xy[lst[i][0][1]][1] ) + 1)
  #print(f"calc {a}")
  lst[i][1] = a

lst.sort(key=lambda x: x[1], reverse=True)

pm(lst, 5)


