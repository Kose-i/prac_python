#!/usr/bin/env python3
import numpy as np

def test1():
    print("\ntest1")
    x = np.array([1,2,3,4,5])
    print(x)
    
    print("np.mean(x)=",np.mean(x)) # average
    print("np.var(x)=",np.var(x)) # dispertion
    print("np.std(x)=",np.std(x)) # standard diviation

    x = np.arange(5)
    print("\nx=np.arange(5)")
    print("x=",x)

    x = np.arange(1, 3, 0.2)
    print("\nx=np.arange(1,3,0.2)")
    print("x=",x)
    print("x.dtype=", x.dtype)

    x = np.array([1,2,3], dtype=float)
    print("\nx = np.array([1,2,3], dtype=float)")
    print("x=",x)


def test2():
    print("\ntest2")

if __name__=='__main__':
    test1()
    test2()

