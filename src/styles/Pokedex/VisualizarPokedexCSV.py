from tabulate import tabulate
import pandas as pd

try:
    df = pd.read_csv("pokedex.csv")
    print("Pokedex lida com sucesso!!!")
    print(tabulate(df.head(49), headers="keys", tablefmt="fancy_grid"))
except:
    print("Erro ao ler CSV")