print(1 + 10)
print(True)
print(False)
print('python')

int(5)
str('python')
bool()
float()

print(str('11') + str('10'))
print(int(11) + int(10))



# dir()
# dir Sem argumentos retorna  a lista de nomes no escopo local
# dir Com argumento retorna uma lista de métodos para o objeto

# print(dir())
# print(dir(2))


# # help() um guia que completo sobre um método, função... 
# help(float)

idade = 18 # definição de variável (python não tem constante, mas tem uma convenção de utilizar o nome da variável em maiusculo para ser uma constante)
IDADE = 18 # constante
nome = 'Ace'
genero = 'Masculino'


# Método .format() permite inserir valores 
# em uma string usando marcadores de posição e, 
# em seguida, fornecer os valores separadamente 
# como argumentos para o método 
print('Meu nome é {}. Tenho {} anos e sou {}'.format(nome, idade, genero))

# forma de formatação de string que permite inserir 
# valores de variáveis diretamente dentro da string.
#  Isso é semelhante ao que é feito com template strings no JavaScript.
print(f'Meu nome é {nome}. Tenho {idade} anos , e sou {genero}')

