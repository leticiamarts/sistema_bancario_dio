def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, valor, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    while True:
        opcao = input(menu)

        match opcao:
            case "d":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, extrato, valor)

            case "s":
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(saldo, extrato, valor, numero_saques, limite, LIMITE_SAQUES)

            case "e":
                exibir_extrato(saldo, extrato)

            case "q":
                print("Saindo do sistema... ")
                break

            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
