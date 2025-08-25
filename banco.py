
print('-+'*10)
print(" SISTEMA BANCARIO")
print('-+'*10)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

# Opções do sistema
menu = """
[1] Deposito
[2] Saque 
[3] Extrato
[4] Sair 

""" 
while True:
    opção = input('Insira a opção desejada: ')
    if opção == '1':
        dp = float(input('Insira o valor desejado R$ '))
        if dp > 0:
            saldo += dp
            extrato += f'Deposito de R${dp:.2f} realizado com sucesso\n'
            print(extrato)
        else:
            print("Valor invalido!")

    elif opção == '2':
        sq = float(input('Insira o valor desejado R$ '))
        excedeu_saldo = sq > saldo
        excedeu_limite = sq > limite
        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo o suficiente.')
        elif excedeu_limite:
            print("Operação falhou! Valor excede o limite de saque.")
        elif excedeu_saques:
            print('Operação falhou! Número limite de saques excedido')
        
        elif sq > 0:
            saldo -= sq
            numero_saques += 1
            extrato += f'Saque de R${sq:.2f} realizado com sucesso\n'
            print(extrato)
        else:
            print('Operação falhou tente novamente')
        
    elif opção == '3':
        print('====== EXTRATO ======')
        print('Não foram realizados movimentações' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')

    elif opção == '4':
        print('Sistema encerrando...')
        break
    
    else:
        print('Valor invalido, tente novamente!')

# Deposito
   
# Saque

# Mostrar extrato

