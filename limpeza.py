import pandas as pd
df = pd.read_csv(r"C:\Users\ramyr\LinguagensDeProgramação\sermil2019.csv", sep=";")

df = df.drop(columns=["RELIGIAO", "SEXO", "MUN_NASCIMENTO", "PAIS_NASCIMENTO", "ESTADO_CIVIL", "VINCULACAO_ANO", "MUN_RESIDENCIA", "JSM", "UF_JSM", "MUN_JSM"])
df = df.dropna()