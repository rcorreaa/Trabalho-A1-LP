import pandas as pd
import matplotlib.pyplot as plt
from concatena_tabelas import concatena_dataframes
from funcoes_limpeza import exclui_colunas

df_2022 = pd.read_csv("sermil2022.csv", encoding = "latin1")
df_2021 = pd.read_csv("sermil2021.csv", encoding = "latin1")
df_2020 = pd.read_csv("sermil2020.csv", encoding = "latin1")
df_2019 = pd.read_csv("sermil2019.csv", encoding = "latin1")
df_2018 = pd.read_csv("sermil2018.csv", encoding = "latin1")

df_2022_limpo = exclui_colunas(df_2022)
df_2021_limpo = exclui_colunas(df_2021)
df_2020_limpo = exclui_colunas(df_2020)
df_2019_limpo = exclui_colunas(df_2019)
df_2018_limpo = exclui_colunas(df_2018)

# Filtrando os DataFrames por colunas desejadas
df_2022_limpo = df_2022_limpo[["UF_JSM", "DISPENSA"]]
df_2021_limpo = df_2021_limpo[["UF_JSM", "DISPENSA"]]
df_2020_limpo = df_2020_limpo[["UF_JSM", "DISPENSA"]]
df_2019_limpo = df_2019_limpo[["UF_JSM", "DISPENSA"]]
df_2018_limpo = df_2018_limpo[["UF_JSM", "DISPENSA"]]

df_completo = concatena_dataframes(df_2022_limpo, df_2021_limpo, df_2020_limpo, df_2019_limpo, df_2018_limpo)

mapeamento_regioes = {
    'AC': 'Norte',
    'AL': 'Nordeste',
    'AM': 'Norte',
    'AP': 'Norte',
    'BA': 'Nordeste',
    'CE': 'Nordeste',
    'DF': 'Centro-Oeste',
    'ES': 'Sudeste',
    'GO': 'Centro-Oeste',
    'MA': 'Nordeste',
    'MG': 'Sudeste',
    'MS': 'Centro-Oeste',
    'MT': 'Centro-Oeste',
    'PA': 'Norte',
    'PB': 'Nordeste',
    'PE': 'Nordeste',
    'PI': 'Nordeste',
    'PR': 'Sul',
    'RJ': 'Sudeste',
    'RN': 'Nordeste',
    'RO': 'Norte',
    'RR': 'Norte',
    'RS': 'Sul',
    'SC': 'Sul',
    'SE': 'Nordeste',
    'SP': 'Sudeste',
    'TO': 'Norte'
}

def cria_regiao(df):
    df["REGIAO"] = df["UF_JSM"].map(mapeamento_regioes)
    return df

def agrupa_por_regiao(df, coluna):
    novo_df = df.groupby("REGIAO")[coluna].value_counts().reset_index()
    return novo_df

df_com_regiao = cria_regiao(df_completo)
df_agrupado = agrupa_por_regiao(df_com_regiao, "DISPENSA")

# Reorganiza os dados para criar um único DataFrame com "Com dispensa" e "Sem dispensa"
df_organizado = df_agrupado.pivot(index='REGIAO', columns='DISPENSA', values='count')

# Define cores para as barras
cores = ["#A50030", "#1A3071"]

# Cria um gráfico de barras com o matplotlib
plt.figure(figsize=(10, 6))
bar_width = 0.35  # Largura das barras

# Adicione linhas de grade
plt.grid(True, axis='y', linestyle='--', color='gray', zorder=0)

# Posições para as barras
posicao = range(len(df_organizado.index))

# Barra para "Com dispensa"
plt.bar(posicao, df_organizado["Com dispensa"], width=bar_width, 
        label="Com dispensa", color=cores[0], edgecolor="black")

# Barra para "Sem dispensa"
plt.bar([i + bar_width for i in posicao], df_organizado["Sem dispensa"], 
        width=bar_width, label="Sem dispensa", color=cores[1], edgecolor="black")

plt.ylabel("Contagem")
plt.title('Contagem de "Com dispensa" e "Sem dispensa" por Região')
plt.xticks([i + bar_width / 2 for i in posicao], df_organizado.index)
plt.legend()
plt.tight_layout()

plt.show()







