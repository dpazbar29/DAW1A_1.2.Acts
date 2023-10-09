import pytest 
from src.dos_diecinueve import * #2.19

#2.19
@pytest.mark.parametrize(
     "input_x,expected",
     [
        ("dpazbar","DPAZBAR")
     ]
)

def test_mayusculasUser(input_x,expected):
     assert mayusculasUser(input_x) == expected

@pytest.mark.parametrize(
     "input_x,expected",
     [
        ("dpazbar",7)
     ]
)

def test_conteoUser(input_x,expected):
     assert contarUser(input_x) == expected

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
      ("DPAZBAR","7","El usuario DPAZBAR tiene un longitud de 7")
    ]
)

def test_mensajeSalida19(input_x,input_y,expected):
     assert mensajeSalida19(input_x,input_y) == expected