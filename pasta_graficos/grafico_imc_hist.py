import matplotlib.pyplot as plt
import pandas as pd
from ..pasta_funcoes.funcoes_limpeza import limpa_PESO, limpa_ALTURA, limpa_ANO_NASCIMENTO, limpa_SEXO
import doctest

def plot_grafico_histograma(path_data = "C:/Users/ramyr/LinguagensDeProgramação", ano1=2010, ano2=2014, ano3=2014, ano4=2022):
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
    
    Exemplos:
    Exemplo válido, em que os caminhos dos arquivos são passados da maneira correta e contém os dataframes desejados.
    >>> plot_grafico_histograma(path_data= "C:/Users/ramyr/LinguagensDeProgramação", ano1 = 2010, ano2 = 2014, ano3 = 2018, ano4 = 2022)
    2010
    count    320684.000000
    mean         22.648520
    std           3.374236
    min          11.317338
    25%          20.415225
    50%          22.145329
    75%          24.280264
    max          86.224490
    Name: IMC, dtype: float64
    2014
    count    329817.000000
    mean         23.050449
    std           3.687635
    min          10.738543
    25%          20.549887
    50%          22.491349
    75%          24.857955
    max          93.877551
    Name: IMC, dtype: float64
    2018
    count    283923.000000
    mean         23.065879
    std           3.918558
    min          10.306888
    25%          20.571429
    50%          22.309356
    75%          24.691358
    max          91.836735
    Name: IMC, dtype: float64
    2022
    count    278007.000000
    mean         22.985457
    std           4.307939
    min          11.680010
    25%          20.069204
    50%          22.038567
    75%          24.784258
    max          83.999799
    Name: IMC, dtype: float64
    
    Exemplo inválido, em que o caminho do Dataframe não contém os dataframes desejados.
    >>> plot_grafico_histograma(path_data="caminho_dataframes_sem_df_2010", ano1 = 2010, ano2 = 2014, ano3 = 2018, ano4 = 2022)
    Erro de leitura no database do ano 2010
    
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
<<<<<<< HEAD:grafico_imc_hist.py
            print("Erro de leitura no database do ano", ano)
=======
            print("Erro de leitura do database do ano", ano)
>>>>>>> b1463649388145b0e71fe02436dbc543c993e49b:pasta_graficos/grafico_imc_hist.py
            return
        
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
