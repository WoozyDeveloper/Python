import math


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def process_item(x):
    x += 1
    while True:
        if prime(x):
            return x
        x += 1


# n = int(input("Enter num:"))
# print(process_item(n))
