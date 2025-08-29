

def depositar(opção, saldo, dp, extrato, /):
    opção = input('Insira a opção desejada: ')
    if opção == '1':
        dp = float(input('Insira o valor desejado R$ '))
    if dp > 0:
        saldo += dp
        extrato += f'Deposito de R${dp:.2f} realizado com sucesso\n'
        print(extrato)
    else:
        print("Valor invalido!")
        
    return saldo, extrato

def sacar(*, opção, saldo, sq, extrato, limite, numero_saques, limite_saque ):
    if opção == '2':
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

def criar_usuarios(usuarios):
    cpf = int(input('Informe seu CPF (somente números): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print('Já existe um usuario com esse cpf')
        return
    nome = input('Infome seu nome completo: ')
    data_nascimento = input('Informe a data de nascimento: ')
    endereco = input('Informe seu endereço (logradouro, nr, bairro - cidade - cigla do estado): ')
    usuarios.append({"nome": nome, 'data_nascimento:': data_nascimento, 'cpf': cpf, 'endereço': endereco})
    print('Usuario criado com sucesso!')

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuarios = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuario não encontrado, fluxo de criação encerrado.')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agencia:\t{conta['agencia']}
        C/C:\t\t{conta['numero_contas']}
        Titular:\t{conta['usuario']['nome']}
    """
        

def main():
    print('-+'*10)
    print(" SISTEMA BANCARIO")
    print('-+'*10)

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 3
    agencia = '0001'
    usuarios = []
    contas = []

    while True:
        menu = print("[1] Deposito",
                     '\n[2] Saque',
                     '\n[3] Extrato',
                     '\n[4] Cadastro de usuario',
                     '\n[5] Criar conta' \
                     '\n[6] Listar usuarios'
                     '\n[0] Sair')
        
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
            criar_usuarios(usuarios)

        elif opção == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            

        elif opção == '0':
            print('Sistema encerrando...')
            break
        
        else:
            print('Valor invalido, tente novamente!')



main()