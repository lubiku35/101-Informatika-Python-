# Toto je uloha, ktora sa zvykne davat (v roznych formach) na pohovoroch.
# Ak je x delitelne 3 a zaroven 5 tak vypis FizzBuzz
# Ak je x delitelne iba 3 tak vypis Fizz
# Ak je x delitelne iba 5 tak vypis Buzz
# Ak ani jedna podmienka nie je splnena, tak vypis x

def fizzbuzz(x):
   # Pis pod tymto riadkom. Vsetok tvoj kod musi byt odsadeny
   divisible_by_3 = x % 3 == 0
   divisible_by_5 = x % 5 == 0

   if divisible_by_3 and divisible_by_5:
      print("FizzBuzz")
   elif divisible_by_3:
      print("Fizz")
   elif divisible_by_5:
      print("Buzz")
   else:
      print(x)



# Ak si chces otestovat svoje riesenie, tak spusti subor a sleduj, ci podla riadkov nizsie vypise to, co sa ma vypisat
fizzbuzz(15) # Vypise FizzBuzz
fizzbuzz(9) # Vypise Fizz
fizzbuzz(20) # Vypise Buzz
fizzbuzz(13) # Vypise 13
fizzbuzz(1) # Vypise 1
fizzbuzz(2) # Vypise 2