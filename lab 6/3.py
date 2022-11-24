import re


def f(my_strings, expr_list):

    result = []
    index = 0
    for index in range(len(my_strings)):
        res = []
        for expr in expr_list:
            res += re.findall(expr, my_strings[index])
            print(my_strings[index])
        if res:
            result.append(res)
    return result


print(f(["Ana", "33",  "are", "mere"], ["\d", "[A-Z][a-z]+"]))
