import pandas as pd
from tabulate import tabulate

df = pd.DataFrame([])
df['00'] = ["03"]
df['01'] = ["A0"]
df['02'] = ["09"]
df['03'] = ["FF"]
df['04'] = ["03"]
df['05'] = ["01"]
df['06'] = ["04"]
df['07'] = ["FF"]

print(tabulate(df, headers='keys', tablefmt='psql'))
