import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funcoes_limpeza import limpa_PESO, limpa_ALTURA, limpa_SEXO, limpa_ANO_NASCIMENTO

v_df = []

for ano in range(2017, 2022+1):
    try:
        df = pd.read_csv("../lp/data/sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"])
    except UnicodeDecodeError:
        df = pd.read_csv("../lp/data/sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"], encoding="latin1")
    except:
        print("Erro de leitura do database")
        continue

    df = limpa_PESO(df)
    df = limpa_ALTURA(df)
    df = limpa_ANO_NASCIMENTO(df, ano)
    
    df["IMC"] = df["PESO"] / ((df["ALTURA"]/100)**2)
    df = df["IMC"]

    v_df.append(df)
    
    print(ano)
    print(df.describe())
    print()


fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

axs[1].boxplot(v_df, sym="")

axs[0].violinplot(v_df, showmedians=True)

plt.show()