# mi_proyecto/mi_modulo/calculadora.py

import pandas as pd


class Calculadora:

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def cargar_datos_desde_csv(self, archivo_csv):
        df = pd.read_csv(archivo_csv)
        datos = list(df.itertuples(index=False, name=None))
        return datos

    def cargar_datos_desde_json(self, archivo_json):
        df = pd.read_json(archivo_json)
        datos = list(df.itertuples(index=False, name=None))
        return datos
