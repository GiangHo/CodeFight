def boxBlur(image):
    hang = len(image)
    cot = len(image[0])
    list_hang = []
    for i in range(0, hang - 2):
        list_cot = []
        average = 0
        for j in range(0, cot - 2):
            average = int((image[i][j] + image[i][j + 1] + image[i][j + 2] + image[i + 1][j] + image[i + 1][
                j + 1] + image[i + 1][j + 2] + image[i + 2][j] + image[i + 2][j + 1] + image[i + 2][j + 2]) /9)
            list_cot.append(average)
        list_hang.append(list_cot)
    return list_hang