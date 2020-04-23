def circleOfNumbers(n, firstNumber):
    tmp = (180/(360/n))+firstNumber
    if tmp>=n:
        so_doi = abs(n -tmp)
    else:
        so_doi = tmp
    return so_doi
