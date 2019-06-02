#! /usr/bin/env python3

def error_happen():
  try:
    print("In try")
    raise ValueError("raise ValueError")
  except TypeError:
    print("except 1")
  except ValueError as Instance:
    print("except 2")
    print(Instance)
  except:
    print("other except")
  else:
    print("pass error")
  finally:
    print("finally")

if __name__=='__main__':
  error_happen()
