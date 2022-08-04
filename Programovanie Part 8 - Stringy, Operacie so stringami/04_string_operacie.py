# Funkcia skip_first_line prijme text, ktory ma (mozno) viacero riadkov. Jej uloha je vratit novy text, ktory bude obsahovat vsetky riadky okrem prveho. Ak text neobsahuje viac ako jeden riadok, tak funkcia vrati text "nice try"


def skip_first_line(lines):
   index = lines.find("\n")
   if index == -1:
      return "nice try"
   else:
      return lines[index + 1:]