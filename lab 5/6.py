def f(l):
    a = [x for x in l if x % 2 == 0]
    b = [x for x in l if x % 2 == 1]
    res = []
    for i in range(len(a)):
        res.append((a[i], b[i]))

    return res


print(f([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
