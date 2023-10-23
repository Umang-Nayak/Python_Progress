import gc

# Check if the garbage collector is enabled
if gc.isenabled():
    print("Garbage collector is enabled.")
else:
    print("Garbage collector is disabled.")

# Enable the garbage collector
gc.enable()
print("Garbage collector is now enabled.")

# Create some objects
a = [1, 2, 3]
b = "Hello, World"
c = 42

# Remove references to the objects
a = None
b = None
c = None

# Manually trigger garbage collection
print(gc.collect())
print("Garbage collection done.")

# Check the number of collected objects
print(f"Collected {gc.collect()} unreachable objects.")

# Check the current count of tracked objects
print(f"Currently, there are {len(gc.get_objects())} tracked objects.")

# Disable the garbage collector
print(gc.disable())
print("Garbage collector is now disabled.")
