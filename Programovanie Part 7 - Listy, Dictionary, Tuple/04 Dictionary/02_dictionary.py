# Do funkcie my_function dopis kod, ktory vytvori a vrati slovnik, ktory bude mat keys hodnoty od m do n zaroven a values budu tieto cisla umocnene na 2

def my_function(m, n):
   dictionary = {}
   for i in range(m, n+1):
      dictionary[i] = i * i
   return dictionary
