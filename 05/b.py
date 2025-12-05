
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


# Merging range algorithm 
def merge(ranges1):
  if not ranges1:
    return []

  ranges1.sort(key=lambda x: x[0]) #Sorting after start ranges
  merged = [ranges[0]]

  for start, current in ranges1[1:]:
    mergeStart, ende = merged[-1]
    if start <= ende:
      merged[-1] = [mergeStart, max(ende, current)]
    else:
      merged.append([start, current])
  return merged

result = merge(ranges)

sum = 0
for i in result:
   sum += (i[1]+1) - i[0]

print(sum)
