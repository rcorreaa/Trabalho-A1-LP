import pandas as pd

def limpa_PESO(df):
    """
    Realiza a remoção de linhas do DataFrame de acordo com a coluna 'PESO',
    permanecendo apenas dados não nulos e em uma faixa de valor entre 40 e 200 kilos.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame com linhas indesejadas removidas.

    Exemplos:
    >>> df = pd.DataFrame({"PESO": [100, 101, 210, 35]})
    >>> limpa_PESO(df)
    df_tratado

    >>> df = pd.DataFrame({"PESO": [pd.NA, 120, 40, 230]})
    >>> limpa_PESO(df)
    df_tratado

    >>> df = pd.DataFrame({"ALTURA": [180, 179, 210, 167]})
    >>> limpa_PESO(df)
    Traceback (most recent call last):
        ...
    A coluna 'PESO' não está presente no DataFrame.

    >>> df = pd.DataFrame({"PESO": [200, "120 kg", 40, 230]})
    >>> limpa_PESO(df)
    df_tratado
    """
    # Criação de cópia do DataFrame, sem alterar o original
    df_tratado = df.copy()

    try:
        # Conversão da coluna PESO para o tipo numérico
        df_tratado["PESO"] = pd.to_numeric(df_tratado["PESO"])
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

    Exemplos:
    >>> df = pd.DataFrame({"ALTURA": [180, 121, 210, 200]})
    >>> limpa_ALTURA(df)
    df_tratado

    >>> df = pd.DataFrame({"ALTURA": [pd.NA, 120, 150, 180]})
    >>> limpa_ALTURA(df)
    df_tratado

    >>> df = pd.DataFrame({"PESO": [180, 179, 210, 167]})
    >>> limpa_ALTURA(df)
    Traceback (most recent call last):
        ...
    A coluna 'PESO' não está presente no DataFrame.

    >>> df = pd.DataFrame({"ALTURA": [200, "179 cm", 140, 230]})
    >>> limpa_ALTURA(df)
    df_tratado
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
        df_tratado(dataframe): DataFrame com linhas indesejadas removidas.

    Exemplos:
    >>> df = pd.DataFrame({"SEXO": ["M", "M", "F","M"]})
    >>> limpa_PESO(df)
    df_tratado

    >>> df = pd.DataFrame({"PESO": [pd.NA, 120, 40, 230]})
    >>> limpa_PESO(df)
    A coluna 'SEXO' não existe.
    """
    # Criação de cópia do DataFrame, sem alterar o original
    df_tratado = df.copy()

    try:
        # Excluindo valores "F" da coluna SEXO
        df_tratado = df_tratado[df["SEXO"] == "M"]
    except KeyError as erro_sexo:
        print(f"A coluna {erro_sexo} não existe.")

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

def exclui_colunas(df, cols_del=["CABECA", "CALCADO", "CINTURA", "JSM", "MUN_NASCIMENTO", "UF_NASCIMENTO", "RELIGIAO"]):
    """
    Remove colunas desnecessárias do DataFrame passado. Por padrão são as colunas: 
    ("CABECA", "CALCADO", "CINTURA", "JSM", "MUN_NASCIMENTO", "UF_NASCIMENTO", "RELIGIAO").

    Parameters:
        df(dataframe): DataFrame a ser processado.
        cols_del(list): Lista de colunas a serem deletadas. (Opcional)

    Returns:
        df_tratado(dataframe): DataFrame sem as colunas especificadas.
    """

    df_tratado = df.copy()

    for col in cols_del:
        try:
            # Exclusão de colunas desnecessárias sem alteração no DataFrame original
            df_tratado = df_tratado.drop(col, axis=1)
        except KeyError:
            print("Coluna não existente no DataFrame:", col)

    return df_tratado

def nivel_ESCOLARIDADE(df):
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
        "Ensino Fundamental Completo": 4,
        "Ensino Médio": 5,
        "Ensino Médio Completo": 7,
        "Ensino Superior": 9,
        "Ensino Superior Completo": 12,
        "Pós-graduação": 15}
    try:
        # Atribuindo valores de nível de escolaridade de acordo com a formação dos indivíduos.
        df_tratado["NIVEL_ESCOLARIDADE"] = df_tratado["ESCOLARIDADE"].replace(grau_escolaridade)
    except KeyError as coluna:
        print(f"Erro: A coluna {coluna} não foi encontrada no DataFrame.")
        return None
    return df_tratado
