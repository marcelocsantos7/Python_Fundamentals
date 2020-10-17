#!/usr/bin/python3
# produto1 = {"nome" :"Tenis", "valor":150}
# produto2 = {"nome" :"Camiseta", "valor":50}
# produto3 = {"nome" :"Camisa", "valor":80}
# produto4 = {"nome" :"Calça", "valor":100}

# carrinho = []

# def adicionaProduto(produto):
#     global carrinho
#     carrinho.append(produto)


# def totalCarrinho(produto):
#     return sum(produto['valor'] for produto in carrinho)


# def cupomDesconto(cupom=""):
#     if cupom == "xyzgratis":
#         return 0.50
#     else:
#         return 1

# adicionaProduto(produto1)
# adicionaProduto(produto2)
# adicionaProduto(produto4)

# print(f"O total de sua compra é : {totalCarrinho(carrinho)*cupomDesconto()}")
# print(f"O total de sua compra com cupom é : {totalCarrinho(carrinho)*cupomDesconto('xyzgratis')}")


#-----------------------------------------------------------------#

# args = tupla
# kwargs = dicionario


# def alterarServidor(*servidores):
#     print('O IP atual é ' , servidores[0])
#     print('O novo IP é ' , servidores[0])
    

# alterarServidor('192.0.0.1', '192.4.5.6', '8.8.8.8')

# def descobreDicionario(**dicionario):
#     print(dicionario)
#     for k in dicionario.keys():
#         print(f'chave: {k}')
#         print(f'Tem o valor: {dicionario[k]}')

# descobreDicionario(servidor = 'frodo', ip='192.168.15.100', dominio = '4linux.com.br')


#-----------------------------------------------------------------#

# var = lambda x, y: x+y
# print(var(1,2))

# produto1 = {"nome" :"Tenis", "valor":150.0}
# produto2 = {"nome" :"Camiseta", "valor":50.0}
# produto3 = {"nome" :"Camisa", "valor":80.0}
# produto4 = {"nome" :"Calça", "valor":100.0}

# carrinho = []

# black_friday = lambda x: x / 2
# carrinho.append(produto1)
# carrinho.append(produto2)
# carrinho.append(produto3)
# carrinho.append(produto4)

# for c in carrinho:
#     print(f'Nome do produto : {c["nome"]}')
#     print(f'Valor original : {c["valor"]}')
#     print(f'Valor com desconto : {black_friday(c["valor"])}')
#     print('-'*70)

#-----------------------------------------------------------------#

# numeros = [2,3,4,5,6,7,8,9]
# #lambda utilizada com map
# dobro = list(map(lambda item: item * 2, numeros))

# print(dobro)

#-----------------------------------------------------------------#

# import json
# from functools import reduce

# numeros = [2,3,4,5,6,7,8,9]
# soma = reduce((lambda x, y: x + y), numeros)

# print(soma)

#-----------------------------------------------------------------#

# numeros = [2,3,4,5,6,7,8,9]

# pares = list(filter(lambda x: x%2 == 0, numeros))

# print(pares)

#-----------------------------------------------------------------#

