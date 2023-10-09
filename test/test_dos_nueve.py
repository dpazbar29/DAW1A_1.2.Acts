import pytest 
from src.dos_nueve import *  #2.9

#2.9
@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
      (1,1,1,3.0)
    ]
  )

def test_suma1(input_x,input_y,input_z,expected):
      assert suma1(input_x,input_y,input_z) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (3.0,"La suma es: 3.0")
    ]
  )

def test_mensajeSalida9(input_x,expected):
      assert mensajeSalida9(input_x) == expected