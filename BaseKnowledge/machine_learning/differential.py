def f(x):
  return (x+1)**2

def df(x, h):
  return (f(x+h) - f(x-h)) / 2*h

for h in [1,1e-1,1e-2]:
  print([h,df(0,h),df(1,h)])
