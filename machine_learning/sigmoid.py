import numpy as np

def sigmoid(x):
  return 1/(1 + np.exp(-x))

def sigmoid_diff(x):
  return (sigmoid(x) *(1 - sigmoid(x)))

print(sigmoid(3))
print(sigmoid_diff(3))
