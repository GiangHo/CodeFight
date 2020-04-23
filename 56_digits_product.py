def digitsProduct(product):
    if product == 0:
        return 10
    elif product == 1:
        return 1
    list_uoc = [i for i in range(2, 10) if product % i == 0]
    if list_uoc == []:
        return -1
    list_tmp = []
    i = len(list_uoc) - 1
    while product!=1:
        if product % list_uoc[i] == 0:
            list_tmp.append(list_uoc[i])
            product = product/list_uoc[i]
        else:
            i = i -1
            if i< 0:
                return -1
    tmp = ""
    for i in range(len(list_tmp)-1, -1, -1):
        tmp = tmp + str(list_tmp[i])
    return (int(tmp))