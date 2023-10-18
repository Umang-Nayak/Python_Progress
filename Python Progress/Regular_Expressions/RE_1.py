"""
re.search() :-
    re.search() is used for searching a string for a pattern.
    It returns a match object if a match is found, or None if no match is found.

group(): Returns the string matched by the regular expression.
start(): Returns the starting position of the match.
end(): Returns the ending position of the match.
span(): Returns a tuple containing the start and end positions of the match
"""

import re

txt = """
Good Morning all of you !!!
My name is Umang.
umangnayak@gmail.com is my email-id.
8401598691 is my phone number.
"""
# The given pattern is to find valid email id
ptn = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

ans = re.search(ptn, txt)
print("Search object =", ans)
print("Start & End Position =", ans.span())
print("Starting Position =", ans.start())
print("Ending Position =", ans.end())
print("Matched Pattern =", ans.group())
