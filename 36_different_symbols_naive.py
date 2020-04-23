def differentSymbolsNaive(s):
    new_s = []
    dem =0
    for i in s:
        if i not in new_s:
            new_s.append(i)
            dem = dem +1
    return dem