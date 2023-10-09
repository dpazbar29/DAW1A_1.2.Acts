import pytest
from src.dos_seis import * #2.6


#2.6
@pytest.mark.parametrize(
    "input_x,expected",
    [
      (10,9.0)
    ]
  )

def test_importeSinIva(input_x,expected):
    assert importeSinIva(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (9.0,"El importe sin IVA es: 9.0")
    ]
  )

def test_mensajeSalida6(input_x,expected):
    assert mensajeSalida6(input_x) == expected