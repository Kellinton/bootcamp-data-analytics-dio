contatos = {
    "ace@gmail.com": {"nome": "ace", "telefone": "3333-2221"},
    "luffy@gmail.com": {"nome": "luffy", "telefone": "3443-2121"},
    "sanji@gmail.com": {"nome": "sanji", "telefone": "3344-9871"},
    "zoro@gmail.com": {"nome": "zoro", "telefone": "3333-7766"},
}


del contatos["ace@gmail.com"]["telefone"]
del contatos["zoro@gmail.com"]

# {'ace@gmail.com': {'nome': 'ace'}, 'luffy@gmail.com': {'nome': 'luffy', 'telefone': '3443-2121'}, 'sanji@gmail.com': {'nome': 'sanji', 'telefone': '3333-7766'}}  # noqa
print(contatos)