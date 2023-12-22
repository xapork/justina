def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    else:
        return "Невозможно преобразовать"
number = "12.22"
conv_number = to_float(number)
print(conv_number)
