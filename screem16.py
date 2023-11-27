def calculate_total_volume(boxes):
    total_volume = 0
    for box in boxes:
        length, width, height = box
        box_volume = length * width * height
        total_volume += box_volume
    return total_volume

dimensions_of_boxes = [(2, 15, 4), (99, 2, 9), (4, 4, 4)]
total_box_volume = calculate_total_volume(dimensions_of_boxes)
print(total_box_volume)
