import random
import collections
import math

x = []
for i in range(3):
  x.append(random.random())
print(x) # 0, 1

y = []
for i in range(3):
  y.append(random.randint(0,1))
print(y)

print(collections.Counter([math.floor(i*10) for i in x]))
