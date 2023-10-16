"""
Módulo responsável por realizar os testes unitários das funções presentes no módulo "funcoes_limpeza".
"""

import os
import io
import sys
import unittest
import pandas as pd
from pasta_graficos.utilitarios.utils import *

# Testes Unitários para a função "limpa_PESO"
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

# Testes Unitários para a função "limpa_ALTURA":
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

# Testes Unitários para a função "limpa_SEXO"
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

# Testes Unitários para a função "limpa_ANO_NASCIMENTO"
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

# Testes Unitários para a função "renomeia_ESCOLARIDADE"
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

# Testes Unitários para a função "exclui_colunas"
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

# Testes Unitários para a função "nivel_ESCOLARIDADE"
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

# Testes Unitários para a função "gera_tabela_escolaridade"
class TestGeraTabelaEscolaridade(unittest.TestCase):
    def test_exemplo_valido(self):
        path_data = "../../pasta_dados/"
        ini_ano = 2018
        fim_ano = 2022
        path_save = "caminho_para_arquivo_de_teste.csv"

        gera_tabela_escolaridade(path_data, ini_ano, fim_ano, path_save)
        # Verifica se o arquivo de saída foi criado
        self.assertTrue(os.path.exists(path_save))
        # Limpa o arquivo de teste após o teste
        os.remove(path_save)  
    
    def test_exemplo_invalido(self):
        path_data = "../../pasta_dados/"
        ini_ano = 1997
        fim_ano = 2004
        path_save = "caminho_para_arquivo_de_teste.csv"

        # Captura a saída padrão (stdout)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        gera_tabela_escolaridade(path_data, ini_ano, fim_ano, path_save)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        # Verifica se a mensagem de erro esperada está na saída capturada
        self.assertIn("Erro de leitura no database do ano", output)
        

if __name__ == '__main__':
    unittest.main()






