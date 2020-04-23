def chessBoardCellColor(cell1, cell2):
    cot = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
    if (int(cot[cell1[0]])%2 == 0 and int(cell1[1])%2 == 0) or int(cot[cell1[0]]%2 != 0 and int(cell1[1])%2 != 0):
        cell1 = "dam"
    else:
        cell1 = "nhat"
    if int(cot[cell2[0]]%2 == 0 and int(cell2[1])%2 == 0) or int(cot[cell2[0]]%2 != 0 and int(cell2[1])%2 != 0):
        cell2 = "dam"
    else:
        cell2 = "nhat"
    if cell1 == cell2:
        return True
    else:
        return False
