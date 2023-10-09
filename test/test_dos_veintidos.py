import pytest 
from src.dos_veintidos import * #2.22

#2.22
@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      ("Buenas tardes","a","BuenAs tArdes")
    ]
)

def test_filtro22(input_x,input_y,expected):
     assert filtro22(input_x,input_y) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("BuenAs tArdes","La frase sera: BuenAs tArdes")
    ]
)

def test_mensajeSalida22(input_x,expected):
     assert mensajeSalida22(input_x) == expected