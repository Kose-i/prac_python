#! /usr/bin/env python3

import pickle
def func1():
  cache = {1:'first', 2:'second', 3:'third'}
  print(cache)
  serialized = pickle.dumps(cache)
  print(serialized)
  deserialized = pickle.loads(serialized)
  print(deserialized)

if __name__=='__main__':
  print("\nfunc1()")
  func1()

