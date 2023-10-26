class Test:
    def __init__(self):
        self.__m1 = 80
        self.__m2 = 60
        self.__m3 = 90

    def __private_marks(self):
        print(f"Marks 1 = {self.__m1}")
        print(f"Marks 2 = {self.__m2}")
        print(f"Marks 3 = {self.__m3}")


t = Test()
# print(t.__m1)
# print(t.__m2)
# print(t.__m3)
# t.__private_marks()
# All the above statement gives error !
# Because we can not directly use the private method & private variable outside the class.
# To resolve this error, we can use Name Mangling

print("\n----- Calling Private Method Using Name Mangling -----")
t._Test__private_marks()

print("\n----- Calling Private Variable Using Name Mangling -----")
print(t._Test__m1)
print(t._Test__m2)
print(t._Test__m3)
