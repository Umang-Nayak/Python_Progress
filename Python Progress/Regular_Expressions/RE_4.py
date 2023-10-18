"""
re.fullmatch() :-
    Determines if the entire string matches the regular expression pattern, returning a match object or None.
"""
import re

txt = "Umang Nayak"
print("Text =",txt)
ptn = input("Enter Full Matching Pattern = ")
ans = re.fullmatch(ptn, txt)

if ans:
    print("Congratulation Full Pattern Match !!!")
    print("Search object =", ans)
    print("Start & End Position =", ans.span())
    print("Starting Position =", ans.start())
    print("Ending Position =", ans.end())
    print("Matched Pattern =", ans.group())
else:
    print("Your pattern is not matching to text !!!")
