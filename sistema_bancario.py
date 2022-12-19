menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Qual o valor a ser depositado?: "))
        if (valor_deposito>0):
            saldo += valor_deposito
            extrato += f"Depósito R${valor_deposito:.2f}\n"
            print(f"Depósito realizado com sucesso. Saldo atual é de: R${saldo:.2f}")
        else:
            print("Valor de deposito não permitido. Operação não realizada.")
    
    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Qual o valor a ser sacado?: "))
        if (numero_saques < 3 and valor_saque <= 500):
            if (saldo - valor_saque >=0):
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque    R${valor_saque:.2f}\n"
                print(f"Saque realizado com sucesso. Saldo atual é de: R${saldo:.2f}")
            else:
                print("Saldo insuficiente. Operação não realizada.")
        else:
            if (numero_saques >= 3):
                print(f"Numero de {LIMITE_SAQUES} saques diários excedido. Operação não realizada.")
            elif (valor_saque > 500):
                print(f"Limite máximo de R${limite:.2f} por saque excedido. Operação não realizada.")      

    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print("---------------------")
        print(f"Saldo    R${saldo:.2f}")

    elif opcao == "q":
        break