#!/usr/bin/python3

from itertools import combinations

def pm(m, laenge):
  for r in range(0, laenge):
    print( m[r] )

from j import points

#1. 0-19
#2. 0-7
#3. 2-13
#4. 7-19

points = points.split("\n")

for i in range(0, len(points)):
  t = points[i].split(",")
  points[i] = [int(t[0]), int(t[1]), int(t[2])]

# points[0] = [162, 817, 812]

# Generate meshgrid (no duplicated pairs like [0,1]-[1,0] and same index pairs [0,0])
lst = []
for i, j in combinations(range(len(points)), 2):
  lst.append([[i, j], 0])


# Calculate all distances (lst = [[0, 19], 316.90219311326956])
for i in range(0, len(lst)):
  lst[i][1] = (
    (points[lst[i][0][0]][0]-points[lst[i][0][1]][0])**2 +
    (points[lst[i][0][0]][1]-points[lst[i][0][1]][1])**2 +
    (points[lst[i][0][0]][2]-points[lst[i][0][1]][2])**2
  )**0.5

lst.sort(key=lambda x: x[1])





# insert first one manually
trees = [
[ lst[0][0][0], lst[0][0][1] ]
]
connections = 1

counter = 10
for i in range(1, len(lst)):  
  circuits = [[], []]
  do_nothing = False
  for j in range(0, len(trees)):
    if ( lst[i][0][0] in trees[j] and lst[i][0][1] in trees[j] ):
      #print(f"Both points are in the same circuit: {j}")
      do_nothing = True
      break
    elif ( lst[i][0][0] in trees[j] ):
      #print(f"First point in circuit {j}")
      circuits[0].append(lst[i][0][1]) # Saving second point
      circuits[1].append(j)
    elif ( lst[i][0][1] in trees[j] ):
      #print(f"Second point in circuit {j}")
      circuits[0].append(lst[i][0][0]) # Saving first point
      circuits[1].append(j)
    else:
      pass
      ##print(f"Points not in specific circuit")
  if ( len(circuits[0]) == 0 and not(do_nothing)):
    #print(f"Creating new circuit {len(trees)} with both points")
    trees.append( [ lst[i][0][0], lst[i][0][1] ] )
    connections += 1
  elif( len(circuits[0]) == 1 ):
    #print(f"Moving point to circuit: {circuits[1][0]}")
    trees[ circuits[1][0] ].append( circuits[0][0] )
    connections += 1
  elif( len(circuits[0]) == 2 ):
    #print(f"Now we need to merge...{circuits[1]}")
    connections += 1
    if ( circuits[1][0] < circuits[1][1] ):
      trees[ circuits[1][0] ] += trees[ circuits[1][1] ]
      trees.pop( circuits[1][1] )
    else:
      trees[ circuits[1][1] ] += trees[ circuits[1][0] ]
      trees.pop( circuits[1][0] )
  else:
    #print(f"Both points are in the same tree")
    connections += 1 #????
    ##print(f"len circuit: {len(circuits[0])}")
  if (connections == 1000):
    break
  #print(f"connections: {connections}")

#trees.sort(key=lambda x: x[0], reverse=True)

# lst.sort(key=lambda x: len(x))
# sorted_lst = sorted(lst, key=lambda x: len(x))

trees.sort(key=len, reverse=True)
#print(trees)

print(len(trees[0]) * len(trees[1]) * len(trees[2]))

