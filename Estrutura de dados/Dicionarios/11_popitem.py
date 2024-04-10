contatos = {"ace@gmail.com": {"nome": "ace", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('ace@gmail.com', {'nome': 'ace', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError