radius = float(input('wtite radius: '))
height = float(input('write height: '))
density = 1000

def calculate_mass(radius, height, density):
    mass = density * radius**2 * height * 3.14
    return mass

result = calculate_mass(radius, height, density)
rounded = round(result, 2)

print(f'The mass of water in the cylinder is {rounded} kilograms.')
