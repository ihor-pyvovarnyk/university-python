import sys
from concurrent.futures import ThreadPoolExecutor
from timeit import timeit
import requests

REPEAT_NUMBER = int(sys.argv[1])
NUMBER_OF_WORKERS = 3

def main():
    pool = ThreadPoolExecutor(max_workers=NUMBER_OF_WORKERS)
    with pool:
        results = pool.map(make_request, REPEAT_NUMBER * ['http://httpbin.org/delay/1'])
        print(f'Results {type(results)}. Number of results: {len(list(results))}')

def make_request(url):
    return requests.get(url).json()

print(timeit(main, number=1))
