
# globals
files = []

# I splitted ranges and ids in two files
if (1==2):
  files = ["i1", "i2"]
else:
  files = ["j1", "j2"]

ranges = []
# Read ranges and split
f = open(files[0], 'r')
content = f.read()
f.close()

content = content.split("\n")
for i in content:
  l = i.split("-")
  ranges.append([int(l[0]), int(l[1])])

ids = []
#Read ids
f = open(files[1], 'r')
content = f.read()
f.close()

content = content.split("\n")
for i in content:
  ids.append(int(i))

#print(ranges)
#print(ids)

sum = 0
for i in range(0, len(ids)):
  for j in ranges:
    if (ids[i]>=j[0] and ids[i]<=j[1]):
      #good
      sum += 1
      ids[i] = 0 #no double counting
      break
    else:
      pass

print(sum)

#print(content)

