#! /usr/bin/env python3

import datetime

def func1():
  tmp_time = datetime.datetime(1000, 1, 1, 0, 0, 0)
  print(tmp_time)
  now_time = datetime.datetime.now()
  list = (now_time.year, now_time.month, now_time.day, now_time.hour, now_time.minute, now_time.second, now_time.microsecond)
  print(list)
  print("now_time - tmp_time=", now_time - tmp_time)

if __name__=='__main__':
  print("\nfunc1()")
  func1()
