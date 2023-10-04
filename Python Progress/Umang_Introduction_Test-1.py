# Q.1) Write a Python program that removes vowels from a string.

s = input("Enter String = ")

if s.isalpha():
    c = 0
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            c = c + 1
        elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            c = c + 1
        else:
            if i != " ":
                print(i, end="")

    print()
    print("Total Vowel =", c)

else:
    print("Enter Only String !!")


# Q.2) Python program to get the Fibonacci series between 0 and 50.

x = input("Enter Value = ")
if x.isdigit():
    n = int(x)
    f1 = 0
    f2 = 1

    while True:
        if f1 <= n:
            print(f1)
        else:
            break

        f3 = f1 + f2
        f1 = f2
        f2 = f3

else:
    print("Enter Only Digits !!!")
