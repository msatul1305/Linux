#Using:
#1. concurrent.futures library
#Using ThreadPoolExecutor() as executor
#Using :
#submit method: If we want to execute a function once at a time - Submit method executes a function once at a time and retuns a future object
#Finally, print results of each submit using as_completed() method

# Difference between threading.Thread() and ThreadpoolExecutor(): ThreadPoolExecutor() provides additional features like future objects, which represent the result of an asynchronous computation.
# and when to use what?:
    # Use threading.Thread() when you need fine-grained control over individual threads.
    # It is suitable for scenarios where you want to manually create and manage threads, control their lifecycle, and have low-level control over thread-specific operations.

    # Use ThreadPoolExecutor() when you have a set of tasks that can be executed concurrently and you want to abstract away the details of managing individual threads.
    # It is suitable for scenarios where you want to submit tasks to a pool of threads and let the executor handle the thread creation, management, and scheduling of tasks.

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1.5) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
      print(f.result())

    # for result in results:
    #     print(result)
 

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
