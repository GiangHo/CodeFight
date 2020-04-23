def avoidObstacles(inputArray):
    max = inputArray[0]
    is_check = False
    for i in inputArray:
        if i > max: max = i
    array_new = [i for i in range(1, max+2) if i not in inputArray]
    for i in array_new:
        distance = i
        test_number = distance
        while test_number<=(max+1):
            if test_number in inputArray:
                is_check = False
                break
            else:
                test_number = test_number+ distance
            is_check = True
        if is_check == True:
            return distance