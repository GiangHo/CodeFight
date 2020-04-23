def longestDigitsPrefix(inputString):
    result = ""
    for i in inputString:
        if i.isnumeric():
            result = result + i
        else:
            break
    return result
