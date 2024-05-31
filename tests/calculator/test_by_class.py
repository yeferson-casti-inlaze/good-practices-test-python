import pytest
from unittest.mock import patch
import pandas as pd
from io import StringIO


class TestByClass:

    @pytest.fixture(autouse=True)
    def setup(self, calculator, data_mock_csv, data_mock_json):
        self.calculator = calculator
        self.data_mock_csv = data_mock_csv
        self.data_mock_json = data_mock_json

    @pytest.mark.arithmetic
    def test_suma(self):
        assert self.calculator.suma(1, 2) == 3
        assert self.calculator.suma(-1, 1) == 0
        assert self.calculator.suma(-1, -1) == -2

    @pytest.mark.arithmetic
    def test_resta(self):
        assert self.calculator.resta(2, 1) == 1
        assert self.calculator.resta(1, 1) == 0
        assert self.calculator.resta(1, 2) == -1

    @pytest.mark.arithmetic
    def test_multiplica(self):
        assert self.calculator.multiplica(2, 3) == 6
        assert self.calculator.multiplica(-1, 3) == -3
        assert self.calculator.multiplica(0, 3) == 0

    @pytest.mark.arithmetic
    def test_divide(self):
        assert self.calculator.divide(6, 3) == 2
        assert self.calculator.divide(-6, 3) == -2

        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            self.calculator.divide(1, 0)

    @pytest.mark.parametrize(
        "num_1, num_2, result",
        [
            (1, 2, 3),  # suma
            (2, 1, 1),  # resta
            (2, 3, 6),  # multiplica
            (6, 3, 2),  # divide
        ],
    )
    @pytest.mark.arithmetic
    def test_operaciones_parametrizadas(self, num_1, num_2, result):
        assert (
            self.calculator.suma(num_1, num_2) == result
            or self.calculator.resta(num_1, num_2) == result
            or self.calculator.multiplica(num_1, num_2) == result
            or self.calculator.divide(num_1, num_2) == result
        )

    @pytest.mark.csv
    def read_mocks_csv(self):
        with patch(
            "pandas.read_csv", return_value=pd.read_csv(StringIO(self.data_mock_csv))
        ):
            return self.calculator.cargar_datos_desde_csv("dummy.csv")

    @pytest.mark.csv
    def test_cargar_datos_desde_csv(self):
        data = self.read_mocks_csv()
        assert data == [(1, 2), (3, 4), (5, 6)]

    @pytest.mark.csv
    @pytest.mark.json
    def realizar_operaciones_y_validaciones(self, datos):
        for a, b in datos:
            assert self.calculator.suma(a, b) == a + b
            assert self.calculator.resta(a, b) == a - b
            assert self.calculator.multiplica(a, b) == a * b
            if b != 0:
                assert self.calculator.divide(a, b) == a / b
            else:
                with pytest.raises(ValueError, match="No se puede dividir por cero"):
                    self.calculator.divide(a, b)

    @pytest.mark.csv
    def test_operaciones_con_datos_mock(self, calculator, data_mock_csv):
        data = self.read_mocks_csv()
        self.realizar_operaciones_y_validaciones(data)

    @pytest.mark.json
    def read_mocks_json(self):
        with patch(
            "pandas.read_json", return_value=pd.read_json(StringIO(self.data_mock_json))
        ):
            return self.calculator.cargar_datos_desde_json("dummy.json")

    @pytest.mark.json
    def test_cargar_datos_desde_json(self):
        data = self.read_mocks_json()
        assert data == [(1, 2), (3, 4), (5, 6)]

    @pytest.mark.json
    def test_operaciones_con_datos_mock_json(self):
        data = self.read_mocks_json()
        self.realizar_operaciones_y_validaciones(data)
