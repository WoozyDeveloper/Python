# Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples
# (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller
# spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0,
# beginning with the closest row from the field.

# 	Example:

# # FIELD

# [[1, 2, 3, 2, 1, 1],

# [2, 4, 4, 3, 7, 2],

# [5, 5, 2, 5, 6, 4],

# [6, 6, 7, 6, 7, 5]]

# Will return : [(2, 2), (3, 4), (2, 4)]

def f(mat):
    res = []
    lines = len(mat)
    rows = len(mat[0])
    print(lines, rows)
    for i in range(lines):
        for j in range(rows):
            # print(mat[i][j])# coloana j
            for x in range(i):
                if mat[x][j] >= mat[i][j]:
                    print(i, ",", j)
                    break


f([[1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]])
