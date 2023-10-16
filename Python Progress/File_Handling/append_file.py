"""
Append to a file :-
    -> You can use the 'a' (append) mode when opening a file to add content to
        the end of an existing file without overwriting the existing content.
    -> If the file doesn't exist, a new file will be created.
    -> Use the write() method to add content to the file,
        and it will be added at the end of the file.
"""


print("3) Append to a file")
with open('myfile.txt', 'a') as f:
    f.write("New content\n")
