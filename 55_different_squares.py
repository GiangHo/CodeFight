def differentSquares(matrix):
    hang = len(matrix)
    cot = len(matrix[0])
    if hang < 2 or cot < 2:
        return 0

    tmp = ""
    list_sub_matrix = set()
    for i in range(0, hang - 1):
        for j in range(0, cot - 1):
            tmp = tmp + str(matrix[i][j]) + str(matrix[i + 1][j]) + str(matrix[i][j + 1]) + str(matrix[i + 1][j + 1])
            list_sub_matrix.add(tmp)
            tmp = ""
    return len(list_sub_matrix)
