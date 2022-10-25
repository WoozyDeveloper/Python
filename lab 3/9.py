def my_function(*pos, **dictionary):
    res = 0
    for current_pos in pos:
        if current_pos in dictionary.values():
            res += 1
    return res


print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
