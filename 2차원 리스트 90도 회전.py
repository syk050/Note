def rotate_a_matrix_by_90(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


matrix = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]
rotate_matrix = rotate_a_matrix_by_90(matrix)
for i in rotate_matrix:
    print(i)
