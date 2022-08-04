# Vo funkcii factorial vypocitaj faktorial cisla x. (Faktorial cisla 5 je 5 * 4 * 3 * 2 * 1)

# Tento vypocet by si vedel spravit aj manualne pomocou for cyklu, ale naco by si to robil, ked uz na to existuje funkcia v zabudovanom module.

# Tvojou ulohou je zistit o aky modul a funkciu ide a pouzit ju v ulohe.

import math


def factorial(x):
   return math.factorial(x)


print(factorial(5))  # Vypise 120
print(factorial(10))  # Vypise 3628800
print(factorial(2))  # Vypise 2