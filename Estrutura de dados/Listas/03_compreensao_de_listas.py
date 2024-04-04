# compreensão de listas (pegar dados de uma lista existente e armazenar em uma nova lista)

# PRIMEIRA FORMA DE FILTRO

numeros = [5, 20, 89, 10, 7, 6, -1, -2 , 110]
numeros_pares = []
numeros_impares = []

for numero in numeros:
    if numero % 2 == 0:

        numeros_pares.append(numero)
        #numeros_pares.push(numero) (forma de adicionar em JS)
    else:
        numeros_impares.append(numero)
        
print(f'''
    
    
                    NÚMEROS

    NÚMEROS PARES: {numeros_pares}
    NÚMEROS ÍMPARES: {numeros_impares}


''')

# SEGUNDA FORMA DE FILTRO

numeros = [5, 20, 89, 10, 7, 6, -1, -2 , 110]

numeros_pares = [numero for numero in numeros if numero % 2 == 0]
numeros_impares = [numero for numero in numeros if numero % 2 == 1]

print(numeros_pares)
print(numeros_impares)



numeros = [5, 20, 10, 7]
numero_quadrado = [numero ** 2 for numero in numeros] # elevar os números ao quadrado