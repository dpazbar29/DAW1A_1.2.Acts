import pytest 
from src.dos_dieciocho import * #2.18

#2.18
@pytest.mark.parametrize(
    "input_x,expected_m",
    [
      ("DaNIel pAZ bARROsO","DANIEL PAZ BARROSO")
    ]
  )

def test_mayusculas(input_x,expected_m):
     assert mayusculas(input_x) == expected_m

@pytest.mark.parametrize(
    "input_x,expected_minus",
    [
      ("DaNIel pAZ bARROsO","daniel paz barroso")
    ]
  )

def test_minusculas(input_x,expected_minus):
     assert minusculas(input_x) == expected_minus

@pytest.mark.parametrize(
    "input_x,expected_regl",
    [
      ("DaNIel pAZ bARROsO","Daniel Paz Barroso")
    ]
  )

def test_reglamentario(input_x,expected_regl):
     assert reglamentario(input_x) == expected_regl

@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
      ("DANIEL PAZ BARROSO","daniel paz barroso","Daniel Paz Barroso","El nombre en mayusculas: DANIEL PAZ BARROSO\nEl nombre en minusculas: daniel paz barroso\nEl nombre bien escrito: Daniel Paz Barroso")
    ]
)

def test_mensajeSalida18(input_x,input_y,input_z,expected):
     assert mensajeSalida18(input_x,input_y,input_z) == expected