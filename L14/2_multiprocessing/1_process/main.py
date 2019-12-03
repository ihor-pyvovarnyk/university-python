from multiprocessing import Process
from time import sleep

def function_to_execute_in_child_process():
    sleep(10)

sleep(10)
process = Process(target=function_to_execute_in_child_process)
process.start()
process.join()
