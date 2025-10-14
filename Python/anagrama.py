#Codigo para saber si dos palabras son anagramas.

def is_anagram(word1, word2):
    if word1.lower() == word2.lower():  # Si las palabras son iguales, no son anagramas
        return False
    return sorted(word1.lower()) == sorted(word2.lower())   # Convertimos ambas palabras a minúsculas y las ordenamos

print(is_anagram("Paco", "Copa"))