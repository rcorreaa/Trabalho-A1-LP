from funcoes_limpeza import *

df_2022 = pd.read_csv("sermil2022.csv")
df_2021 = pd.read_csv("sermil2022.csv")
df_2020 = pd.read_csv("sermil2022.csv")
df_2019 = pd.read_csv("sermil2022.csv")
df_2018 = pd.read_csv("sermil2022.csv")

# Filtrando os DataFrames por colunas desejadas
df_2022 = df_2022[["UF_RESIDENCIA", "ESCOLARIDADE"]]
df_2021 = df_2021[["UF_RESIDENCIA", "ESCOLARIDADE"]]
df_2020 = df_2020[["UF_RESIDENCIA", "ESCOLARIDADE"]]
df_2019 = df_2019[["UF_RESIDENCIA", "ESCOLARIDADE"]]
df_2018 = df_2018[["UF_RESIDENCIA", "ESCOLARIDADE"]]

# Renomeando os registros da coluna ESCOLARIDADE
df_2022 = renomeia_ESCOLARIDADE(df_2022)
df_2021 = renomeia_ESCOLARIDADE(df_2022)
df_2020 = renomeia_ESCOLARIDADE(df_2022)
df_2019 = renomeia_ESCOLARIDADE(df_2022)
df_2018 = renomeia_ESCOLARIDADE(df_2022)

# Adição da da coluna NIVEL DE ESCOLARIDADE nos DATAFRAMES
df_2022 = nivel_escolaridade(df_2022)
df_2021 = nivel_escolaridade(df_2021)
df_2020 = nivel_escolaridade(df_2020)
df_2019 = nivel_escolaridade(df_2019)
df_2018 = nivel_escolaridade(df_2018)

# Junção dos DataFrames verticalmente
df_concatenado = pd.concat([df_2022, df_2021, df_2020, df_2019, df_2018], ignore_index=True)

# Remoção da coluna de escolaridade
df_concatenado.drop("ESCOLARIDADE", axis=1, inplace=True)

# Média de escolaridade por estado
media_escolaridade_estados = df_concatenado.groupby("UF_RESIDENCIA")["NIVEL_ESCOLARIDADE"].mean().reset_index()

# Remoção do estado 'KK' e resetação de índices
media_escolaridade_estados = media_escolaridade_estados.loc[media_escolaridade_estados["UF_RESIDENCIA"] != "KK"]
media_escolaridade_estados = media_escolaridade_estados.reset_index(drop=True)

# Adição de proporção proporção no nível de escolaridade através da função exponencial
media_escolaridade_estados["NIVEL_ESCOLARIDADE"] = 2.5**media_escolaridade_estados["NIVEL_ESCOLARIDADE"]

# Extração de máximo e mínimo do Data
escolaridade_maxima = media_escolaridade_estados["NIVEL_ESCOLARIDADE"].max()
escolaridade_minima = media_escolaridade_estados["NIVEL_ESCOLARIDADE"].min()

# Normalização do nível de escolaridade na escala de 0 a 100
media_escolaridade_estados["NIVEL_ESCOLARIDADE"] = (media_escolaridade_estados["NIVEL_ESCOLARIDADE"] - escolaridade_minima)/(escolaridade_maxima-escolaridade_minima)*100