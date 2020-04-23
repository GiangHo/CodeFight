def arrayMaxConsecutiveSum(inputArray, k):
    tong = sum(inputArray[0:k])
    max_sum = tong
    for i in range(k-1, len(inputArray)-1):
        tong = tong - inputArray[i-k+1] + inputArray[i+1]
        if tong> max_sum: max_sum = tong
    return max_sum