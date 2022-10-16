def combine(my_list):
    res_list = []
    result = []
    dim = 0
    for lst in my_list:
        if len(lst) > dim:
            dim = len(lst)

    for i in range(dim):
        for current_list in my_list:
            if i >= len(current_list):
                res_list.append("None")
            else:
                res_list.append(current_list[i])
        result.append(res_list)
        res_list = []
    return result


print(combine([[1, 2, 3], [5, 6, 7], ['a', 'b', 'c', 'd']]))
