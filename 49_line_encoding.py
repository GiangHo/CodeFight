def lineEncoding(s):
    list_character = []
    list_tmp = [s[0]]
    for i in range(1, len(s)):
        if s[i]== s[i-1]:
            list_tmp.append(s[i])
            if i == len(s) -1:
                list_character.append(list_tmp)
        else:
            list_character.append(list_tmp)
            list_tmp=[s[i]]
            if i == len(s) -1:
                list_character.append(list_tmp)
    result = ""
    for i in list_character:
        tmp = 0
        if len(i) >1:
            tmp = str(len(i))+ i[0]
        else:
            tmp = i[0]
        result = result + tmp
    return result
