contatos = {"ace@gmail.com": {"nome": "ace", "telefone": "3333-2221"}}

resultado = contatos.pop("ace@gmail.com")  # {'nome': 'ace', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("ace@gmail.com", {})  # {}
print(resultado)