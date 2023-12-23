my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
my_dict[list(my_dict.keys())[-1]], my_dict[list(my_dict.keys())[0]] = my_dict[list(my_dict.keys())[0]], my_dict[list(my_dict.keys())[-1]]

del my_dict[list(my_dict.keys())[1]]

my_dict['new_key'] = 'frucku'

print(my_dict)