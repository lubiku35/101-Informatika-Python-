# Vyries slovnu ulohu:

# Majka v praci zarobi kazdy den v mesiaci o jedno euro navyse. Prvy den v mesiaci zarobi 1 euro. Druhy den zarobi 2 eura. Treti den 3 eura. A tak dalej, az v 30. dni mesiaca zarobi 30 eur. Napis program, ktory pomoze Majke vypocitat, kolko penazi zarobi za mesiac. (Dajme tomu, ze mesiac ma 30 dni). Program vypise vyslednu sumu

pay = 1
temp = 0

for i in range(0, 30):
   temp += pay  
   pay += 1


print(temp)
