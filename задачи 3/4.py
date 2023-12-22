def summa_v_stroke(s):
    digits = '1234567890'
    current_number = ''
    numbers = []

    for char in s:
        if char in digits:
            current_number += char
        else:
            if current_number:
                numbers.append(int(current_number))
                current_number = ''

    if current_number:
        numbers.append(int(current_number))

    result = sum(numbers)
    print(result)

    return result

summa_v_stroke('123jfds54ngfdbnj53')