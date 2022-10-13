def fibo(dim):
    my_list = list()
    a = 1
    b = 1
    my_list.append(a)
    my_list.append(b)
    index = 2
    while index < dim:
        c = a + b
        a = b
        b = c
        my_list.append(c)
        index = index + 1
    return my_list


print(fibo(5))
