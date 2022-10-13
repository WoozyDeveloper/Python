def cmmdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


n = int(input())
numbers = list()

for i in range(n):
    num = int(input())
    numbers.append(num)

total_cmmdc = numbers[0]
for i in range(n):
    total_cmmdc = cmmdc(total_cmmdc, numbers[i])
    # print(total_cmmdc)


print(total_cmmdc)
