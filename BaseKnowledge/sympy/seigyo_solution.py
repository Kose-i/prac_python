import sympy as sp
import numpy as np

sp.init_printing()
"""
problem:
\omega*(x+y)/(1-\omega*\omega*x*y) = phy(\omega)

answer:T1, T2 <= x, y
"""
data_g = [[1, 16.514], [2, 31.765], [3, 43.517],[3.2,42.857],[3.25,45],[3.5,46.154], [4,42.961], [5,59.45], [6,44.703], [7, 69.231],[8,70.949],[9,76.721],[10,79.266]]
sp.var('x, y')

for i,e in enumerate(data_g):
  j = i+1
  while j != len(data_g):
    eq1=sp.Eq(data_g[i][0]*(x+y)/(1-data_g[i][0]*data_g[i][0]*x*y), np.tan(data_g[i][1]))
    eq2=sp.Eq(data_g[j][0]*(x+y)/(1-data_g[j][0]*data_g[j][0]*x*y), np.tan(data_g[j][1]))
    print("w[rad/s]:", i, j)
    print(sp.solve ([eq1, eq2], [x, y]) )
    j += 1
