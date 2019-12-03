import sys
from multiprocessing import Pool
from timeit import timeit

REPEAT_NUMBER = int(sys.argv[1])
POOL_SIZE = int(sys.argv[2])

def cpu_bound_function(num):
    pow(num, 2)

def main():
    with Pool(POOL_SIZE) as pool:
        pool.map(cpu_bound_function, range(REPEAT_NUMBER))

print(timeit(main, number=1))
