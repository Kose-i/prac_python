#!/usr/bin/env python3
import numpy as np

def test1():
    print("\ntest1")
    print("numpy.random.rand()=",np.random.rand())
    print("numpy.random.rand(2,5)=",np.random.rand(2,5))
    print("numpy.random.rand(5)=",np.random.rand(5))
    print("numpy.random.randint(4)=",np.random.randint(4))
    print("numpy.random.randint(2,5)=",np.random.randint(2,5))
    print("numpy.random.randint(4, size=(3,3))=",np.random.randint(4,size=(3,3)))

def test2():
    print("\ntest2")
    print("numpy.random.seed(1)")
    np.random.seed(1)
    print("numpy.random.rand(3)=",np.random.rand(3))
    print("numpy.random.seed(1)")
    np.random.seed(1)
    print("numpy.random.rand(3)=",np.random.rand(3))

def test3():
    print("\ntest3")
    print("rs1 = numpy.random.RandomState(10)")
    print("rs2 = numpy.random.RandomState(10)")
    rs1 = np.random.RandomState(10)
    rs2 = np.random.RandomState(10)
    for i in range(3):
        print("num:",i+1, "  rs1.rand() = ", rs1.rand())
    for i in range(3):
        print("num:",i+1, "  rs1.rand() = ", rs2.rand())


if __name__=='__main__':
    test1()
    test2()
    test3()

