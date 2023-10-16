"""
Write to a file :-
    We can use the write() method to add content to an
    existing file or create a new file if it doesn't exist.
"""
print("2) Writing to a file")

with open('myfile.txt', 'r') as file:
    print("Old Content :- ")
    print(file.read())

with open('myfile.txt', 'w') as f:
    f.write("This is a line of text.\n")
    f.write("Another line of text.\n")

with open('myfile.txt', 'r') as file:
    print("New Content :- ")
    print(file.read())
