# Funkcia my_function vrati string vytvoreny z prvych 3 a poslednych 3 znakov parametra. Ak vsak ma parameter menej ako 3 znaky, tak vrat prazdny string.


def my_function(param: str):
   if len(param) < 3:
      return ""
   else:
      return param[:3] + param[-3:]