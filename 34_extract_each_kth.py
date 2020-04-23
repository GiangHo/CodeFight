def extractEachKth(inputArray, k):
    number_div = len(inputArray)/k
    extract_list = []
    position_remove = []
    for i in range(1, number_div+1):
        position_remove.append(k*i - 1)
    for i in range(len(inputArray)):
        if i not in position_remove:
            extract_list.append(inputArray[i])
    return extract_list