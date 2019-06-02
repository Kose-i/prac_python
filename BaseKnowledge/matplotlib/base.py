#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def test1():
    x = np.array([0,1,2,3])
    y = np.array([3,7,4,8])

    plt.plot(x,y, color="r")
    plt.title("test1")
    plt.show()

def test2():
    x = np.array([0,1,2,3])
    y = np.array([3,7,4,8])

    plt.title("test2")
    plt.scatter(x,y, color="r")
    plt.show()

def test3():
    x = np.linspace(-5, 5, 50)
    y1 = x**2
    y2 = (x-2)**2

    plt.title("test3")
    plt.plot(x,y1, color="r")
    plt.plot(x,y2, color="k",linestyle="--")
    plt.show()

def test4():
    np.random.seed(0)
    l =[]
    for _ in range(1000):
        l.append(np.random.randint(1,7,size=10).sum())
    plt.title("test4")
    plt.hist(l,20,color="gray")
    plt.show()

def test5():
    x = np.linspace(-5, 5, 300)
    sin_x = np.sin(x)
    cos_x = np.cos(x)

    #fig, axes = plt.subplots(2,1)
    fig, axes = plt.subplots(1,2)
    axes[0].set_ylim([-1.5,1.5])
    axes[1].set_ylim([-1.5,1.5])
    axes[0].plot(x, sin_x, color="r")
    axes[1].plot(x, cos_x, color="k")

    plt.title("test5")
    plt.show()

def test6():
    def f(x, y):
        return x**2 + (y**2/4)
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    xmesh, ymesh = np.meshgrid(x, y)
    print("xmesh=",xmesh)
    print("ymesh=",ymesh)

    #z = f(xmesh.ravel(), ymesh.ravel()).reshape(xmesh.shape)
    #plt.contour(x, y, z, colors="k",levels=[1,2,3,4,5])

    z = f(xmesh, ymesh)
    colorslabel = ["0.1", "0.3", "0.5", "0.7"]
    levelslabel = [1,2,3,4,5]
    plt.contourf(x, y, z, colors = colorslabel ,levels = levelslabel)

    plt.title("test6")
    plt.show()

if __name__=='__main__':
    #test1()
    #test2()
    #test3()
    #test4()
    #test5()
    test6()
