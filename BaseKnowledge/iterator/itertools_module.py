#! /usr/bin/env python3

import itertools

def func1():
  rows = iter(['Alice', 'Bob', 'Carol'])
  for rows in itertools.islice(rows, 2):
    print(rows)

if __name__=='__main__':
  func1()
