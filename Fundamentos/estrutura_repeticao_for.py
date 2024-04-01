# const texto = 'pessoa';
# const vogais = 'AEIOU';

# for (const letra of texto) {
#    if(vogais.includes(letra.toLocaleUpperCase())) {
#         console.log(letra);
#    }
# } em javascript


texto = 'pessoa'
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in  VOGAIS:
        print(letra, end='')
print()

# função range
# range(0, 11, 2) 0 é o início (start) / 11 é o fim (stop) / 2 é que será de 2 em 2 (step/ passo).
# print(list(range(0, 11)))
print(list(range(0, 51, 5)))
# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")