# Mali by byt dva sposoby, akym mozes spocitanim dvoch hodnot z listu numbers ziskat cislo 5. Pristup k cislam pomocou indexov.

numbers = [5, -10, 15, 25, 3, 10, 2]
first_possibility = numbers[1] + numbers[2]
second_possibility = numbers[-5] + numbers[-6]

print(first_possibility) # Should print 5
print(second_possibility) # Should print 5
if first_possibility != second_possibility != 5:
   print("task failed")