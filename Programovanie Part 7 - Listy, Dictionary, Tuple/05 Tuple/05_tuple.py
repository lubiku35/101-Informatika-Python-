# Dopln kod tak, aby funkcia min_and_max vracala tuple, v ktorom prvy item je najmensi prvok z list_param a druhy item najvacsi prvok

def min_and_max(list_param):
   return min(list_param), max(list_param)



print((1, 3) == min_and_max([1, 2, 3]))  # (1, 3)
print(min_and_max([-10, 20, -5, 10, 50]))  # (-10, 50)