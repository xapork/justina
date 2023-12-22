def cleaned_str(st):
    result = ''
    for i in st:
        if i != '@':
            result += i
    return result

word_with_at = "гр@оо@лк@оц@ва"

print("Исходная строка:", example)
print("Очищенная строка:", cleaned_example)