# Napis funkciu s nazvom my_function, ktora vypise iba neparne cisla od x po y (vratane y, x a y su parametrami funkcie)

def my_function(x, y):
   for i in range(x, y + 1):
      if i % 2 != 0:
         print(i)