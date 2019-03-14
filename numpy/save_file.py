#!/usr/bin/env python3
import numpy as np

data = np.random.randn(5)
print("data now:", data)
np.save('datafile/datafile.npy', data)
data = []
print("data now:",data)
data = np.load('datafile/datafile.npy')
print("data now:",data)
