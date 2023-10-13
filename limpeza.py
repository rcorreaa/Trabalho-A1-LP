def limpeza(caminho_csv):
    '''
    Args:
    caminho_csv: O caminho do arquivo CSV a ser lido.
    
    Returns:
    df_limpo: O dataframe original após a limpeza dos dados.
    
    Exemplo:
        >>> caminho_arquivo = "dados.csv"
        >>> df_limpo = limpeza(caminho_arquivo)
        >>> print(df_limpo.head())
    '''
    import pandas as pd #Importo o Pandas.
    df = pd.read_csv(caminho_csv, sep=";") #Leio o arquivo CSV a ser analisado.
    df_limpo = df.copy() #Crio uma cópia do meu Dataframe original.
    #Removo colunas que não serão utilizadas na visualização.
    df_limpo = df_limpo.drop(columns=["RELIGIAO", "SEXO", "MUN_NASCIMENTO", "PAIS_NASCIMENTO", "ESTADO_CIVIL", "VINCULACAO_ANO", "MUN_RESIDENCIA", "JSM", "UF_JSM", "MUN_JSM"])
    df_limpo = df_limpo.dropna() #Removo linhas com ao menos 1 item em branco.
    return df_limpo #Retorno o Dataframe limpo.