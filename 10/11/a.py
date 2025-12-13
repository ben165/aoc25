#!/usr/bin/python3

# I removed the ":" in the input file
from j import data

data = data.split("\n")

for i in range(0, len(data)):
  data[i] = data[i].split(" ")

#breakpoint()

class Node:
  def __init__(self, name):
    self.name = name
    self.connections = []
  def add_connection(self, other_node):
    self.connections.append(other_node)

nodes = {}

for i in range (0, len(data)):
  if data[i][0] not in nodes:
    nodes[data[i][0]] = Node( data[i][0] )

  for j in range(1, len(data[i])):
    if data[i][j] not in nodes:
      nodes[data[i][j]] = Node(data[i][j])
    nodes[data[i][0]].add_connection( nodes[data[i][j]] )


# DFS-Function, from "you" to "out"
def dfs(current, path, all_paths):
  path.append(current.name)

  if current.name == "out":
    all_paths.append(list(path))
  else:
    for neighbor in current.connections:
      if neighbor.name in path: # prevent cycles
        continue
      dfs(neighbor, path, all_paths)
  path.pop()

# Cellect paths
all_paths = []
dfs(nodes["you"], [], all_paths)

# Result
print(len(all_paths))