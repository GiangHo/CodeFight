def commonCharacterCount(s1, s2):
    s1_tmp = [i for i in s1]
    s2_tmp = [i for i in s2]
    kq = []
    for item in s2_tmp:
        if item in s1_tmp:
            kq.append(item)
            s1_tmp.remove(item)
    return len(kq)