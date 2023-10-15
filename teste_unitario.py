import unittest
import pandas as pd
import funcoes_limpeza as fl
import os
from grafico_escolaridade_mapa import plot_grafico_mapa

# Testes unitários para funcoes_limpeza:
class TestLimpaPESO(unittest.TestCase):

    def test_dados_validos(self):
        df = pd.DataFrame({"PESO": [100, 101, 210, 35]})
        resultado = fl.limpa_PESO(df)
        esperado = pd.DataFrame({"PESO": [100, 101]})
        self.assertTrue(resultado.equals(esperado))

    def test_dados_nulos(self):
        df = pd.DataFrame({"PESO": [pd.NA, 120, 40]})
        resultado = fl.limpa_PESO(df)
        esperado = pd.DataFrame({"PESO": [120.0, 40.0]}, index=[1, 2])
        self.assertTrue(resultado.equals(esperado))    

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"ALTURA": [180, 179, 210, 167]})
        with self.assertRaises(KeyError):
            fl.limpa_PESO(df)

    def test_valores_nao_numericos(self):
        df = pd.DataFrame({"PESO": [200, "120 kg", 40, 230]})
        with self.assertRaises(TypeError):
            fl.limpa_PESO(df)


class TestLimpaALTURA(unittest.TestCase):
    
    def test_dados_validos(self):
        df = pd.DataFrame({"ALTURA": [180, 121, 210, 200]})
        resultado = fl.limpa_ALTURA(df)
        esperado = pd.DataFrame({"ALTURA": [180, 210, 200]}, index = [0, 2, 3])
        self.assertTrue(resultado.equals(esperado))

    def test_dados_nulos(self):
        df = pd.DataFrame({"ALTURA": [pd.NA, 120, 150, 180]})
        resultado = fl.limpa_ALTURA(df)
        esperado = pd.DataFrame({"ALTURA": [150.0, 180.0]}, index = [2, 3])
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"PESO": [180, 179, 210, 167]})
        with self.assertRaises(KeyError):
            fl.limpa_ALTURA(df)

    def test_valores_nao_numericos(self):
        df = pd.DataFrame({"ALTURA": [200, "179 cm", 140, 230]})
        with self.assertRaises(TypeError):
            fl.limpa_ALTURA(df)


class TestLimpaSEXO(unittest.TestCase):
    def test_dados_validos(self):
        df = pd.DataFrame({"SEXO": ["M", "M", "F", "M"]})
        resultado = fl.limpa_SEXO(df)
        esperado = pd.DataFrame({"SEXO": ["M", "M", "M"]}, index = [0, 1, 3])
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"PESO": [pd.NA, 120, 40, 230]})
        with self.assertRaises(KeyError):
            fl.limpa_SEXO(df)


class TestLimpaANO_NASCIMENTO(unittest.TestCase):
    def test_idade_correta(self):
        df = pd.DataFrame({"ANO_NASCIMENTO": [2004, 2003, 2005, 2000]})
        resultado = fl.limpa_ANO_NASCIMENTO(df, 2022)
        esperado = pd.DataFrame({"ANO_NASCIMENTO": [2004, 2003]})
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"PESO": [pd.NA, 120, 40, 230]})
        with self.assertRaises(KeyError):
            fl.limpa_ANO_NASCIMENTO(df, 2019)


class TestRenomeiaESCOLARIDADE(unittest.TestCase):
    def test_renomeia_categorias(self):
        df = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Superior", "Mestrado", "Ensino Fundamental", "Doutorado"]})
        resultado = fl.renomeia_ESCOLARIDADE(df)
        esperado = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Superior", "Pós-graduação", "Ensino Fundamental", "Pós-graduação"]})
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"OUTRA_COLUNA": [1, 2, 3]})
        with self.assertRaises(KeyError):
            fl.renomeia_ESCOLARIDADE(df)

    def test_coluna_completa(self):
        df = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Fundamental Completo", "Doutorado Completo"]})
        resultado = fl.renomeia_ESCOLARIDADE(df)
        esperado = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio Completo", "Ensino Fundamental Completo", "Doutorado Completo"]})
        self.assertTrue(resultado.equals(esperado))


class TestExcluiColunas(unittest.TestCase):
    def test_exclui_colunas(self):
        df = pd.DataFrame({"coluna_1": [1, 2, 3], "coluna_2": [4, 5, 6]})
        resultado = fl.exclui_colunas(df, ["coluna_1"])
        esperado = pd.DataFrame({"coluna_2": [4, 5, 6]})
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"coluna_1": [1, 2, 3], "coluna_2": [4, 5, 6]})
        resultado = fl.exclui_colunas(df, ["coluna_3"])
        self.assertTrue(resultado.equals(df))        


class TestNivelESCOLARIDADE(unittest.TestCase):
    def test_nivel_escolaridade(self):
        df = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio", "Alfabetizado"]})
        resultado = fl.nivel_ESCOLARIDADE(df)
        esperado = pd.DataFrame({"ESCOLARIDADE": ["Ensino Médio", "Alfabetizado"], "NIVEL_ESCOLARIDADE": [5, 1]})
        self.assertTrue(resultado.equals(esperado))

    def test_coluna_inexistente(self):
        df = pd.DataFrame({"PESO": [100, 85, 115, 79], "ALTURA": [180, 169, 120, 240]})
        resultado = fl.nivel_ESCOLARIDADE(df)
        self.assertTrue(resultado.equals(df))


class TestGeraTabelaEscolaridade(unittest.TestCase):
    def test_gera_tabela_escolaridade(self):
        # Executa a função para gerar a tabela de escolaridade
        fl.gera_tabela_escolaridade()

        # Verifica se o arquivo CSV foi gerado
        self.assertTrue(os.path.isfile("tabela_escolaridade.csv"))

        # Verifica se o arquivo CSV possui os cabeçalhos esperados
        df = pd.read_csv("tabela_escolaridade.csv")
        self.assertIn("UF_RESIDENCIA", df.columns)
        self.assertIn("NIVEL_ESCOLARIDADE", df.columns)



# Testes unitários para as funções de gráficos:



'''
print("Resultado:")
print(resultado)
print("Esperado:")
print(esperado)
'''

if __name__ == '__main__':
    unittest.main()






