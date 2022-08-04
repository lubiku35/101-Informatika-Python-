# 1.
# Napis program, ktory sa ta dokola bude pytat ci mas rad Python az pokym nepovies ano

should_continue = True
while should_continue:
    answer = input("Mas rad python? ")
    if answer == "ano":
        should_continue = False

print("Konecne spravna odpoved")


# 2.
# Vo while cykle sa pýtaj používateľa, aby si tipol tvoje šťastné číslo.
# Pýtaj sa ho dovtedy, dokým si netipne správne. Ak sa mu to napokon podarí, tak ho pochváľ.

lucky_number = 8
while True:
    number = int(input("Tipni si ake je moje stastne cislo: "))
    if number == lucky_number:
        break
    else:
        print("Nespravne, skus este raz")

print("Chvalim ta")


# 3.
# Napíš funkciu, ktorá bude vypisovať fibonacciho postupnosť do cisla 1000.
# Fibonacciho postupnosť začína číslami 1 a 2. Každé ďalšie číslo sa vypočíta ako súčet predchádzajúcich dvoch čísel.
# Čiže postupnosť by mala vyzerať nejak takto: 1 2 3 5 8 13 21 34 55 89 144 233 ….

def fibonacci():
    n1 = 1
    print(n1)
    n2 = 2
    print(n2)
    while n1 + n2 <= 1000:
        next = n1 + n2 # Vypocitam dalsie cislo vo fibonacci postupnosti
        n1 = n2 # updatnem n1
        n2 = next # updatnem n2
        print(n2)

fibonacci()

# 4.
# V cykle načítavaj vstup od používateľa, ktorý vypisuje iba čísla.
# Tento vstup dokola načítavaj, pokým používateľ nenapíše q.
# Ak ho napíše, tak vypíš súčet a priemer všetkých načítaných čísel.


result = 0
count = 0

should_continue = True

while should_continue:
    user_input = input("Zadaj cislo alebo q ak chces skoncit: ")
    if user_input == "q":
        should_continue = False
    else:
        number = int(user_input)
        count += 1
        result += number

if count >= 1:
    print("Sum is " + str(result))
    avg = result / count
    print("Average is " + str(avg))
else:
    print("No nevypisem ti nic lebo si nezadal ziadne cislo")

# 5.
# Vypis vsetky prvocisla od 1 po 1000. Proviclo je take cislo ktore je delitelne len 1 a sebou samym

for number in range(1, 1001):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)