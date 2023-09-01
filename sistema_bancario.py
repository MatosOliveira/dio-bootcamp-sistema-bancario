def menu():
    menu = """

    Digite a opção desejada:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

def sacar(*, saldo, valor):
    if(numero_saques < LIMITE_DIARIO):
        extrato += "Quantidade de saques excede o limite diário. Máximo permitido: {LIMITE_DIARIO}"
    elif(valor <= limite):
        extrato +=  "Valor excede o limite diário para saque. Valor máximo permitido: {limite}"
    else:
        if(saldo > 0):
            saldo -= valor
            numero_saques += 1
            valor_sacado += valor
            extrato += "Quantidade de saques realizados: {} \nValor sacado: R$ {} \nQuantidade de depositos recebidos: {} \nValor depositado: R$ {} \nSaldo atual: R$ {}"
        else:
            print("Saldo insuficiente!")


def exibir_extrato():
    print("testes")

def depositar():
    print("testes")

def encerrar():
    print("testes")

def main():
    saldo = 0.0
    limite = 500.0
    extrato = ""
    deposito = 0
    valor_depositado = 0
    numero_saques = 0
    LIMITE_DIARIO = 3
    valor_sacado = 0

    while True:
        opcao = input(menu) 
        
        if opcao == "e":
            if (numero_saques == 0 and deposito == 0):
                extrato = "Não foram realizadas movimentações."
                print(extrato)
            else:
                extrato = "Quantidade de saques realizados: {} \nValor sacado: R$ {} \nQuantidade de depositos recebidos: {} \nValor depositado: R$ {} \nSaldo atual: R$ {}"
                print(extrato.format(numero_saques, valor_sacado, deposito, valor_depositado, saldo))

        elif opcao == "q":
            break

        else:
            valor = float(input("Digite o valor desejado: "))
            
            if valor > 0:

                if opcao == "d":
                    saldo += valor
                    deposito += 1
                    valor_depositado += valor

                elif opcao == "s":
                    sacar(saldo, valor)

            else:
                print("O valor desejado deve ser maior que 0!")

main()
