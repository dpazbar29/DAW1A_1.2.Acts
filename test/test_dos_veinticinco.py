import pytest 
from src.dos_veinticinco import * #2.25


#2.25
@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("29/01/2005","29")
    ]
)

def test_filtroDia(input_x,expected):
     assert filtroDia(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("29/01/2005","01")
    ]
)

def test_filtroMes(input_x,expected):
     assert filtroMes(input_x) == expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
      ("29/01/2005","2005")
    ]
)

def test_filtroAño(input_x,expected):
     assert filtroAño(input_x) == expected

@pytest.mark.parametrize(
    "input_x,input_y,input_z,input_s,expected",
    [
      ("29","01","2005","29/01/2005","Dia: 29\nMes: Enero\nAño: 2005"),
      ("9","1","2005","9/1/2005","Dia: 9\nMes: Enero\nAño: 2005")
    ]
)

def test_mensajeSalida25(input_x,input_y,input_z,input_s,expected):
     assert mensajeSalida25(input_x,input_y,input_z,input_s) == expected