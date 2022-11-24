import re


def f(my_string):
    res = re.findall("\w+", my_string)
    return res


print(f("Ana are mere"))
