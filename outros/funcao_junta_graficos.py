import matplotlib.pyplot as plt
from grafico_dispensa_bar_chart import plot_grafico_barras
from grafico_dispensa_stacked_bar import plot_grafico_stacked_bar
import doctest

def combina_graficos(path_data, ini_ano=2018, fim_ano=2022, ax=None):
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    plot_grafico_barras(path_data, ini_ano, fim_ano, ax=axs[0])
    plot_grafico_stacked_bar(path_data, ini_ano, fim_ano, ax=axs[1])
    plt.tight_layout()
    plt.show()
    return axs

if __name__ == "__main__":
    doctest.testmod()

# Chamando a função para combinar os gráficos
combina_graficos("C:\\Users\\samue\\OneDrive\\Documentos\\Dados\\", 2018, 2022)