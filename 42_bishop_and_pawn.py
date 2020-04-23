def bishopAndPawn(b, p):
    b=[ord(b[0]),int(b[1])]
    p=[ord(p[0]),int(p[1])]
    return b[1]-b[0]==p[1]-p[0] or sum(b)==sum(p)
