def count_happy_numbers(length):
    count = 0

    if length % 2 != 0:
        return 0
    for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
        left_part = sum(int(digit) for digit in str(num))
        right_part = sum(int(digit) for digit in str(num * 2))

        if left_part == right_part:
            count += 1

    return count
length = 678
print(count_happy_numbers(length))