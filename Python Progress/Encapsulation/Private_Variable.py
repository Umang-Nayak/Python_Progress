class MyClass:
    def __init__(self):
        self.__name = "Umang"
        self.__age = 20
        self.__gender = "Male"

    def __private_data(self):
        print(f"NAME = {self.__name}")
        print(f"AGE = {self.__age}")
        print(f"GENDER = {self.__gender}")

    def show_data(self):
        print("---------- Calling Private Method ----------")
        self.__private_data()


m = MyClass()
m.show_data()

# m.__private_data()
# Above Statement Gives Error, Because we can not directly use the private method outside the class !

# print(m.__name)
# Above Statement Gives Error, Because we can not directly use the private method outside the class !
