import pandas as pd
from tabulate import tabulate

df = pd.DataFrame([]) #cria tabela
df['usuario'] = ['isabela', 'eric']
df['arquivo'] = ['n*n', 'n*n']
df['path'] = ['\isabelan*n', '\ericn*n']
df.to_csv('arquivos.csv', index=False)
