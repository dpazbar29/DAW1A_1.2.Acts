import pytest
from src.dos_cuatro import * #2.4


#2.4
@pytest.mark.parametrize(
    "input_x,expected",
    [
      (10,50.0)
    ]
  )

def test_conversor_params(input_x,expected):
    assert conversor(input_x) == expected
  
@pytest.mark.parametrize(
    "input_x,expected",
    [
      (50.0,"La temperatura en F es: 50.0")
    ]
  )

def test_mensajeSalida4(input_x,expected):
    assert mensajeSalida4(input_x) == expected