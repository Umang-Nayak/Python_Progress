class Employee:
    def __init__(self):
        self.__EmpName = "UMANG"
        self.__EmpAge = 20
        self.__EmpDOB = "3rd May 2003"

    def get_Age(self):
        return self.__EmpAge

    def set_Age(self, age):
        if age < 18:
            print("Invalid Age")
        else:
            self.__EmpAge = age


e = Employee()
print("Old Age = ", e.get_Age())
new_age = int(input("Enter New Age = "))
print("New Age = ", e.get_Age())
