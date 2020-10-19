parte 1 exercicio oldbank

import random
import datetime



class Banco:


    def __init__(self, conta, cliente):
        self.nbanco = '999'
        self.conta = conta
        self.agencia = '08'
        self.cliente = cliente
        self.sald = random.randint(0, 5000) + random.random()

    def depositar(self):
        x = float(input('\033[1mValor a ser depositado: R$\033[m'))
        self.sald += x
        print(f'\033[1mNovo saldo: {self.sald:.2f}\033[m')
    def sacar(self):
        y = float(input('\033[1mValor a ser sacado: R$\033[m'))
        if y <= self.sald:
            self.sald -= y
            print(f'\033[1mSeu novo saldo é de: {self.sald:.2f}\033[m')
        else:
            print('\033[1mSaldo insuficiente\033[m')
    def extrato(self):
        print(f'\033[1mNúmero do Banco: {self.nbanco}')
        print(f'Número da Agência: {self.agencia}')
        print(f'Cliente: {self.cliente}')
        print(f'Seu saldo atual: {self.sald:.2f}')
        print(f'Data {datetime.date.today()}\033[m')

parte 2 exercicio oldbank

from banco import Banco




print(f'{"OldBank":^25}')
print('='*25)
x = str(input('Digite o Número da Conta: '))
y = str(input('Nome do Cliente: '))
print(f'{"Bem vindo(a)!":^25}')
print(f'O que deseja fazer hoje {y}?')

cliente1 = Banco(x,y)

while True:
    print('''Para extrato digite 1
Para saque digite 2
Para deposito digite 3
Para sair digite 000''')
    print('='*25)
    x = int(input('Opção desejada: '))
    print('='*25)
    if x == 1:
        cliente1.extrato()
        print('=' * 25)
    elif x == 2:
        cliente1.sacar()
        print('=' * 25)
    elif x == 3:
        cliente1.depositar()
        print('=' * 25)
    elif x == 000:
        print('Tenha um ótimo dia, até mais.')
        break
    else:
        print('Opção inválida, tente novamente.')