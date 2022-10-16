def sum():
    print("im from def sum")


sum()


def add_nos(a, b):
    print(a + b)


add_nos(10, 4)


def add_mul(*a):
    som = 0
    for i in a:
        som = som + i
    print(som)


add_mul(1, 2, 3, 4, 5, 6)
