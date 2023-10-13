import matplotlib.pyplot as plt
import pandas as pd
from funcoes_limpeza import limpa_PESO, limpa_ALTURA, limpa_ANO_NASCIMENTO

def histograma():
    '''
    
    Args:
    
    
    Returns:
    
    '''
    
    for ano in range(2017, 2022+1):
        try:
            df = pd.read_csv("../sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"])
        except UnicodeDecodeError:
            df = pd.read_csv("../sermil{}.csv".format(ano), usecols=["PESO", "ALTURA", "SEXO", "ANO_NASCIMENTO"], encoding="latin1")
        except:
            print("Erro de leitura do database")
            continue
        df = limpa_PESO(df)
        df = limpa_ALTURA(df)
        df = limpa_ANO_NASCIMENTO(df, ano)
        df["IMC"]=10000*df["PESO"]/df["ALTURA"]**2
        plt.hist(df["IMC"], len(df["IMC"].unique()), density = True)
        plt.subplot().set_facecolor("#373737")
        plt.xlabel("Índice de Massa Corporal")
        plt.ylabel("Densidade")
        plt.title(f"IMC dos alistados no ano de {ano}")
        plt.xlim(0,50)
        plt.ylim(0,0.8)
        plt.show()
        
    
histograma()