#! /usr/bin/env python3
import csv
 
mojiretu = "Hello World first csv file"
data = mojiretu.split()
print(data)

f = open('result.csv', 'w')
writer = csv.writer(f)
writer.writerows(data)
f.close()
