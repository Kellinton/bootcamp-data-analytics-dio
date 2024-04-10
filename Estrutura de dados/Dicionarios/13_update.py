contatos = {"ace@gmail.com": {"nome": "ace", "telefone": "3333-2221"}}

contatos.update({"ace@gmail.com": {"nome": "portgas"}})
print(contatos)  # {'ace@gmail.com': {'nome': 'portgas'}}

contatos.update({"luffy@gmail.com": {"nome": "luffy", "telefone": "3322-8181"}})
# {'ace@gmail.com': {'nome': 'portgas'}, 'luffy@gmail.com': {'nome': 'luffy', 'telefone': '3322-8181'}}
print(contatos)