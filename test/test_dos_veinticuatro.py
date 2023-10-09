import pytest 
from src.dos_veinticuatro import * #2.24

#2.24
@pytest.mark.parametrize(
    "input_x,expected",
    [
      (15.23,15)
    ]
)

def test_euros(input_x,expected):
     assert euros(input_x) == expected

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      (15.23,15,23)
    ]
)

def test_centimos(input_x,input_y,expected):
     assert centimos(input_x,input_y) == expected

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      (15,23,"Euros: 15\nCentimos: 23")
    ]
)

def test_mensajeSalida24(input_x,input_y,expected):
     assert mensajeSalida24(input_x,input_y) == expected