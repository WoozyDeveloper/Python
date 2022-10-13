import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for num in range(3, int(math.sqrt(n)) + 1, 2):
        if n % num == 0:
            return False
    return True


def extract_prime(my_list):
    current_list = list()
    for element in my_list:
        if is_prime(element):
            current_list.append(element)
    return current_list


l = list()
for x in range(1, 20):
    l.append(x)

answer = list()
answer = extract_prime(l)

print(l)
print(answer)
