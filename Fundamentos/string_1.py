texto = 'Python'

print(texto.upper()) # PYTHON
print(texto.lower()) # python
print(texto.title()) # Python

print(texto.strip()) #Python remover espaços dos lados, lstrip para a esuqerda e rstrip para a direita
# console.log(texto.trim()) remover espaços em javascript

print(texto.center(40, "#")) #   ##Python## centralizar com 40 caracteres

print(" . ".join(texto)) #P.y.t.h.o.n # Juntar com ponto

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))