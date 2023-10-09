import pytest
from src.dos_siete import *  #2.7


#2.7
@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
      (2,2,2,6),
      (8.5,2.25,1.25,12)
    ]
  )

def test_suma3(input_x,input_y,input_z,expected):
      assert suma3(input_x,input_y,input_z) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (6.0,"El resultado de la suma es: 6.0"),
      (12.0,"El resultado de la suma es: 12.0")
    ]
  )

def test_mensajeSalida7(input_x,expected):
      assert mensajeSalida7(input_x) == expected

