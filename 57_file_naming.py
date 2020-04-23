def fileNaming(names):
    file_name = []
    dict_name = {}
    for i in names:
        if dict_name.get(i) == None:
            file_name.append(i)
            dict_name[i] = 1
        else:
            new_name = i+ "("+str(dict_name.get(i))+")"
            while dict_name.get(new_name) != None:
                dict_name[i] = dict_name[i] + 1
                new_name = i + "(" + str(dict_name.get(i)) + ")"

            file_name.append(new_name)
            dict_name[i] = dict_name[i] + 1
            dict_name[new_name] = 1
    return  (file_name)
