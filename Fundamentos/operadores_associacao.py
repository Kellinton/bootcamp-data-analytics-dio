# in verifica se um objeto está presente em uma sequência

curso = 'Curso de Python' # Sequência de Caracteres
frutas = ['laranja', 'uva', 'limão'] # Sequência Lista
saques = [1500, 100] # Sequência Lista

verificar_sequencia_caracter = 'Python' in curso
print(verificar_sequencia_caracter) # True

verificar_sequencia_lista_frutas = 'maçã' not in frutas
print(verificar_sequencia_lista_frutas) # True

verificar_sequencia_lista_saques = 200 in saques
print(verificar_sequencia_lista_saques) # False
