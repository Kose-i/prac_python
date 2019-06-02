#! /usr/bin/env python3

def deco1():
  def deco_func(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
      res = "Hello, "
      res += func(*args,**kwargs)
      res += "."
      return res
    return wrapper
  return deco_func

def deco2(func):
  import time
  def new_f(*args, **kwds):
    t =time.time()
    result = func(*args, **kwds)
    print("%ss"%(time.time() - t))

    return result
  return new_f

@deco1()
def test_your_name(name):
  return name

@deco2
def test_multiple(x, y):
  return x*x + y*y

if __name__=='__main__':
  print(test_your_name('ko'))
  print(test_multiple(2,3))
