n = 5
a = [
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 5],
    [9, 10, 11, 12, 5],
    [13, 14, 15, 16, 5],
    [1, 2, 3, 4, 5]
]
final = list()

for i in range(0, n // 2):
    for j in range(i, n - i):
        final.append(a[i][j])
    for j in range(i + 1, n - i):
        final.append(a[j][n - i - 1])
    for j in range(n - i - 2, i - 1, -1):
        final.append(a[n - i - 1][j])
    for j in range(n - i - 2, i, -1):
        final.append(a[j][i])
    if n % 2 == 1:
        final.append(a[n//2][n//2])

print(final, " ", len(final))
