import sys
from concurrent.futures import ThreadPoolExecutor
from timeit import timeit
import requests

REPEAT_NUMBER = int(sys.argv[1])
NUMBER_OF_WORKERS = 3

def main():
    pool = ThreadPoolExecutor(max_workers=NUMBER_OF_WORKERS)
    with pool:
        results_futures = []
        for _ in range(REPEAT_NUMBER):
            results_futures.append(pool.submit(make_request, delay=1))
        results = [fut.result() for fut in results_futures]
        print(f'Number of results: {len(results)}')

def make_request(delay):
    return requests.get(f'http://httpbin.org/delay/{delay}').json()

print(timeit(main, number=1))
