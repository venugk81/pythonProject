tup = (132, 234, 23, 54, 65, 233, 654, 765, 9324, 2, 5, 6, 7, 8)
print(tup[0])
print(tup.__len__())

print(len(tup))
print(type(tup))

for it in tup:
    print(it)
print("-----------------------")
for it in range(len(tup)):
    print(tup[it])

print("====================")
i = 0
while i < len(tup):
    print(tup[i])
    i = i + 1

tup1 = (1, 2, 3)
tup2 = ("a", "b")

tup3 = tup1 + tup2
print(tup3)
print(tup3 * 2)

print(tup3[0])
print(tup3.index('a'))
