#!/usr/bin/python3

from j import data

#print(data)
def pm(m):
  for r in m:
    for c in r:
      print(c , end="")
    print()

lines = data.split("\n")


m = []
for i in lines:
  m.append(list(i))

rlen = len(m)
clen = len(m[0])


#breakpoint()

def findPos(r, pos):
  for i in range(0, len(m[r])):
    if m[r][i] == "|":
      pos.append(i)

# creating timelines
timelines = []
for i in range(0, len(m[0])):
  timelines.append(0)

# find start
for i in range(0, len(m[0])):
  if ( m[0][i] == "|" ):
    timelines[i] = 1
    break


# Start
# Helped to solve second prob with visual solution to get an idea:
# https://www.reddit.com/r/adventofcode/comments/1pgbg8a/2025_day_7_part_2_visualization_for_the_sample/#lightbox
split = 0
for r in range(0, rlen-1):
  pos = []
  findPos(r, pos)
  for c in range(0, clen):
    if (c in pos):
      if ( m[r][c] == "|"):
        if ( m[r+1][c] == "^" ):
          t = timelines[c]
          timelines[c] = 0
          timelines[c-1] += t
          timelines[c+1] += t

          m[r+1][c-1] = "|"
          m[r+1][c+1] = "|"
          split+=1
        else:
          m[r+1][c] = "|"
    #print( m[r][c], end="")
  #print()

#pm(m)
#print(split)
#print(timelines)

sum = 0
for i in timelines:
  sum += i
print(sum)

#print(m[0][7]) #S

#start = lines.find("S")




