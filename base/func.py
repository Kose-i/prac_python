#! /usr/bin/env python3

def func1(func1_target ='World'):
  print("Hello", func1_target)

def func2(*lists):
  print("Hello "+'.'.join(lists))

def func3(**dictionary):
  print("Hello")
  print(dictionary)

y = 2
def func4(x):
  x = x + 1
  global y
  y = 3
  print("x=",x,",y=",y)

def func5(x):
  return x*x

def func6(x,func1, func2):
  return func2(func1(x))

if __name__=='__main__':
  print("\nfunc1()")
  func1()
  func1(func1_target='python')
  print("\nfunc2()")
  func2(*['test1', 'test2'])
  print("\nfunc3()")
  func3(**{'dic1':'1', 'dic2':'2'})
  print("\nfunc4()")
  x = 2
  print("func4()=",func4(x))
  print("x=",x,",y=",y)
  print("\nfunc5()")
  power = func5
  print("power( 3 )=", power(3))
  print("\nfunc6")
  lambda_test = lambda x:x+1
  print("func6(2, lambda_test, func5)=", func6(2, lambda_test, func5))

