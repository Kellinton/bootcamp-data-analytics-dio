contato = {"nome": "ace", "telefone": "3333-2221"}

contato.setdefault("nome", "luffy")  # "ace"
print(contato)  # {'nome': 'ace', 'telefone': '3333-2221'}

contato.setdefault("idade", 18)  # 18
print(contato)  # {'nome': 'ace', 'telefone': '3333-2221', 'idade': 28}