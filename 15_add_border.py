def addBorder(picture):
    hang = len(picture)
    cot = len(picture[0])
    boder_outer = ""
    new_picter = []
    for i in range(cot +2):
        boder_outer = boder_outer + "*"
    new_picter.append(boder_outer)
    for i in picture:
        new_element = "*"+i+"*"
        new_picter.append(new_element)
    new_picter.append(boder_outer)
    return new_picter