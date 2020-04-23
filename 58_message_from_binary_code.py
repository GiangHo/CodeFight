def binaryToDecimal(binaryString):
    result = 0
    for i in range(0, 8):
        result += int(binaryString[i])*pow(2, 7-i)
    return result


def messageFromBinaryCode(code):
    result = ""
    for i in range(0, len(code)-7, 8):
        binaryString = (code[i:i+8])
        result = result + chr(binaryToDecimal(binaryString))
    return result
