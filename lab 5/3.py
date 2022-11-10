x = "Programming in Python is fun"


def f1(a):
    res = []
    for x in a:
        if x in "aeiouAEIOU":
            res.append(x)
    return res


def f2(a):
    return [x for x in a if x in "aeiouAEIOU"]


def f3(a):
    return list(filter(lambda x: x in "aeiouAEIOU", a))


print(f1(x))
print(f2(x))
print(f3(x))
