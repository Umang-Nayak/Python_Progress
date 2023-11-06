"""
Multithreading :-
    Multithreading is a technique that allows to execute multiple tasks simultaneously within a single Python program.
    This can be useful for improving the performance of your program, especially for tasks that are I/O-bound,
    such as making network requests or reading from files.


Benefits :-
    -> Improved performance
    -> Responsiveness
    -> Simpler code
"""

import threading
import time


# Indicates some task being done
def check_time(seconds):
    print(f"\nSleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Sleeping Done")


t1 = threading.Thread(target=check_time, args=[5])
t2 = threading.Thread(target=check_time, args=[4])
t3 = threading.Thread(target=check_time, args=[3])

time1 = time.perf_counter()
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()

print(f"Total Time = {time2 - time1}")
