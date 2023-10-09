import pytest 
from src.dos_veintiseis import * #2.26


#2.26
@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("manzanas, peras, plátanos", ['manzanas', ' peras', ' plátanos'])
    ]
)

def test_filtro26(input_x,expected):
     assert filtro26(input_x) == expected