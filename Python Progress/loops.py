# for loop
print("Multiplication Table With For Loop")
n = int(input("Enter Number = "))
for i in range(1,11):
    print(n,"X",i,"=",n*i)



# while loop
print("Multiplication Table With while Loop")
n = int(input("Enter Number = "))
i=1
while(i<=10):
    print(n,"X",i,"=",n*i)
    i = i + 1



# Patterns
print("Pattern 1 :-")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

print("Pattern 2 :-")
for i in range(5):
    for j in range(i + 1):
        print(i, end="")
    print()

print("Pattern 3 :-")
for i in range(5):
    for j in range(i + 1):
        print(j, end="")
    print()