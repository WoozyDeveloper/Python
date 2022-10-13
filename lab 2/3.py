def intersect(a, b):
    ans = list()
    for element in a:
        if element in b:
            ans.append(element)
    return ans


def reunite(a, b):
    ans = a
    for element in b:
        if element not in a:
            ans.append(element)
    return ans


def minus(a, b):
    ans = list()
    for element in a:
        if element not in b:
            ans.append(element)
    return ans


print(intersect([1, 2, 3], [3, 4, 5, 6]))
print(reunite([1, 2, 3], [3, 4, 5, 6]))
print(minus([1, 2, 3], [3, 4, 5, 6]))
