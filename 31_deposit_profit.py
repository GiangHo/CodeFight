def depositProfit(deposit, rate, threshold):
    dem =0
    while (deposit < threshold):
        deposit = deposit + deposit *float(float(rate)/100)
        dem = dem +1
    return dem
