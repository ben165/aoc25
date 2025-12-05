
# globals
count = []
lst1 = []

# Read input.txt and split
f = open("j", "r")
lines = f.readlines()
for i in lines:
  line = i.replace("\n", "")
  lst1.append(line)
f.close()

def getBattery(str1):
  lst1 = []
  for i in str1:
    lst1.append(int(i))

  nr = [-1, -1]
  for i in range(0, len(lst1)):
    if nr[0] < lst1[i]:
      nr[0] = lst1[i]
      nr[1] = i

  t = []
  nr2 = [-1, -1]
  if (nr[1] != len(lst1)-1):
    for i in range(nr[1], len(lst1)):
      if (i == nr[1]):
        continue
      if nr2[0] < lst1[i]:
        nr2[0] = lst1[i]
        nr2[1] = i
  else:
    for i in range(0, len(lst1)-1):
      if nr2[0] < lst1[i]:
        nr2[0] = lst1[i]
        nr2[1] = i
    t.append(nr[0])
    t.append(nr[1])
    nr[0] = nr2[0]
    nr[1] = nr2[1]
    nr2[0] = t[0]
    nr2[1] = t[1]


  return(str(nr[0]) + str(nr2[0]))
  #return nr[0] * 10 + nr2[0]

def search():
  c = 0
  for i in lst1:
    a = getBattery(i)
    #print(a)
    c += int(a)
  print()
  print(c)

search()

def show():
  c = 0
  for i in lst1:
    print(c, i)
    c += 1
