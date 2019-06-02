import numpy as np

x = np.array([[0,0,1,0,0,0],[0,0,2,0,0,0],[0,1,2,1,0,0],[0,1,2,1,0,0],[1,2,2,2,1,0],[1,2,3,2,1,0]])

result = []

for i in range(0, len(x), 2):
  row = []
  for j in range(0, len(x[0]), 2):
    row.append(np.max(x[i:i+2,j:j+2]))
  result.append(row)

print(result)
