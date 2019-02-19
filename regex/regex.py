#! /usr/bin/env python3

import re

def func1():
  pattern = re.compile('[aiueo]j')

  pattern_target = "jklajkfeojwifejkalijio"
  result = pattern.search(pattern_target)
  print("pattern=",pattern)
  print("pattern_target=",pattern_target)

  print(result)

def func2():
  pattern = re.compile('^[a-z]')
  pattern_target = "jfla;fjeoafjpfio;ejap";
  print("pattern=",pattern)
  print("pattern_target=",pattern_target)
  print(pattern.sub('P',pattern_target))

def func3():
  pattern = re.compile('(?P<group_name>[a-z]+)')
  pattern_target = "jfkla;jfdioaj efaj"
  print("pattern=",pattern)
  print("pattern_target=",pattern_target)
  result = pattern.search(pattern_target)
  print(result.group('group_name'))

if __name__=='__main__':
  print("\nfunc1()")
  func1()
  print("\nfunc2()")
  func2()
  print("\nfunc3()")
  func3()

