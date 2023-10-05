"""
Dictionary :-
    1) Dictionary is a collection of multiple Data type value in a key & value formate.
    2) Dictionary is mutable.
    3) The keys & values of a Dictionary are in sequential order.
    4) Dictionary are defined using curly brackets { key : value }.
"""

d = {
    "name": "Umang",
    "surname": "Nayak",
    "age": 20,
    "marks": [99, 75, 80, 70],
    "dc": {"color": "orange", "gender": "Male", "height": 6.5}
}
print(d)
print(type(d))


# print(d["age"])  # return error
print(d.get("age"))  # return none
print(d.keys())  # display keys
print(d.values())  # display all the values


d["Marks"] = [45, 90]  # changing value of key of dictionary
print("Marks =", d['Marks'])
print("Gender =", d["dc"]["gender"])

d1 = {"who": "ok"}
d.update(d1)

x = ["Umang", "Nayak", 49, "@", "gmail", ".com"]
y = 0

thisD = dict.fromkeys(x, y)
print(thisD)

doc = {
    "name": "Umang",
    "surname": "Nayak",
    "age": 20,
    "marks": [99, 75, 80, 70],
    "dc": "good"
}
print(doc.items())
print(doc.get("age"))
print(doc.keys())
print(doc.values())
doc.setdefault("new", 10)
print(doc)
doc.popitem()
print("pop Last Item =", doc)
doc.pop("name")
print("pop Item of key name =", doc)
