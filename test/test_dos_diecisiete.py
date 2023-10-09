import pytest 
from src.dos_diecisiete import * #2.17


#2.17
@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("dani \n" * 3,"dani \n"*3)
    ]
  )

def test_impresionUsuario(input_x,expected):
     assert impresionUsuario(input_x) == expected