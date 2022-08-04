# Zisti aku funkciu mas pouzit z modulu math, aby funkcia my_function vratila odmocninu z cisla x

import math


# Vrati odmocninu
def my_function(x):
   return math.sqrt(x)


print(my_function(9)) # Vypise 3
print(my_function(36)) # Vypise 6
print(my_function(100)) # Vypise 10