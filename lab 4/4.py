import sys
import os


def f(my_path):
    dir = os.listdir(my_path)
    l = []
    for i in dir:
        l.append(i.split(".")[-1])
    res = list(set(l))
    res.sort()
    return res


print(f('my_dir'))
