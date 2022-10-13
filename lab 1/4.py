my_text = input()
ans = list()
for i in range(0, len(my_text) - 1):
    ans.append(my_text[i].lower())
    if my_text[i + 1] == my_text[i + 1].upper():
        ans.append('_')

ans.append(my_text[len(my_text)-1])
print(''.join(ans))
