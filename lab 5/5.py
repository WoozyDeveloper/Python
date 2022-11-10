def f(x):
    x = str(x)
    x = x.replace('\'', 'ggg')
    x = x.replace('{', 'ggg')
    x = x.replace('}', 'ggg')
    import re
    res = re.findall(r"[^ggg]+[0-9]+\.?[0-9]*(?:(?!ggg).).", str(x))
    return re.findall(r"[0-9]+\.?[0-9]*", str(res))


def f2(x):
    res = []
    for i in x:
        if type(i) == int or type(i) == float:
            res.append(i)
    return res


print(f2([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
