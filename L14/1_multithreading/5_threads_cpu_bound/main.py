import sys
from functools import partial
from threading import Thread
from timeit import timeit

REPEAT_NUMBER = int(sys.argv[1])

def main():
    threads = []
    for num in range(REPEAT_NUMBER):
        t = Thread(target=partial(pow, num, 2))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

print(timeit(main, number=1))
