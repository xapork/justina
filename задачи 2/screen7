def generate_message(input_text):
    output_message = ""
    fig = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    
    for char in input_text:
        if char.upper() in fig:
            count = fig[char.upper()]
            output_message += char * count

    return output_message
input_text = "beach"
output_text = generate_message(input_text)
print(output_text)
