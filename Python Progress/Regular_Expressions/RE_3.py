"""
re.findall() :-
    The re.findall() function is used to find all non-overlapping matches of a
        regular expression pattern in a string and return them as a list of strings.

re.finditer() :-
    -> The re.finditer() function is used to find all non-overlapping matches of a
        regular expression pattern in a string and return an iterator of match objects.
    -> This is useful when you need more than just the matched strings,
        it allows you to access additional information about each match,
        such as the match's position in the original string.
"""
import re

txt = """Umang = umangnayak49@gmail.com
Hemil = hemilsoni12345@yahoo.com
tirth = tirthvyas13579@gmail.com
aman = aman@yahoo.com
"""

ptn = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

ans = re.findall(ptn, txt)
print("List of all matched pattern =", ans)

print("-------------------------------------------------------")
c = 0
for i in ans:
    c = c + 1
    print(f"Matched Pattern {c} = {i}")

print("-------------------------------------------------------")
ans = re.finditer(ptn, txt)
for i in ans:
    print(i)


