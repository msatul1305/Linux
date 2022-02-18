# same as multithreading3 but using map
# map returns the results instead of a future object(as in submit method) - It returns the result in the order that they were started i.e. 1, 2, 3, 4, 5 instead of the order that they got completed i.e. 1, 2, 3, 4, 5
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
