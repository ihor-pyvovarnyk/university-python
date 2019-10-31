import sys
from timeit import timeit

REPEAT_NUMBER = int(sys.argv[1])

def main():
    sqrts = []
    for num in range(REPEAT_NUMBER):
        sqrts.append(pow(num, 2))
    return sqrts

print(timeit(main, number=1))
