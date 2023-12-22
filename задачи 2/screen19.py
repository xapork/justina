arr = [44, 55, 1, 6890]
arrdop = []

def what(arr):
    last_sum = 0
    for number in arr:
        last_sum += number
        arrdop.append(last_sum)
    print(arrdop)
    return arrdop

what(arr)