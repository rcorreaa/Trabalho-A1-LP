import unittest
import pandas as pd
import sys
import os

sys.path.append("C:/Users/samue/Repositorios_git/")
df = pd.read_csv("C:/Users/samue/Repositorios_git/Trabalho_A1_LP/pasta_dados/tabela_escolaridade.csv")

from Trabalho_A1_LP.pasta_funcoes.funcoes_limpeza import *
from Trabalho_A1_LP.pasta_graficos.grafico_escolaridade_mapa import plot_grafico_mapa
from Trabalho_A1_LP.pasta_graficos.grafico_dispensa_bar_chart import plot_grafico_barras
from Trabalho_A1_LP.pasta_graficos.grafico_dispensa_stacked_bar import plot_grafico_stacked_bar
from Trabalho_A1_LP.pasta_graficos.grafico_imc_hist import plot_grafico_histograma
from Trabalho_A1_LP.pasta_graficos.grafico_imc_violin import plot_grafico_violin

# Testes unitários para funcoes_limpeza:

class TestLimpaPESO(unittest.TestCase):

    def test_dados_validos(self):
        df = pd.DataFrame({"PESO": [100, 101, 210, 35]})
        resultado = limpa_PESO(df)
        esperado = pd.DataFrame({"PESO": [100, 101]})
        self.assertTrue(resultado.equals(esperado))

    def test_dados_nulos(self):
        df = pd.DataFrame({"PESO": [pd.NA, 120, 40]})
        resultado = limpa_PESO(df)
        esperado = pd.DataFrame({"PESO": [120.0, 40.0]}, index=[1, 2])
        self.assertTrue(resultado.equals(esperado))    

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"ALTURA": [180, 179, 210, 167]})
        with self.assertRaises(KeyError):
            limpa_PESO(df)

    def test_valores_nao_numericos(self):
        df = pd.DataFrame({"PESO": [200, "120 kg", 40, 230]})
        with self.assertRaises(TypeError):
            limpa_PESO(df)


class TestLimpaALTURA(unittest.TestCase):
    
    def test_dados_validos(self):
        df = pd.DataFrame({"ALTURA": [180, 121, 210, 200]})
        resultado = limpa_ALTURA(df)
        esperado = pd.DataFrame({"ALTURA": [180, 210, 200]}, index = [0, 2, 3])
        self.assertTrue(resultado.equals(esperado))

    def test_dados_nulos(self):
        df = pd.DataFrame({"ALTURA": [pd.NA, 120, 150, 180]})
        resultado = limpa_ALTURA(df)
        esperado = pd.DataFrame({"ALTURA": [150.0, 180.0]}, index = [2, 3])
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"PESO": [180, 179, 210, 167]})
        with self.assertRaises(KeyError):
            limpa_ALTURA(df)

    def test_valores_nao_numericos(self):
        df = pd.DataFrame({"ALTURA": [200, "179 cm", 140, 230]})
        with self.assertRaises(TypeError):
            limpa_ALTURA(df)


class TestLimpaSEXO(unittest.TestCase):
    def test_dados_validos(self):
        df = pd.DataFrame({"SEXO": ["M", "M", "F", "M"]})
        resultado = limpa_SEXO(df)
        esperado = pd.DataFrame({"SEXO": ["M", "M", "M"]}, index = [0, 1, 3])
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"PESO": [pd.NA, 120, 40, 230]})
        with self.assertRaises(KeyError):
            limpa_SEXO(df)


class TestLimpaANO_NASCIMENTO(unittest.TestCase):
    def test_idade_correta(self):
        df = pd.DataFrame({"ANO_NASCIMENTO": [2004, 2003, 2005, 2000]})
        resultado = limpa_ANO_NASCIMENTO(df, 2022)
        esperado = pd.DataFrame({"ANO_NASCIMENTO": [2004, 2003]})
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"PESO": [pd.NA, 120, 40, 230]})
        with self.assertRaises(KeyError):
            limpa_ANO_NASCIMENTO(df, 2019)


class TestRenomeiaESCOLARIDADE(unittest.TestCase):
    def test_renomeia_categorias(self):
        df = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Superior", "Mestrado", "Ensino Fundamental", "Doutorado"]})
        resultado = renomeia_ESCOLARIDADE(df)
        esperado = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Superior", "Pós-graduação", "Ensino Fundamental", "Pós-graduação"]})
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"OUTRA_COLUNA": [1, 2, 3]})
        with self.assertRaises(KeyError):
            renomeia_ESCOLARIDADE(df)

    def test_coluna_completa(self):
        df = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Fundamental Completo", "Doutorado Completo"]})
        resultado = renomeia_ESCOLARIDADE(df)
        esperado = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Fundamental Completo", "Doutorado Completo"]})
        self.assertTrue(resultado.equals(esperado))


class TestExcluiColunas(unittest.TestCase):
    def test_exclui_colunas(self):
        df = pd.DataFrame({"coluna_1": [1, 2, 3], "coluna_2": [4, 5, 6]})
        resultado = exclui_colunas(df, ["coluna_1"])
        esperado = pd.DataFrame({"coluna_2": [4, 5, 6]})
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"coluna_1": [1, 2, 3], "coluna_2": [4, 5, 6]})
        resultado = exclui_colunas(df, ["coluna_3"])
        self.assertTrue(resultado.equals(df))        


class TestNivelESCOLARIDADE(unittest.TestCase):
    def test_nivel_escolaridade(self):
        df = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio", "Alfabetizado"]})
        resultado = nivel_ESCOLARIDADE(df)
        esperado = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio", "Alfabetizado"], "NIVEL_ESCOLARIDADE": [5, 1]})
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"PESO": [100, 85, 115, 79], "ALTURA": [180, 169, 120, 240]})
        resultado = nivel_ESCOLARIDADE(df)
        self.assertTrue(resultado.equals(df))


class TestGeraTabelaEscolaridade(unittest.TestCase):
    def test_gera_tabela_escolaridade(self):
        # Executa a função para gerar a tabela de escolaridade
        gera_tabela_escolaridade()

        # Verifica se o arquivo CSV foi gerado
        self.assertTrue(os.path.isfile("C:/Users/samue/Repositorios_git/Trabalho_A1_LP/pasta_dados/tabela_escolaridade.csv"))

        # Verifica se o arquivo CSV possui os cabeçalhos esperados
        df = pd.read_csv("C:/Users/samue/Repositorios_git/Trabalho_A1_LP/pasta_dados/tabela_escolaridade.csv")
        self.assertIn("UF_RESIDENCIA", df.columns)
        self.assertIn("NIVEL_ESCOLARIDADE", df.columns)


# Testes unitários para as funções de gráficos:

class TestPlotGraficoMapa(unittest.TestCase):

    def test_caminho_correto(self):
        # Verifica se a função executa sem erros quando os caminhos corretos são fornecidos
        path_data = "tabela_escolaridade.csv"
        path_geografia = "BR_UF_2021.zip"
        self.assertIsNone(plot_grafico_mapa(path_data, path_geografia))

    def test_caminho_dataframes_errado(self):
        # Verifica se a função lida corretamente com caminhos de DataFrames errados
        path_data = "caminho_dataframes_errado"
        path_geografia = "BR_UF_2021.zip"
        self.assertIsNone(plot_grafico_mapa(path_data, path_geografia))

    def test_caminho_geografia_errado(self):
        # Verifica se a função lida corretamente com caminhos de geografia errados
        path_data = "tabela_escolaridade.csv"
        path_geografia = "caminho_brasil_errado"
        self.assertIsNone(plot_grafico_mapa(path_data, path_geografia))

'''
print("Resultado:")
print(resultado)
print("Esperado:")
print(esperado)
'''

if __name__ == '__main__':
    unittest.main()






