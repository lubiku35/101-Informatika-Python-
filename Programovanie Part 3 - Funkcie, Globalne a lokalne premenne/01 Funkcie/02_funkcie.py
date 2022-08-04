# Zabezpec, aby funkcia return_concatenate(a, b) vratila spojene dva texty "a" a "b".

def return_concatenate(a, b):
   return a + b


helloworld = return_concatenate("hello ", "world")
print(helloworld) # Vypise hello world

print(return_concatenate("informatika", "101")) # Vypise informatika101