set1 = {1, 2, 3, 4, 5, 6}

print(set1)
print(len(set1))
print("------------------")
for x in set1:
    print(x)
print("===================")

set1.add(7)
print(set1)

set1.update({2, 4, 55})
print(set1)

set1.remove(1)
print(set1)
set1.discard(11)
print(set1)

set1.pop()
print(set1)
print("===============")
set1.pop()
print(set1)

set2 = {"a", "b", "c"}
for x in set2:
    print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)