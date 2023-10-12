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











