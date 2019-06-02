#! /usr/bin/env python3

def func1():
  x = iter([1,2,3,21,43,4])

  print(x)
  print(next(x))

def func2():
  def generator():
    yield 1
    yield 2
    yield 3
    yield 4
  for e in generator():
    print(e)

def func3():
  def func3_inner():
    receive = 0
    receive = (yield receive)
    print("receive =", receive, " from func3_inner()")
  gen = func3_inner()
  next(gen)
  print(gen.send(2))

if __name__=='__main__':
  print("\nfunc1()")
  func1()
  print("\nfunc2()")
  func2()
  print("\nfunc3()")
  func3()
