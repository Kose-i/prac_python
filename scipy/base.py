#!/usr/bin/env python3

from scipy import sparse
from scipy import linalg

def test1():
    print("\ntest1")
    a=sparse.lil_matrix((4,5))
    print("a=sparse.lil_matrix((4,5))=", sparse.lil_matrix((4,5)).toarray())
    print("type(a)=", type(a))
    a[0,1] = 1
    a[0,3] = 2
    a[2,2] = 3
    a[3,4] = 4
    print("\na[0,1]=1, a[0,3]=2, a[2,2]=3, a[3,4]=4")
    print("a=",a.toarray())

    b = sparse.lil_matrix((5,4))
    b[0,2] = 1
    b[1,2] = 2
    b[2,3] = 3
    b[3,3] = 4
    print("\nb = sparse.lil_matrix((5,4)),b[0,2]=1, b[1,2]=2,b[2,3]=3,b[3,3]=4")
    print("b=",b.toarray())

    print("\na.dot(b)=", a.dot(b).toarray())

    a_csr = a.tocsr()
    b_csr = b.tocsr()
    print("\ntype(a.tocsr())=", type(a_csr))
    print("a.tocsr().dot(b.tocsr())=",a_csr.dot(b_csr).toarray())

    a_csc = a.tocsc()
    b_csc = b.tocsc()
    print("\ntype(a.tocsc())=", type(a_csc))
    print("a.tocsc().dot(b.tocsc())=",a_csc.dot(b_csc).toarray())

def test2():
    print("\ntest2")
    """
    (3 1 1)(x) (1)
    (1 2 1)(y)=(2)
    (0-1 1)(z) (3) solve x,y,z
    """
    a = np.array([[3,1,1],[1,2,1],[0,-1,1]])
    b = np.array([1,2,3])
    print("\na=",a)
    print("b=",b)
    lu, p = linalg.lu_factor(a)
    print("lu, p = linalg.lu_factor(a)")
    print("x,y,z=linalg.lu_solve((lu, p), b)",linalg.lu_solve((lu, p),b))

if __name__=='__main__':
    test1()
    test2()
