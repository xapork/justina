def clay(string):
    res = ''
    array = []
    array2 = []
    i = 0
    for char in string:
        if char == ',':
            array.append(res)
            res = ''
        elif char == ' ':
            pass
        else:
            res = res + char
        i += 1

    if res:
        array.append(res)

    j = 0
    while j < len(array):
        array2.append(int(array[j]))
        j += 1

    result = 1
    i = 0
    while i < len(array2):
        result = result * array2[i]
        i += 1

    return result

print(clay('893, 33, 22, 30, 20, 4'))