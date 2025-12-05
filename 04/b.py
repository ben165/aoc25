
# globals
maze = []
maze2 = []

def print_maze(a):
  for i in a:
    for j in i:
      print(j, end="")
    print()

# Read input.txt and split
f = open("j", 'r')
content = f.read()
f.close()

content = content.split("\n")
content.pop(-1)
#print(content)

# Create maze
maze = []

# adding first/last line
first = []
last = []
l = len(content[0])
for i in range(0, l):
  first.append(".")
  last.append(".")

content.insert(0, first)
content.append(last)

# making two grid
for i in content:
  e = []
  f = []
  e.append(".")
  f.append(".")
  for j in i:
    e.append(j)
    f.append(j)
  e.append(".")
  f.append(j)
  maze.append(e)
  maze2.append(f)


#print_maze(maze)
sum = 0
# checking sourroundings
for many in range(0, 500):
  for r in range(1, len(maze)-1):
    for c in range(1, len(maze[0])-1):
      counter = 0
      if (maze[r][c]) != ".":
        if (maze[r-1][c-1] == "@"):
          counter+=1
        if (maze[r-1][c] == "@"):
          counter+=1
        if (maze[r-1][c+1] == "@"):
          counter+=1
        if (maze[r][c-1] == "@"):
          counter+=1
        if (maze[r][c+1] == "@"):
          counter+=1
        if (maze[r+1][c-1] == "@"):
          counter+=1
        if (maze[r+1][c] == "@"):
          counter+=1
        if (maze[r+1][c+1] == "@"):
          counter+=1
        
        if (counter < 4):
          sum += 1
          maze[r][c] = "."
  


'''
# checking sourroundings
for r in range(1, len(maze)-1):
  for c in range(1, len(maze[0])):
    print(maze[r][c], end="")
  print()
'''
  

#print_maze(maze)
#print()
#print_maze(maze2)
print(sum)

