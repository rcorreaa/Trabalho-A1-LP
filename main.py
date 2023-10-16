from modulo_graficos.grafico_dispensa_bar_chart import plot_grafico_barras
from modulo_graficos.grafico_escolaridade_mapa import plot_grafico_mapa
from modulo_graficos.grafico_imc_hist import plot_grafico_histograma
from modulo_graficos.grafico_imc_violin import plot_grafico_violin

plot_grafico_histograma("data/", 2018, 2022)
plot_grafico_violin("data/", 2018, 2022)
plot_grafico_barras("data/")
plot_grafico_mapa(path_data="data/tabela_escolaridade.csv", path_geografia="data/BR_UF_2021.zip")