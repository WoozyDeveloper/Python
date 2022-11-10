
# A
print('Punctul A')


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def f(*args, **kw):
        print(args, kw)
        return function(*args, **kw)
    return f


augmented_multiply_by_two = print_arguments(multiply_by_two)
print(augmented_multiply_by_two(10))

augmented_add_numbers = print_arguments(add_numbers)
print(augmented_add_numbers(3, 4))


# B

print('Punctul B')


def multiply_output(function):
    def f(*args, **kw):
        return 2*function(*args, **kw)
    return f


def multiply_by_three(x):
    return x * 3


augmented_multiply_by_three = multiply_output(multiply_by_three)
print(augmented_multiply_by_three(10))


# C
print("Punctul C")


def augment_function(function, decorators):
    def f(*args, **kw):
        result = function
        for deco in decorators:
            result = deco(result)
        return result(*args, **kw)
    return f


decorated_function = augment_function(
    add_numbers, [print_arguments, multiply_output])
x = decorated_function(3, 4)
print(x)
