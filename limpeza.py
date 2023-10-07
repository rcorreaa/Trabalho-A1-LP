def limpeza(caminho_csv):
    import pandas as pd #Importo o Pandas
    df = pd.read_csv(caminho_csv, sep=";") #Leio o arquivo CSV a ser analisado
    df_limpo = df.copy() #Crio uma cópia do meu Dataframe original
    #Removo colunas que não serão utilizadas na visualização
    df_limpo = df_limpo.drop(columns=["RELIGIAO", "SEXO", "MUN_NASCIMENTO", "PAIS_NASCIMENTO", "ESTADO_CIVIL", "VINCULACAO_ANO", "MUN_RESIDENCIA", "JSM", "UF_JSM", "MUN_JSM"])
    #Removo linhas com ao menos 2 itens em branco
    df_limpo = df_limpo.dropna(thresh =df.shape[1]-1)
    #As células nulas na coluna altura (a única com células nulas) são trocadas pela mediana da altura
    m = df_limpo["ALTURA"].median() #Encontro a mediana
    df_limpo["ALTURA"].fillna(m, inplace = True) #Executo o desejado
    return df_limpo #Retorno o Dataframe limpo