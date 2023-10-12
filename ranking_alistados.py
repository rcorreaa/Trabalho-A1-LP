import pandas as pd
import matplotlib.pyplot as plt

df_2022 = pd.read_csv("sermil2022.csv", encoding = "latin1")

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

df_com_regiao = cria_regiao(df_2022)
df_agrupado = agrupa_por_regiao(df_com_regiao, "DISPENSA")

# Reorganize os dados para criar um único DataFrame com "Com dispensa" e "Sem dispensa"
df_pivot = df_agrupado.pivot(index='REGIAO', columns='DISPENSA', values='count')

# Crie um gráfico de barras com o matplotlib
plt.figure(figsize=(10, 6))
bar_width = 0.35  # Largura das barras

# Posições para as barras
x = range(len(df_pivot.index))

# Barra para "Com dispensa"
plt.bar(x, df_pivot['Com dispensa'], width=bar_width, label='Com dispensa')

# Barra para "Sem dispensa"
plt.bar([i + bar_width for i in x], df_pivot['Sem dispensa'], width=bar_width, label='Sem dispensa')

plt.xlabel('Região')
plt.ylabel('Contagem')
plt.title('Contagem de "Com dispensa" e "Sem dispensa" por Região')
plt.xticks([i + bar_width / 2 for i in x], df_pivot.index)
plt.legend()
plt.tight_layout()

plt.show()










