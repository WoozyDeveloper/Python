def f(x):
    x = str(x)
    x = x.replace('\'', 'ggg')
    x = x.replace('{', 'ggg')
    x = x.replace('}', 'ggg')
    import re
    res = re.findall(r"[^ggg]+[0-9]+\.?[0-9]*(?:(?!ggg).).", str(x))
    return re.findall(r"[0-9]+\.?[0-9]*", str(res))


print(f([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
