# vph- Valor por Hora
# ht- Hora Trabalhada
class Salario:

    def __init__(self, vph: float, ht: float):
        self.vph = vph
        self.ht = ht
        self.sab = self.vph * self.ht
        self.fgt = 0
        self.sindicat = 0
        self.ir = 0
        self.dt = 0

    def imr(self):

        if self.sab <= 1900:
            self.ir = 0
            print('Sem desconto de IR')
            return self.ir

        elif self.sab <= 2800:
            self.ir = self.sab * (7 / 100)
            print(f'(-) IR (7%):{self.ir:.2f}')
            return self.ir
        elif self.sab <= 3700:
            self.ir = self.sab * (15 / 100)
            print(f'(-) IR (15%):{self.ir:.2f}')
            return self.ir
        elif self.sab <= 4600:
            self.ir = self.sab * (22 / 100)
            print(f'(-) IR (22%):{self.ir:.2f}')
            return self.ir
        else:
            self.ir = self.sab * (27 / 100)
            print(f'(-) IR (27%):{self.ir:.2f}')
            return self.ir

    def sindicato(self):
        self.sindicat = self.sab * (3 / 100)
        return self.sindicat

    def fgts(self):
        self.fgt = self.sab * (11 / 100)
        return self.fgt

    def dct(self):
        self.dt = self.ir + self.sindicat
        return self.dt

    def sl(self):
        sl = self.sab - self.dt
        return sl


vph = float(input('Qual seu valor por hora de trabalho: '))
ht = float(input('Quantas horas você trabalhou nesse mês: '))
sb = vph * ht
Sal1 = Salario(vph, ht)

print(f'Valor da hora: R${vph}')
print(f'Horas Trabalhadas: {ht}')
print(f'Salário Bruto R${Sal1.sab:.2f}')
Sal1.imr()
print(f'(-)Sindicato 3%: {Sal1.sindicato():.2f}')
print(f'FGTS (11%): {Sal1.fgts():.2f}')
print(f'Total de Descontos: R${Sal1.dct():.2f}')
print(f'Salário Liquido: R${Sal1.sl():.2f}')
