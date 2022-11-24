import re


def f(cnp):

    if re.match("^[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[0-1])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$", cnp):
        return True
    return False


print(f("5010409270015"))
