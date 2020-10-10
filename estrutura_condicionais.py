#!/usr/bin/python3
# n1 = 1 
# n2 = 2
# if n1 == n2:
#     print('é verdadeiro')
# else:
#     print('é falso')

# idade = int(input('Digite sua idade: '))
# habilitacao = True
# if idade >= 18 and habilitacao:
#     print('Bora beber')
# else:
#     print('Não pode beber')

#Calcule a media de um aluno:

media = 0

for i in range(4):
    n = float(input(f"insira nota {i+1}: "))
    media += n
media = media / 4
print(f"Sua média foi : {media}")

if media > 7:
    print('Aprovado')
elif media > 4 and media <=7:
    print('Recuperação')
else:
    print('Reprovado')

#********************************************
# usuarios = ['marcelo', 'rei', 'bussa']
# tentativas = 2
# while True:
#     login = input('Digite seu login: ')
#     if login in usuarios:
#         print('Acesso Permitido')
#         break
#     elif tentativas == 0:
#         print('Acesso temporariamente bloqueado')
#         break
#     else:
#         print('Acesso Negado')
#         tentativas-= 1
#         continue
#*********************************************

# fruta = ['laranja', 'limao', 'pera']

# for num, item in enumerate(fruta):
#     print(f'N: {num}\n Item: {item}')