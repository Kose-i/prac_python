#!/usr/bin/env python3

import numpy as np

def test1():
    print("\ntest1")
    a = np.array([[3,1,1],[1,2,1],[0,-1,1]])
    print("\na=",a)
    print("\nnp.linalg.inv(a)=",np.linalg.inv(a))
    """
    (3 1 1)(x) (1)
    (1 2 1)(y)=(2)
    (0-1 1)(z) (3) solve x,y,z
    """
    b = np.array([1,2,3])
    print("\na=",a)
    print("b=",b)
    print("x,y,z=np.linalg.solve(a,b)=",np.linalg.solve(a,b))



if __name__=='__main__':
    test1()
