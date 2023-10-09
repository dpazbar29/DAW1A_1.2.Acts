import pytest 
from src.dos_veinte import * #2.20

#2.20
@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("+34-664714939-54","664714939")
    ]

)

def test_filtro(input_x,expected):
     assert filtro(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("664714939","El numero de telefono integro es: 664714939")
    ]
)

def test_mensajeSalida20(input_x,expected):
     assert mensajeSalida20(input_x) == expected