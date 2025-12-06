#!/usr/bin/python3

# I removed the operations and the last line at the input file
# This was a tough one

lst=[]

def printList():
  for i in lst:
    print(i)

def add(a, b):
  return a + b
def mul(a, b):
  return a * b

ops = "+   *   *  +    *   +    +   *   +    *   +  +   *   *  +   *   *  *   *   *  +  +  *  +    *   +    +  *  +   +   *   +  +    *   *   *  +  +   *   *  *  *   *   +   *  +  *  *  +    +    *   +    +   *  *  *  *  +  +   *  +    +   *   *  +   *   *  *   *   *   +  *  *   *   *  *   *  *  *   *  +   +   +  *   +   *  *  *   +   *  *  *  +    +    *  *  *   *   *  *  +   *   *   +   *  +   *  +   *  *  +   *  *   *  +   *   *   +    *   +   *   *  +   +  *  +  *   *  *  +    *   *   +    *  +    *  +   +  +    +  +  *   *  *   +   *  +   *  *   *  +   +    +  *  +  +  *  *  *   *  +   +  +   +   +  *  *   +    +    +  +    +   *   *  *  *   +   *  +   *  *  *  *  *   *   +   +  *   *   +  *   +   *  *  +  *  *   *   +   +    *  +  +  +   *  *  *  *  *   +    +  *  *  +    *  *   +  +  *  *  +  +    *   *   *   *  +  +   *   *  +  +    *   +    *  *   *  *  +  *   *   *  *  +  +   *  *   *  *  +  +   +   +  +   *  +   *  +   +   *  +    *  *   +  *  *   *  +  +    +    +  *  *   *  *   +   *   +    *  +  *  *  +  *  +    +  *  +  +    +  *   *   +  +    *  +    *   *   *  *   +    +    *  +   +   +  +    *   *  *   +  *  +   *  +   *  *  *   +    +  +   +   *  +   +  *   +  *  *   +    +    *  +  *   *  +   +   *   +  *   +   *   *  *   +    *  +  *   +   +  *   +    *   +    +   +    *  +   *   +    +   *  *  *   *   +  +   +   *   *   +  +  *   *  +    *   *  *  +  +    *   *   *  *   *  *  *   +    *   *  *   *   +  +   *  +    *   +  +   +  *  +  +    +   +  *   *  *   *   *   +    *  *   *  +    *  *   +  +    *   +  +   +   *   +   *  +    +   *  *  *   *  +   *  +   *   *  *   *  +    +   *  +    +  *  +    *  +  *   +  *  *  *   *  *  *  +  +   +    +    +  *  +  +   *   +    +  *   *   +   *  +  +    *  +  *  +   +    +   +  *   *  +    +    +    +    +    *   +   +    *   *   *   +    *  *   *   *  *  +   +    *  +   +   +    *   +  +  *  *   +   *  +    +    *  *   *  *  *  *  +    *   *  *   *  *   *   *   +   *   *  +  +  *  *   *   *  *  *   +   *   +  +    +  *   +    +  +   +    *  *  *   *  +    *  +    +   +   +   +  *   *  +   +   +   +    *  *  +   *   *  *  +  +  *   +    *  *   *  *   *  +    *   *  +    +   +  *   *   +   *  *  +    *  +  *  *   +   *   +   *   *  +  +  *  *  +    *   *   *  +  *   *  +   +  *   +   +    *  *  +  *  *   +   +    *  *   *   +  +  *  +    +    +   +  +  *  +   +    *   +  *  +  *   *  +   *   +  *   *   *   +    *  +   *   +  +    *  *  +  +  *  *   *   +   *  +   +    *   *   +    +    *   *  *  *  *   *  *  +  *   *   *  +  +    +    +  +   *  +  +   *  *  +  *   +   *   +   +    +  *   *   +   +  +  *   +    +   *  +    +    +    +   *  *  +   +  *  *  +  +   +   *  *   +  *  +   +  *   +  *  *   +    +    +  *  +   +  +  +    *   *   +    +   *  *  +   *  +   +    *   *  +  +  *   *   *   +  *  +   *   +  +   +   +  *   *   +   *  +   *   *  *  +  +    *   *   +   +    *  +   *   *   *   +   +   *   *   +   *   *   +    +   +    *  *   +   +  +  +  +  *   *   +   +   *   *  *  +  *   *  +  *  *  +    *   *   *   +   *  *  +    +   +  *   +   *  +    *   *  +  +  +  *  +  *  *   +   *  *   +   *  *   *   +  +    +    *  +    *  *   *  +  +  *   +  *   *   +   *  *   *  *  *  *   *  *   *   *   +  +    +    *  *   *   *   +  *   *  *   *  *  +    *  *   *  *   *  +    *  *   *   *  *   +  +    *  *  *  *  +   *  *  +   +    *   *   *  *   +    +   *   *  *  *   *   *   *  *   *  *   *  *   +   +    *  *   +    *   *   +   +   +    *   *  *  *  +    *  *  *   +  *  *   +    +   *   +  +   *  +  *  *   *  +    +  +   *   *  *   *   +    *   +   *  +   *   *  *  +   +  *   +  *  *  *  *   *   +  *  *  *   *   +  *   +    +    +  *  *  +    *  +    *  +   *   *   *  +    +    S"
#ops = "*   +   *   +   S"

sep = []
for i in range(0, len(ops)):
  if (ops[i] in ("+", "*", "S")):
    sep.append(i)

f = open("j", 'r')
content = f.read()
f.close()

# ops and newline removed
content = content.split("\n")

for i in range(0, len(sep)-1):
  a = []
  for r in content:
    a.append( r[sep[i]:sep[i+1]-1] )
  lst.append(a)

#All same length
#for r in range(0, len(lst)):
#  for c in range(0, len(lst[0])):
#    lst[r][c] = lst[r][c].zfill(4)



ops = ops[0:-1]
ops = ops.split()
#print(ops)

#lst.pop()
#lst.pop()
#lst.pop()

#printList()

'''
for c in range(0, len(r)):
  
if ops[counter] == "+":
  sum = 0
  f = add
else:
  sum = 1
  f = mul
'''

total = 0
counter = 0
for r in lst:
  if ops[counter] == "+":
    sum = 0
    f = add
  else:
    sum = 1
    f = mul

  #print(r)
  nrs = ["", "", "", ""]
  for c in range(0, len(r)):
    for i in range(0, 4):
      try:
        nrs[i] += r[c][i]
      except:
        pass
  #print(nrs)
  for i in range(0, len(nrs)):
    try:
      nrs[i] = int(nrs[i])
    except:
      if ops[counter] == "+":
        nrs[i] = 0
      else:
        nrs[i] = 1
  for i in range(0, len(nrs)):
    sum = f(sum, nrs[i])
  #print(sum)
  total += sum
  counter += 1
print(total)


#for r in range(0, len(content)):
#  for c in range(0, len(content[0])):

