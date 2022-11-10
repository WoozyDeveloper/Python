def f(my_list):
    res = []
    d = dict()
    for tup in my_list:
        a = tup[0]
        b = tup[1]
        d['sum'] = a+b
        d['prod'] = a*b
        d['pow'] = a**b
        e = str(d)
        res.append(e)
    return res


print(f([(5, 2), (19, 1), (30, 6), (2, 2)]))
