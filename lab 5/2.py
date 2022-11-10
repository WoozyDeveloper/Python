anonymous = lambda *args, **kw: sum(kw.values())


def my_function(*args, **kw):
    return sum(kw.values())


print(anonymous(1, 2, a=3, b=4))
print(my_function(1, 2, a=3, b=4))
