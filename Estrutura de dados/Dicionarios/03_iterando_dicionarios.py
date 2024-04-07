contatos = {
    "luffy@gmail.com": {"nome": "Luffy", "telefone": "3333-2221"},
    "ace@gmail.com": {"nome": "Ace", "telefone": "3443-2121"},
    "zoro@gmail.com": {"nome": "Zoro", "telefone": "3344-9871"},
    "sanji@gmail.com": {"nome": "Sanji", "telefone": "3333-7766"},
}


for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)