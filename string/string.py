#! /usr/bin/env python3

def func1():
  str = "%s is %s."%('aiueo', 'kakikukeko')
  print(str)

def func2():
  pass

if __name__=='__main__':
  print("func1()")
  func1()
  print("func2()")
  func2()
