fv = []
my_str = input()
for i in range(128):
    fv.append(0)
big = 0
for c in my_str:
    fv[ord(c)] = fv[ord(c)] + 1
    if (fv[ord(c)] > big and c.isalpha()):
        big = fv[ord(c)]
        letter = c

print(letter)
