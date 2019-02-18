#! /usr/bin/env python3

if __name__=='__main__':
  a = 3
  if a == 0:
    print("a==0")
  elif a > 0:
    print("a>0")
  else:
    print("a<0")

  b = 2
  print("b >= 0") if b >= 0 else print("b < 0")
