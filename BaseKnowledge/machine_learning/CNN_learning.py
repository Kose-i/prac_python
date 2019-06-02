import numpy as np

x = np.array([[1,1,2,1,0,0],[0,0,1,1,2,0],[0,0,0,1,2,1],[0,0,0,1,3,2],[1,1,1,3,2,0],[2,2,3,2,1,0]])

f = np.array([[0,1,1],[0,1,1],[0,1,1]])

result = []

for i in range(len(x) - len(f) + 1):
  row = []
  for j in range(len(x[0]) - len(f[0]) + 1):
    row.append(np.sum(x[i:i+len(f),j:j+len(f[0])]*f))
  result.append(row)

print(result)
