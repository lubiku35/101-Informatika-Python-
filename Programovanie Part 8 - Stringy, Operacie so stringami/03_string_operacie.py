# Funkcia my_string_function robi nasledovne:
#Ak su vsetky znaky v parametri upper case, tak ich vsetky zmeni na lower case

# Ak su vsetky znaky v parametri lower case, tak ich vsetky zmeni na upper case

# Ak nie su vsetky ani upper ani lower tak vrati taky string aky dostala

# Poznamka: Ak napiseme str_param: str tak povieme PyCharm, ze ocakavame string,
# ale Python nam v skutocnosti dovoli poslat aj nieco ine ako string
# Vyhoda je ta, ze nam PyCharm bude doplnat funkcie nad premennou str_param

# V tejto funkcii dopln kod
def my_string_function(str_param: str):

   if str_param.isupper():
      return str_param.lower()
   elif str_param.islower():
      return str_param.upper()
   else:
      return str_param