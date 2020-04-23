def isIPv4Address(inputString):
    list_data = (inputString.split("."))
    list_data_new = []
    is_check = True
    count = 0
    if 7 <= len(inputString) <= 15 and len(list_data) == 4:
        for i in list_data:
            try:
                element = int(i)
                if 0 <= element <= 255:
                    list_data_new.append(i)
            except:
                pass
        if len(list_data_new) != 4:
            is_check = False

    else:
        is_check = False
    return is_check
