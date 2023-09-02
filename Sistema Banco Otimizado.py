import textwrap

def menu():
    menu = """\n
    ======== BEM-VINDO AO BANCO MEGA =========

    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [c]\tCadastrar Usuário
    [cc]\tCriar Conta Corrente
    [lc]\tListar Contas
    [q]\tSair

    ==========================================
    Comando => """
    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente!")

    elif excedeu_limite:
        print("Limite de valor de saque excedido!")

    elif excedeu_saques:
        print("Número de saques diários excedido!")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso')

    else:
        print("Valor inválido! Tente valores positivos.")

    return saldo, extrato

    
def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print('\n Depósito realizado com sucesso')

    else:
        print('Valor inválido! Tente valores positivos.')
    
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("============================== EXTRATO ==============================")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=====================================================================")

def cadastro_clientes(usuarios):
    
    cpf = input('Informe seu CPF (somente números): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Conta já cadastrada')
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento(DD/MM/AAAA): ')
    endereco = input('Informe seu endereço (logradouro, n° - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário cadastrado com sucesso')

def filtrar_usuarios(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastro_contas(agencia, numero_conta, usuarios):

    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\n Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n Usuario não encontrado, fluxo de criação de conta encerrado!')
    return None

def listar_contas(contas):

    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
    """
    print('=' * 100)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor de depósito: '))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor de saque: '))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            extrato(saldo, extrato=extrato)

        elif opcao == 'c':
            cadastro_clientes(usuarios)

        elif opcao == 'cc':
            numero_conta = len(contas) + 1
            conta = cadastro_contas(AGENCIA, numero_conta, usuarios)

            if conta:
                conta.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Opção inválida! Por gentileza selecione alguma opção do menu principal.')

main()