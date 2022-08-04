# Zabezpec, aby funkcia add pripocitala vzdy parameter x globalnej premennej my_number

def add(x):
   global my_number
   my_number += x

# Moja globalna premenna
my_number = 5

# Vypise 6
add(1)
print(my_number)

# Vypise 12
add(6)
print(my_number)