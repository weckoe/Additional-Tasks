import threading
from random import randint
import time


def bubble(array):
    ARRAY_LEN = len(array)
    print(threading.currentThread().getName() + '\n')
    for i in range(ARRAY_LEN):
        for j in range(0, ARRAY_LEN-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

if __name__ == '__main__':
    start = time.time()
    for k in range(7):
        arr = [randint(1, 9) for n in range(10000)]
        thr = threading.Thread(target=bubble, args=(arr,))
        thr.start()
        thr.join()
        print(f'{k} after', arr)
    end = time.time() - start
    print(end)
        
        
