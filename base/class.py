#! /usr/bin/env python3
class A:
  def __init__(self): #constructor
    self.name = ""
    print("__init__class A")
  def __del__(self): #destructor
    print("__del__class A")
  def set_name(self, name): #function setter
    self.name = name
  def get_name(self): #function getter
    return self.name

class B(A):
  def __init__(self):
    print("__init__class B")
    super(B, self).__init__()
  def __del__(self):
    super(B, self).__del__()
  def print_param(self):
    print("B name:",self.get_name())

class C:
  def _set_color(self, rgb):
    self._rgb = tuple(v / 255.0 for v in rgb)
  def _get_color(self):
    return tuple(v*255.0 for v in self._rgb)
  color = property(_get_color, _set_color)
  def __imul__(self, factor):
    t = self.color
    self.color = tuple(v*factor for v in t)
    return self

class D:
  def __init__(self, score):
    self.score = score
  def get_score(self):
    return self.score
  @classmethod
  def define_class_D_score(cls, init_score):
    score = init_score
  @staticmethod
  def perfect_score():
    return 100

if __name__=='__main__':
  print("\nclass A")
  x = A()
  x.set_name("hoge")
  print(x.get_name())
  print("\nclass B")
  y = B()
  y.set_name("hogehoge")
  y.print_param()
  print("\nclass C")
  z = C()
  z.color = (0,24,2)
  z *= 3
  print(z.color)
  print("\nClass D")
  a = D(20)
  b = D(30)
  print("a.get_score()=",a.get_score(), "b.get_score=",b.get_score())
  D.define_class_D_score(30)
  print("a.get_score()=",a.get_score(), "b.get_score=",b.get_score())
  print(D.perfect_score())
