# Pouzi potrebne funkcie listu tak, aby komenty zodpovedali kodu.

vegetables = ["carrot", "cucumber", "ginger", "pumpkin"]
vegetables.remove("cucumber")
print(vegetables)  # ['carrot', 'ginger', 'pumpkin']

vegetables.append("salad")
print(vegetables)  # ['carrot', 'ginger', 'pumpkin', 'salad']

vegetables.pop()
print(vegetables)  # ['carrot', 'ginger', 'pumpkin']

# Tu nepouzi funkciu, ale zmen hodnotu prvku v liste
vegetables[0] = "onion"
print(vegetables)  # ['onion', 'ginger', 'pumpkin']

# Tu pouzi funkciu, ktora obrati prvky v liste.
# Skus vygooglit, lebo som to nespomenul
vegetables.reverse()
print(vegetables)  # ['pumpkin', 'ginger', 'onion']
