def f(a, b):
    for x in a.items():
        if x[0] not in b.keys() or x[1] not in b.values():
            return False
    return True


x = dict({"abc": [1, 1], "aaa": [2, 2]})
y = dict({"abc": [1, 1], "aaa": [2, 2]})

print(f(x, y))
