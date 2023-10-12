import pandas as pd

def cria_novo_df(df, ano):
    """
    Recebe um DataFrame e o seu ano. Calcula as medidas de resumo do "PESO" e da "ALTURA" do DataFrame 
    escolhido e cria um novo DataFrame com essas medidas. 

    Parameters:
        df(dataframe): DataFrame a ser processado.
        ano(ano): Ano do Dataframe escolhido.

    Returns:
        df_pronto(dataframe): DataFrame com as medidas de resumo do peso e da altura.
    """

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

def concatena_dataframes(*dataframes):
    # Verifica se pelo menos um DataFrame foi fornecido
    if not dataframes:
        return None

    # Usa o primeiro DataFrame como base para a concatenação
    resultado = dataframes[0]

    # Loop pelos DataFrames restantes e concatene-os verticalmente
    for df in dataframes[1:]:
        resultado = pd.concat([resultado, df], ignore_index=True)

    return resultado
