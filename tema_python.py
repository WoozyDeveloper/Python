'''
# 3
search_string = input()
main_string = input()

print(main_string.count(search_string))


# 4
my_text = input()
my_text = my_text.lower().replace(" ", "_")
print(my_text)
'''
# 5
n = 4
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
final = list()

for i in range(0, n // 2):
    for j in range(i, n - i):
        final.append(a[i][j])
    for j in range(i + 1, n - i):
        final.append(a[j][n - i - 1])
    for j in range(n - i - 1, i - 1, -1):
        final.append(a[n - i - 1][j])
    for j in range(n - i - 1, i, -1):
        final.append(a[j][i])
    if n % 2 == 1:
        final.append(a[n//2][n//2])

print(final)

'''
# 6
def pal(n):  # sau preiau n ca string si verific partea stanga cu dreapta sa fie in oglinda
    og = 0
    d = n
    while n != 0:
        og = og * 10 + n % 10
        n = n // 10
    return d == og


n = int(input())
print(pal(n))

# 7
import re

test_string = input()

temp = re.findall(r'\d+', test_string)
res = list(map(int, temp))

print("The numbers list is : " + str(res))


# 8

def decimalToBinary(n):
    return bin(n).replace("0b", "")

count = 0
n = int(input())
my_str = decimalToBinary(n)
for c in my_str:
    if c == '1':
        count = count + 1
print(count)

# 9
fv = []
my_str = input()
for i in range(128):
    fv.append(0)
big = 0
for c in my_str:
    fv[ord(c)] = fv[ord(c)] + 1
    if(fv[ord(c)] > big):
        big = fv[ord(c)]
        letter = c

print(letter)



# 10
my_str = input()
count = 1
for c in my_str:
    if c == ' ':
        count = count + 1
print(count)
'''
