import pytest 
from src.dos_ocho import *  #2.8

#2.8   
@pytest.mark.parametrize(
    "expected",
    [
      (6)
    ]
  )

def test_suma2(expected):
    assert suma2(expected) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (6,"La suma es: 6")
    ]
  )

def test_mensajeSalida8(input_x,expected):
    assert mensajeSalida8(input_x) == expected