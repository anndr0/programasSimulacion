def canicas(v, mat):
    """Programming Drill 3.1.1"""
    mat0 = [0 for i in range(len(v))]
    for i in range(len(v)):
        res = 0
        for j in range(len(v)):
            res += mat[i][j] * v[j]
        mat0[i] = res
    print(mat0)

mat = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]]
v = [6, 2, 1, 5, 3, 10]
v1 = [0, 0, 12, 5, 1, 9]

canicas(v1, mat)