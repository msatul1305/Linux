# same as multithreading3 but using map
#Using:
#1. concurrent.futures library
#Using ThreadPoolExecutor() as executor
#Using :
#submit method: If we want to execute a function once at a time - Submit method executes a function once at a time and retuns a future object
#Finally, print results of each submit using as_completed() method

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
