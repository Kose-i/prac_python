#!/usr/bin/env python3
import numpy as np

def func1():
    print("func1\n")
    data = np.random.randn(5)
    print("data now:", data)
    np.save('datafile/datafile1.npy', data)
    data = []
    print("data now:",data)
    data = np.load('datafile/datafile1.npy')
    print("data now:",data)

def func2():
    print("func2\n")
    data1 = np.random.randn(5)
    data2 = np.random.randn(10)
    print("data1 now:", data1)
    print("data2 now:", data2)
    np.savez('datafile/datafile2.npz', data1=data1, data2=data2)
    data1 = []
    data2 = []
    print("data1 now:", data1)
    print("data2 now:", data2)
    outputfile = np.load('datafile/datafile2.npz')
    print("outputfile:",outputfile)
    data1 = outputfile['data1']
    data2 = outputfile['data2']
    print("data1 now:", data1)
    print("data2 now:", data2)

if __name__=='__main__':
    func1()
    func2()
