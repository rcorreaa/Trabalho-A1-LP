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
    """
    Remove os valores "F" da coluna SEXO do DataFrame.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame sem as colunas especificadas.
    """
    try:
        #Excluindo valores "F" da coluna SEXO
        df_tratado = df.copy()
        df_tratado = df_tratado.loc[df["SEXO"] != "F"]
    except ValueError as erro_sexo:
        print("Não há sexo feminino na coluna: ", erro_sexo)
    return df_tratado


def exclui_colunas(df):
    """
    Remove colunas desnecessárias do DataFrame passado. São elas: 
    ("CABECA", "CALCADO", "CINTURA", "JSM", "MUN_JSM", "UF_JSM", "RELIGIAO").

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame sem as colunas especificadas.
    """
    try:
        # Excluindo colunas desnecessárias sem alterar o DataFrame original
        df_tratado = df.copy()
        df_tratado = df_tratado.drop(["CABECA", "CALCADO", "CINTURA", "JSM",
                                      "MUN_JSM", "UF_JSM", "RELIGIAO"], axis=1)
    except KeyError:
        print("Alguma(s) coluna(s) não existe(m) no DataFrame.")
    return df_tratado
