
# Convertendo TIPOS
# função builtin (função nativa, que não precisa de biblioteca externa para utilizar)
input_primeiro_numero = input('Digite um número: ')
input_segundo_numero = input('Digite o segundo número: ')

input_primeiro_numero = int(input_primeiro_numero)
input_segundo_numero = int(input_segundo_numero)

print(input_primeiro_numero + input_segundo_numero)

preco = 10
print(preco)
# Saída: 10

preco = float(preco)
print(preco)
# Saída: 10.0

preco = 10 / 2
print(preco)
# Saída: 5.0

# Convertendo String para float
preco = "10.5"
preco = float(preco)
print(preco)
# Saída: 10.5

valor = 10
valor_str = str(valor)

print(type(valor))
print(type(valor_str))

numero1 = 10
numero2 = 2
numero3 = 10
numero4 = 2

print(numero1, numero2, numero3, numero4,  sep='-')