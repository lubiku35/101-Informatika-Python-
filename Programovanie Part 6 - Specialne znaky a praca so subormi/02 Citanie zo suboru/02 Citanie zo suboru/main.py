# Vypis pocet negativnych cisel v subore numbers.txt


my_file = open("numbers.txt")
counter = 0
for line in my_file:
   stripped = int(line.strip())
   if stripped < 0:
      counter += 1

my_file.close()
print(counter)


