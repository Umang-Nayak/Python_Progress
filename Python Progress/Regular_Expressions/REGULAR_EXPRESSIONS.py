"""
Regular Expression :-
    -> Regular expressions also referred as "regex" is used
        for text processing and pattern matching.
    -> To use Regular Expression, we have to import "re" module in python.
    -> To search pattern in text, we have to "r" before that string,
        so that string change from normal string to a raw string
    -> And that raw string contain Metacharacters in regular expression.

"""
import re

txt = """
Umang Nayak is 20 years old 
and he is doing python internship
in Sigma Solve Pvt. Ltd. Company !
Peter Parker is 35 years old and 
he is a secret power called spider web,
he is also known as spider man !
"""

print(txt)
ptn = input("Enter Pattern You Want To Find = ")
r1 = re.search(ptn, txt)

if r1:
    print("Match Found :", r1.group())
else:
    print("Pattern Not Found !")
