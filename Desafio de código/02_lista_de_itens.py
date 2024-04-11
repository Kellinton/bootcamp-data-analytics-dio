# Lista para armazenar os itens
itens = []

# Loop para cadastrar os itens
for i in range(3):
    item = str(input())
    itens.append(item)

# Exibindo a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")