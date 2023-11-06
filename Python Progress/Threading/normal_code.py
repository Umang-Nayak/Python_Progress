import time


# Indicates some task being done
def check_time(seconds):
    print(f"\nSleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Sleeping Done")


time1 = time.perf_counter()
check_time(5)
check_time(4)
check_time(3)
time2 = time.perf_counter()

print(f"Total Time = {time2 - time1}")
