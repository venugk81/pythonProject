thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

thisdict1 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict1)

print(thisdict1["brand"])
print("================")
for key in thisdict1.keys():
    print(thisdict1[key])
print("================")
print(thisdict1.get("year"))

print(thisdict1.items())

for x, y in thisdict1.items():
    print(x, y)
