def camel(st):
    result = ''
    upper = True 
    for char in st:
        if char.isalpha():
            if upper:
                result += char.upper()
            else:
                result += char.lower()
            upper = not upper
        else:
            result += char 

    return result
text_sample = "здравствуйте, завтра будет урок?"
result = camel(text_sample)
print(result)