def f(*args, **kw):
    res = []
    for x in args:
        if type(x) is dict:
            if len(x) >= 2:
                for i in x.keys():
                    if type(i) is str and len(i) >= 3:
                        res.append(x)
                        break
    for x in kw.values():
        if type(x) is dict:
            if len(x) >= 2:
                for i in x.keys():
                    if type(i) is str and len(i) >= 3:
                        res.append(x)
                        break
    return res


print(f({1: 2, 3: 4, 5: 6},
        {'a': 5, 'b': 7, 'c': 'e'},
        {2: 3},
        [1, 2, 3],
        {'abc': 4, 'def': 5},
        3764,
        dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
        test={1: 1, 'test': True}))
