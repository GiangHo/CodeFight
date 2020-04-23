def minesweeper(matrix):
    hang = len(matrix)
    cot = len(matrix[0])
    b =[[0 for col in range(cot)] for row in range(hang)]
    for i in range(hang):
        for j in range(cot):
            if matrix[i][j] is True:
                if (0<=i-1<hang and 0<=j-1 <cot):
                    b[i - 1][j - 1] = b[i - 1][j - 1] + 1

                if (0<=i - 1<hang and 0<=j<cot):
                    b[i - 1][j] = b[i - 1][j] + 1

                if (0<=i - 1<hang and 0<=j+1<cot):
                    b[i - 1][j + 1] = b[i - 1][j + 1] + 1

                if (0<=i<hang and 0<=j-1 <cot):
                    b[i][j - 1] = b[i][j - 1] + 1

                if (0<=i<hang and 0<=j+1<cot):

                    b[i][j + 1] = b[i][j + 1] + 1

                if (0<=i + 1 <hang and 0<=j-1 <cot):
                    b[i + 1][j - 1] = b[i + 1][j - 1] + 1

                if (0<=i + 1 <hang and 0<=j<cot):
                    b[i + 1][j] = b[i + 1][j] + 1

                if (0<=i + 1 <hang and 0<=j+1<cot):
                    b[i + 1][j + 1] = b[i + 1][j + 1] + 1

    return b