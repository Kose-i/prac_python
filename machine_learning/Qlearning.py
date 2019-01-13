import numpy as np

#position
S = np.array([0,1,2,3])

#action
A = np.array([0,1])

#reward
R = np.array([[1,-20],[4,-1],[0,25],[0,0]])

#move to
S1 = np.array([[1,2],[3,0],[0,3],[None,None]])

#go to pre
p = 0.5
#study rate
alpha = 0.01
#rate
gamma = 0.8
#trying num
n = 3000

#initialize table
Q = np.zeros(R.shape)

# detect by using probability
def pi(p):
  if np.random.uniform(0,1) <= p:
    return 0 # forward
  else:
    return 1 # back

def q_learning():
  s = S[0]
  a = 0
  while S1[s,a] != None:
    a = pi(p)
    max_q = max(Q[S1[s,a],0], Q[S1[s,a],1])
    td = R[s,a] + gamma * max_q - Q[s,a]
    Q[s,a] += alpha*td
    s = S1[s,a]
  print(Q[0,0],Q[0,1])

for i in range(n):
  q_learning()

