def fibo():
    res = []
    res.append(1)
    res.append(1)
    for i in range(2, 1000):
        res.append(res[i-2] + res[i-1])
    return res


def f(**kw):
    fib = fibo()
    if 'filters' in kw.keys():
        for f in kw['filters']:
            fib = list(filter(f, fib))

    if 'offset' in kw.keys():
        fib = fib[kw['offset']:]

    if 'limit' in kw.keys():
        fib = fib[:kw['limit']]
    return fib


def sum_digits(x):

    return sum(map(int, str(x)))


print(f(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],

        limit=2,

        offset=2))
