import pandas as pd
import matplotlib.pyplot as plt

def plot_grafico_stacked_bar(path_data, ini_ano=2018, fim_ano=2022):
    v_df = []
    for ano in range(ini_ano, fim_ano+1):
        # Leitura do database com tratamento de erro
        try:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano), usecols=["UF_JSM", "DISPENSA", "VINCULACAO_ANO"])
        except UnicodeDecodeError:
            df = pd.read_csv(path_data + "sermil{}.csv".format(ano), usecols=["UF_JSM", "DISPENSA", "VINCULACAO_ANO"], encoding="latin1")
        except:
            print("Erro de leitura no database do ano", ano)
            return    
        v_df.append(df)
        
    # Juntando todos os DataFrames
    df_completo = pd.concat(v_df, ignore_index=True) 

    # Criando dicionário para mapear os estados
    mapeamento_regioes = {
        'AC': 'Norte',
        'AL': 'Nordeste',
        'AM': 'Norte',
        'AP': 'Norte',
        'BA': 'Nordeste',
        'CE': 'Nordeste',
        'DF': 'Centro-Oeste',
        'ES': 'Sudeste',
        'GO': 'Centro-Oeste',
        'MA': 'Nordeste',
        'MG': 'Sudeste',
        'MS': 'Centro-Oeste',
        'MT': 'Centro-Oeste',
        'PA': 'Norte',
        'PB': 'Nordeste',
        'PE': 'Nordeste',
        'PI': 'Nordeste',
        'PR': 'Sul',
        'RJ': 'Sudeste',
        'RN': 'Nordeste',
        'RO': 'Norte',
        'RR': 'Norte',
        'RS': 'Sul',
        'SC': 'Sul',
        'SE': 'Nordeste',
        'SP': 'Sudeste',
        'TO': 'Norte'
    }

    # Cria novo DataFrame com a coluna REGIAO
    df_completo["REGIAO"] = df_completo["UF_JSM"].map(mapeamento_regioes)
    df_agrupado = df_completo.groupby("REGIAO")["DISPENSA"].value_counts().reset_index()
    
    # Cria novo DataFrame com as proporções dos valores da DISPENSA
    somas = df_agrupado.groupby(["REGIAO", "DISPENSA"])["count"].sum()
    soma_total = df_agrupado.groupby("REGIAO")["count"].sum()
    proporcoes = somas.unstack().div(soma_total, axis=0).reset_index()
    proporcoes.columns = ["REGIAO", "Com dispensa", "Sem dispensa"]

    proporcoes["Com_dispensa_percent"] = proporcoes["Com dispensa"] * 100
    proporcoes["Sem_dispensa_percent"] = proporcoes["Sem dispensa"] * 100

    bar1 = plt.barh(proporcoes["REGIAO"], proporcoes["Com_dispensa_percent"], label="Com dispensa", color="#A50030")
    bar2 = plt.barh(proporcoes["REGIAO"], proporcoes["Sem_dispensa_percent"], left=proporcoes["Com_dispensa_percent"], label="Sem dispensa", color="#1A3071")

    plt.bar_label(bar1, fmt='%.2f%%', label_type="center", fontsize=10)
    plt.bar_label(bar2, fmt='%.2f%%', label_type="center", fontsize=10)

    plt.suptitle("Proporção de Com Dispensa e Sem Dispensa por Região")
    plt.suptitle("Proporção")
    plt.suptitle("Região")
    plt.legend()
    plt.show()
    return None

plot_grafico_stacked_bar("C:\\Users\\samue\\OneDrive\\Documentos\\Dados\\")