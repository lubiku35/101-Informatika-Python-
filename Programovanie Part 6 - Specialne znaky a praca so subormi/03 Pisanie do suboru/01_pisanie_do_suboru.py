# Vo funkcii create_file() vytvor subor my_file.txt do ktoreho vloz text tak, aby obsah suboru mal nasledovne 2 riadky
# Informatika 101
# www.streetofcode.sk

def create_file():
   file = open("my_file.txt", "w")
   file.write("Informatika 101\nwww.streetofcode.sk")
   file.close()
