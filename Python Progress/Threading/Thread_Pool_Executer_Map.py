import time
from concurrent.futures import ThreadPoolExecutor


def check_time(seconds):
    print(f"\nSleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


my_list = [3, 1, 5, 4, 2]
with ThreadPoolExecutor() as tpe:
    results = tpe.map(check_time, my_list)

    for i in results:
        print(i)

