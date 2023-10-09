import pytest
from src.dos_cinco import * #2.5


#2.5
@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      (10,1.21,12.1),
      (10,1.10,11.0),
      (10,1.04,10.4)
    ]
  )

def test_calculoIva_params(input_x,input_y,expected):
    assert calculoIva(input_x,input_y) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (12.1,"El importe final es: 12.1"),
      (11.0,"El importe final es: 11.0"),
      (10.4,"El importe final es: 10.4")
    ]
  )

def test_mensajeSalida5(input_x,expected):
     assert mensajeSalida5(input_x) == expected