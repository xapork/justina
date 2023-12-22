def list_to_tuple(input_list):
    return tuple(input_list)

def first_last(letter, st):
    indices = [i for i in range(len(st)) if st[i] == letter]

    if not indices:  
        return list_to_tuple((None, None))
    else:
        return list_to_tuple((min(indices), max(indices)))

target_letter = "п"
target_string = "плов съел коровпу"

result_indices = first_last(target_letter, target_string)
print(result_indices)