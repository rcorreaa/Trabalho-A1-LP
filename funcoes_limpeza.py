import pandas as pd

df = pd.read_csv("sermil2007.csv", encoding='latin-1')

def limpa_PESO(df):
    #Limpando coluna PESO
    df = df.dropna(subset=['PESO'])
    df = df.loc[df['PESO'] >= 40]
    df = df.loc[df['PESO'] <= 200]
    return df

def limpa_ALTURA(df):
    #Limpando coluna ALTURA
    df = df.dropna(subset=['ALTURA'])
    df = df.loc[df['ALTURA'] >= 140]
    df = df.loc[df['ALTURA'] <= 220]
    return df

def limpa_SEXO(df):
    #Limpando coluna SEXO
    df = df.loc[df['SEXO'] != "F"]
    return df

def exclui_colunas(df):
    #Excluindo colunas desnecessárias
    df = df.drop(["CABECA", "CALCADO", "CINTURA", "JSM", "MUN_JSM", "UF_JSM"])
    return df
