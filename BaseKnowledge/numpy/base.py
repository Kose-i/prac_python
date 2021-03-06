#!/usr/bin/env python3
import numpy as np

def test1():
    print("\ntest1")
    x = np.array([1,2,3,4,5])
    print(x)
    
    print("np.sum(x)=",np.sum(x)) # sum
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

def test4():
    print("\ntest4")
    a = np.array([[1,1,1],[1,1,1]])#2*3
    print("\na=", a)
    b = np.array([[2,2,2,2],[2,2,2,2]])#2*4
    print("\nb=", b)
    print("\nnumpy.c_[a,b]=",np.c_[a,b])
    a = np.array([[1,1,1],[1,1,1]])#2*3
    print("\na=", a)
    b = np.array([[2,2,2],[2,2,2],[2,2,2]])#3*3
    print("\nb=", b)
    print("\nnumpy.r_[a,b]=",np.r_[a,b])

def test5():
    print("\ntest5")
    a = np.arange(3.,8.)
    print("\na=",a)
    print("\nnp.exp(a)=",np.exp(a))
    print("\nnp.log(a)=",np.log(a))
    print("\nnp.sqrt(a)=",np.sqrt(a))
    print("\na+3=",a+3)
    print("\na*3=",a*3)
    print("\na>4=",a>4)
    print("\na[a>4]=",a[a>4])

    print("\nnp.arange(9.).reshape(3,3)=", np.arange(9.).reshape(3,3))

def test6():
    print("\ntest6")
    a = np.arange(4)
    b = np.arange(3,7)
    print("\na=",a)
    print("\nb=",b)
    print("\na+b=",a+b)
    print("\na*b=", a*b)
    print("\na@b=", a@b) # python3.5 latter
    print("\nnp.dot(a, b)=", np.dot(a, b))

if __name__=='__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

