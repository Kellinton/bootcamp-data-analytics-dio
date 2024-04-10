contatos = {"ace@gmail.com": {"nome": "ace", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get("chave", "Chave não encontrada")  # Chave não encontrada
print(resultado)

resultado = contatos.get(
    "ace@gmail.com", {}
)  # {"ace@gmail.com": {"nome": "ace", "telefone": "3333-2221"}
print(resultado)