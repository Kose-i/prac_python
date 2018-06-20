def deco():
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

@deco()
def test_your_name(name):
  return name

print test_your_name('ko')
