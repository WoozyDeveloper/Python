def f(*sets):
    d = dict()
    for i in range(len(sets) - 1):
        a = sets[i]
        b = sets[i+1]
        print(a, b)
        txt = str(a) + ' | ' + str(b)
        d[txt] = a | b

        txt = str(a) + ' & ' + str(b)
        d[txt] = a & b

        txt = str(a) + ' - ' + str(b)
        d[txt] = a - b

        txt = str(b) + ' - ' + str(a)
        d[txt] = b - a

    return d


print(f({1, 2}, {2, 3}, {3, 4}))
