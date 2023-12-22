def converter(time):
    if 'AM' in time:
        if time[:2] == '12':
            result = '00' + time[2:-2]
        else:
            result = time[:-2]
    else:  
        if time[:2] == '12':
            result = time[:-2]
        else:
            result = str(int(time[:2]) + 12) + time[2:-2]

    print(result)
    return result

converter('7:34 AM')