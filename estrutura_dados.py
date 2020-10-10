#!/usr/bin/python3
# isso é um comentario

"""
isso é uma docstring - serve pra documentacao do codigo

"""

# string = 'Eu sou uma string'
# inteiro = 10 
# flutuante = 10.0
# booleanos = True # ou False
# lista = [1,2, '', True, inteiro, flutuante, ['casa', 'batata']]
# tupla = (1,2, 'String')
# dicionario = {'chave': 'valor', 'nome':'marcelo', 'idade' : 27}

# entrada e saida de dados

# saida de dados
# animal = 'leão'
# print(animal)

# nome = input('Digite seu nome: ')
# sobrenome = input('Digite seu sobrenome: ')

# print(f'Prazer em conhecer {nome} {sobrenome}')
# print('Prazer em conhecer', nome, sobrenome, sep=" ", end="\n")
# print('Prazer em conhecer {} {}'.format(nome, sobrenome))

# str()
# int()
# float()
# bool()
# list()
# tuple()
# dict()

# numero1 = int(input('Digite um numero: '))
# numero2 = int(input('Digite outro numero: '))

# soma = numero1 + numero2

# print(f'Resultado : {soma}')

# texto = 'Python é a linguagem mais quente do momento'
# print(type(texto))
# print(texto.upper())
# print(texto.lower())
# print(texto.split(' ')) # divide a string

# print(texto.startswith('P')) #procura uma ocorrencia no comeco
# print(texto.endswith('m')) #procura uma ocorrencia no fim

# print('antes do strip')
# print(texto.strip())
# print('depois do strip')

# print(texto.replace('e', 'E'))

print("********************************************************")

#Listas, Tuplas e Dicionarios

# frutas =['abacaxi', 'banana', 'uva']

# print(frutas[0])
# print(frutas[-1])

# frutas.append('acerola') # insere o item a ultima posicao
# print(frutas)
# frutas.insert(2, 'Pera')# adiciona a poiscao do indice
# frutas.remove('acerola')# remove o item do da seleção
# frutas.pop(3)# remove o item da posicao

# print(frutas.count('abacaxi'))
# print(frutas)

# frutas_definitivas = ('uva', 'maçã')
# frutas_definitivas = ('uva', 'maçã', 'abacaxi')

# lista_n = [1,2,3,[4,5,6,[7,8,9]]]

# print(lista_n[3][3][1])

dados = {'Funcionario1': {'Nome': 'Rafael', 'Sobrenome': 'Castro', 'Idade': 35, 'Projetos': {
    'Projeto n1':{
        'Nome': 'n1',
        'Status': 'Concluído'
    },
    'Projeto n2': {
        'Nome': 'n2',
        'Status': 'Em desenvolvimento'
    }}
},'Funcionario2': {'Nome': 'Carlos', 'Sobrenome': 'Medeiros', 'Idade': 25, 'Projetos': {
    'Projeto n3':{
        'Nome': 'n3',
        'Status': 'Concluído'
    },
    'Projeto n4': {
        'Nome': 'n4',
        'Status': 'Em desenvolvimento'
    }}
}}

print(dados.keys()) # retorna as chave
print(dados.values()) #retorna o valor do campo
print(dados.items) #retorna chave e valor
