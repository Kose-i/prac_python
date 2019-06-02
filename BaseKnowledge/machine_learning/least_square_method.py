data = [[0,1.5],[2,1.7],[3,2.1],[5,2.2],[6,2.8],[7,2.9],[9,3.2],[11,3.7]]

def dEa(a, b):
  sum = 0
  for i in data:
    sum += i[0] * (i[0]*a + b - i[1])
  return sum

def dEb(a, b):
  sum = 0
  for i in data:
    sum += i[0]*a + b - i[1]
  return sum

eta = 0.006 # study rate
a, b = 2,1 # start

for i in range(0,200):
  a += -eta *dEa(a,b)
  b += -eta *dEb(a,b)
  print([a,b])
