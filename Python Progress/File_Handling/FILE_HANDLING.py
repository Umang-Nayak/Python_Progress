"""
File Handling :-
    1) File handling is the process of creating, reading, writing, and manipulating files.
    2) Before performing any task across the file we have to open the file.
        syntax - open("file_name", "file_mode")
    3) After performing the task across the file, the file has to be closed.
        syntax - file.close()
    4) If we don't want to write a close syntax of the file, we can use "with" keyword.
        with open('File_name', 'file_mode') as any_name:

To open a file, we can use the open() function,
which takes the file name and mode as arguments.

'r' : Read (default mode)
'w' : Write (creates a new file or truncates an existing file)
'a' : Append (creates a new file or appends to an existing file)
'b' : Binary mode (e.g., 'rb' or 'wb')
"""

print("Example :- ")
f = open('myfile.txt', 'r')  # Opens a file in read mode
print(f)  # Print the object of file
print(f.read())  # Print the content of file
print(type(f.read()))  # Print the type of file
f.close()  # Close a file





