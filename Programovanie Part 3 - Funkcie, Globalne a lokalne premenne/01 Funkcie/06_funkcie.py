# Sprav funkciu is_between, ktora ma 3 parametre x,y,z. Funkcia vrati pravdivostnu hodnotu, ci sa x nachadza medzi y a z

def is_between(x, y, z):
   
   if x > y and x < z:
      return True
