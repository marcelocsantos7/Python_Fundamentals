#!/usr/bin/python3
# class Pai:

#     def __init__(self):
#         self.nome = 'Paulo'
#         self.sobrenome = 'Cardoso'
#         self.profissao = 'Programador PHP'

    
#     def programar(self):
#         print('Estou sofrendo com PHP')

# class Filho(Pai):
#     def __init__(self):
#         super().__init__()
#         #Pai().__init__()
#         self.nome = 'Eduardo'
#         self.profissao = 'Programador Python'


# f1 = Filho()
# print(f1.nome)
# print(f1.programar())


class Automovel:
    def __init__(self):
        self.motor = True
        self.combustivel = True

    def acelerar(self):
        print("Acelerando...")

class Carro(Automovel):
    def __init__(self):
        super().__init__()

class Barco(Automovel):
    def __init__(self):
        super().__init__()

class Aviao(Automovel):
    def __init__(self):
        super().__init__()