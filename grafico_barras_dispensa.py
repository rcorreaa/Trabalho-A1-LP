import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec

def plot_grafico_barras(path_data, ini_ano=2018, fim_ano=2022):
    """
    Cria um gráfico de ranking junto com um stacked bar que analisam a quantidade de valores 
    "Sem dispensa" e "Com dispensa" da coluna DISPENSA e a proporção de cada um com relação 
    ao alistamento militar dos anos de 2018 a 2022.

    Parameters:
        path_data(caminho): Caminho dos DataFrames.
        ini_ano(int): Ano de início. 2018 por padrão
        fim_ano(int): Ano de término. 2022 por padrão

    Returns:
        None:
    """
    
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

    # Cria novo DataFrame com a coluna REGIAO e conta a quantidade dos valores da DISPENSA
    df_completo["REGIAO"] = df_completo["UF_JSM"].map(mapeamento_regioes)
    df_agrupado = df_completo.groupby("REGIAO")["DISPENSA"].value_counts().reset_index()
    df_organizado = df_agrupado.pivot(index="REGIAO", columns="DISPENSA", values="count")

    # Cria novo DataFrame com as proporções dos valores da DISPENSA
    somas = df_agrupado.groupby(["REGIAO", "DISPENSA"])["count"].sum()
    soma_total = df_agrupado.groupby("REGIAO")["count"].sum()
    proporcoes = somas.unstack().div(soma_total, axis=0).reset_index()
    proporcoes.columns = ["REGIAO", "Com dispensa", "Sem dispensa"]

    # Crie um grid 1x2
    fig = plt.figure(figsize=(16, 6))
    gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1])  # 2 colunas e a primeira com o dobro da largura

    # Visualização 1: Gráfico de barras lado a lado
    ax0 = plt.subplot(gs[0])  # Célula da primeira coluna
    cores = ["#A50030", "#1A3071"]
    bar_width = 0.35
    posicao = range(len(df_organizado.index))

    ax0.grid(True, axis="y", linestyle="--", color="gray", zorder=0)

    ax0.bar(posicao, df_organizado["Com dispensa"], width=bar_width, 
            label="Com dispensa", color=cores[0], edgecolor="black")

    ax0.bar([i + bar_width for i in posicao], df_organizado["Sem dispensa"], 
            width=bar_width, label="Sem dispensa", color=cores[1], edgecolor="black")

    ax0.set_ylabel("Contagem")
    ax0.set_title('Contagem de "Com dispensa" e "Sem dispensa" por Região')
    ax0.set_xticks([i + bar_width / 2 for i in posicao])
    ax0.set_xticklabels(df_organizado.index)
    ax0.legend()

    # Visualização 2: Gráfico de barras empilhadas horizontal
    ax1 = plt.subplot(gs[1])  # Célula da segunda coluna
    cores = ["#A50030", "#1A3071"]

    proporcoes["Com_dispensa_percent"] = proporcoes["Com dispensa"] * 100
    proporcoes["Sem_dispensa_percent"] = proporcoes["Sem dispensa"] * 100

    bar1 = ax1.barh(proporcoes["REGIAO"], proporcoes["Com_dispensa_percent"], label="Com dispensa", color="#A50030")
    bar2 = ax1.barh(proporcoes["REGIAO"], proporcoes["Sem_dispensa_percent"], left=proporcoes["Com_dispensa_percent"], label="Sem dispensa", color="#1A3071")

    ax1.bar_label(bar1, fmt='%.2f%%', label_type="center", fontsize=10)
    ax1.bar_label(bar2, fmt='%.2f%%', label_type="center", fontsize=10)

    ax1.set_title("Proporção de Com Dispensa e Sem Dispensa por Região")
    ax1.set_xlabel("Proporção")
    ax1.set_ylabel("Região")
    ax1.legend()

    # Ajuste o layout para melhor visualização
    plt.tight_layout()
    plt.show()
    return None 

plot_grafico_barras("C:\\Users\\samue\\OneDrive\\Documentos\\Dados\\")

