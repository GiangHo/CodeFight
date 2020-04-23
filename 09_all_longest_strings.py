def allLongestStrings(inputArray):
    max = len(inputArray[0])
    dict_count = {}
    for i in inputArray:
        if len(i)> max:
            max = len(i)
        if dict_count.get(len(i)) is None:
            list_element = []
            list_element.append(i)
            dict_count[len(i)] = list_element
        else:
            list_element = dict_count.get(len(i))
            list_element.append(i)
            dict_count[len(i)] = list_element
    return dict_count.get(max)