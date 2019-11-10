import sys
from threading import Thread
from timeit import timeit
import requests

REPEAT_NUMBER = int(sys.argv[1])

def main():
    threads = []
    for num in range(REPEAT_NUMBER):
        t = Thread(target=make_request)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def make_request():
    requests.get('http://httpbin.org/delay/1').json()

print(timeit(main, number=1))
