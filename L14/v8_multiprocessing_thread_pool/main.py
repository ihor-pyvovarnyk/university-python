import sys
from multiprocessing.pool import ThreadPool
from timeit import timeit
import requests

REPEAT_NUMBER = int(sys.argv[1])
NUMBER_OF_WORKERS = 3

def main():
    pool = ThreadPool(NUMBER_OF_WORKERS)

    results = pool.map(make_request, REPEAT_NUMBER * ['http://httpbin.org/delay/1'])
    print(f'Number of results: {len(results)}')

    pool.terminate()
    pool.join()

def make_request(url):
    return requests.get(url).json()

print(timeit(main, number=1))
