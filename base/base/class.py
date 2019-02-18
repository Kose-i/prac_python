#! /usr/bin/env python3
class A:
  def __init__(self): #constructor
    print("__init__")
  def __del__(self): #destructor
    print("__del__")
  def set_name(self, name): #function setter
    self.name = name
  def get_name(self): #function getter
    return self.name

if __name__=='__main__':
  x = A()
  x.set_name("hoge")
  print(x.get_name())
