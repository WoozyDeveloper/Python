my_string = input()
count = 0
for c in my_string:
    if c.lower() in "aeiou":
        count = count+1
print(count)

print(*map(my_string.lower().count, "aeiou"))
