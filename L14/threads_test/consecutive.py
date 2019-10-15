import math
from random import randint
from timeit import timeit

def main():
    sqrts = []
    for _ in range(100000):
        num = randint(0, 100)
        sqrts.append(math.sqrt(num))
    return sqrts

time = timeit(main, number=1)
print(time)
