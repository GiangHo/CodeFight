def sudoku(grid):
    check = True
    hang = len(grid)
    cot = len(grid[0])
    for i in range(hang):
        if len(set(grid[i])) != len(grid[i]):
            check = False
            return check
    for i in range(cot):
        list_cot = []
        for j in range(hang):
            list_cot.append(grid[j][i])
        if len(set(list_cot)) != len(list_cot):
            check = False
            return check
    list_hang = []
    for i in range(0, hang, 3):
        list_hang = grid[i:i + 3]

        list_grid_1 = []
        list_grid_2 = []
        list_grid_3 = []
        for j in list_hang:
            list_grid_1 = list_grid_1+ (j[0:3])
            list_grid_2 = list_grid_2 + (j[3:6])
            list_grid_3 = list_grid_3 + (j[6:9])
        if len(set(list_grid_1)) != len(list_grid_1):
            check = False
            return check
        if len(set(list_grid_2)) != len(list_grid_2):
            check = False
            return check
        if len(set(list_grid_3)) != len(list_grid_3):
            check = False
            return check
    return check