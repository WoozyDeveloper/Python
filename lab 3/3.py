def f(a, b):
    print(a.items())
    print(b.keys())
    print(b.values())
    for x in a.items():
        l = []
        l.append(b.get(x[0]))
        if x[0] not in b.keys() or x[1] not in l:
            return False
    return True


# x = dict({"a": 1, "b": 2, 1: {2: {3: 4}}})
# y = dict({"a": 1, "b": 2, 1: {2: {3: 4}}})
x = dict({"a": 1, "b": 2})
y = dict({"a": 2, "b": 1})

print(f(x, y))
