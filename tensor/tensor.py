import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])

print(a)
print(b)

print(a.dot(b))

A = np.matrix([[1,2,3],[4,5,6]])
B = np.matrix([[1,2],[3,4],[5,6]])

print(A*B)
