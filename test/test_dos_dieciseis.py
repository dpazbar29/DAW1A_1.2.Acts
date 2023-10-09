import pytest 
from src.dos_dieciseis import * #2.16


#2.16
@pytest.mark.parametrize(
    "input_x,expected_1",
    [
      (5,10.47)
    ]
  )

def test_descuento(input_x,expected_1):
     assert descuento(input_x) == expected_1 

@pytest.mark.parametrize(
    "input_x,input_y,expected_2",
    [
      (5,10.47,6.98)
    ]
  )

def test_costeBarras(input_x,input_y,expected_2):
     assert costeBarras(input_x,input_y) == expected_2

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (6.98,"El precio final es: 6.98")
    ]
)

def test_mensajeSalida16(input_x,expected):
     assert mensajeSalida16(input_x) == expected