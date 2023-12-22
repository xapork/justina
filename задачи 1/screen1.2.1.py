def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
lst = [110, 22, 244444, 9]
print(change(lst))