import math
from random import randint
from timeit import timeit
from time import sleep

def main():
    sqrts = []
    for _ in range(10000):
        num = randint(0, 100)
        sqrts.append(math.sqrt(num))
        sleep(.01)
    return sqrts

time = timeit(main, number=1)
print(time)
