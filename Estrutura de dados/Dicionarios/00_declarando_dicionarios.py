contatos = {
    "luffy@email.com" : {"nome" : "Luffy", "idade" : 18},
    "ace@email.com" : {"nome" : "Ace", "idade" : 19}
}

print(contatos["ace@email.com"]["nome"])

pessoa = dict(
    nome = "Ace",
    idade = 19
)

print(pessoa["nome"])

contatos = dict(
    acegmailcom = {"nome" : "Ace", "idade" : 19},
    luffygmailcom = {"nome" : "Luffy", "idade" : 18}
)

print(contatos["luffygmailcom"]["nome"])