def sortByHeight(a):
    b = [item for item in a if item != -1]

    for i in range(1, len(b)):
        for j in range(i):
            if b[i] < b[j]:
                tmp = b[i]
                b[i] = b[j]
                b[j] = tmp

    for index, item in enumerate(a):
        if item != -1:
            a[index] = b[0]
            b.pop(0)
    return a
