def makeArrayConsecutive2(statues):
    min =statues[0]
    max = statues[0]
    for i in statues:
        if i> max:
            max = i
        if i< min:
            min = i
    return (max - min +1)- len(statues)