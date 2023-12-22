def reverse(a):
    res = ''
    for wheel in a:
        if wheel.istitle() == True:
            res = wheel.lower() + res 
        else:
            res = wheel.upper() + res 
    print(res)
    return res 
reverse('TBjkYFVV')