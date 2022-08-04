# V task_file.txt je 2000 nahodnych cisel od -100 po 100. Tvojou ulohou je vypisat cislo, ktore sa v tomto subore nachadza najviackrat

my_file = open("task_file.txt")

occurrencies = {}

for line in my_file:
   number = int(line.strip())
   occurrencies[number] = occurrencies.get(number, 0) + 1

maximum = 0
max_value = 0

for key in occurrencies:
   if occurrencies[key] > max_value:
      maximum = key
      max_value = occurrencies[key]

print(maximum)