# Adicionar um novo elemento a lista 


# .append()

# Em Python, append() adiciona um item ao final da lista.
# Em JavaScript, push() adiciona um ou mais itens ao final de um array.

# .clear()

# O método clear() remove todos os elementos de uma lista em Python, deixando-a vazia.
# JavaScript não tem um método equivalente para limpar completamente um array, 
# alcança o mesmo efeito atribuindo um array vazio para redefini-lo.

#.copy()

# O método copy() em Python cria uma cópia superficial (shallow copy) da lista. 
# Isso significa que ele cria uma nova lista e copia os elementos da lista original 
# para a nova lista. Se os elementos forem objetos mutáveis, as referências aos objetos
#  são copiadas, mas os próprios objetos não são duplicados.
# JavaScript não tem um método equivalente chamado copy() para arrays. 
# Você pode criar uma cópia superficial de um array usando o operador spread (...) ou o método slice().

# pyhton                                 # javascript
lista_original = [1, 2, 3]              # const arrayOriginal = [1, 2, 3];
copia_lista = lista_original.copy()     # const copiaArray = [...arrayOriginal];

print(lista_original)
print(copia_lista)

# .count()

# Python - count():

# Python tem o método count() que retorna o número de vezes 
# que um item aparece na lista. JavaScript não tem um método equivalente.

# .extend()

# Python - extend() vs JavaScript - concat():

# Em Python, extend() adiciona os elementos de um iterável (como outra lista) 
# ao final da lista.
# Em JavaScript, concat() cria uma nova matriz combinando 
# a matriz em que foi chamada com outras matrizes e/ou valores.

# .index()

# Python - index() vs JavaScript - indexOf():

# Em Python, index() retorna o índice do primeiro
#  item na lista que corresponde ao valor especificado.
# Em JavaScript, indexOf() retorna o índice da primeira 
# ocorrência de um valor especificado em uma matriz.

# .pop()

# Python - pop() vs JavaScript - pop():

# Ambos os métodos removem e retornam um elemento de uma posição específica da lista/array.
#  A diferença é que em Python o índice é passado como argumento para pop(),
#   enquanto em JavaScript é um método do array 
# e você só precisa chamar pop() sem passar argumentos para remover o último elemento.

# .remove()

# Python - remove() vs JavaScript - splice():

# Em Python, remove() remove o primeiro item da lista que corresponde ao valor especificado.
# Em JavaScript, splice() é uma operação mais poderosa que pode remover, 
# substituir ou adicionar elementos em uma matriz.

# .reverse()

# Python - reverse() vs JavaScript - reverse():

# Ambos os métodos invertem a ordem dos elementos na lista/array.

# .sort()

# Python - sort() vs JavaScript - sort():

# Ambos os métodos ordenam os elementos na lista/array. Em Python, sort() ordena a lista 
# em ordem crescente, enquanto em JavaScript, sort() por padrão classifica os elementos como strings Unicode.

# .len()

# Python - len() vs JavaScript - length:
# Em Python, len() retorna o número de elementos em uma lista.
# Em JavaScript, length é uma propriedade de array que indica o número de elementos na matriz.

# .insert()

# Python - insert():

# Python tem o método insert() para inserir um item em uma posição específica na lista.
#  JavaScript não tem um método equivalente, mas pode-se usar a técnica de splicing para 
#  alcançar resultados semelhantes.