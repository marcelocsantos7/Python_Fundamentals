#!/usr/bin/python3

class FolhaPagamento:


    def __init__(self, valorHora, quantidadeHoras):
        self.valorHora = float
        self.quantidadeHoras = float
        # self.salarioBruto = calculaSalarioBruto()
        # self.salarioLiquido = calculaSalarioLiquido()
        # self.contribuicaoSindical = float 0.03
        # self.impostoRenda = float
        # self.fgts = float


    def calculaSalarioBruto(self):
        salBruto = self.valorHora * self.quantidadeHoras
        return salBruto

    def calculaIr(self):
        if(self.calculaSalarioBruto() <= 1900):
            aliquota = 0
        elif(self.calculaSalarioBruto() <= 2800):
            aliquota = 0.07
        elif(self.calculaSalarioBruto() <= 3700):
            aliquota = 0.15
        elif(self.calculaSalarioBruto() <= 4600):
            aliquota = 0.22
        elif(self.calculaSalarioBruto() > 4600):
            aliquota = 0.27

        return self.calculaSalarioBruto() * aliquota


    def calculaSindicato(self):
        return self.calculaSalarioBruto() * 0.03

    
    def calculaSalarioLiquido(self):
        salLiquido = self.calculaSalarioBruto() - (self.calculaIr() + self.calculaSindicato())
        return salLiquido


    def calculaFGTS(self):
        return self.calculaSalarioBruto() * 0.11


    def printFolha(self):
        print(f"Valor da hora: {self.valorHora}")
        print(f"Quantidade de horas trabalhadas: {self.quantidadeHoras}")
        print(f"Salario Bruto: ({self.valorHora} * {self.quantidadeHoras}): {self.calculaSalarioBruto()} ")
        print(f"( - ) IR :")


valorHora = float(input("Valor da Hora: "))
quantidadeHoras = float(input("Quantidade de horas trabalhadas: "))
marcelo = FolhaPagamento(valorHora, quantidadeHoras)
