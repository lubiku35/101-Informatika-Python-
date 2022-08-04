# Do funkcie write_numbers(n) napis kod, ktory vytvori subor numbers.txt. Do suboru napiseme cisla od 1 az po n vratane. Kazde cislo na novy riadok a taktiez odsadene tabulatorom vzdy o jedenkrat viac ako predosle cislo.

def write_numbers(n):
   my_file = open("numbers.txt", "w")
   for i in range(1, n + 1):
      for j in range(1, i):
         my_file.write("\t")
      my_file.write(str(i) + "\n")
   my_file.close()



write_numbers(3)  # Subor bude mat text nasledovne:
# 1
#     2
#         3

write_numbers(7)  # Subor bude mat text nasledovne:
# 1
#     2
#         3
#             4
#                 5
#                     6
#                         7