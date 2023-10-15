import matplotlib.pyplot as plt
import pandas as pd
from funcoes_limpeza import limpa_PESO, limpa_ALTURA, limpa_ANO_NASCIMENTO, limpa_SEXO
import doctest

def plot_grafico_histograma(path_data, ano1=2010, ano2=2014, ano3=2014, ano4=2022):
    """
    Plota o histograma com as densidades dos IMCs dentre 4 anos selecionados.

    Parameters:
        path_data(string): diretório dos arquivos dos arquivos .csv
        ano1: ano a ser analisado. 2010 por padrão
        ano2: ano a ser analisado. 2014 por padrão
        ano3: ano a ser analisado. 2018 por padrão
        ano4: ano a ser analisado. 2022 por padrão
        
    Returns:
        None
    """
    anos = [ano1, ano2, ano3, ano4]
    cores = ['b', 'g', 'y', 'r']

    for i, ano in enumerate(anos):
        
        #Leitura com tratamento de erro
        try:
            df = pd.read_csv(path_data + "\\sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"])
        except UnicodeDecodeError:
            df = pd.read_csv(path_data + "\\sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"], encoding="latin1")
        except:
            print("Erro de leitura do database do ano", ano)
            continue
        
        #Limpeza dos valores nulos e filtro no público a ser analisado
        df = limpa_SEXO(df)
        df = limpa_PESO(df)
        df = limpa_ALTURA(df)
        df = limpa_ANO_NASCIMENTO(df, ano)
        
        #Criação da coluna IMC com base na coluna PESO e ALTURA
        df["IMC"] = 10000 * df["PESO"] / df["ALTURA"] ** 2
       
        #Imprime algumas estatísticas de resumo
        print(ano)
        print(df["IMC"].describe())
        
        #Plota o histograma de densidade com os parâmetros desejados
        plt.hist(df["IMC"], bins=50, density=True, histtype="step", alpha=0.6, color=cores[i], label=str(ano))

    #Personaliza o plot
    plt.subplot().set_facecolor("#373737")
    plt.xlim(0, 50)
    plt.xlabel("IMC")
    plt.ylabel("Densidade")
    plt.title("Distribuição do IMC ao longo dos anos")
    plt.grid(True, color="black")
    
    #Personaliza a legenda
    legenda_personalizada = [plt.Line2D([0], [0], color=cores[i], lw=2, label=str(ano)) for i, ano in enumerate(anos)]
    plt.legend(handles=legenda_personalizada)
    
    #Exibe o gráfico
    plt.show()
    return None

if __name__ == "__main__":
    doctest.testmod()