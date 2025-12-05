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

def maxlen(nr):
  print(len(str(nr)))

'''
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
'''

def isInvalid2(nr):
  nr_str = str(nr)
  len_str = len(nr_str)

  #1
  if (len_str > 1):
    b = nr_str[0]
    c = 1
    for i in range(1, len_str):
      if (b == nr_str[i]):
        c += 1
        continue
    if (c == len_str):
      return True
  
  #2
  if (len_str >= 4 and len_str%2==0):
    parts = len_str//2
    l = []
    step = 2
    start = 0
    ende = start + step
    for i in range(0, parts):
      l.append(nr_str[start:ende])
      start += step
      ende += step
    
    b = l[0]
    c = 1
    for i in range(1, len(l)):
      if (b == l[i]):
        c += 1
        continue
    if (c == len(l)):
      return True

  #3
  if (len_str >= 6 and len_str%3==0):
    parts = len_str//3
    l = []
    step = 3
    start = 0
    ende = start + step
    for i in range(0, parts):
      l.append(nr_str[start:ende])
      start += step
      ende += step
    
    b = l[0]
    c = 1
    for i in range(1, len(l)):
      if (b == l[i]):
        c += 1
        continue
    if (c == len(l)):
      return True
    
  #4
  if (len_str >= 8 and len_str%4==0):
    parts = len_str//4
    l = []
    step = 4
    start = 0
    ende = start + step
    for i in range(0, parts):
      l.append(nr_str[start:ende])
      start += step
      ende += step
    
    b = l[0]
    c = 1
    for i in range(1, len(l)):
      if (b == l[i]):
        c += 1
        continue
    if (c == len(l)):
      return True
    
  #5
  if (len_str >= 10 and len_str%5==0):
    parts = len_str//5
    l = []
    step = 5
    start = 0
    ende = start + step
    for i in range(0, parts):
      l.append(nr_str[start:ende])
      start += step
      ende += step
    
    b = l[0]
    c = 1
    for i in range(1, len(l)):
      if (b == l[i]):
        c += 1
        continue
    if (c == len(l)):
      return True

#for i in ids:
#  maxlen(i[1])


sum = 0
for i in ids:
  #print(i[0], len(str(i[0])))
  #print(i[1]-i[0])
  for j in range(i[0], i[1]+1):
    if (isInvalid2(j)):
      #print(j)
      sum += j
print(sum)
