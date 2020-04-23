def absoluteValuesSumMinimization(a):
    so_thu_nhat = a[len(a)/2]
    so_thu_hai = None

    if len(a)/2 -1 >=0:
        so_thu_hai = a[len(a)/2 -1]
    min_1 = 0
    min_2 = 0
    for i in range(0, len(a)):
        min_1 = min_1 + abs(so_thu_nhat-a[i])
        if so_thu_hai is not None:
            min_2 = min_2 + abs(so_thu_hai - a[i])
    if so_thu_hai is not None and min_2 <= min_1:
        min = min_2
        kq = a[len(a)/2 -1]
    else:
        min = min_1
        kq = a[len(a)/2]
    return kq
