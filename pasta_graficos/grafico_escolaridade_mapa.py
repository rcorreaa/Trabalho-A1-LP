import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
import doctest

# Insira o caminho da 'tabela_escolaridade.csv' e 'BR_UF_2021.zip' presentes na 'pasta_dados'
def plot_grafico_mapa(path_data, path_geografia):
    """
    Plota o gráfico de mapa do nível de escolaridade por estado.

    Parameters:
        path_data(string): diretório dos arquivos .csv
        path_geografia(string): diretório do arquivo .zip dos dados geográficos do Brasil
    
    Returns:
        None

    Exemplos:
    Exemplo válido, em que os caminhos dos arquivos são passados da maneira correta
    >>> plot_grafico_mapa(path_data="../pasta_dados/tabela_escolaridade.csv", path_geografia="../pasta_dados/BR_UF_2021.zip")

    Exemplo inválido, em que o caminho do Dataframe não contém o arquivo desejado
    >>> plot_grafico_mapa(path_data="caminho_dataframes_errado", path_geografia="../pasta_dados/BR_UF_2021.zip")
    O Diretório caminho_dataframes_errado não contém os arquivos de DataFrames necessários.

    Exemplo inválido, em que o caminho passado não contém o zip dos dados geográficos
    >>> plot_grafico_mapa(path_data="../pasta_dados/tabela_escolaridade.csv", path_geografia="caminho_brasil_errado")
    Caminho do arquivo dos dados geoespaciais do Brasil inválido.
    """
    try:
        # Carregar dados geoespaciais do Brasil
        brasil = gpd.read_file(path_geografia, compression="zip", encoding="utf-8")
    except:
        print("Caminho do arquivo dos dados geoespaciais do Brasil inválido.")
        return None
    try:
        # Carregar dados da tabela de escolaridade
        df_mapa = pd.read_csv(path_data)
    except:
        print(f"O Diretório {path_data} não contém os arquivos de DataFrames necessários.")
        return None

    df_mapa = df_mapa.rename(columns={"UF_RESIDENCIA": "SIGLA"})

    # Reoordenando o DataFrame de acordo com o nível de escolaridade
    df_mapa = df_mapa.sort_values(by="NIVEL_ESCOLARIDADE")

    # Normalização dos valores do nível de escolaridade
    df_mapa["NIVEL_ESCOLARIDADE"] = df_mapa["NIVEL_ESCOLARIDADE"] / 100

    # Criação de tabela de cor gradiente dos níveis de escolaridade
    df_mapa["COR_GRADIENTE"] = [to_rgba(plt.cm.Reds(value)) for value in df_mapa["NIVEL_ESCOLARIDADE"]]
    df_mapa = df_mapa.set_index("SIGLA").reindex(brasil["SIGLA"]).reset_index()

    # Personalização do mapa
    janela, graf_mapa = plt.subplots(1, 1, figsize=(10, 10))
    brasil.plot(ax=graf_mapa, color=df_mapa["COR_GRADIENTE"], edgecolor="black", linewidth=0.7)
    graf_mapa.set_title("Nível de Escolaridade por Estado", fontdict={"fontsize": "15", "fontname": "Arial","fontweight": "bold"})

    # Rótulos nos eixos
    graf_mapa.set_xlabel("Latitude", fontdict={"fontsize": "12", "fontname": "Arial"})
    graf_mapa.set_ylabel("Longitude", fontdict={"fontsize": "12", "fontname": "Arial"})

    # Cores dos paineis
    graf_mapa.set_facecolor("#8CBCDB")
    janela.set_facecolor("white")

    # Demarcação do gráfico (linhas de latitude e longitude)
    graf_mapa.set_xticks([-70, -60, -50, -40, -30])
    graf_mapa.set_yticks([-30, -20, -10, 0])

    plt.show()
    return None

if __name__ == "__main__":
    doctest.testmod()

#plot_grafico_mapa(path_data="../pasta_dados/tabela_escolaridade.csv", path_geografia="../pasta_dados/BR_UF_2021.zip")