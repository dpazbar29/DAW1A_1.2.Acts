import pytest
from src.dos_dos import *

#2.2
@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      (10,10,100)
    ]
  )

def test_horas_trabajo_params(input_x,input_y,expected):
    assert horas_trabajo(input_x,input_y) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
         (100,"Cobra: 100")
    ]
)

def test_mensaje_salida2(input_x,expected):
     assert mensaje_salida2(input_x)  == expected
