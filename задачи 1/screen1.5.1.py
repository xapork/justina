def list_sort(lst):
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst
lst = [32.000001, -1.1, 1, -10596, 32]
print(list_sort(lst))