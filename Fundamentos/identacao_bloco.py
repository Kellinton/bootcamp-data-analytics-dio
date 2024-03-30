# def sacar(self, valor: float): # os : seria o {} do javascript e serve para abrir um bloco de código
#     if self.saldo >= valor: # : abre o bloco de código da condicional If
#         self.saldo -= valor

# método sacar

def sacar(saldo, valor):
    if valor > saldo:
        print('Saldo Insuficiente!')
        print('--------------------')
        print('                     ')

    else:
        saldo_restante = saldo - valor
        print(f'Valor de R$ {valor} foi sacado!')
        print('--------------------------------')
        print('                                 ')
        print(f'Saldo restante: R$ {saldo_restante}')


print('             BANCO             ')
print('-------------------------------')
print('                               ')
       
saldo_disponivel = float(542)
valor_sacar = float(input('Quanto deseja sacar? '))
print('                               ')






print(sacar(saldo_disponivel, valor_sacar))