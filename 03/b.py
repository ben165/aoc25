
# globals
count = []
lst1 = []

def show():
  c = 0
  for i in lst1:
    print(c, i)
    c += 1

# Read input.txt and split
f = open("j", "r")
lines = f.readlines()
for i in lines:
  line = i.replace("\n", "")
  lst1.append(line[::-1]) #reverse is better for this task
f.close()

def makeList(str1):
  l = []
  for i in range(0, len(str1)):
    l.append([int(str1[i]), i])
  return l


def findBiggest(l, pos1, pos2):
  t = 0
  p = 0
  for i in range(pos1, pos2):
    if l[i][0]>=t:
      t = l[i][0]
      p = l[i][1]
  return [t, p]


sum = 0
for i in lst1:
  l = makeList(i)
  pos1 = 11
  pos2 = len(i)
  biggestNr = ""
  for i in range(0,12):
    nr, pos2 = findBiggest(l, pos1, pos2)
    biggestNr += str(nr)
    pos1 -= 1
  sum += int(biggestNr)

print(sum)
#show()




'''
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
'''