import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funcoes_limpeza import limpa_PESO, limpa_ALTURA, limpa_SEXO, limpa_ANO_NASCIMENTO

def plot_grafico_violin(path_data, ini_ano=2013, fim_ano=2022):
    """
    Plota o grafico de violino do imc entre os anos ini_ano e fim_ano.

    Parameters:
        path_data(string): diretorio dos arquivos dos arquivos .csv
        ini_ano(int): ano de inicio. 2013 por padrão
        fim_ano(int): ano do final. 2022 por padrão
    
    Returns:
        None
    """
     
    v_df = []

    for ano in range(ini_ano, fim_ano+1):
        #leitura do database com tratamento de erro
        try:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"])
        except UnicodeDecodeError:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"], encoding="latin1")
        except:
            print("Erro de leitura no database do ano", ano)
            return

        #limpeza de valores nulos e filtro no publico alvo
        df = limpa_PESO(df)
        df = limpa_ALTURA(df)
        df = limpa_SEXO(df)
        df = limpa_ANO_NASCIMENTO(df, ano)
        
        #calculo do imc com base na culuna PESO e ALTURA
        df["IMC"] = df["PESO"] / ((df["ALTURA"]/100)**2)
        df = df["IMC"]

        #adicionado a serie filtrada em um array
        v_df.append(df)
        
        #Imprime algumas estatisticas de resumo
        print(ano)
        print(df.describe())
        print()

    #define o estilo
    plt.style.use("seaborn-v0_8-notebook")

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

    #plot violin
    axs[0].violinplot(v_df, showmedians=True)
    
    #plot boxplot
    axs[1].boxplot(v_df, sym="")

    #personalizacao do plot
    axs[0].set_title('Violin plot do IMC por ano')
    axs[1].set_title('Boxplot do IMC por ano')
                     
    for ax in axs:
        ax.yaxis.grid(True)
        
        ax.set_xticks([y + 1 for y in range(len(v_df))], labels=[ano for ano in range(ini_ano, fim_ano+1)])

        ax.set_xlabel('Ano')
        ax.set_ylabel('IMC')

    plt.show()
    return None

plot_grafico_imc_violin("../lp/data/")