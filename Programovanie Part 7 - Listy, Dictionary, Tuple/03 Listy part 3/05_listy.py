# Zmen kazdy jeden prvok v liste tak, aby vysledne hodnoty zodpovedali komentu pri print prikaze.

numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

numbers = [number * 2 for number in numbers]

print(numbers)  # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

# alebo

numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

for number in range(len(numbers)):
   numbers[number] *= 2

print(numbers)  