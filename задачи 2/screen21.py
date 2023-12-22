def calculate_median(arr):
    sorted_array = sorted(arr)
    length = len(sorted_array)
    if length % 2 == 1:
       
        return sorted_array[length // 2]
    else:
        middle_left = sorted_array[length // 2 - 1]
        middle_right = sorted_array[length // 2]
        median = (middle_left + middle_right) / 2
        return median

numbers = [5, 2, 8, 1, 7]
median_value = calculate_median(numbers)
print(median_value)
