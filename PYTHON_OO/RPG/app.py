#!/usr/bin/python3
import os
from time import sleep
import modules.personagem as personagem
import modules.monstro as monstro
from random import randint

if __name__ == "__main__":
    clear = os.system('clear')

    def selecionarPersonagem():
        while True:
            print("selecione o Personagem: ")
            print("1 - Mago")
            print("2 - Guerreiro ")
            print("0 - Sair ")
            try:
                opcao = int(input('Opção: '))
                if opcao == 1:
                    persona = personagem.Mago()
                    clear
                elif opcao == 2:
                    persona = personagem.Guerreiro()
                    clear
                elif opcao == 0:
                    exit()
                    clear
                else:
                    raise TypeError('Opção inválida')
            except TypeError as terr:
                clear
                print(terr)
                sleep(2)
                clear
                continue
            selecionarMonstro(personagem)

    def selecionarMonstro(personagem):
        while True:
            print("Selecione o monstro: ")
            print("1 - Orc")
            print("2 - Dementador ")
            print("0 - Sair ")
            try:
                opcao = int(input('Opção: '))
                if opcao == 1:
                    monster = monstro.Orc()
                    clear
                elif opcao == 2:
                    monster = monstro.Dementador()
                    clear
                elif opcao == 0:
                    exit()
                    clear
                else:
                    raise TypeError('Opção inválida')
            except TypeError as terr:
                clear
                print(terr)
                sleep(2)
                clear
                continue
            principal(personagem, monstro)


    def principal(pers, monst):
        dano_personagem = randint(1,50)
        dano_monstro = randint(1, 60)

        if dano_monstro < dano_personagem:
            monstro.hp -= dano_personagem
            print(f"Monstro tomou dano \nHP {monstro.hp}\nDano: {dano_personagem}")
            
            if monstro.hp <= 0:
                os.system('clear')
                print("Fim de Jogo\nVocê Ganhou")
                sleep(2)
                selecionarPersonagem()
        else:
            personagem.hp -= dano_monstro
            print(f"Você tomou dano  \nHP: {personagem.hp}\nDano: {dano_monstro}")
            if personagem.hp <= 0:
                os.system('clear')
                print('Você perdeu!')
                sleep(2)
                selecionarPersonagem()


selecionarPersonagem()
