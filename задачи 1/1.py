def search_substr(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"
substring = "горчица"
string = "горчица я огорчила"

result = search_substr(substring, string)
print(result)