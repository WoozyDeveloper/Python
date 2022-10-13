
# cu nr
def pal(n):  # sau preiau n ca string si verific partea stanga cu dreapta sa fie in oglinda
    n = int(n)
    og = 0
    d = n
    while n != 0:
        og = og * 10 + n % 10
        n = n // 10
    return d == og

# cu string


def pal2(n):
    n = str(n)
    return n == n[::-1]


n = "12321"


print(pal(n))
print(pal2(n))
