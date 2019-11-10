import sys
from timeit import timeit
import requests

REPEAT_NUMBER = int(sys.argv[1])

def main():
    for _ in range(REPEAT_NUMBER):
        make_request()

def make_request():
    requests.get('http://httpbin.org/delay/1').json()

print(timeit(main, number=1))
