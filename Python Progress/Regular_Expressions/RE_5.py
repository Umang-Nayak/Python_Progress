import re


txt = "The rain in Spain"
x = re.findall("[a-m]", txt)  # Find all lower case characters alphabetically between "a" and "m"
print("1) ", x)


txt = "That will be 59 dollars"
x = re.findall("\d", txt)  # Find all digit characters
print("2) ", x)


txt = "hello planet hippo"
x = re.findall("h...o", txt)  # Here "..." means any 3 character
print("3) ", x)


txt = "Hello Umang Nayak"
x = re.findall("^Hello", txt)  # Check if the string starts with 'Hello'
if x:
    print("4) Yes, the string starts with =", x)
else:
    print("4) No match")


txt = "hello planet"
x = re.findall("planet$", txt)  # Check if the string ends with 'planet'
if x:
    print("5) Yes, the string ends with =", x)
else:
    print("5) No match")


txt1 = "helulalilo planet"
txt2 = "hello planet"
txt3 = "heo planet"
txt4 = "helo planet"

x1 = re.findall("he.*o", txt1)  # Here ".*" means match by 0 or more (any) characters
x2 = re.findall("he.*o", txt2)
x3 = re.findall("he.*o", txt3)
x4 = re.findall("he.*o", txt4)
print(f"6) All * matches = 1){x1}, 2){x2}, 3){x3}, 4){x4}")

y1 = re.findall("he.+o", txt1)  # Here ".+" means match by 1 or more (any) characters
y2 = re.findall("he.+o", txt2)
y3 = re.findall("he.+o", txt3)
y4 = re.findall("he.+o", txt4)
print(f"7) All + matches = 1){y1}, 2){y2}, 3){y3}, 4){y4}")

z1 = re.findall("he.?o", txt1)  # Here ".?" means match by 0 or 1 (any) characters
z2 = re.findall("he.?o", txt2)
z3 = re.findall("he.?o", txt3)
z4 = re.findall("he.?o", txt4)
print(f"8) All ? matches = 1){z1}, 2){z2}, 3){z3}, 4){z4}")


txt = "hello planet"
x = re.findall("he.{2}o", txt)  # Match exactly 2 (any) characters
print("9) ", x)


txt = "Everyone knows that Peter parker is spider-man !"
x = re.findall("Umang|Jonny|Peter|Stany", txt)  # Check if the string contains Umang or Jonny or Peter or Stany
print("10) ", x)
if x:
    print("11) Yes, there is at least one match !")
else:
    print("11) No match")


txt = "The rain in Spain"
x = re.findall("\AThe", txt)  # Check if the string starts with "The"
print("12) ", x)
if x:
    print("13) Yes, there is a match !")
else:
    print("13) No match")


txt = "The rain in Spain"
x1 = re.findall(r"\bain", txt)  # Check if "ain" is present at the beginning of a WORD
y1 = re.findall(r"\bra", txt)  # Check if "ra" is present at the beginning of a WORD
print("14) ", x1)
print("15) ", y1)
x2 = re.findall(r"\Bain", txt)  # Check if "ain" is present, but NOT at the beginning of a word
y2 = re.findall(r"\Bra", txt)  # Check if "ra" is present, but NOT at the beginning of a word
print("16) ", x2)
print("17) ", y2)


txt1 = "The rain in Spain"
txt2 = "My phone number is 100"
x1 = re.findall("\d", txt1)  # Check if the string contains any digits (numbers from 0-9)
x2 = re.findall("\d", txt2)
print("18) ", x1)
print("19) ", x2)
y1 = re.findall("\D", txt1)
y2 = re.findall("\D", txt2)
print("20) ", y1)
print("21) ", y2)


txt = "The rain      in Spain"
x = re.findall("\s", txt)  # Return a match at every white-space character
y = re.findall("\S", txt)  # Return a match at every NON white-space character
print("22) ", y)
print("23) ", x)

txt = "The rain in Spain"
# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)
x = re.findall("\w", txt)
print("24) ", x)
# Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.)
y = re.findall("\W", txt)
print("25) ", y)


txt = "The rain in Spain"
x = re.findall("Spain\Z", txt)  # Check if the string ends with "Spain"
print("26) ", x)
