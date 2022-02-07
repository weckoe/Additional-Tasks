import threading
import time
import asyncio
from random import randint
from multiprocessing import Process


def bubble(array):
    ARRAY_LEN = len(array)
    for i in range(ARRAY_LEN):
        for j in range(0, ARRAY_LEN - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


async def bubble_with_async_1(array):
    bubble(array)
    await asyncio.sleep(10)
    print('first bubble')


async def bubble_with_async_2(array):
    bubble(array)
    await asyncio.sleep(0)
    print('second bubble')


async def bubble_with_async_3(array):
    bubble(array)
    await asyncio.sleep(5)
    print('third bubble')


async def bubble_with_async_4(array):
    bubble(array)
    await asyncio.sleep(0)
    print('fourth bubble')


async def bubble_with_async_5(array):
    bubble(array)
    await asyncio.sleep(15)
    print('last one')


def runInParallel(*fns):
    """function for making multiprocessing"""
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


if __name__ == '__main__':
    # threading
    start_1 = time.time()
    for k in range(7):
        arr = [randint(1, 9) for n in range(10000)]
        thr = threading.Thread(target=bubble, args=(arr,))
        thr.start()
        thr.join()
    end_1 = time.time() - start_1
    print(end_1)
    # asyncio
    start_2 = time.time()
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(bubble_with_async_1([randint(1, 9) for n in range(10000)])),
        loop.create_task(bubble_with_async_2([randint(1, 9) for n in range(10000)])),
        loop.create_task(bubble_with_async_3([randint(1, 9) for n in range(10000)])),
        loop.create_task(bubble_with_async_4([randint(1, 9) for n in range(10000)])),
        loop.create_task(bubble_with_async_5([randint(1, 9) for n in range(10000)])),
    ]
    wait_tasks = asyncio.wait(tasks)
    loop.run_until_complete(wait_tasks)
    loop.close()
    end_2 = time.time() - start_2
    print(end_2)
    # multiprocessing
    start_3 = time.time()
    runInParallel(
        bubble([randint(1, 9) for n in range(10000)]),
        bubble([randint(1, 9) for n in range(10000)]),
        bubble([randint(1, 9) for n in range(10000)]),
        bubble([randint(1, 9) for n in range(10000)]),
        bubble([randint(1, 9) for n in range(10000)]),
    )
    end_3 = time.time() - start_3
    # synchronously
    start_4 = time.time()
    bubble([randint(1, 9) for n in range(10000)])
    bubble([randint(1, 9) for n in range(10000)])
    bubble([randint(1, 9) for n in range(10000)])
    bubble([randint(1, 9) for n in range(10000)])
    bubble([randint(1, 9) for n in range(10000)])
    end_4 = time.time() - start_4
    print(end_3)
