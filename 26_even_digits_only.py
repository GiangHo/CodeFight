def evenDigitsOnly(n):
    str_input = str(n)
    is_check_only = True
    for i in range(len(str_input)):
        if int(str_input[i])%2 !=0:
            is_check_only = False
            break
    return is_check_only