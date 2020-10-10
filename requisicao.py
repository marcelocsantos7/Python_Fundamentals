import requests

print('Sistema de consultas de CEP')
cep = input('Digite o CEP: ')

url = f'https://viacep.com.br/ws/{cep}/json'

response = requests.get(url)

print(response.status_code)

print(response.json())