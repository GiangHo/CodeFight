def electionsWinners(votes, k):
    max = 0
    number_max = 0
    for i in votes:
        if i> max:
            max= i
    result = 0
    for i in votes:
        if i ==max:
            number_max = number_max +1
        if i+k > max and k !=0:
            result = result +1
    if k ==0 and number_max ==1:
        result = 1
    elif k ==0 and number_max>1:
        result = 0
    return result