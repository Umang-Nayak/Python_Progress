"""
re.match() :-
    re.match() is used to determine if the regular expression pattern matches at the beginning of a string.
    It returns a match object if a match is found at the beginning of the string, or None if no match is found.

group(): Returns the string matched by the regular expression.
start(): Returns the starting position of the match.
end(): Returns the ending position of the match.
span(): Returns a tuple containing the start and end positions of the match.
"""

import re

txt = """Jay Shree Ram !!!
My name is Umang Nayak.
umangnayak@gmail.com is my email-id.
8401598691 is my phone number.
"""

ptn = "Jay Shree Ram"
ans = re.match(ptn, txt)
print("Search object =", ans)
print("Start & End Position =", ans.span())
print("Starting Position =", ans.start())
print("Ending Position =", ans.end())
print("Matched Pattern =", ans.group())

