knight_moves = [(-2, 1), (-2, -1), (-1, 2), (-1, -2),
                (2, 1), (2, -1), (1, 2), (1, -2)]

def chessKnight(cell):
    col = ord(cell[0]) - 96
    row = int(cell[1])
    return sum(1 for sc, sr in knight_moves
               if 1 <= col+sc <= 8 and 1 <= row+sr <= 8)