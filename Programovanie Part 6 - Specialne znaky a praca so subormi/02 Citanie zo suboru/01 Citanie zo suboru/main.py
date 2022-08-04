# Precitaj subor my_file a vypis na obrazovku. Pozor aby si nevypisal/a navyse prazdne riadky

my_file = open("my_file.txt")

for line in my_file:
   stripped_line = line.rstrip()
   print(stripped_line)

my_file.close()