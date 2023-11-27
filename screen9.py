def destroy_ur_enemies(names_array, enemies_array):
    return [name for name in names_array if name not in enemies_array]

names = ["tony", "peter", "paul", "john", "ringo", "love", "moriarty", "voland"]
enemies = ["ringo", "moriarty", "voland", "love"]

perfect_names = destroy_ur_enemies(names, enemies)
print(perfect_names)
