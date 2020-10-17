#!/usr/bin/python3
# arquivo = open('arquivo.txt', 'x') # crio o  
# arquivo = open('arquivo.txt', 'w')
# arquivo.write('Novo arquivo')

# arquivo.close()

# with open('arquivo.txt', 'a') as f:
#     print(f.read)

import pandas as pd

df = pd.read_csv('dados.csv', sep=";")
print(df.head())

