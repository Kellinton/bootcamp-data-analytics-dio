# Parâmetros passados por chave=valor


# Keywords arguments

#após o ' *, ' aceita apenas parâmetros nomeados
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


# Positional-only and kewords arguments (híbrido)

#após o ' *, ' aceita apenas parâmetros nomeados
def criar_carro(modelo, ano, /, placa, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
