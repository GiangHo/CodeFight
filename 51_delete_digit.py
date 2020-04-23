def deleteDigit(n):
    list_number = [x for x in str(n)]
    list_number_new = [x for x in str(n)]
    min = list_number_new[0]
    index = 0
    for i in range(0, len(list_number_new)):
        if list_number_new[i] < min:
            min = list_number_new[i]
            index = i
    del list_number_new[index]

    result_tmp = int(''.join(str(e) for e in list_number_new))
    result_2 = None

    min = list_number[0]
    index_2= 0
    if index == len(list_number) - 1:
        for i in range(0, len(list_number)-1):
            if list_number[i] < min:
                min = list_number[i]
                index_2 = i

        del list_number[index_2]
        result_2 = int(''.join(str(e) for e in list_number))

    if result_2 is not None:
        if result_tmp < result_2:
            result = result_2
        else:
            result = result_tmp
    else:
        result = result_tmp

    return ((result))