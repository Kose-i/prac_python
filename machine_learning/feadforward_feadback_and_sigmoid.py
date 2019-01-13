import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

def softmax(x):
  e = np.exp(x)
  return e/np.sum(e)

V = np.array([[0.1,0.3],[0.2,0.4]])
W = np.array([[0.1,0.3],[0.2,0.4]])

t = np.array([[1,0]])

eta = 0.005

# feadforward
x = np.array([[1,0.5]])
y = sigmoid(x.dot(V))
z = sigmoid(y.dot(W))

#
delta2 = z - t
grad_W = y.T.dot(delta2)
sigmoid_dash = y*(1-y)
delta1 = delta2.dot(W.T) * sigmoid_dash
grad_V = x.T.dot(delta1)

W = -eta*grad_W
V = -eta*grad_V

print(W)
print(V)
