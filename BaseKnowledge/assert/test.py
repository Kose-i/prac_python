#! /usr/bin/env python3

# -O (optimized) を指定することで, assertは無視される
# python3 test.py -> Fail
# python3 -O test.py -> Success

if __name__=='__main__':
    a = 3
    assert(a != 3)
    print(a)

