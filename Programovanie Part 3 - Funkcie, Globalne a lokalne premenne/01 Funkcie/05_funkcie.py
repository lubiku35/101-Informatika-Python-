# Dopis do funkcii potrebny kod

# Vrati rozdiel
def difference(a, b):
   return a - b

# Vrati vacsie cislo z dvoch parametrov (ak su cisla rovnake tak vrati hocijake z nich)
def bigger_number(a, b):
   if a > b:
      return a
   elif b > a:
      return b
   else:
      return a or b

# result bude 15:
#   najprv ziskame vacsie cislo z 10 a 20, co je 20
#   potom ziskame vacsie cislo z 3 a 5, co je 5
#   na zaver odpocitame 5 od 20, resp 20 - 5
#   vysledok ulozime do result
result = difference(bigger_number(10, 20), bigger_number(3, 5))
print(result) # vypise 15

# Co vypise toto? Subor si vzdy mozes spustit a overit vysledok
print(difference(bigger_number(6, 12), bigger_number(4, 3)))