import pytest 
from src.dos_once import * #2.11

#2.11
@pytest.mark.parametrize(
    "input_x,expected",
    [
      (5,15)
    ]
  )

def test_pedir(input_x,expected):
      assert pedir(input_x) == expected

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      (15,5,"La suma de los numeros desde 1 hasta 5 es 15")
    ]
  )

def test_mensajeSalida11(input_x,input_y,expected):
      assert mensajeSalida11(input_x,input_y) == expected