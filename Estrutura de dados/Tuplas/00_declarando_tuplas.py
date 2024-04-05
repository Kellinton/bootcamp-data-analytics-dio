# tuplas são estruturas de dados parecida com as listas,
# a principal diferença é que as tuplas são IMUTÁVEIS enquanto
# listas são MUTÁVEIS(que pode ser alterado). 
# Usa-se a  classe tuple para criar tuplas, ou colocando valores
# separados por vírgula de parenteses () ex: tupla = ()
# lista = [1, 2, 3] // tupla = (1, 2, 3) // lista = [] // tupla = ()
# em python chamamos de lista e em javascript chamamos de array, array = Array()

lista = tuple(range(5, 10, 2))
pais = ("brasil",) # colocar ',' para o python não confundir com uma precedência de valores de uma operação matemática, mas sim uma tupla
print(pais)

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)
