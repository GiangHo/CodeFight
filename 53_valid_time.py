def validTime(time):
    h,m=map(int,time.split(":"))
    return 0<=h<24 and 0<=m<60