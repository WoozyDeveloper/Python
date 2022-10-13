import re

test_string = input()

temp = re.findall(r'-?\d+', test_string)
res = list(map(int, temp))

print(str(res[0]))
