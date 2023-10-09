import pytest 
from src.dos_veintisiete import * #2.27


#2.27
@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      (4.54,3,13.62)
    ]
)

def test_calculoCoste(input_x,input_y,expected):
  assert calculoCoste(input_x,input_y) == expected 

@pytest.mark.parametrize(
    "input_x,input_y,input_z,input_s,expected",
    [
      ("pan",4.54,3,13.62,"pan - 00004.54 - 003 - 00013.62")
    ]
)

def test_cadenaFinal(input_x,input_y,input_z,input_s,expected):
  assert cadenaFinal(input_x,input_y,input_z,input_s) == expected 

@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("pan - 00004.54 - 003 - 00013.62","Resultado final: pan - 00004.54 - 003 - 00013.62")
    ]
)

def test_mensajeSalida27(input_x,expected):
     assert mensajeSalida27(input_x) == expected