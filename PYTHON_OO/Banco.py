#!/usr/bin/python3
class Conta:
    def __init__(self, titular, conta):
        self.titular = titular
        self.conta = conta
        self.agencia = "08"
        self.saldo = 0.0
        self.banco = "999"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Saldo disponivel apos o deposito de $ {valor}: ${self.saldo} ")

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print(f"Saldo disponivel apos o saque de $ {valor}: ${self.saldo} ")
        else:
            print('Saldo insuficiente')


    def extrato(self):
        print(f"Banco: {self.banco}")
        print(f"Agência: {self.agencia}")
        print(f"Nome do Cliente: {self.titular}")
        print(f"Saldo disponível: {self.saldo}")


def oldbank(cliente):
    print('OldBank')
    print('Bem vindo(a)!')
    print('Selecione uma opção abaixo: ')
    print('Para extrato, digite 1')
    print('Para saque digite 2')
    print('Para deposito, digite 3')

    escolha = int(input(">> "))

    if escolha == 1:
        cliente.extrato()
    elif escolha == 2:
        valor = float(input("Informe o valor do saque: $"))
        cliente.sacar(valor)
    elif escolha == 3:
        valor = float(input("Informe o valor do deposito: $"))
        cliente.depositar(valor)
    else:
        print("opção inválida")
        oldbank(cliente)

marcelo = Conta('Marcelo','12345')
marcelo.depositar(10000)

oldbank(marcelo)
