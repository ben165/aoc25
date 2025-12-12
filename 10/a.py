#!/usr/bin/python3
from j import data

import algos

def pm(m):
  for i in m:
    print(i)

data = data.split("\n")
lend = len(data)

for i in range(0, lend):
  data[i] = data[i].split("-")
  data[i].pop() # is not used for now

  # [i][0 = Bitmuster]
  data[i][0] = data[i][0].replace("[", "")
  data[i][0] = data[i][0].replace("]", "")
  data[i][0] = data[i][0].replace(".", "0")
  data[i][0] = data[i][0].replace("#", "1")
  data[i][0] = [int(c) for c in data[i][0]]

  # [i][1 = Switches]
  data[i][1] = data[i][1].replace("(", "")
  data[i][1] = data[i][1].replace(")", "")
  data[i][1] = data[i][1].split(" ")
  for j in range(0, len(data[i][1])):
    numbers = data[i][1][j]
    numbers = numbers.split(",")
    newNumbers = []
    for k in range(0, len(numbers)):
      newNumbers.append(int(numbers[k]))
    data[i][1][j] = newNumbers

sum = 0
for k in range(0, len(data)): #len(data)
  buttons = []
  for i in range(0, len(data[k][1])):
    t = []
    for x in data[k][0]:
      t.append(0)

    for j in range(0, len(data[k][1][i])):
      #print( data[k][1][i][j] )
      t[ data[k][1][i][j] ] = 1
    #print()
    buttons.append(t)

  #pm(buttons)

  particular, nullspace = algos.gaussian_elimination_gf2(buttons, data[k][0])
  solution, weight = algos.minimal_hamming_solution(particular, nullspace)
  #print("Ergebnis:", solution, "Drücke:", weight)
  sum += weight

print(sum)

#print( f"target: {data[0][0]}" )
#pm(buttons)



#buttons = [0, 0, 0, 1]
#[0, 1, 0, 1]
#[0, 0, 1, 0]
#[0, 0, 1, 1]
#[1, 0, 1, 0]
#[1, 1, 0, 0]

#target = [0,1,1,0]



