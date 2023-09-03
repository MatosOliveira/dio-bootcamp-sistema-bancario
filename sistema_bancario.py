import textwrap

def menu():
    menu = """\n

    Digite a opção desejada:

    [d]\tDepositar
    [s]\tSacar
    [e]\tExibir Extrato
    [c]\tCriar nova conta
    [l]\tListar conta(s)
    [u]\tCriar novo usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def sacar(*, saldo, valor, extrato, numero_saques, limite_diario, valor_limite):
    if(numero_saques > limite_diario):
        print("Quantidade de saques excede o limite diário. Máximo permitido: {limite_diario}")

    elif(valor > valor_limite):
        print("Valor excede o limite diário para saque. Valor máximo permitido: {valor_limite}")

    else:
        if(saldo > 0):
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("Saldo insuficiente!")

    return saldo, extrato


def exibir_extrato(numero_saques, saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")

    return saldo, extrato


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
    print("Testes")


def verifica_usuario(cpf, usuarios):
    usuario_verificado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_verificado[0] if usuario_verificado else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o numero do CPF (somente numeros): ")
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


def main():
    
    LIMITE_DIARIO = 3
    AGENCIA = "0001"

    saldo = 0.0
    valor_limite = 500.0
    extrato = ""
    numero_saques = 0
   
    contas = []
    usuarios = []

    while True:
        opcao = menu()
        
        if opcao == "e":
            exibir_extrato(numero_saques, saldo, extrato=extrato)

        elif opcao == "q":
                break
            
        elif opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato = sacar(
                saldo= saldo, 
                valor= valor, 
                extrato= extrato, 
                numero_saques=numero_saques, 
                limite_diario=LIMITE_DIARIO, 
                valor_limite=valor_limite
            )

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "u":
            criar_usuario(usuarios)

        else:
            print("Opção inválida.")

main()
