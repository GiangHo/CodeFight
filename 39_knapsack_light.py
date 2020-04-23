def knapsackLight(value1, weight1, value2, weight2, maxW):
    if (weight1+weight2) <= maxW:
        return value1 + value2
    elif maxW < weight1 and maxW <weight2:
        return 0
    else:
        if float(value1/weight1) > float(value2/weight2):
            return value1
        else:
            return value2
