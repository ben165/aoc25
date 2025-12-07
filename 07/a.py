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

split = 0


#breakpoint()

def findPos(r, pos):
  for i in range(0, len(m[r])):
    if m[r][i] == "|":
      pos.append(i)

#Start
for r in range(0, rlen-1):
  pos = []
  findPos(r, pos)
  for c in range(0, clen):
    if (c in pos):
      if ( m[r][c] == "|"):
        if ( m[r+1][c] == "^" ):
          m[r+1][c-1] = "|"
          m[r+1][c+1] = "|"
          split+=1
        else:
          m[r+1][c] = "|"
    #print( m[r][c], end="")
  #print()

#pm(m)
print(split)
#print(m[0][7]) #S

#start = lines.find("S")




