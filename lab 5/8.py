
# A
print('Punctul A')


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    function_string = '''def new_function(*args, **kwargs):
    print("Arguments are:", *args)
    print("Key arguments are:", **kwargs)
    return function(*args,**kwargs)'''
    globals()['function'] = multiply_by_two
    exec(function_string, globals())
    return new_function


augmented_multiply_by_two = print_arguments(multiply_by_two)
print(augmented_multiply_by_two(3))


# B

print('Punctul B')


def multiply_by_three(x):
    return x * 3


def multiply_output(function):
    function_string = '''def new_function(*args, **kwargs):
    return function(*args,**kwargs)'''
    globals()['function'] = multiply_by_three
    exec(function_string, globals())
    return new_function


augmented_multiply_by_three = multiply_output(multiply_by_three)
print(augmented_multiply_by_three(10))


# C
print('Punctul C')


def add_numbers(a, b):
    return a + b


# def augmented_function(function, decorators):
#     function_string = '''def new_function(decorators,*args, **kwargs):
#     res = []
#     for d in decorators:
#         res.append(d(*args,**kwargs))
#     return res'''
#     globals()['function'] = add_numbers
#     exec(function_string, globals())
#     return new_function(decorators)


# decorated_function = augmented_function(
#     add_numbers, [print_arguments, multiply_output])

# print(decorated_function(3, 4))
