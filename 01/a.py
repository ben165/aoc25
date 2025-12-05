# globals
leftRight = []
nr1 = []
counter = [0]

# linked list
class chain:
 pos = 0
 right = 0
 left = 0

lst1 = []
for i in range(0, 100):
  t = chain()
  lst1.append(t)

for i in range(1, 99):
  lst1[i].pos = i
  lst1[i].left = lst1[i-1]
  lst1[i].right = lst1[i+1]

lst1[0].pos = 0
lst1[0].left = lst1[99]
lst1[0].right = lst1[1]

lst1[99].pos = 99
lst1[99].left = lst1[98]
lst1[99].right = lst1[0]

current = []
current.append(lst1[50])

def left(l):
  t = current[0]
  for i in range(0, l):
    t = t.left
  current[0] = t
  if t.pos == 0:
    counter[0] = counter[0] + 1
  #print(current[0].pos)

def right(r):
  t = current[0]
  for i in range(0, r):
    t = t.right
  current[0] = t
  if t.pos == 0:
    counter[0] = counter[0] + 1

  #print(current[0].pos)

# Read input.txt and split
f = open("input", "r")
lines = f.readlines()
for i in lines:
  line = i.replace("\n", "")
  leftRight.append(line[0:1])
  nr1.append(int(line[1:]))
f.close()

#print(leftRight)
#print(nr1)
for i in range(0, len(nr1)):
  if leftRight[i] == "L":
    left(nr1[i])
  else:
    right(nr1[i])

print(counter[0])


#230444-ce07cedc
#3629415-f1356522