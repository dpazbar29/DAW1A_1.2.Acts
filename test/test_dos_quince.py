import pytest 
from src.dos_quince import * #2.15


#2.15
@pytest.mark.parametrize(
    "input_x,expected_1",
    [
      (5,5.2)
    ]
  )

def test_calculoInteres1(input_x,expected_1):
      assert calculoIntereses1(input_x) == expected_1

@pytest.mark.parametrize(
    "input_x,expected_2",
    [
      (5.2,5.41)
    ]
  )

def test_calculoInteres2(input_x,expected_2):
      assert calculoIntereses2(input_x) == expected_2

@pytest.mark.parametrize(
    "input_x,expected_3",
    [
      (5.41,5.63)
    ]
  )

def test_calculoInteres3(input_x,expected_3):
      assert calculoIntereses3(input_x) == expected_3

@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
      (5.2,5.41,5.63,"El saldo del anio uno sera 5.2, el saldo del anio dos sera 5.41, y el saldo del anio tres sera 5.63")
    ]
)

def test_mensajeSalida15(input_x,input_y,input_z,expected):
     assert mensajeSalida15(input_x,input_y,input_z) == expected