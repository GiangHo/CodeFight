def isBeautifulString(inputString):
    s = string.ascii_lowercase
    for i in range(1, len(s)):
        if inputString.count(s[i]) > inputString.count(s[i-1]): return False
    return True