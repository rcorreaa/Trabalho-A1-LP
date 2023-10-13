import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funcoes_limpeza import limpa_PESO, limpa_ALTURA, limpa_SEXO, limpa_ANO_NASCIMENTO

v_df = []
ini_ano = 2016
fim_ano = 2022

for ano in range(ini_ano, fim_ano+1):
    try:
        df = pd.read_csv("../lp/data/sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"])
    except UnicodeDecodeError:
        df = pd.read_csv("../lp/data/sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"], encoding="latin1")
    except:
        print("Erro de leitura do database")
        continue

    df = limpa_PESO(df)
    df = limpa_ALTURA(df)
    df = limpa_SEXO(df)
    df = limpa_ANO_NASCIMENTO(df, ano)
    
    df["IMC"] = df["PESO"] / ((df["ALTURA"]/100)**2)
    df = df["IMC"]

    v_df.append(df)
    
    print(ano)
    print(df.describe())
    print()


fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

axs[0].violinplot(v_df, showmedians=True)
axs[1].boxplot(v_df, sym="")

for ax in axs:
    ax.yaxis.grid(True)
    
    ax.set_xticks([y + 1 for y in range(len(v_df))], labels=[ano for ano in range(ini_ano, fim_ano+1)])
    
    ax.set_xlabel('Ano')
    ax.set_ylabel('IMC')

plt.show()