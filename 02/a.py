#!/usr/bin/python3

# globals
lst1 = []
invalid = []

# Read input.txt and split
f = open("j", 'r')
content = f.read()
f.close()

content = content.replace("\n", "")
content = content.split(",")

ids = []
for i in content:
  t = i.split("-")
  ids.append([int(t[0]), int(t[1])])

#print(ids)

def isInvalid(nr):
  nr_str = str(nr)
  len1 = len(nr_str)
  if (len1 % 2 == 0):
    len0 = int(len1/2)
    z1 = nr_str[0:len0]
    z2 = nr_str[len0:]
    if (z1 == z2):
      return True
  else:
    return False

sum = 0
for i in ids:
  #print(i[0], len(str(i[0])))
  #print(i[1]-i[0])
  for j in range(i[0], i[1]+1):
    if (isInvalid(j)):
      #print(j)
      sum += j
print(sum)

