#! /usr/bin/env python3

import json
def func1():
  str_target = {1:("fjkdslajfklwjeio", "jalfjds"), 2:"jks"}
  json_str = json.dumps(str_target)
  print(json_str)
  print(json.loads(json_str))

if __name__=='__main__':
  print("\nfunc1()")
  func1()

