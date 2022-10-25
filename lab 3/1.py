def intersect(a, b):
    ans = set()
    for element in a:
        if element in b:
            ans.add(element)
    return ans


def reunite(a, b):
    ans = set(a)
    for element in b:
        if element not in a:
            ans.add(element)
    return ans


def minus(a, b):
    ans = set()
    for element in a:
        if element not in b:
            ans.add(element)
    return ans


def f(a, b):
    ans = []
    ans.append(intersect(a, b))
    ans.append(reunite(a, b))
    ans.append(minus(a, b))
    ans.append(minus(b, a))
    return ans


print(f([1, 2, 3], [3, 4, 5, 6]))
