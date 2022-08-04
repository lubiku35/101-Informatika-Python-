# Vypis zaokruhleny priemer vsetkych pozitivnych cisel v subore numbers.txt


my_file = open("numbers.txt")
average_positive = 0
count = 0
for line in my_file:
   stripped = int(line.strip())
   if stripped > 0:
      average_positive += stripped
      count += 1

my_file.close()
print(round(average_positive / count))