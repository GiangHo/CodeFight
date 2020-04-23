def palindromeRearranging(inputString):
    dict_string = {}
    count = 0
    for i in inputString:
        if dict_string.get(i) is None:
            dict_string[i] = 1
        else:
            dict_string[i] = dict_string.get(i)+1
    for k, v in dict_string.items():
        if v%2!=0:
            count = count +1
            if count >1:
                return False
    return True