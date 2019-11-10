from threading import Thread

def function_to_execute_in_thread():
    print(f"CUSTOM THREAD: print 1")
    print(f"CUSTOM THREAD: print 2")

thread = Thread(target=function_to_execute_in_thread)

print("MAIN THREAD: Before start")
thread.start()
print("MAIN THREAD: After start")
thread.join()
print("MAIN THREAD: After join")