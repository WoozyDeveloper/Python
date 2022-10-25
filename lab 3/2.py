def f(my_string):
    dictionary = dict()
    for c in my_string:
        dictionary[c] = my_string.count(c)
    #sort_orders = sorted(dictionary.items(), key=lambda x: x[0])
    return dictionary


print(f("Ana has apples."))
