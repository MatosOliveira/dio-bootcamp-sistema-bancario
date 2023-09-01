menu = """

Digite a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

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
                if (numero_saques < LIMITE_DIARIO) and (valor <= 500.0):
                    if(saldo > 0):
                        saldo -= valor
                        numero_saques += 1
                        valor_sacado += valor
                    else:
                        print("Saldo insuficiente.")
                        
                else:
                    print("Limite ou valor diario excedido")

        else:
            print("O valor desejado deve ser maior que 0!")
