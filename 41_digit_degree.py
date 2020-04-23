def digitDegree(n):
    if n <10:
        return 0
    dem = 0
    while n >=10:
        tong = 0
        for i in str(n):
            tong = tong + int(i)
        n = tong
        tong = 0
        dem = dem +1
    return dem