# Q.1) How to iterate over 2 lists at the same time. [Sorted Output] [with single iteration]

try:
    size1 = int(input("Enter Size for 1st List = "))
    ml1 = []
    for i in range(size1):
        x1 = int(input("Enter Value = "))
        ml1.append(x1)
    print("1st List =", ml1)

    size2 = int(input("Enter Size for 2nd List = "))
    ml2 = []
    for i in range(size2):
        x2 = int(input("Enter Value = "))
        ml2.append(x2)
    print("2nd List =", ml2)

    ml1.extend(ml2)
    print("Concatenating List1 & List2 = ", ml1)

    for i in range(len(ml1)):
        for j in range(len(ml1)):
            if ml1[i] < ml1[j]:
                temp = ml1[i]
                ml1[i] = ml1[j]
                ml1[j] = temp
    print("Ascending Order List =", ml1)

    for i in range(len(ml1)):
        for j in range(len(ml1)):
            if ml1[i] > ml1[j]:
                temp = ml1[i]
                ml1[i] = ml1[j]
                ml1[j] = temp
    print("Descending Order List =", ml1)

except ValueError:
    print("Enter Integer Value Only !!!")

except:
    print("Something Wrong Happened !!!")


# Q.2) Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

try:
    def palindrome(size):
        ml = []
        for i in range(size):
            x = int(input("Enter Value = "))
            ml.append(x)
        print("List =", ml)

        if ml == ml[::-1]:
            return True
        else:
            return False

    s = int(input("Enter Size of your List = "))
    ans = palindrome(s)
    print(ans)

except ValueError:
    print("Enter Integer Value Only !!!")

except:
    print("Something Wrong !")

finally:
    print()
    print("Thank you !")


"""
2nd Logic :- 

list1 = [0, 0, 3, 4, 3, 0, 0]
print(list1.reverse())


if list1 == list1.reverse():
    print("Palindrome")
else:
    print("Not Palindrome")
"""

"""
3rd Logic :-

list1 = [0, 0, 3, 4, 3, 0, 0]
list2 = []

for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])

if list1 == list2:
    print("Palindrome")
else:
    print("Not Palindrome")
"""

"""
4th Logic :-

list1 = [0, 0, 3, 4, 3, 0, 0]

k = len(list1)-1

for i in list1:
    if i == list1[k]:
        k = k - 1

if k == -1:
    print("Palindrome")
else:
    print("Not Palindrome")
"""

