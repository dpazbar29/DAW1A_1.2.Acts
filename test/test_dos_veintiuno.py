import pytest 
from src.dos_veintiuno import * #2.21


#2.21
@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("Buenas tardes","sedrat saneuB")
    ]
)

def test_darVuelta(input_x,expected):
     assert darVuelta(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("sedrat saneuB","La frase invertida es: sedrat saneuB")
    ]
)

def test_mensajeSalida21(input_x,expected):
     assert mensajeSalida21(input_x) == expected