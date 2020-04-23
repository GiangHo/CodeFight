def alphabeticShift(inputString):
    result = ""
    for i in inputString:
        if ord(i) == 122:
            new_ac = 97
        else:
            new_ac = ord(i)+1
        result = result + str(chr(new_ac))
    return result
