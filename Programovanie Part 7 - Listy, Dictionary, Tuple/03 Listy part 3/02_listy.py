# Podla komentarov v kode skus vydedukovat, co ma funkcia my_function vracat. Ak nevies, tak si pozri hinty

# a and b are list of numbers
def my_function(a, b):
   b.sort()
   return (b + a) * 2


# Prints [3, 4, 1, 2, 3, 4, 1, 2]
print(my_function([1, 2], [4, 3]))

# Prints [3, 7, 8, 1, 2, 3, 7, 8, 1, 2]
print(my_function([1, 2], [7, 8, 3]))

# Prints [5, 10, 11, 3, 0, 5, 5, 10, 11, 3, 0, 5]
print(my_function([3, 0, 5], [10, 5, 11]))