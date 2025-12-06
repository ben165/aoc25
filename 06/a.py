#!/usr/bin/python3

# File read
# Read input.txt and split
f = open("j", 'r')
content = f.read()
f.close()

content = content.split("\n")
content.pop()

for i in range(0, len(content)):
  content[i] = content[i].split()

sum = 0

operations = content[-1]
#print(operations)
content.pop()

def add(a, b):
  return a + b
def mul(a, b):
  return a * b

for r in range(0, len(content)):
  for c in range(0, len(content[0])):
    content[r][c] = int(content[r][c])

#print(content)

sum2 = 0
for c in range(0, len(content[0])):
  #print()
  if operations[c] == "+":
    sum = 0
    f = add
  else:
    sum = 1
    f = mul
  for r in range(0, len(content)):
    #print(content[r][c])
    sum = f(sum, content[r][c])
  sum2 += sum

print(sum2)

