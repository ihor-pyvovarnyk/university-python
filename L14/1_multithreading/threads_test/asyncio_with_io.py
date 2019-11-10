import asyncio
import math
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from random import randint
from threading import Thread
from timeit import timeit
from time import sleep


async def do():
    num = randint(0, 100)
    math.sqrt(num)
    await asyncio.sleep(.01)


async def async_main():
    await asyncio.gather(*[
        do()
        for _ in range(10000)
    ])


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())

time = timeit(main, number=1)
print(time)
