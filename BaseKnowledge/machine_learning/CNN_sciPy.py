from scipy import signal

x = np.array([[1,1,2,1,0,0],[0,0,1,1,2,0],[0,0,0,1,2,1],[0,0,0,1,3,2],[1,1,1,3,2,0],[2,2,3,2,1,0]])

f = np.array([[0,1,1],[0,1,1],[0,1,1]])

signal.correlate(x, f, 'valid')
