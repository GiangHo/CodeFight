def check_trung(str_1, str_2):
    count = 0
    for i in range(0, len(str_1)):
        if str_1[i]!= str_2[i]:
            count = count +1
    if count ==1:
        return True
    else:
        return False


def find_next_sequence(string_compare, inputArray, is_used):
    kq = 0
    for i in range(len(inputArray)):
        if check_trung(string_compare, inputArray[i]) == True and is_used[i] != 1:
            is_used[i] = 1
            kq = inputArray[i]
            break
    return kq


def stringsRearrangement(inputArray):
    result = False
    for i in range(len(inputArray)):
        string_created = inputArray[i]
        is_used = [0 for j in range(len(inputArray))]
        is_used[i] = 1
        n = 1
        string_current = string_created
        while n < len(inputArray):
            string_return = find_next_sequence(string_current, inputArray, is_used)
            if string_return == 0:
                break
            else:
                string_current = string_return
                n = n+1
        if n == len(inputArray):
            result = True
            break
    return result