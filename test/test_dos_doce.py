import pytest 
from src.dos_doce import * #2.12


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      (121.43,1.93,32.6)
    ]
  )

def test_indiceMasa(input_x,input_y,expected):
      assert indiceMasa(input_x,input_y) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (32.6,"Tu IMC es: 32.6")
    ]
  )

def test_mensajeSalida12(input_x,expected):
      assert mensajeSalida12(input_x) == expected