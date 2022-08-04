# Dopis v programe potrebne prikazy tak, aby sa preskocilo vypisanie cisla ak cislo bude 4 alebo 6

i = 1
while i <= 10:
   if i == 4 or i == 6:
      i += 1
      continue
   print(i)
   i += 1 # Skrateny zapis inkrementovania (i = i + 1)