def find_x_times(my_lists, x):
    ans = list()
    my_set = set()
    for llist in my_lists:
        for element in llist:
            my_set.add(element)

    counter = 0
    for element in my_set:
        for my_list in my_lists:
            if element in my_list:
                counter = counter + 1
        #print(element, ' ', counter)
        if counter == x:
            ans.append(element)
        counter = 0
    return ans


print(find_x_times([[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]], 2))
