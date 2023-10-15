import pandas as pd

def cria_novo_df(df, ano):
    """
    Recebe um DataFrame e um ano como entrada, calcula medidas de resumo para as colunas "PESO" e 
    "ALTURA" do DataFrame fornecido com base na coluna "UF_JSM", e cria um novo DataFrame com essas medidas.

    Parâmetros:
    df (pd.DataFrame): O DataFrame a ser processado, deve conter as colunas "UF_JSM", "PESO" e "ALTURA".
    ano (int): O ano associado aos dados do DataFrame.

    Retorna:
    pd.DataFrame: Um novo DataFrame contendo as medidas de resumo das colunas "PESO" e "ALTURA, agregadas 
    por "UF_JSM" e "Brasil".

    Exemplo:
    df = pd.DataFrame({
        'UF_JSM': ['A', 'A', 'B', 'B', 'A', 'B'],
        'PESO': [70, 80, 60, 75, 80, 70],
        'ALTURA': [170, 175, 160, 165, 175, 165]
    })
    ano = 2023
    resultado = cria_novo_df(df, ano)
    """

    try:
        # Verifica se o DataFrame é válido e contém as colunas necessárias
        if not isinstance(df, pd.DataFrame) or "UF_JSM" not in df.columns or "PESO" not in df.columns or "ALTURA" not in df.columns:
            raise ValueError("O DataFrame fornecido não é válido ou não contém as colunas necessárias.")

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
    except Exception as e:
        return None

def concatena_dataframes(*dataframes):
    """
    Concatena vários DataFrames verticalmente.

    Esta função aceita um número variável de DataFrames com as mesmas colunas
    e os concatena verticalmente, um abaixo do outro.

    Parameters:
        *dataframes: Um ou mais DataFrames a serem concatenados.

    Returns:
        pd.DataFrame: O DataFrame resultante da concatenação.

    Example:
    ```
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    resultado = concatena_dataframes(df1, df2)
    ```
    """
    try:
        # Verifica se pelo menos um DataFrame foi fornecido
        if not dataframes:
            return None

        # Verifica se todos os DataFrames têm as mesmas colunas
        colunas_primeiro_df = set(dataframes[0].columns)
        for df in dataframes[1:]:
            if set(df.columns) != colunas_primeiro_df:
                raise ValueError("Os DataFrames fornecidos não têm as mesmas colunas.")

        # Usa o primeiro DataFrame como base para a concatenação
        resultado = dataframes[0]

        # Loop pelos DataFrames restantes e concatene-os verticalmente
        for df in dataframes[1:]:
            resultado = pd.concat([resultado, df], ignore_index=True)

        return resultado
    except Exception as e:
        return None
