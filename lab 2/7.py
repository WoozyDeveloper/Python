from venv import create


def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def create_tuple(numbers):
    dim = 0
    greatest = -1
    for number in numbers:
        if is_palindrome(number):
            if number > greatest:
                greatest = number
            dim = dim + 1
    return [dim, greatest]


print(create_tuple([112, 121, 131, 114, 111]))
