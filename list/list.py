#! /usr/bin/env python3

def func1():
  x = [1,2,3,4,5]
  
  print(type(x))
  print(x)
  print(x[2:])
  print(x[2:4])
  print(x[-2])

def func2():
  x = [1,2]
  y = [x * 3] * 4
  z = y
  
  print(y)
  y[1][0] = 3
  print(z)
  z[0][1] = 5
  print(y)

def func3():
  x = [[i+j for i in range(1+j,3+j)] for j in range(4)]
  
  print(x)

def func4():
  x = list((1,2,3))
  y = list((1,2,3))
  z = list((1,2,3))

  x.append('hello')
  y.extend(['hello', 'world'])
  z.insert(2,3)
  x.remove(3)
  del(y[0])

  print(x)
  print(y)
  print(z)
  
def func5():
  x = [1,2,3,1,2,4,2]

  print(x)
  print("x.index(3)=", x.index(3))
  print("3 in x=", 3 in x)
  print("x.count(2)=", x.count(2))
  print("len( x )=", len(x))
  print("max( x )=", max(x))
  print("min( x )=", min(x))
  print("sum( x )=", sum(x))
  x.sort()
  print("sort( x )=", x)
  x.reverse()
  print("reverse( x )=", x)

def func6():
  x = [True, False, True, False]

  print(x)
  print("any( x )=",any(x))
  print("all( x )=", all(x))

if __name__ == '__main__':
  print("\nfunc1()")
  func1()
  print("\nfunc2()")
  func2()
  print("\nfunc3()")
  func3()
  print("\nfunc4()")
  func4()
  print("\nfunc5()")
  func5()
  print("\nfunc6()")
  func6()
