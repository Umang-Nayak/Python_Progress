"""
concurrent.futures :-
    This module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads,
using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
Both implement the same interface, which is defined by the abstract Executor class.
"""
import time
from concurrent.futures import ThreadPoolExecutor


def check_time(seconds):
    print(f"\nSleeping for {seconds} seconds")
    time.sleep(seconds)
    return "Sleeping Done"


with ThreadPoolExecutor() as tpe:
    f1 = tpe.submit(check_time, 5)
    f2 = tpe.submit(check_time, 4)
    f3 = tpe.submit(check_time, 3)

    print(f1.result())
    print(f2.result())
    print(f3.result())
    