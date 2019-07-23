import sympy as sp

sp.init_printing()
"""
problem:
2*x + 3*y = 1
1*x + 2*y = 1

answer:
x = -1
y =  1
"""
sp.var('x, y')
eq1=sp.Eq(2*x+3*y, 1)
eq2=sp.Eq(1*x+2*y, 1)
print(sp.solve ([eq1, eq2], [x, y]) )
#print(x,y)
