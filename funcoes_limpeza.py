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
    # Criação de cópia do DataFrame, sem alterar o original

    df_tratado = df.copy()

    try:
        # Conversão da coluna PESO para o tipo numérico
        df_tratado["PESO"] = pd.to_numeric(df_tratado["PESO"], errors="coerce")
    except KeyError:
        print("A coluna 'PESO' não está presente no DataFrame.")
    except ValueError:
        print("Impossível converter a coluna 'PESO' para o tipo numérico.")
    # Limpeza da coluna 'PESO'
    df_tratado = df_tratado.dropna(subset=["PESO"])
    df_tratado = df_tratado.loc[df_tratado["PESO"] >= 40]
    df_tratado = df_tratado.loc[df_tratado["PESO"] <= 200]
    
    return df_tratado

def limpa_ALTURA(df):
    """
    Realiza a remoção de linhas do DataFrame de acordo com a coluna 'ALTURA',
    permanecendo apenas dados não nulos e em uma faixa de valor entre 140 e 220 centímetros.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame com linhas indesejadas removidas.
    """
    # Criação de cópia do DataFrame, sem alterar o original

    df_tratado = df.copy()

    try:
        # Conversão da coluna ALTURA para o tipo numérico
        df_tratado["ALTURA"] = pd.to_numeric(df_tratado["ALTURA"], errors="coerce")
    except KeyError:
        print("A coluna 'ALTURA' não está presente no DataFrame.")
    except ValueError:
        print("Impossível converter a coluna 'ALTURA' para o tipo numérico.")
    # Limpeza da coluna 'ALTURA'
    df_tratado = df_tratado.dropna(subset=['ALTURA'])
    df_tratado = df_tratado[(df_tratado['ALTURA'] >= 140) & (df_tratado['ALTURA'] <= 220)]

    return df_tratado

def limpa_SEXO(df):
    """
    Remove os valores "F" da coluna SEXO do DataFrame.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame sem as colunas especificadas.
    """

    df_tratado = df.copy()

    try:
        #Excluindo valores "F" da coluna SEXO
        df_tratado = df_tratado[df["SEXO"] != "F"]
    except ValueError as erro_sexo:
        print("Não há sexo feminino na coluna: ", erro_sexo)

    return df_tratado

def limpa_ANO_NASCIMENTO(df, ano):
    """
    Remove as linhas de pessoas com mais de 19 anos do DataFrame.

    Parameters:
        df(dataframe): DataFrame a ser processado.
        ano: ano do dataframe

    Returns:
        df_tratado(dataframe): DataFrame sem as linhas especificadas.
    """

    df_tratado = df.copy()

    try:
        #Excluindo valores "F" da coluna SEXO
        df_tratado = df_tratado[(df["ANO_NASCIMENTO"] == ano-18) | (df["ANO_NASCIMENTO"] == ano-19)]
    except ValueError as erro_ano:
        print("Não há coluna: ", erro_ano)

    return df_tratado

def renomeia_ESCOLARIDADE(df):
    """
    Renomeia as categorias da coluna ESCOLARIDADE, a fim de agrupar.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame com a coluna atualizada.
    """
    
    def aux_renomeia(x):
        if x.find("Completo")!=-1:
            return x
        elif x.find("Ensino Médio")!=-1:
            return "Ensino Médio"
        elif x.find("Ensino Fundamental")!=-1:
            return "Ensino Fundamental"
        elif x.find("Ensino Superior")!=-1:
            return "Ensino Superior"
        elif x.find("Pós")!=-1 or x.find("Mestrado")!=-1 or x.find("Doutorado")!=-1:
            return "Pós-graduação"
        else:
            return x
    
    df_tratado = df.copy()
    
    try:
        df_tratado["ESCOLARIDADE"] = df_tratado["ESCOLARIDADE"].apply(lambda x: aux_renomeia(x))
    except ValueError as erro_ano:
        print("Não há coluna: ", erro_ano)
    
    return df_tratado

def exclui_colunas(df):
    """
    Remove colunas desnecessárias do DataFrame passado. São elas: 
    ("CABECA", "CALCADO", "CINTURA", "JSM", "MUN_NASCIMENTO", "UF_NASCIMENTO", "RELIGIAO").

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame sem as colunas especificadas.
    """

    df_tratado = df.copy()

    try:
        # Exclusão de colunas desnecessárias sem alteração no DataFrame original
        df_tratado = df_tratado.drop(["CABECA", "CALCADO", "CINTURA", "JSM",
                                      "MUN_NASCIMENTO", "UF_NASCIMENTO", "RELIGIAO"], axis=1)
    except KeyError:
        print("Alguma(s) coluna(s) não existe(m) no DataFrame.")

    return df_tratado

def nivel_escolaridade(df):
    """
    Cria a coluna NIVEL_ESCOLARIDADE a fim de medir em valor quantitativo o
    nível de escolaridade dos indivíduos.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame com a coluna NIVEL_ESCOLARIDADE adicionada.
    """

    df_tratado = df.copy()
    grau_escolaridade = {
        "Analfabeto": 0,
        "Alfabetizado": 1,
        "Ensino Fundamental": 2,
        "Ensino Fundamental Completo": 3,
        "Ensino Médio": 4,
        "Ensino Médio Completo": 5,
        "Ensino Superior": 6,
        "Ensino Superior Completo": 7,
        "Pós-graduação": 8}
    # Atribuindo valores de nível de escolaridade de acordo com a formação dos indivíduos.
    df_tratado["NIVEL_ESCOLARIDADE"] = df_tratado["ESCOLARIDADE"].replace(grau_escolaridade)
    return df_tratado
