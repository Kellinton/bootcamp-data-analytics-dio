opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")





escolha = 8

while escolha != 10:
    if(escolha % 2 == 0):
        print(f'{escolha} é PAR!')

    elif(escolha % 2 == 1):
        print(f'{escolha} é ÍMPAR!')

print('Obrigado por utilizar o programa!')

