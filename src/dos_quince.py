#2.15 Lee la cantidad de dinero que entr en la cuenta,luego mostrar lo ahorrado tras 1,2 y 3 años

def calculoIntereses1(deposito:float) -> float:
    '''calculo del saldo en cuenta tras 1 año'''
    
    return round(deposito * (1 + 0.04),2)

def calculoIntereses2(saldo_año_1:float) -> float:
    '''calculo del saldo en cuenta tras 2 años'''

    return round(saldo_año_1 * (1 + 0.04),2)

def calculoIntereses3(saldo_año_2:float) -> float:
    '''calculo del saldo en cuenta tras 3 años'''

    return round(saldo_año_2 * (1 + 0.04),2)

def mensajeSalida15(saldo_año_1:float,saldo_año_2:float,saldo_año_3:float) -> str:

    return "El saldo del anio uno sera " + str(saldo_año_1) + ", el saldo del anio dos sera " + str(saldo_año_2) + ", y el saldo del anio tres sera " + str(saldo_año_3)

if __name__ == "__main__":

    #leemos
    deposito = float(input("Ingresa la cantidad de dinero depositado: "))

    #proceso
    saldo_año_1 = calculoIntereses1(deposito)
    saldo_año_2 = calculoIntereses2(saldo_año_1)
    saldo_año_3 = calculoIntereses3(saldo_año_2)
    mensaje_salida = mensajeSalida15(saldo_año_1,saldo_año_2,saldo_año_3)

    #devolvemos
    print(mensaje_salida)