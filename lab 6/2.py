import re


def f(regex, text, x):
    res = re.findall(regex, text)
    return [i for i in res if len(i) == x]


print(f("\w+", "Ana are mere", 3))
