# Pouzi vhodne podmienky a operator tak, aby vypisany text daval zmysel




def which_color(color):
   if color == "red" or color == "blue":
      print("color is red or blue")
   elif color == "orange" or color == "yellow":
      print("color is orange or yellow")
   else:
      print("color is unknown")

def which_color_2(color):
   if color in ["red", "blue"]:
      print("color is red or blue")
   elif color in ["orange", "yellow"]:
      print("color is orange or yellow")
   else:
      print("color is unknown")


# Ak si chces otestovat svoje riesenie, tak spusti subor a sleduj, ci podla riadkov nizsie vypise to, co sa ma vypisat
which_color("blue") # -> Vypise "color is red or blue"
which_color("red") # -> Vypise "color is red or blue"
which_color("orange") # -> Vypise "color is orange or yellow"
which_color("yellow") # -> Vypise "color is orange or yellow"
which_color("black") # -> Vypise "color is unknown"