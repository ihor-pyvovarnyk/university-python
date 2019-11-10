import math
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
    threads = []
    for _ in range(10000):
        t = Thread(target=do)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    return sqrts

time = timeit(main, number=1)
print(time)
