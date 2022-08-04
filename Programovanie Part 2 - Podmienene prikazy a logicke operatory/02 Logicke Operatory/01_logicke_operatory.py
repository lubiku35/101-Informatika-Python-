# Vyuzi vhodny logicky operator a vytvor (zlozeny vyrok) podmienku tak, aby si zistil/a, ze x je medzi 10 a 100

def between_10_and_100(x):
   # Nizsie pridaj kod (nevsimaj si riadok vyssie)
   if x > 10 and x < 100:
      print("x is between 10 and 100")

# Ak si chces otestovat svoje riesenie, tak spusti subor a sleduj, ci podla riadkov nizsie vypise to, co sa ma vypisat
between_10_and_100(9.9) # -> Nevypise nic
between_10_and_100(50) # -> Vypise "x is between 10 and 100"