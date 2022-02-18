#basic multithreading using 
#1. "threading" library
#2. thread.start() and thread.join()

import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

threads_list = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads_list.append(t)  
  
for thread in threads_list:
  thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
