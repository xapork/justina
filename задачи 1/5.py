def shortener(st):
    result = ''
    inside_brackets = 0

    for char in st:
        if char == '(':
            inside_brackets += 1
        elif char == ')' and inside_brackets > 0:
            inside_brackets -= 1
        elif inside_brackets == 0:
            result += char

    return result

text = "зачем(незачем) нужно жить?"
result = shortener(text)
print(result)