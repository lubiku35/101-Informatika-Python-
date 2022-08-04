# Do prazdneho slovnika pridaj "birds" a "fish". Obe budu mat hodnotu listy.
# "birds" bude mat hodnotu crow a pigeon

# "fish" bude salmon a shrimp

animals = {}

animals["birds"] = ["crow", "pigeon"]
animals["fish"] = ["salmon", "shrimp"]
print(animals["birds"])
print(animals["fish"])

# alebo

animals = {}

animals = {"birds": ["crow", "pigeon"], "fish" : ["salmon", "shrimp"]}

print(animals["birds"])
print(animals["fish"])