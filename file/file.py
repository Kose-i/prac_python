#! /usr/bin/env python3

def func1():
  f = open("test.txt", 'w')
  f.write("This is test")
  f.close()

def func2():
  f = open("test.txt", 'r')
  print(f.read())
  f.close()

import codecs
def func3():
  f = codecs.open("test.txt", 'w', 'utf-8', 'ignore')
  f.write("test func3")
  f.close()

import os.path
def func4():
  path = "tmp/tmp-1/tmp.txt"
  print(os.path.split(path))

import shutil
def func5():
  shutil.copyfile("test.txt", "test2.txt")

import glob
def func6():
  print(glob.glob('*'))

import tempfile
def func7():
  tmpfd, tmpname = tempfile.mkstemp(dir='.')
  print(tmpname)
  f = os.fdopen(tmpfd, 'w+b')
  f.close()

if __name__=='__main__':
  print("\nfunc1()")
  func1()
  print("\nfunc2()")
  func2()
  print("\nfunc3()")
  func3()
  print("\nfunc4()")
  func4()
  print("\nfunc5()")
  func5()
  print("\nfunc6()")
  func6()
  print("\nfunc7()")
  func7()
