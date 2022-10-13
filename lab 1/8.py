def decimalToBinary(n):
    return bin(n).replace("0b", "")


count = 0
n = int(input())
my_str = decimalToBinary(n)
for c in my_str:
    if c == '1':
        count = count + 1
print(count)
