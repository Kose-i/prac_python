import numpy as np

a = np.matrix([[1,2],[3,4]])

print(a)
print(np.linalg.inv(a))


b = np.matrix([[1,2],[2,4]])

print(np.linalg.det(b))
if np.linalg.det(b) != 0:
  print(np.linalg.inv(b))
