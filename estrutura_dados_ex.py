#!/usr/bin/python3

estados = {
    'estados': {
        'sp': {
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 4404
        },
        'rj': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }
}

# code_estados = ['sp', 'rj', 'mg']
for i in estados['estados'].keys():
    print(f'Estado: {estados["estados"][i]["nome"]}')
    print(f'Municipios: {estados["estados"][i]["municipios"]}')
    print(f'Populacao: {estados["estados"][i]["populacao"]}')
    print("-----------")

print(f"Populacao do rio: {estados['estados']['rj']['populacao']}")

print(f"Estado: {estados['estados']['mg']['nome']}")