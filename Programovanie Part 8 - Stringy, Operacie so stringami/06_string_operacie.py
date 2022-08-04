# Funkcia get_sum_from_text vrati sucet vsetkych cisel v texte

def get_sum_from_text(param: str):
   sum = 0
   for char in param:
      if char.isdigit():
         sum += int(char)
   return sum


print(get_sum_from_text("aa123"))  # 6
print(get_sum_from_text("he11o informatika 101 \n mega course"))  # 4
print(get_sum_from_text("1 0 0 1 3 4 5 6 -1 s a b"))  # 21
print(get_sum_from_text("1a2b3c 4a5b"))  # 15