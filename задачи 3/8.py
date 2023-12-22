def number_to_words_russian(number):
    if not 0 <= number <= 999:
        return "Число должно быть от 0 до 999"

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
             "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if number == 0:
        return "ноль"

    result = []
    if number >= 100:
        result.append(hundreds[number // 100])
        number %= 100
    if 10 <= number <= 19:
        result.append(teens[number - 10])
    else:
        if number >= 20:
            result.append(tens[number // 10])
            number %= 10
        if number > 0:
            result.append(units[number])

    return ' '.join(result)

print(number_to_words_russian(894)) 