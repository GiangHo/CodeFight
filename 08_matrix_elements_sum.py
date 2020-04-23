def matrixElementsSum(matrix):
    hang = len(matrix)
    cot = len(matrix[0])
    tong = sum(matrix[0])
    for i in range(1, hang):
        for j in range(0, cot):
            if matrix[i-1][j] == 0:
                matrix[i][j] = 0
            elif matrix[i][j]!=0:
                tong = tong + matrix[i][j]
    return tong