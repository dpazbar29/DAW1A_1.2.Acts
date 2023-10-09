import pytest
from src.dos_catorce import * #2.14

#2.14
@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      (10,10,1.87)
    ]
  )

def test_calculadoraPesoPaquete(input_x,input_y,expected):
      assert calculadoraPesoPaquete(input_x,input_y) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (1.87, "El peso en kilogramos del paquete es: 1.87")
    ]
  )

def test_mensajeSalida14(input_x,expected):
      assert mensajeSalida14(input_x) == expected