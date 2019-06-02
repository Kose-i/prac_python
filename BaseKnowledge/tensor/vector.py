import numpy as np
import math

a = np.array([1,2])
b = np.array([3,4])

print(a)
print(b)

print(b - a)

print(np.linalg.norm(a)) # norm a
print(math.sqrt(sum([i**2 for i in a]))) # norm a

print(a.dot(b)) # dot

