import datetime

from person.main import Persona


class TestPersona:
    def test_constructor(self):

        persona = Persona(nombre="Diego", edad=25)

        assert persona.dar_nombre() == "Diego"

        assert persona.dar_edad() == 25

    def test_asingacion(self):
        persona = Persona(nombre="Diego", edad=25)
        persona.asignar_edad(28)
        persona.asignar_nombre("Adriana")
        assert persona.dar_nombre() != "Diego"
        assert persona.dar_edad() != 25
        assert persona.dar_nombre() == "Adriana"
        assert persona.dar_edad() == 28

    def test_contiene_texto(self):
        persona = Persona(nombre="María Alejandra", edad=22)
        assert "Alejandra" in persona.dar_nombre()

    def test_anio_nacimiento(self):
        persona = Persona(nombre="María Alejandra", edad=22)
        assert (
            persona.calcular_anio_nacimiento(True) == datetime.datetime.now().year - 22
        )
        assert (
            persona.calcular_anio_nacimiento(False)
            == datetime.datetime.now().year - 22 + 1
        )
