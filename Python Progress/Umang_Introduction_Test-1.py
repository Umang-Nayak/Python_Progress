# Q.1) Write a Python program that removes vowels from a string.

s = input("Enter String = ")

c = 0

for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        c = c+1
    elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        c = c+1
    else:
        if i != " ":
            print(i, end="")

print()
print("Total Consonant =", c)

# Q.2) Python program to get the Fibonacci series between 0 and 50.

n = int(input("Enter Value = "))

f1 = 0
f2 = 1

print(f1)
print(f2)

while True:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    if f3 <= n:
        print(f3)
    else:
        break
