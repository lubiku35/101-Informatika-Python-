# Vo funkcii is_word_reserved mas vratit True alebo False podla toho, ci je slovo rezervovane a nemoze byt pouzite ako identifikator premennych alebo funkcie.

# Existuje zabudovany modul, ktory ti vie pomoct

import keyword


def is_word_reserved(word):
   return keyword.iskeyword(word)


print(is_word_reserved("True"))  # Vypise True
print(is_word_reserved("False"))  # Vypise True
print(is_word_reserved("continue"))  # Vypise True
print(is_word_reserved("not"))  # Vypise True
print(is_word_reserved("blabla"))  # Vypise False
print(is_word_reserved("variable"))  # Vypise False
print(is_word_reserved("my_variable"))  # Vypise False
print(is_word_reserved("name"))  # Vypise False