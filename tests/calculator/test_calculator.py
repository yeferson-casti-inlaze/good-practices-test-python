# mi_proyecto/tests/test_calculadora.py

import pytest
from unittest.mock import patch
import pandas as pd
from io import StringIO
from calculator.calculator import Calculadora


@pytest.fixture
def calculadora():
    return Calculadora()


def test_suma(calculadora):
    assert calculadora.suma(1, 2) == 3
    assert calculadora.suma(-1, 1) == 0
    assert calculadora.suma(-1, -1) == -2


def test_resta(calculadora):
    assert calculadora.resta(2, 1) == 1
    assert calculadora.resta(1, 1) == 0
    assert calculadora.resta(1, 2) == -1


def test_multiplica(calculadora):
    assert calculadora.multiplica(2, 3) == 6
    assert calculadora.multiplica(-1, 3) == -3
    assert calculadora.multiplica(0, 3) == 0


def test_divide(calculadora):
    assert calculadora.divide(6, 3) == 2
    assert calculadora.divide(-6, 3) == -2

    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        calculadora.divide(1, 0)


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (1, 2, 3),  # suma
        (2, 1, 1),  # resta
        (2, 3, 6),  # multiplica
        (6, 3, 2),  # divide
    ],
)
def test_operaciones_parametrizadas(calculadora, a, b, esperado):
    assert (
        calculadora.suma(a, b) == esperado
        or calculadora.resta(a, b) == esperado
        or calculadora.multiplica(a, b) == esperado
        or calculadora.divide(a, b) == esperado
    )


# Mock para la carga de datos desde CSV con pandas
@pytest.fixture
def datos_mock():
    datos = "a,b\n1,2\n3,4\n5,6\n"
    return datos


def test_cargar_datos_desde_csv(calculadora, datos_mock):
    with patch("pandas.read_csv", return_value=pd.read_csv(StringIO(datos_mock))):
        datos = calculadora.cargar_datos_desde_csv("dummy.csv")
        assert datos == [(1, 2), (3, 4), (5, 6)]


# Pruebas adicionales a partir de los datos mockeados
def test_operaciones_con_datos_mock(calculadora, datos_mock):
    with patch("pandas.read_csv", return_value=pd.read_csv(StringIO(datos_mock))):
        datos = calculadora.cargar_datos_desde_csv("dummy.csv")

        for a, b in datos:
            assert calculadora.suma(a, b) == a + b
            assert calculadora.resta(a, b) == a - b
            assert calculadora.multiplica(a, b) == a * b
            if b != 0:
                assert calculadora.divide(a, b) == a / b
            else:
                with pytest.raises(ValueError, match="No se puede dividir por cero"):
                    calculadora.divide(a, b)


# Mock para la carga de datos desde JSON con pandas
@pytest.fixture
def datos_mock_json():
    datos = '[{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]'
    return datos


def test_cargar_datos_desde_json(calculadora, datos_mock_json):
    with patch(
        "pandas.read_json", return_value=pd.read_json(StringIO(datos_mock_json))
    ):
        datos = calculadora.cargar_datos_desde_json("dummy.json")
        assert datos == [(1, 2), (3, 4), (5, 6)]


# Pruebas adicionales a partir de los datos mockeados
def test_operaciones_con_datos_mock_json(calculadora, datos_mock_json):
    with patch(
        "pandas.read_json", return_value=pd.read_json(StringIO(datos_mock_json))
    ):
        datos = calculadora.cargar_datos_desde_json("dummy.json")

        for a, b in datos:
            assert calculadora.suma(a, b) == a + b
            assert calculadora.resta(a, b) == a - b
            assert calculadora.multiplica(a, b) == a * b
            if b != 0:
                assert calculadora.divide(a, b) == a / b
            else:
                with pytest.raises(ValueError, match="No se puede dividir por cero"):
                    calculadora.divide(a, b)
