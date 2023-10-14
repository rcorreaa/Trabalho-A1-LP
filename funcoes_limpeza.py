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
    Exemplo válido, com a coluna 'PESO' presente, e os dados são todos númericos
    >>> df = pd.DataFrame({"PESO": [100, 101, 210, 35]})
    >>> limpa_PESO(df)
       PESO
    0   100
    1   101

    Exemplo válido, com a coluna 'PESO' presente, e os dados prontos para serem convertidos para números
    >>> df = pd.DataFrame({"PESO": [pd.NA, "120", "40", "230"]})
    >>> limpa_PESO(df)
        PESO
    1  120.0
    2   40.0

    Exemplo inválido, o DataFrame não apresenta a coluna 'PESO'
    >>> df = pd.DataFrame({"ALTURA": [180, 179, 210, 167]})
    >>> limpa_PESO(df)
    Traceback (most recent call last):
        ...
    KeyError: ['PESO']

    Exemplo inválido, a coluna 'PESO' do DataFrame apresenta valores não numéricos
    >>> df = pd.DataFrame({"PESO": [200, "120 kg", 40, 230]})
    >>> limpa_PESO(df)
    Traceback (most recent call last):
           ...
    TypeError: '>=' not supported between instances of 'str' and 'int'
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
    Exemplo válido, com a coluna 'ALTURA' presente, e os dados são todos númericos
    >>> df = pd.DataFrame({"ALTURA": [180, 121, 210, 200]})
    >>> limpa_ALTURA(df)
       ALTURA
    0     180
    2     210
    3     200

    Exemplo válido, com a coluna 'ALTURA' presente, e os dados prontos para serem convertidos para números
    >>> df = pd.DataFrame({"ALTURA": [pd.NA, "120", "150", "180"]})
    >>> limpa_ALTURA(df)
       ALTURA
    2   150.0
    3   180.0

    Exemplo inválido, o DataFrame não apresenta a coluna 'ALTURA'
    >>> df = pd.DataFrame({"PESO": [180, 179, 210, 167]})
    >>> limpa_ALTURA(df)
    Traceback (most recent call last):
        ...
    KeyError: ['ALTURA']

    Exemplo inválido, a coluna 'PESO' do DataFrame apresenta valores não numéricos
    >>> df = pd.DataFrame({"ALTURA": [200, "179 cm", 140, 230]})
    >>> limpa_ALTURA(df)
    Traceback (most recent call last):
        ...
    TypeError: '>=' not supported between instances of 'str' and 'int'
    """
    # Criação de cópia do DataFrame, sem alterar o original

    df_tratado = df.copy()

    try:
        # Conversão da coluna ALTURA para o tipo numérico
        df_tratado["ALTURA"] = pd.to_numeric(df_tratado["ALTURA"])
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
    Exemplo válido, com a coluna 'SEXO' presente, e os dados são se apresentam da forma correta
    >>> df = pd.DataFrame({"SEXO": ["M", "M", "F","M"]})
    >>> limpa_SEXO(df)
      SEXO
    0    M
    1    M
    3    M

    Exemplo inválido, o DataFrame não apresenta a coluna 'SEXO'
    >>> df = pd.DataFrame({"PESO": [pd.NA, 120, 40, 230]})
    >>> limpa_SEXO(df)
    A coluna 'SEXO' não existe.
       PESO
    0  <NA>
    1   120
    2    40
    3   230
    """
    # Criação de cópia do DataFrame, sem alterar o original
    df_tratado = df.copy()

    try:
        # Excluindo valores "F" da coluna SEXO
        df_tratado = df_tratado[df["SEXO"] == "M"]
    except KeyError as erro_sexo:
        raise erro_sexo

    return df_tratado


def limpa_ANO_NASCIMENTO(df, ano):
    """
    Remove as linhas de pessoas com mais de 19 anos do DataFrame.

    Parameters:
        df(dataframe): DataFrame a ser processado.
        ano: ano do dataframe

    Returns:
        df_tratado(dataframe): DataFrame sem as linhas especificadas.

    Exemplos:
    Exemplo válido, com a coluna 'ALTURA' presente, e os dados são todos númericos
    >>> df = pd.DataFrame({"ANO_NASCIMENTO": [2004, 2003, 2005, 2000]})
    >>> limpa_ANO_NASCIMENTO(df, 2022)
       ANO_NASCIMENTO
    0            2004
    1            2003

    Exemplo inválido, o DataFrame não apresenta a coluna 'ANO_NASCIMENTO'
    >>> df = pd.DataFrame({"PESO": [pd.NA, 120, 40, 230]})
    >>> limpa_ANO_NASCIMENTO(df, 2019)
    A coluna 'ANO_NASCIMENTO' não existe.
       PESO
    0  <NA>
    1   120
    2    40
    3   230
    """

    df_tratado = df.copy()

    try:
        # Filtrando indivíduos com a idade correta de alistamento.
        df_tratado = df_tratado[(df["ANO_NASCIMENTO"] == ano - 18) | (df["ANO_NASCIMENTO"] == ano - 19)]
    except KeyError as erro_ano:
        raise erro_ano

    return df_tratado


def renomeia_ESCOLARIDADE(df):
    """
    Renomeia as categorias da coluna ESCOLARIDADE, a fim de agrupar.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame com a coluna atualizada.

    Exemplos:
    Exemplo válido, com a coluna 'ESCOLARIDADE', e dados prontos para serem processados
    >>> df = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Superior", "Mestrado", "Ensino Fundamental", "Doutorado"]})
    >>> renomeia_ESCOLARIDADE(df)
                ESCOLARIDADE
    0  Ensino Médio Completo
    1        Ensino Superior
    2          Pós-graduação
    3     Ensino Fundamental
    4          Pós-graduação

    Exemplo inválido, o DataFrame não apresenta a coluna 'ESCOLARIDADE'
    >>> df = pd.DataFrame({"OUTRA_COLUNA": [1, 2, 3]})
    >>> renomeia_ESCOLARIDADE(df)
    Coluna 'ESCOLARIDADE' não existente no DataFrame.
       OUTRA_COLUNA
    0             1
    1             2
    2             3
    """

    def aux_renomeia(registro_ESCOLARIDADE):
        if registro_ESCOLARIDADE.find("Completo") != -1:
            return registro_ESCOLARIDADE
        elif registro_ESCOLARIDADE.find("Ensino Médio") != -1:
            return "Ensino Médio"
        elif registro_ESCOLARIDADE.find("Ensino Fundamental") != -1:
            return "Ensino Fundamental"
        elif registro_ESCOLARIDADE.find("Ensino Superior") != -1:
            return "Ensino Superior"
        elif registro_ESCOLARIDADE.find("Pós") != -1 or registro_ESCOLARIDADE.find(
                "Mestrado") != -1 or registro_ESCOLARIDADE.find("Doutorado") != -1:
            return "Pós-graduação"
        else:
            return registro_ESCOLARIDADE

    df_tratado = df.copy()

    try:
        df_tratado["ESCOLARIDADE"] = df_tratado["ESCOLARIDADE"].apply(
            lambda registro_ESCOLARIDADE: aux_renomeia(registro_ESCOLARIDADE))
    except KeyError as erro_coluna:
        raise erro_coluna

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

    Exemplos:
    # Exemplo válido, excluindo a coluna 'coluna_1' existente no DataFrame
    >>> df = pd.DataFrame({"coluna_1":[1,2,3],"coluna_2":[4,5,6]})
    >>> exclui_colunas(df, ["coluna_1"])
       coluna_2
    0         4
    1         5
    2         6

    Exemplo inválido, a função não exclui 'coluna_3' por não estar presente no DataFrame
    >>> df = pd.DataFrame({"coluna_1":[1,2,3],"coluna_2":[4,5,6]})
    >>> exclui_colunas(df, ["coluna_3"])
    Coluna coluna_3 não existente no DataFrame.
       coluna_1  coluna_2
    0         1         4
    1         2         5
    2         3         6
    """
    # Criação de cópia do DataFrame, sem alterar o original
    df_tratado = df.copy()

    for coluna in cols_del:
        try:
            # Exclusão de colunas desnecessárias sem alteração no DataFrame original
            df_tratado = df_tratado.drop(coluna, axis=1)
        except:
            print(f"Coluna {coluna} não existente no DataFrame.")

    return df_tratado


def nivel_ESCOLARIDADE(df):
    """
    Cria a coluna NIVEL_ESCOLARIDADE a fim de medir em valor quantitativo o
    nível de escolaridade dos indivíduos.

    Parameters:
        df(dataframe): DataFrame a ser processado.

    Returns:
        df_tratado(dataframe): DataFrame com a coluna NIVEL_ESCOLARIDADE adicionada.

    Exemplos:
    Exemplo válido, com a coluna 'ESCOLARIDADE' presente no DataFrame e dados de 'NIVEL_ESCOLARIDADE' prontos para serem criados
    >>> df = pd.DataFrame({"ESCOLARIDADE":["Ensino Médio", "Alfabetizado"]})
    >>> nivel_ESCOLARIDADE(df)
       ESCOLARIDADE  NIVEL_ESCOLARIDADE
    0  Ensino Médio                   5
    1  Alfabetizado                   1

    Exemplo inválido, não se aplica a funcionadade por não existir a coluna 'ESCOLARIDADE'
    >>> df = pd.DataFrame({"PESO":[100, 85, 115, 79], "ALTURA":[180, 169, 120, 240]})
    >>> nivel_ESCOLARIDADE(df)
    A coluna 'ESCOLARIDADE' não foi encontrada no DataFrame.
       PESO  ALTURA
    0   100     180
    1    85     169
    2   115     120
    3    79     240
    """
    # Criação de cópia do DataFrame, sem alterar o original
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
        # Atribuindo valores de nível de escolaridade de acordo com a formação dos indivíduos
        df_tratado["NIVEL_ESCOLARIDADE"] = df_tratado["ESCOLARIDADE"].replace(grau_escolaridade)
    except KeyError as coluna:
        print(f"A coluna {coluna} não foi encontrada no DataFrame.")

    return df_tratado


def gera_tabela_escolaridade(path_data="", ini_ano=2018, fim_ano=2022):
    """
    A função tem por objetivo gerar um arquivo csv dos dados da média dos estados de
    escolaridade do Brasil do período passado. Por padrão, de 2018 até 2022.

    Parameters:
        path_data(string): diretório dos arquivos dos arquivos .csv
        ini_ano(int): ano de inicio. 2018 por padrão
        fim_ano(int): ano do final. 2022 por padrão

    Exemplos:
    Exemplo válido, realizando o download do arquivo csv obtido
    >>> gera_tabela_escolaridade(path_data="", ini_ano=2018, fim_ano=2022)

    Exemplo inválido, o ano 1997 não está disponível para análise
    >>> gera_tabela_escolaridade(path_data="", ini_ano=1997, fim_ano=2004)
    Erro de leitura no database do ano 1997
    """
    # Lista a ser preenchida dos DataFrames utilizados
    lista_df = []

    for ano in range(ini_ano, fim_ano + 1):
        # Leitura do database com tratamento de erro
        try:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano), usecols=["UF_RESIDENCIA", "ESCOLARIDADE"])
        except UnicodeDecodeError:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano), usecols=["UF_RESIDENCIA", "ESCOLARIDADE"], encoding="latin1")
        except:
            print("Erro de leitura no database do ano", ano)
            return

        # Agrupando dados da coluna de escolaridade e criando coluna de nível de escolaridade
        df = renomeia_ESCOLARIDADE(df)
        df = nivel_ESCOLARIDADE(df)

        lista_df.append(df)

    # Junção dos DataFrames verticalmente
    df_concatenado = pd.concat(lista_df, ignore_index=True)

    # Remoção da coluna de escolaridade
    df_concatenado.drop("ESCOLARIDADE", axis=1, inplace=True)

    # Média de escolaridade por estado
    media_escolaridade_estados = df_concatenado.groupby("UF_RESIDENCIA")["NIVEL_ESCOLARIDADE"].mean().reset_index()

    # Remoção do estado 'KK' e resetação de índices
    media_escolaridade_estados = media_escolaridade_estados.loc[media_escolaridade_estados["UF_RESIDENCIA"] != "KK"]
    media_escolaridade_estados = media_escolaridade_estados.reset_index(drop=True)

    # Mudança de escala no nível de escolaridade
    media_escolaridade_estados["NIVEL_ESCOLARIDADE"] = 2.5**media_escolaridade_estados["NIVEL_ESCOLARIDADE"]

    # Extração de máximo e mínimo do DataFrame
    escolaridade_maxima = media_escolaridade_estados["NIVEL_ESCOLARIDADE"].max()
    escolaridade_minima = media_escolaridade_estados["NIVEL_ESCOLARIDADE"].min()

    # Normalização do nível de escolaridade na escala de 0 a 100
    media_escolaridade_estados["NIVEL_ESCOLARIDADE"] = (media_escolaridade_estados["NIVEL_ESCOLARIDADE"] - escolaridade_minima)/(escolaridade_maxima-escolaridade_minima)*100

    # Geração do arquivo CSV utilizado para confecção da análise
    media_escolaridade_estados.to_csv("tabela_escolaridade.csv", index=False)
