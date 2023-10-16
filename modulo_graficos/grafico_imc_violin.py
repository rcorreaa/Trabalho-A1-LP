"""
Módulo da visualização do Gráfico de Violino feito pelo integrante Anderson. 
"""

import pandas as pd
import matplotlib.pyplot as plt
import doctest

if __name__=="__main__":
    from utilitarios.utils import limpa_PESO, limpa_ALTURA, limpa_SEXO, limpa_ANO_NASCIMENTO
else:
    from modulo_graficos.utilitarios.utils import limpa_PESO, limpa_ALTURA, limpa_SEXO, limpa_ANO_NASCIMENTO

#import os
#root_path = os.path.dirname(__file__)
#os.chdir(root_path)

def plot_grafico_violin(path_data, ini_ano=2013, fim_ano=2022):
    """
    Plota o grafico de violino do imc entre os anos ini_ano e fim_ano.

    Parameters:
        path_data(string): diretorio dos arquivos dos arquivos .csv
        ini_ano(int): ano de inicio. 2013 por padrão
        fim_ano(int): ano do final. 2022 por padrão

    Returns:
        None

    Exemplo:
    Exemplo válido, em que os caminhos dos arquivos são passados da maneira correta e contém os dataframes desejados.
    >>> plot_grafico_violin("data/", 2018, 2022)

    Exemplo Inválido, em que a função tenta buscar o ano de 2013 no path_data, porém ele é inexistente
    nesse diretório
    >>> plot_grafico_violin(path_data="Trabalho_A1_LP.pasta_errada", ini_ano=2013, fim_ano=2022)
    Erro de leitura no database do ano 2013
    """

    lista_df = []

    for ano in range(ini_ano, fim_ano + 1):
        # Leitura do database com tratamento de erro
        try:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano),
                             usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"])
        except UnicodeDecodeError:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano),
                             usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"], encoding="latin1")
        except:
            print("Erro de leitura no database do ano", ano)
            return

        # Limpeza de valores nulos e filtro no publico alvo
        df = limpa_PESO(df)
        df = limpa_ALTURA(df)
        df = limpa_SEXO(df)
        df = limpa_ANO_NASCIMENTO(df, ano)

        # Calculo do imc com base na culuna PESO e ALTURA
        df["IMC"] = df["PESO"] / ((df["ALTURA"] / 100) ** 2)
        df = df["IMC"]

        # Adicionado a serie filtrada em um array
        lista_df.append(df)

    # Define o estilo
    plt.style.use("seaborn-v0_8-notebook")

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

    # Plot violin
    axs[0].violinplot(lista_df, showmedians=True)

    # Plot boxplot
    axs[1].boxplot(lista_df, sym="")

    # Personalizacao do plot
    axs[0].set_title("Violin plot do IMC por ano", fontdict={"fontsize": "15", "fontname": "Arial", "fontweight": "bold"})
    axs[1].set_title("Boxplot do IMC por ano", fontdict={"fontsize": "15", "fontname": "Arial", "fontweight": "bold"})

    for ax in axs:
        ax.yaxis.grid(True)

        ax.set_xticks([y + 1 for y in range(len(lista_df))], labels=[ano for ano in range(ini_ano, fim_ano + 1)])

        ax.set_xlabel("Ano", fontdict={"fontsize": "12", "fontname": "Arial"})
        ax.set_ylabel("IMC", fontdict={"fontsize": "12", "fontname": "Arial"})

    plt.savefig("visualizacoes/violin_imc.png", format="png")
    #plt.show()
    return None

if __name__ == "__main__":
    doctest.testmod()

#plot_grafico_violin("data/", 2018, 2022)
