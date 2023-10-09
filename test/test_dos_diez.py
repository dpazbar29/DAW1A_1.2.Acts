import pytest
from src.dos_diez  import * #2.10


#2.10
def test_operacion():
      assert operacion() == 0.25

@pytest.mark.parametrize(
    "input_x,expected",
    [
      (0.25,"El resultado de ((3+2)/2*5)^2 es: 0.25")
    ]
)

def test_mensajeSalida10(input_x,expected):
     assert mensajeSalida10(input_x) == expected