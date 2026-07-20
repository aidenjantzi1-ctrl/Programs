def upperQuartile(gpa):
    gpa.sort()
    l = len(gpa)

    mid_i = int(l / 2 - 1)
    new = gpa[mid_i + 1:]
    mid_i = int(len(new) / 2 - 1)
    return new[mid_i + 1]