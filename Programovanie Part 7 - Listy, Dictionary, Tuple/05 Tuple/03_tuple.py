# Vo funkcii check zisti, ci su vsetky prvy v tuple rovnake

def check(my_tuple):
   for i in my_tuple:
      if i != my_tuple[0]:
         return False
   return True

print(check((1, 1, 1, 1)))  # True
print(check((1, 1, 2, 1)))  # False
print(check((1, 1, "c", 1)))  # False
print(check(("a", "a", "a", "a")))  # True