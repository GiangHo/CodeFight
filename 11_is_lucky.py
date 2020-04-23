def isLucky(n):
    n_new = [int(item) for item in str(n)]
    n_dau = sum(n_new[0:(len(n_new)/2)])
    n_cuoi = sum(n_new[len(n_new)/2:len(n_new)])
    if n_dau == n_cuoi:
        return True
    else:
        return False
