from typing import List

class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.contas: List[Conta] = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, agencia: str, numero_conta: str, cliente: Cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0
        self.limite = 500
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor: float):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if self.extrato:
            for operacao in self.extrato:
                print(operacao)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome: str, cpf: str):
        if self.verificar_cpf_existente(cpf):
            print(f"Cliente com CPF {cpf} já existe.")
        else:
            cliente = Cliente(nome, cpf)
            self.clientes.append(cliente)
            print(f"Cliente {nome} cadastrado com sucesso!")
            return cliente

    def verificar_cpf_existente(self, cpf: str) -> bool:
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return True
        return False

    def criar_conta(self, agencia: str, numero_conta: str, cliente: Cliente):
        conta = Conta(agencia, numero_conta, cliente)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        print(f"Conta {numero_conta} criada com sucesso para o cliente {cliente.nome}!")
        return conta

    def visualizar_historico(self, cliente: Cliente):
        print(f"\nHistórico do cliente {cliente.nome}:")
        for conta in cliente.contas:
            print(f"\nAgência: {conta.agencia}, Conta: {conta.numero_conta}")
            conta.exibir_extrato()

def main():
    banco = Banco()

    menu_principal = """
    [1] Cadastrar Cliente
    [2] Criar Conta
    [3] Depósito
    [4] Saque
    [5] Extrato
    [6] Histórico do Cliente
    [7] Sair
    => """

    cliente = None
    conta = None

    while True:
        opcao = input(menu_principal)

        match opcao:
            case "1":
                nome = input("Informe o nome do cliente: ")
                cpf = input("Informe o CPF do cliente: ")
                cliente = banco.cadastrar_cliente(nome, cpf)

            case "2":
                if cliente:
                    agencia = input("Informe o número da agência: ")
                    numero_conta = input("Informe o número da conta: ")
                    conta = banco.criar_conta(agencia, numero_conta, cliente)
                else:
                    print("Por favor, cadastre um cliente primeiro.")

            case "3":
                if conta:
                    valor = float(input("Informe o valor do depósito: "))
                    conta.depositar(valor)
                else:
                    print("Por favor, crie uma conta primeiro.")

            case "4":
                if conta:
                    valor = float(input("Informe o valor do saque: "))
                    conta.sacar(valor)
                else:
                    print("Por favor, crie uma conta primeiro.")

            case "5":
                if conta:
                    conta.exibir_extrato()
                else:
                    print("Por favor, crie uma conta primeiro.")

            case "6":
                if cliente:
                    banco.visualizar_historico(cliente)
                else:
                    print("Por favor, cadastre um cliente primeiro.")

            case "7":
                print("Saindo do sistema...")
                break

            case _:
                print("Opção inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()
