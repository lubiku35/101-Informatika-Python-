# Pouzi vhodny logicky operator a podmienky tak, aby vypisany text daval zmysel


def which_color(color):
   if color not in ["red", "blue"]:
      # farba nie je cervena ani modra
      print("color is neither red nor blue")
   else:
      print("color is red or blue")

def which_color_2(color):
   if color != "red" and color != "blue":
      # farba nie je cervena ani modra
      print("color is neither red nor blue")
   else:
      print("color is red or blue")
      
# Ak si chces otestovat svoje riesenie, tak spusti subor a sleduj, ci podla riadkov nizsie vypise to, co sa ma vypisat
which_color("blue") # -> Vypise "color is red or blue"
which_color("red") # -> Vypise "color is red or blue"
which_color("orange") # -> Vypise "color is neither red nor blue"
which_color("yellow") # -> Vypise "color is neither red nor blue"

which_color_2("blue") # -> Vypise "color is red or blue"
which_color_2("red") # -> Vypise "color is red or blue"
which_color_2("orange") # -> Vypise "color is neither red nor blue"
which_color_2("yellow") # -> Vypise "color is neither red nor blue"