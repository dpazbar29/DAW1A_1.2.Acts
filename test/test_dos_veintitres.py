import pytest 
from src.dos_veintitres import * #2.23


#2.23
@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("danielpazbar@gmail.com","danielpazbar")
    ]
)

def test_filtro23(input_x,expected):
     assert filtro23(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("danielpazbar","Su nuevo correo es: danielpazbar@ceu.es")
    ]
)

def test_mensajeSalida23(input_x,expected):
     assert mensajeSalida23(input_x) == expected