#!/usr/bin/python3

from itertools import combinations
from j import xy

def plot(xy):
  f = open('points.txt', 'w')
  for i in range(0, len(xy)):
    f.write(f"{xy[i][0]}  {xy[i][1]}\n")
  f.close()

def pm(m, l):
  for i in range(0, l):
    print(m[i])

xy = xy.split("\n")

# Make int
for i in range(0, len(xy)):
  t = xy[i].split(",")
  xy[i] = [int(t[0]), int(t[1])] # [2 3]


# Finding ranges
xrange = [xy[0][0], xy[0][0]]
yrange = [xy[0][1], xy[0][1]]

for i in range(0, len(xy)):
  # Checking x
  if (xy[i][0] < xrange[0]):
    xrange[0] = xy[i][0]
  if (xy[i][0] > xrange[1]):
    xrange[1] = xy[i][0]
  
  # Checking y
  if (xy[i][1] < yrange[0]):
    yrange[0] = xy[i][1]
  if (xy[i][1] > yrange[1]):
    yrange[1] = xy[i][1]

#print(f"xrange: {xrange}")
#print(f"yrange: {yrange}")

# Cartesian coordinate system
ymax = yrange[1]
for i in range(0, len(xy)):
  xy[i][1] = ymax - xy[i][1]

# Saves the points for plotting
#plot(xy)

# I plottet all the points, look at full.gif and half.gif
# In this way I were able to skip a big range of points 
# which are not valid. I suggested the biggest rectangle 
# is created with points in the lower part of the circle.
# Only using points with y > 20000 and y < 48300

ymax = 48300
ymin = 20000
points2 = []
for i in range(0, len(xy)):
  if ( xy[i][1] >= ymin and xy[i][1] <= ymax ):
    points2.append( xy[i] )

#print(len( points2 ))

plot(points2)

# Generate meshgrid (no duplicated pairs like [0,1]-[1,0] and same index pairs [0,0])
lst = [] #[[0, 1], 0]
for i, j in combinations(range(len(points2)), 2):
  lst.append([[i, j], 0])


'''
..............
..AAAAA#AAA#.. (7,7) (11, 7)
..AAAAAAAAAA..
..#AAAA#AAAA.. (2,5) (7, 5)
..............                A --> 6 * 3
..#......#....
..............
.........#.#..
..............

xmin = min(x1, x2)
xmax = max(x1, x2)
ymin = min(y1, y2)
ymax = max(y1, y2)
inside_strict = (xmin < x < xmax) and (ymin < y < ymax)
--> if true, reactangle cant be used
'''



# Find the biggest rectangle
for i in range(0, len(lst)):
  # Skip if x or y the same, to small rectangle
  if ( points2[lst[i][0][0]][0] == points2[lst[i][0][1]][0] or points2[lst[i][0][0]][1] == points2[lst[i][0][1]][1] ):
    continue
  # Calc area
  a = (abs(points2[lst[i][0][0]][0] - points2[lst[i][0][1]][0]) + 1) * ( abs( points2[lst[i][0][0]][1] - points2[lst[i][0][1]][1] ) + 1)
  #print(f"calc {a}")
  lst[i][1] = a # calculated area

# Filter out rectangles were points are in between
for i in range(0, len(lst)):
  if (lst[i][1] == 0):
    continue
  
  for j in range(0, len(points2)):
    xx = (points2[lst[i][0][0]][0], points2[lst[i][0][1]][0] ) #x1, x2
    yy = (points2[lst[i][0][0]][1], points2[lst[i][0][1]][1] ) #y1, y2
    xmin = min(xx)
    xmax = max(xx)
    ymin = min(yy)
    ymax = max(yy)
    if ( (xmin < points2[j][0] < xmax) and (ymin < points2[j][1] < ymax) ):
      lst[i][1] = 0 # set the area to zero
      break


lst.sort(key=lambda x: x[1], reverse=True)

pm(lst, 5) # print first biggest areas
