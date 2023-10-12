import pandas as pd

df_2022 = pd.read_csv("sermil2022.csv", encoding = "latin1")
df_2021 = pd.read_csv("sermil2021.csv", encoding = "latin1")

def cria_novo_df(df, ano):
    media_peso_uf = df.groupby("UF_JSM")["PESO"].mean()
    mediana_peso_uf = df.groupby("UF_JSM")["PESO"].median()
    moda_peso_uf = df.groupby("UF_JSM")["PESO"].agg(pd.Series.mode)
    media_altura_uf = df.groupby("UF_JSM")["ALTURA"].mean()
    mediana_altura_uf = df.groupby("UF_JSM")["ALTURA"].median()
    moda_altura_uf = df.groupby("UF_JSM")["ALTURA"].agg(pd.Series.mode)
    df_novo = pd.DataFrame({"ANO": ano, "UF": media_peso_uf.index, "PESO_MEDIA": media_peso_uf, 
                            "PESO_MEDIANA": mediana_peso_uf, "PESO_MODA": moda_peso_uf, 
                             "ALTURA_MEDIA": media_altura_uf, "ALTURA_MEDIANA": mediana_altura_uf, 
                             "ALTURA_MODA": moda_altura_uf})
    
    linha_geral = pd.DataFrame({"UF": ["Brasil"], "ANO": [ano], "PESO_MEDIA": [df["PESO"].mean()], 
                                "PESO_MEDIANA": [df["PESO"].median()], "PESO_MODA": [df['PESO'].mode().values[0]], 
                                "ALTURA_MEDIA": [df["ALTURA"].mean()], "ALTURA_MEDIANA": [df["ALTURA"].median()], 
                                "ALTURA_MODA": [df["ALTURA"].mode().values[0]]})
    
    df_geral = pd.concat([df_novo, linha_geral], ignore_index=True)
    df_pronto = df_geral.set_index("UF")
    return df_pronto

print(cria_novo_df(df_2021, 2021))
print(cria_novo_df(df_2022, 2022))







