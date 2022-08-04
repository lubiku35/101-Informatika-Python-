# Do modulu my_module vytvor funkciu say_hello s jednym parametrom. Tato funkcia pozdravi nasledovne. Ak je parameter "Petra", tak funkcia vypise "Hello Petra"

# Dalej v task.py pouzi say_hello vo funkcii my_task s premennou my_name.

from my_module import say_hello

def my_task():
   my_name = "Jakub"
   say_hello(my_name)

my_task() # Prints "Hello Jakub"