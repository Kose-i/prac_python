x = set([1,2,3,4,5])
y = set([3,4,5,6,7])

print(x)
print(y)

print(x | y) # x U y
print(x & y) # x ~U y
print(x - y) # x - (x ~U y)
