#! /usr/bin/env python3
x = [1,2,3,4,5]

print(type(x))
print(x)
print(x[2:])
print(x[2:4])
print(x[-2])

y = [[0] * 3] * 4

print(y)
y[1][2] = 3
print(y)

z = [[i+j for i in range(1+j,3+j)] for j in range(4)]

print(z)
