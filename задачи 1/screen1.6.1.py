def all_eq(lst):
    max_len = max(len(i) for i in lst)
    new_list = []
    for i in lst:
        if len(i) < max_len:
            new_list.append(i + '_' * (max_len - len(i)))
        else:
            new_list.append(i)
    return new_list
input_list = ["672982763", "000abcdefg", "xernya"]
result = all_eq(input_list)
print(result)