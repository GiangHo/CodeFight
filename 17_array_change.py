def arrayChange(inputArray):
    dem =0
    for index, value in enumerate(inputArray):
        if index!=0:
            if inputArray[index]<= inputArray[index-1]:
                dem = dem + inputArray[index-1]+1 - inputArray[index]
                inputArray[index] = inputArray[index - 1] + 1
    return dem