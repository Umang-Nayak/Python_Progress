"""
Read from a file :-
    We can use various methods to read the content of a file,
    such as read(), readline(), or readlines().
"""

print("1) Reading from a file")


print()
print("read() method :-")
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)


print()
print("readline() method :-")
with open('myfile.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')  # 'end' parameter to avoid double spacing (newline)
        line = file.readline()


print()
print("readlines() method :-")
with open('myfile.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')  # 'end' parameter to avoid double spacing (newline)
