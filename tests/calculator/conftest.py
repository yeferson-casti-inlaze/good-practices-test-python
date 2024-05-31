import pytest
from calculator.calculator import Calculadora


@pytest.fixture
def calculator():
    return Calculadora()


@pytest.fixture
def data_mock_csv():
    datos = "a,b\n1,2\n3,4\n5,6\n"
    return datos


@pytest.fixture
def data_mock_json():
    datos = '[{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]'
    return datos
