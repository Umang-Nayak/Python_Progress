str1='Hello'
str2="This will split all words into a list"
str3=""" hello
         boy """
list=["This","will","split","all","words","into","a","list"]

print(str3)

print("Lower case :- ",str1.lower())
print("Upper case :- ",str1.upper())
print("Split :- ",str2.split())
print("Find :- ",str2.find("all"))
print("Replace :- ",str2.replace("all","whole"))
print("Join :- ",".".join(list))



ok="hello and welcome to my world."
print(ok.capitalize())


a="8401598691"
x=a.isdigit();
print(x)

a="umang"
x=a.isalpha();
print(x)

x=ok.index("welcome");
print(x)


a = """
Hi Man,
Umang
Bhai
"""

for ok in a:
    print(ok)
