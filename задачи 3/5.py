def sosedi(a):
    i = 0
    flag = True

    while i < len(a):
        if a[i] != '+':
            flag = False
            break
        i += 2

    print(flag)
    return flag

sosedi('+87')