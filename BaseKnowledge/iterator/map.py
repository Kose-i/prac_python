#! /usr/bin/env python3

def func1():
  try:
    for m in map(int, ['1', '2', '3', '4L']):
      print(m)
  except ValueError as instance:
    print(instance)

if __name__=='__main__':
  print("\nfunc1()")
  func1()
