# Funkcia my_function zisti, ktory znak je v texte najcastejsie a potom vrati tolkokrat ten isty znak za sebou


def my_function(param: str):
   result = ""
   highest_occurrence = 0

   for i in param:
      if param.count(i) > highest_occurrence:
         result = i
         highest_occurrence += 1

   return result * highest_occurrence


print(my_function("aaabb"))  # aaa
print(my_function("babab"))  # bbb
print(my_function("12312312333"))  # 33333