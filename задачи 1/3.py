def top3(st):
    st = st.replace(" ", "")
    char_count_list = []
    for char in st:
        found = False
        for entry in char_count_list:
            if entry[0] == char:
                entry[1] += 1
                found = True
                break

        if not found:
            char_count_list.append([char, 1])
    sorted_chars = sorted(char_count_list, key=lambda x: x[1], reverse=True)[:3]

    result_str = ", ".join(f"{char} - {count}" for char, count in sorted_chars)

    return result_str
text_sample = "что же случилось с людьми?"
result = top3(text_sample)
print(result)