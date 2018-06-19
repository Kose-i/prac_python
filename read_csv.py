import csv
import numpy as np

#csv_file = open("test.csv", "r")
array = np.genfromtxt("test.csv", delimiter=',')
print(array)
#f = csv.reader(csv_file)
#for f in csv_file:
#  print(f)
#print(f)
