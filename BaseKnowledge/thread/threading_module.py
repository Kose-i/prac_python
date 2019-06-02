#! /usr/bin/env python3

import threading
import time

def thread1_func():
    # thread の名前を取得
    print('start 1')
    time.sleep(5)
    print('end 1')

def thread2_func():
    print('start 2')
    time.sleep(5)
    print('end 2')

if __name__ == '__main__':
    # スレッドに workder1 関数を渡す
    thread1 = threading.Thread(target=thread1_func)
    thread2 = threading.Thread(target=thread2_func)
    # スレッドスタート
    thread1.start()
    thread2.start()
    print('started all')
