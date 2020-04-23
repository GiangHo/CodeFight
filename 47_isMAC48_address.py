def isMAC48Address(inputString):
    list_mac = inputString.split("-")
    check = True
    if len(list_mac) !=6:
        check = False
    else:
        for i in list_mac:
            if len(i) != 2:
                check = False
                break
            if i.isnumeric() != True:
                for j in i:
                    if j.isnumeric()!= True:
                        if ord(j)<65 or ord(j) > 70:
                            check = False
                            break
            if check == False:
                break
    return check