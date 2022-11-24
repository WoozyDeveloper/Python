
import re


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele

    return str1


def f(my_string):
    res = re.findall("\w+", my_string)
    result = []
    for word in res:
        r = ''
        if word[0] in "aeiouAEIOU" and word[-1] in "aeiouAEIOU":
            for i in range(0, len(word)):
                if (i + 1) % 2 == 1:
                    r += '*'
                else:
                    r += word[i]
        if r:
            result.append(r)
        else:
            result.append(word)
    res2 = ''
    for word in result:
        res2 += word + ' '
    return res2


print(f("Ana are mere"))
