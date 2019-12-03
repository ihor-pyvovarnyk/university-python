import sys
from multiprocessing import Process
from timeit import timeit

REPEAT_NUMBER = int(sys.argv[1])

def main():
    processes = []
    for num in range(REPEAT_NUMBER):
        p = Process(target=pow, args=(num, 2))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

print(timeit(main, number=1))
