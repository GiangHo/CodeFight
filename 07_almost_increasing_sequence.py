def almostIncreasingSequence(sequence):
    A1 = sequence
    A2 = []
    A2.append(A1[0])
    index =0
    element_remove = None
    ischeck = True
    for i in range(1, len(A1)):
        if A1[i]> A2[len(A2)-1] and index <=1:
            A2.append(A1[i])
        elif index == 1 and element_remove is not None:
            A2.remove(A2[len(A2) - 1])
            if len(A2)!=0 and element_remove> A2[len(A2) - 1]:
                A2.append(element_remove)
            elif len(A2) ==0:
                A2.append(element_remove)
            else:
                ischeck = False
                break
            if A1[i] > element_remove:
                A2.append(A1[i])
            else:
                ischeck = False
                break
        else:
            index = index +1
            element_remove = A1[i]

            if index>1:
                ischeck = False
                break

    return ischeck

