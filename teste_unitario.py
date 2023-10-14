import unittest
import pandas as pd
import funcoes_limpeza as fl

'''
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
'''

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





'''
print("Resultado:")
print(resultado)
print("Esperado:")
print(esperado)
'''

if __name__ == '__main__':
    unittest.main()






