#! /usr/bin/env python3

def func1():
  x = (1,2,3,4,5)
  
  print(type(x))
  print(x)
  print("x[3]=", x[3])
  print("x.index(3)=", x.index(3))
  print("x.count(3)=", x.count(3))

def func2():
  x = (1,2,3)
  y = [1,2]
  z = [x,y]

  print(z)
  print(x)
  x += (4,5)
  print(x)
  print(y)
  y+= [3,4]
  print(y)
  print(z)

if __name__=='__main__':
  print("\nfunc1")
  func1()
  print("\nfunc2")
  func2()
