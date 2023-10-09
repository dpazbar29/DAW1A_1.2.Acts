import pytest 
from src.dos_trece import * #2.13


#2.13
@pytest.mark.parametrize(
    "input_x,input_y,expected_x",
    [
      (9,4,2)
    ]
  )

def test_cocienteDiv(input_x,input_y,expected_x):
      assert cocienteDiv(input_x,input_y) == expected_x

@pytest.mark.parametrize(
    "input_x,input_y,expected_y",
    [
      (9,4,1)
    ]
  )

def test_restoDiv(input_x,input_y,expected_y):
      assert restoDiv(input_x,input_y) == expected_y

@pytest.mark.parametrize(
    "input_x,input_y,input_z,input_s,expected",
    [
      (9,4,1,2,"La división de 9 y 4, tiene de resto 1 y de cociente 2")
    ]
  )

def test_mensajeSalida13(input_x,input_y,input_z,input_s,expected):
      assert mensajeSalida13(input_x,input_y,input_z,input_s) == expected