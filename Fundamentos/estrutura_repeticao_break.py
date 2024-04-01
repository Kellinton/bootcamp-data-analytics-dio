# utilizando break em um loop infinito

while True:
    numero = int(input('Informe um número: '))

    if numero == 10:
        break

    print(numero)


for number in range(100):

    if number % 2 == 0:
        continue

    print(number, end=" ")