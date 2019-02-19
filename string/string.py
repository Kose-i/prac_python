#! /usr/bin/env python3

def func1():
  str = "%s is %s."%('aiueo', 'kakikukeko')
  str1 = "tmpstr"

  print(str)
  print("str.find('k')", str.find('k'))
  print(','.join([str, str1]))
  print(str.startswith('a'))
  print(str.split('k'))

def func2():
  str = "hogehogehoge"
  print(str.replace('o','a'))
  print(str.strip('h'))

if __name__=='__main__':
  print("\nfunc1()")
  func1()
  print("\nfunc2()")
  func2()
