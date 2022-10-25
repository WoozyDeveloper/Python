def f(l):
    s = set(l)
    return (len(s), len(l) - len(s))


print(f([1, 2, 2, 2, 3]))
