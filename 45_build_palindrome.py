def check_is_palindrome(string_palindrome):
    check = True
    for i in range(0, len(string_palindrome)/2):
        if string_palindrome[i] != string_palindrome[len(string_palindrome) -i-1]:
            check = False
    if check == True:
        return True
    else:
        return False
def buildPalindrome(st):
    if check_is_palindrome(st) == True:
        return st
    tmp = ""
    for i in range(len(st)-1):
        str_palindrome = st
        tmp = st[i] + tmp
        str_palindrome =  str_palindrome +tmp
        check = check_is_palindrome(str_palindrome)
        if check == True:
            return str_palindrome