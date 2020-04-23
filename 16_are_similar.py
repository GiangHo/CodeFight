def areSimilar(a, b):
    count = 0
    is_check = False
    a_dup = []
    b_dup = []
    if (set(a)==set(b)):
        for i in range(len(a)):
            if a[i]!=b[i]:
                count = count +1
                a_dup.append(a[i])
                b_dup.append(b[i])
        if count ==2 or count==0:
            if set(a_dup) == set(b_dup):
                is_check = True
    return is_check

    # count = 0
    # vitri = []
    # for i in range(0,len(a)):
    #     if(a[i] != b[i]):
    #         count += 1
    #         vitri.append(i)
    # if(count == 0):
    #     return True
    # elif(count == 2):
    #     m = vitri[0]
    #     n = vitri[1]
    #     if((a[m] != b[n]) or (a[n] != b[m])):
    #         return False
    #     return True
    # else:
    #     return False