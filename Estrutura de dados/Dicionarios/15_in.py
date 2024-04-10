contatos = {
    "ace@gmail.com": {"nome": "ace", "telefone": "3333-2221"},
    "luffy@gmail.com": {"nome": "luffy", "telefone": "3443-2121"},
    "sanji@gmail.com": {"nome": "sanji", "telefone": "3344-9871"},
    "zoro@gmail.com": {"nome": "zoro", "telefone": "3333-7766"},
}

resultado = "ace@gmail.com" in contatos  # True
print(resultado)

resultado = "nami@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["ace@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["luffy@gmail.com"]  # True
print(resultado)