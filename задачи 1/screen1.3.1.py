def to_list(*args):
    return list(args) if args else "there're no arguments"
result_list = to_list('tgif', 'flucku', 'tomorrow no yesterday')
print(result_list)