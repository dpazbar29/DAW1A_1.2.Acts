import pytest 
from src.dos_tres import * #2.3

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (17,8.5)
    ]
)

def test_calculo1(input_x,expected):
     assert calculo1(input_x) == expected

@pytest.mark.parametrize(
    "input_x2,expected",
    [
      (17,8)
    ]
)

def test_calculo2(input_x2,expected):
     assert calculo2(input_x2) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (12.0,4.0)
    ]
)

def test_calculo3(input_x,expected):
     assert calculo3(input_x) == expected

@pytest.mark.parametrize(
    "expected",
    [
      (11)
    ]
)

def test_calculo4(expected):
     assert calculo4() == expected

@pytest.mark.parametrize(
    "input_x,input_y,input_z,input_s,expected",
    [
      ("8.5","8","4.0","11","8.5\n8\n4.0\n11")
    ]
)

def test_mensajeSalida3(input_x,input_y,input_z,input_s,expected):
     assert mensajeSalida3(input_x,input_y,input_z,input_s) == expected