#!/usr/bin/python3

# pip install pulp

import pulp

from j import data

# This function was AI generated
def solve_machine(A, b):
  n_counters = len(A)
  n_buttons = len(A[0])

  prob = pulp.LpProblem("factory", pulp.LpMinimize)

  # x_j = Anzahl Tastendrücke für Button j
  x = [
    pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer")
    for j in range(n_buttons)
  ]

  # Ziel: minimale Gesamtanzahl Tastendrücke
  prob += pulp.lpSum(x)

  # Jeder Counter muss exakt seinen Zielwert erreichen
  for i in range(n_counters):
    prob += pulp.lpSum(A[i][j] * x[j] for j in range(n_buttons)) == b[i]

  prob.solve(pulp.PULP_CBC_CMD(msg=False))

  return int(pulp.value(prob.objective)), [int(pulp.value(v)) for v in x]

def pm(m):
  for i in m:
    print(i)

data = data.split("\n")
lend = len(data)

for i in range(0, lend):
  data[i] = data[i].split("-")

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

  # [i][2 = voltages]
  data[i][2] = data[i][2].replace("{", "")
  data[i][2] = data[i][2].replace("}", "")
  data[i][2] = data[i][2].split(",")
  data[i][2] = [int(c) for c in data[i][2]]

# Build Buttons
allButtons = []
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
  allButtons.append( buttons )
#print( f"target: {data[0][0]}" )
#pm(buttons)

sum = 0
for i in range(0, len(data)):
  # Transformation
  A = list(map(list, zip(*allButtons[i])))

  cost, presses = solve_machine(A, data[i][2])
  #print(cost, presses)
  sum += cost

print(sum)








