import pandas as pd
from tabulate import tabulate

df = pd.DataFrame([]) #cria tabela
df['usuarios'] = ['isabela', 'eric']
df.to_csv('usuarios.csv', index=False)
