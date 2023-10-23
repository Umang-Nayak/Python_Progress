import gc

# Enable the garbage collector (it's typically enabled by default)
gc.enable()


# Define a class that holds references
class DemoObject:
    def __init__(self, name):
        self.name = name


# Create objects and create reference cycles
a = DemoObject("Object A")
b = DemoObject("Object B")
a.ref = b  # Object A references Object B
b.ref = a  # Object B references Object A

# Remove references to the objects
a = None
b = None

# Run the garbage collector (you can also let Python handle this automatically)
gc.collect()

# Check the number of collected objects
print(f"Collected {gc.collect()} unreachable objects.")

# Check the current count of tracked objects
print(f"Currently, there are {len(gc.get_objects())} tracked objects.")
