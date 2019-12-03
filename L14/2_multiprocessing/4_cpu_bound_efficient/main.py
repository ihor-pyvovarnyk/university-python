import sys
from multiprocessing import Process
from timeit import timeit

REPEAT_NUMBER = int(sys.argv[1])
CHULD_PROCESSES_NUMBER = int(sys.argv[2])
REPEATS_PER_PROCESS = int(REPEAT_NUMBER / CHULD_PROCESSES_NUMBER)

def cpu_bound_function(repeat_num):
    for num in range(repeat_num):
        pow(num, 2)

def main():
    processes = []
    for num in range(CHULD_PROCESSES_NUMBER):
        p = Process(target=cpu_bound_function, args=(REPEATS_PER_PROCESS,))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

print(timeit(main, number=1))
