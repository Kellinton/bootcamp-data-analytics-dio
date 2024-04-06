conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)

# quando elementos de um conjunto não estão presentes em outro conjunto
# Conjuntos Disjuntos: Em matemática, dois conjuntos são ditos disjuntos se não tiverem nenhum elemento em comum