import pandas as pd
from tabulate import tabulate

inst_df = pd.DataFrame([])
inst_df['Mnemonico'] = ["JP", "JZ", "LV", "+", "-", "*", "/",
                        "LD", "MM", "SC", "OS", "IO", "RS", "GD", "PD"]
inst_df['Codigo'] = ["01", "02", "03", "04", "05", "06", "07", "08", "09",
                     "0A", "0B", "0C", "0D", "0E", "0F"]

inst_df.to_csv('instrucoes.csv', index=False)

print "Tabela de instrucoes"
print(tabulate(inst_df, headers='keys', tablefmt='psql'))
