import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba

# Carregar dados geoespaciais do Brasil
brasil = gpd.read_file("BR_UF_2021.zip", compression="zip", encoding="utf-8")

# Carregar dados da tabela de escolaridade
df_mapa = pd.read_csv("tabela_escolaridade.csv")
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
graf_mapa.set_title("Nível de Escolaridade por Estado", fontdict={"fontsize": "15", "fontname": "Arial"})

# Rótulos nos eixos
graf_mapa.set_xlabel("Latitude", fontdict={"fontsize": "12", "fontname": "Arial"})
graf_mapa.set_ylabel("Longitude", fontdict={"fontsize": "12", "fontname": "Arial"})

# Cores dos paineis
graf_mapa.set_facecolor("#8CBCDB")
janela.set_facecolor("gray")

# Demarcação do gráfico (linhas de latitude e longitude)
graf_mapa.set_xticks([-70, -60, -50, -40, -30])
graf_mapa.set_yticks([-30, -20, -10, 0])

plt.show()