# mi_proyecto/tests/test_calculadora.py

import pytest
from calc.calculadora import Calculadora


# Mejor práctica 1: Usar fixtures para la configuración de objetos comunes
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

    # Mejor práctica 2: Probar excepciones
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        calculadora.divide(1, 0)


# Mejor práctica 3: Pruebas parametrizadas para reducir código repetitivo
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
