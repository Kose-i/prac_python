#! /usr/bin/env python3

import csv

fcsv = open("result.csv", 'r')
for row in csv.reader(fcsv):
  print(row)
