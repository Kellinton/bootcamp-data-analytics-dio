nome = 'Fulano'
idade = 18
profissao = "Desenvolvedor"
linguagem = "Python"
saldo = 45.435

pessoa = {
    "nome": "Fulano",
    "idade": 18
}

print("Nome:  %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**pessoa))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}") # :10.2f  (10 de espaço, 2 casas e f para número float)


print(nome[0])