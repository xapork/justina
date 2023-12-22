def increasing(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            return False
    return True
numbers = [1, 4, 55, 7, 12]
if increasing(numbers):
    print('it is')
else:
    print('its not')
