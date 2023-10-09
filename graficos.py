import matplotlib.pyplot as plt
import numpy as np
import limpeza
def grafico1(caminho_csv):
    '''
    
    Args:
    caminho_csv: O caminho do arquivo CSV a ser lido.
    
    Returns:
    grafico: O histograma de frequência de acordo com a altura dos alistados.
    
    Exemplo:
    >>> caminho_arquivo = "dados.csv"
    >>> grafico = grafico1(caminho_arquivo)
    >>> plt.show()
    '''
    df = limpeza(caminho_csv)
    intervalos = np.arange(120,231,1)
    grafico = plt.hist(df["ALTURA"], intervalos, edgecolor = "black")
    grafico = plt.subplot().set_facecolor("#373737")
    grafico = plt.xlabel("Altura (cm)")
    grafico = plt.ylabel("Frequência")
    grafico = plt.title("Histograma das alturas")
    return grafico

def grafico2(caminho_csv):
    '''
    
    Args:
    caminho_csv: O caminho do arquivo CSV a ser lido.
    
    Returns:
    grafico: O histograma de densidade de acordo com a altura dos indivíduos sem dispensa.
    
    Exemplo:
    >>> caminho_arquivo = "dados.csv"
    >>> grafico = grafico2(caminho_arquivo)
    >>> plt.show()
    '''
    df = limpeza(caminho_csv)
    df_sem_dispensa = df[df["DISPENSA"] == "Sem dispensa"]
    df_altura_sem_dispensa = df_sem_dispensa[["ALTURA"]]
    grafico = plt.hist(df_altura_sem_dispensa, 100, density = True, edgecolor = "black")
    grafico = plt.subplot().set_facecolor("#373737")
    grafico = plt.xlabel("Altura (cm)")
    grafico = plt.ylabel("Probabilidade de não obter dispensa")
    grafico = plt.title("Probabilidade de não obter dispensa de acordo com a altura")
    return grafico

def grafico3(caminho_csv):
    '''
    
    Args:
    caminho_csv: O caminho do arquivo CSV a ser lido.
    
    Returns:
    grafico: O histograma de densidade de acordo com o Índice de Massa Corporal (IMC) dos indivíduos sem dispensa.
    
    Exemplo:
    >>> caminho_arquivo = "dados.csv"
    >>> grafico = grafico3(caminho_arquivo)
    >>> plt.show()
    '''
    df = limpeza(caminho_csv)
    df["IMC"]=10000*df["PESO"]/df["ALTURA"]**2
    df_sem_dispensa = df[df["DISPENSA"] == "Sem dispensa"]
    df_imc_sem_dispensa = df_sem_dispensa[["IMC"]]
    grafico = plt.hist(df_imc_sem_dispensa, len(df_imc_sem_dispensa["IMC"].unique()), density = True)
    grafico = plt.subplot().set_facecolor("#373737")
    grafico = plt.xlabel("Índice de Massa Corporal")
    grafico = plt.ylabel("Probabilidade de não obter dispensa")
    grafico = plt.title("Probabilidade de não obter dispensa de acordo com o IMC")
    grafico = plt.ylim(0,0.5)
    return grafico

def grafico4(caminho_csv):
    '''
    
    Args:
    caminho_csv: O caminho do arquivo CSV a ser lido.
    
    Returns:
    grafico: O histograma de densidade de acordo com o peso (em quilogramas) dos indivíduos sem dispensa.
    
    Exemplo:
    >>> caminho_arquivo = "dados.csv"
    >>> grafico = grafico4(caminho_arquivo)
    >>> plt.show()
    '''
    df = limpeza(caminho_csv)
    df_sem_dispensa = df[df["DISPENSA"] == "Sem dispensa"]
    df_peso_sem_dispensa = df_sem_dispensa[["PESO"]]
    grafico = plt.hist(df_peso_sem_dispensa, 100, density = True, edgecolor = "black")
    grafico = plt.subplot().set_facecolor("#373737")
    grafico = plt.xlabel("Peso (kg)")
    grafico = plt.ylabel("Probabilidade de não obter dispensa")
    grafico = plt.title("Probabilidade de não obter dispensa de acordo com o peso")
    return grafico