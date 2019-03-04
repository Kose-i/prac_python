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
    a = np.array([[1,2,3],[4,5,6]])
    print("a=",a)
    a = np.arange(15.).reshape(3,5)
    print("a=",a)
    print("a.shape=", a.shape)
    print("a.ndim=", a.ndim)
    print("a.size=", a.size)
    b = a.reshape(5, -1)
    print("b = a.reshape(5, -1)=", b)
    print("b.ravel()=", b.ravel())
    print("b[:, np.newaxis]=", b[:,np.newaxis])
    print("b[:, None]=", b[:, None])

def test3():
    print("\ntest3")
    print("\nnp.zeros((2,3))=",np.zeros((2,3)))
    print("\nnp.ones((3,3))=",np.ones((3,3)))
    print("\nnp.ones((2,2))*3=", np.ones((2,2))*3)
    print("\nnp.empty((5,5))=",np.empty((5,5)))
    print("\nnp.linspace(0,1,10)=", np.linspace(0,1,10))

if __name__=='__main__':
    test1()
    test2()
    test3()

