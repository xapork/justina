def avg_5(a, b, c, d):
    average = (a + b + c + d) / 4
    rounded_average = round(average, 5)
    return rounded_average
result = avg_5(777, 212, 1, 77777777777777777)
print(result)