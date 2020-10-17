#!/usr/bin/python3

# usuarios = ['Renato', 'Marcelo', 'Jonas', 'Asdrubal', 'Bruno', 'Ricardo',
#             'Paloma', 'Paulo', 'Leo']

# usuarios_bloqueados = []

# try:
#     nome = input("entre com seu usuario: ")
#     # for usuario in range(len(usuarios)):
#     if nome in usuarios:
#         if nome == 'Paloma' :
#             usuarios_bloqueados.append('Paloma')
#             print('acesso bloqueado ao usuario')
#         elif nome == 'Leo':
#             usuarios_bloqueados.append('Leo')
#             print('acesso bloqueado ao usuario')
#         elif nome == 'Paulo':
#             usuarios_bloqueados.append('Paulo')
#             print('acesso bloqueado ao usuario')
#         else:
#             print('Acesso liberado')
#     else:
#         raise NameError("acesso bloqueado ao usuario")  
# except NameError as err:
#     print("usuario não encontrado :" + nome)


#!/usr/bin/python3

usuarios = ['renato', 'caio', 'camila',
            'paloma', 'patricia', 'paulo',
            'joao', 'sebastião', 'leo']

usuarios_bloqueados = []


def adiciona_usuario(user):
    global usuarios
    return usuarios.append(user)


def bloqueia_usuario(user):
    if user in usuarios:
        global usuarios_bloqueados
        usuarios_bloqueados.append(user)
    else:
        print('usuario não encontrado')


def remove_usuario(user):
    global usuarios
    return usuarios.remove(user)


def desbloqueia_usuario(user):
    global usuarios_bloqueados
    if user in usuarios_bloqueados:
        usuarios_bloqueados.append(user)
    else:
        print('usuario não encontrado')


tentativas = 3

while tentativas > 0:
    try:
        login = input('Login: ')
        if login.lower() in usuarios_bloqueados:
            raise NameError('Usuario bloquado, contante o RH')
            # break
        elif login.lower() in usuarios:
            print('Acesso permitido!')
            # break
        else:
            tentativas -= 1 
            raise ValueError('Usuario nao encontrado.')
            # continue
    except NameError as nerr:
        print(nerr)
    except ValueError as verr:
        print(verr)
