import pandas as pd

def limpa_PESO(df):
    """
    Realiza a remoção de linhas do DataFrame de acordo com a coluna 'PESO',
    permanecendo apenas dados não nulos e em uma faixa de valor entre 40 e 200 kilos.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame com linhas indesejadas removidas.
    """
    df_tratado = df.copy()
    try:
        # Conversão da coluna PESO para o tipo numérico
        df_tratado["PESO"] = pd.to_numeric(df_tratado["PESO"], errors="coerce")
    except KeyError:
        print("A coluna 'PESO' não está presente no DataFrame.")
    except ValueError:
        print("Impossível converter a coluna 'PESO' para o tipo numérico.")
    # Limpando a coluna PESO usando df_tratado em vez de df
    df_tratado = df_tratado.dropna(subset=["PESO"])
    df_tratado = df_tratado.loc[df_tratado["PESO"] >= 40]
    df_tratado = df_tratado.loc[df_tratado["PESO"] <= 200]
    return df_tratado

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
