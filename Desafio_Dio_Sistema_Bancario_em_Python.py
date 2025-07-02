menu = """
Bem-vindo(a) ao Banco Python!
Escolha uma opção:

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
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("O número máximo de saques é 3 por dia.")
        valor = float(input("Informe o valor do saque: "))
        if 0 < valor <= saldo and numero_saques < LIMITE_SAQUES and valor <= limite:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! Verifique as condições e tente novamente.")

    elif opcao == "e":
        print("\n================ EXTRATO ================\n")
        print(extrato if extrato else "Nenhuma transação realizada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("\n==========================================\n")

    elif opcao == "q":
        print("Obrigado por usar o Banco Python! Até logo!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")