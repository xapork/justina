def mul_to_int(a,b):
    if (a*b)/int(a*b) == 1:
        res = a*b
        print(int(res))
        return int(res)
    else:
        print(a*b)
        return a*b
mul_to_int(21, 2)