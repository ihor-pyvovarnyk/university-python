import os
from multiprocessing import Pool

def print_process_id(_unused_agument):
    pid = os.getpid()
    print(f'PID: {pid}')

if __name__ == '__main__':
    with Pool(1) as pool:
        pool.map(print_process_id, range(5))