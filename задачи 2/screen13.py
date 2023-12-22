string = 'who    are u                 really ?'

def space_deleting(string):
    string_lower = string.lower()
    lst_char1 = ''
    lst_char2 = ''
    i = 0

    while i < len(string):
        lst_char2 = lst_char1
        lst_char1 = string[i]

        if lst_char1 == lst_char2 and lst_char1 == ' ':
            string = string[:i] + string[i+1:]
        else:
            i += 1

    print(string)
    return string
space_deleting(string)