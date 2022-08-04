# Pridaj potrebnu podmienku, aby si zistil, ci je cislo x parne alebo neparne

def even_or_odd(x):
   # Nizsie pridaj kod (nevsimaj si riadok vyssie)
   if x % 2 == 0:
      print("x is even")
   else:
      print("x is odd")

# alebo

def even_or_odd_2(x):
   # Nizsie pridaj kod (nevsimaj si riadok vyssie)
   if not x & 1:
      print("x is even")
   else:
      print("x is odd")

even_or_odd(2)
even_or_odd_2(2)
