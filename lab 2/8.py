a = '0'
print(ord(a))


def f(x=1, my_list=[], flag=True):
    res = []
    current_list = []
    if flag == True:
        for word in my_list:
            for c in word:
                if ord(c) % x == 0:
                    current_list.append(c)
            res.append(current_list)
            #print("current list = ", current_list)
            #print("total list = ", res)
            current_list = []
    else:
        for word in my_list:
            for c in word:
                if ord(c) % x != 0:
                    current_list.append(c)
            res.append(current_list)
            #print("current list = ", current_list)
            #print("total list = ", res)
            current_list = []
    return res


print(f(2, ["test", "hello", "lab002"], False))
