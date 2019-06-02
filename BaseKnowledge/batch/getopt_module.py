#! /usr/bin/env python3

import sys
import getopt

argv = sys.argv[1:]
print(argv)

options, arguments = getopt.getopt(argv, "a:", ('apple'))

for name, value in options:
  print("name:",name, ", value:", value)

for argument in arguments:
  print("argument:", argument)
