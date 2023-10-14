from funcoes_limpeza import *
import pandas as pd

def gera_tabela_escolaridade(pathdata, ini_ano=2018, fim_ano=2022):
    """
    A função tem por objetivo gerar um arquivo csv dos dados da média dos estados de
    escolaridade do Brasil do período passado. Por padrão, de 2018 até 2022.

    Parameters:
        path_data(string): diretório dos arquivos dos arquivos .csv
        ini_ano(int): ano de inicio. 2018 por padrão
        fim_ano(int): ano do final. 2022 por padrão
    Returns:
        tabela_escolaridade_csv(csv): csv utilizado para o mapa.
    """
    v_df = []

    for ano in range(ini_ano, fim_ano + 1):
        # leitura do database com tratamento de erro
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

        v_df.append(df)

    # Junção dos DataFrames verticalmente
    df_concatenado = pd.concat(v_df, ignore_index=True)

    # Remoção da coluna de escolaridade
    df_concatenado.drop("ESCOLARIDADE", axis=1, inplace=True)

    # Média de escolaridade por estado
    media_escolaridade_estados = df_concatenado.groupby("UF_RESIDENCIA")["NIVEL_ESCOLARIDADE"].mean().reset_index()

    # Remoção do estado 'KK' e resetação de índices
    media_escolaridade_estados = media_escolaridade_estados.loc[media_escolaridade_estados["UF_RESIDENCIA"] != "KK"]
    media_escolaridade_estados = media_escolaridade_estados.reset_index(drop=True)

    # Adição de proporção proporção no nível de escolaridade através da função exponencial
    media_escolaridade_estados["NIVEL_ESCOLARIDADE"] = 2.5**media_escolaridade_estados["NIVEL_ESCOLARIDADE"]

    # Extração de máximo e mínimo do Data
    escolaridade_maxima = media_escolaridade_estados["NIVEL_ESCOLARIDADE"].max()
    escolaridade_minima = media_escolaridade_estados["NIVEL_ESCOLARIDADE"].min()

    # Normalização do nível de escolaridade na escala de 0 a 100
    media_escolaridade_estados["NIVEL_ESCOLARIDADE"] = (media_escolaridade_estados["NIVEL_ESCOLARIDADE"] - escolaridade_minima)/(escolaridade_maxima-escolaridade_minima)*100

    tabela_escolaridade_csv = media_escolaridade_estados.to_csv(index=False)

    return tabela_escolaridade_csv
