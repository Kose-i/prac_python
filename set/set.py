#! /usr/bin/env python3

def func1():
  x = set([1,2,3,4])
  y = set([3,4,5,6,7])
  z = frozenset([4,5])
  
  print(x)
  print(y)
  x.add(5)
  x.remove(3)
  print(x)

  print("x|y=", x | y) # x U y
  print("x.union(y)=", x.union(y))
  print("x&y=", x & y) # x ~U y
  print("x.intersection(y)=", x.intersection(y))
  print("x-y=", x - y) # x - (x ~U y)
  print("x.difference(y)=", x.difference(y))
  print("x.symmetric_difference(y)=", x.symmetric_difference(y))

def func2():
  x = frozenset([1,2,3,4])
  y = frozenset([1,2])

  print(x)
  print(y)
  print("x.issubset(y)=", x.issubset(y))
  print("x.issuperset(y)=", x.issuperset(y))

def func3():
  x = set([1,2,3])
  y = set([5,6,7])

  print(x)
  x.update(y)
  print(x)

if __name__=="__main__":
  print("\nfunc1()")
  func1()
  print("\nfunc2()")
  func2()
  print("\nfunc3()")
  func3()
