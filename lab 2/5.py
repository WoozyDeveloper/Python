def rpl(matrix):
    for i in range(0, 3):
        for j in range(0, 3):
            if i > j:
                matrix[i][j] = 0
    return matrix


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rpl(A))
