import math
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from random import randint
from threading import Thread
from timeit import timeit
from time import sleep


def main():
    sqrts = []
    def do():
        num = randint(0, 100)
        sqrts.append(math.sqrt(num))
        sleep(.01)
    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = []
        for _ in range(10000):
            futures.append(executor.submit(do))
        for future in futures:
            sqrts.append(future.result())
    return sqrts

time = timeit(main, number=1)
print(time)
