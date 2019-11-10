import sys
from multiprocessing.pool import ThreadPool
from timeit import timeit
import requests

REPEAT_NUMBER = int(sys.argv[1])
NUMBER_OF_WORKERS = 3

def main():
    pool = ThreadPool(NUMBER_OF_WORKERS)
    with pool:
        results = pool.map(make_request, REPEAT_NUMBER * [None])
        print(f'Number of results: {len(results)}')

def make_request(_required_but_unused_argument):
    return requests.get('http://httpbin.org/delay/1').json()

print(timeit(main, number=1))
