"""
Módulo da visualização do Gráfico de Histograma feito pelo integrante Ramyro. 
"""

import matplotlib.pyplot as plt
import pandas as pd
from utilitarios.utils  import limpa_PESO, limpa_ALTURA, limpa_ANO_NASCIMENTO, limpa_SEXO
import doctest

import os
root_path = os.path.dirname(__file__)
os.chdir(root_path)

def plot_grafico_histograma(path_data, ini_ano=2018, fim_ano=2022):
    """
    Plota o histograma com as densidades dos IMCs entre os anos "ini_ano" e "fim_ano".

    Parameters:
        path_data(string): diretório dos arquivos dos arquivos .csv
        ini_ano(int): ano inicial a ser analisado. 2018 por padrão
        fim_ano(int): ano final a ser analisado. 2022 por padrão
        
    Returns:
        None
    
    Exemplos:
    Exemplo válido, em que os caminhos dos arquivos são passados da maneira correta e contém os dataframes desejados.
    >>> plot_grafico_histograma("../data/", 2018, 2022)
    
    Exemplo inválido, em que o caminho do Dataframe não contém os dataframes desejados.
    >>> plot_grafico_histograma("caminho_errado/", 2018, 2022)
    Erro de leitura no database do ano 2018
    
    """
    anos = [ano for ano in range(ini_ano, fim_ano+1)]
    cores = ["black", "green", "yellow", "red", "pink"]

    for i, ano in enumerate(anos):
        
        # Leitura com tratamento de erro
        try:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"])
        except UnicodeDecodeError:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"], encoding="latin1")
        except:
            print("Erro de leitura no database do ano", ano)
            return
        
        # Limpeza dos valores nulos e filtro no público a ser analisado
        df = limpa_SEXO(df)
        df = limpa_PESO(df)
        df = limpa_ALTURA(df)
        df = limpa_ANO_NASCIMENTO(df, ano)
        
        # Criação da coluna IMC com base na coluna PESO e ALTURA
        df["IMC"] = 10000 * df["PESO"] / df["ALTURA"] ** 2
        
        # Plota o histograma de densidade com os parâmetros desejados
        plt.hist(df["IMC"], bins=50, density=True, histtype="step", alpha=0.6, color=cores[i], label=str(ano))

    # Personaliza o plot
    plt.subplot().set_facecolor("#373737")
    plt.xlim(0, 50)
    plt.xlabel("IMC", fontdict={"fontsize": "12", "fontname": "Arial"})
    plt.ylabel("Densidade", fontdict={"fontsize": "12", "fontname": "Arial"})
    plt.title("Distribuição do IMC ao longo dos anos", fontdict = {"fontsize": "15", "fontname": "Arial", "fontweight": "bold"})
    plt.grid(True, color="black")
    
    # Personaliza a legenda
    legenda_personalizada = [plt.Line2D([0], [0], color=cores[i], lw=2, label=str(ano)) for i, ano in enumerate(anos)]
    plt.legend(handles=legenda_personalizada)
    
    # Exibe o gráfico
    plt.savefig("../visualizacoes/histograma_imc.png", format="png")
    #plt.show()
    return None

if __name__ == "__main__":
    doctest.testmod()

#plot_grafico_histograma("../data/", 2018, 2022)
