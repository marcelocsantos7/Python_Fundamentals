#!/usr/bin/python3

class Personagem:
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.xp = 0
        self.nivel = 1
        self.esquiva = 0
    
    def subirNivel(self):
        if self.xp > (20 * self.nivel):
            self.nivel +=1
            print("Level Up!!!")
        
class Mago(Personagem):
    def __init__(self):
        super().__init__()
        self.atq = 30
        self.arma = 'cajado'
        self.msq_atq = 'Magia das Trevas!!!'
        self.poderEspecial = 3

    def recuperacaoMana(self):
        if self.poderEspecial > 0:
            if self.mp >= 70:
                self.mp = 100
                self.poderEspecial -= 1
                print(f'Mana recuperada: {self.mp}')
            else:
                self.mp += 30
                self.poderEspecial -= 1
        else:        
            print('Sem cargas')

    def recuperacaoVida(self):
        if self.poderEspecial > 0:
            if self.mp >= 70:
                self.mp = 100
                self.poderEspecial -= 1
                print(f'Vida recuperada: {self.hp}')
            else:
                self.hp += 30
                self.poderEspecial -= 1
        else:        
            print('Sem cargas')


class Guerreiro(Personagem):
    def __init__(self):
        super().__init__()
        self.atq = 50
        self.arma = 'espada'
        self.msq_atq = 'Arrrrrrrrrrghhhhhhhhh!!!'
        self.poderEspecial = 3

    def furia(self):
        if self.poderEspecial > 0:
            self.atq += 15
            print("Ataque aumentado: {self.atq}")
        else:        
            print('Sem cargas')
