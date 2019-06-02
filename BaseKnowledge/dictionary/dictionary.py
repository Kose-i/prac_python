#! /usr/bin/env python3

def func1():
  x ={3:"three", 2:"two"}

  print(x)
  print("x[3] = ", x[3])
  print("x.get(4)=", x.get(4))
  print("x.keys()=", x.keys());
  print("x.values()=", x.values());
  print("x.items()=", x.items());
  print("len( x )=", len(x));

def func2():
  x = dict([(3,"three"), (2,"two")])
  y = dict({10:"ten",11:"eleven"})

  x[1] = "one"
  x.setdefault(4, "four")
  print(x)
  del x[3]
  print(x)
  x.update(y)
  print(x)
  x.pop(2)
  x.popitem()
  print(x)

def func3():
  x = dict.fromkeys([1,2])
  y = x.copy()

  print(y)

if __name__=='__main__':
  print("\nfunc1()")
  func1()
  print("\nfunc2()")
  func2()
  print("\nfunc3()")
  func3()
