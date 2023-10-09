def calculo1(ancho:int) -> str:

    return ancho / 2

def calculo2(ancho:int) -> str:

    return ancho // 2

def calculo3(alto:float) -> str:

    return alto / 3

def calculo4() -> str:

    return 1 + 2 * 5

def mensajeSalida3(c1:str,c2:str,c3:str,c4:str) -> str:

    return str(c1) + "\n" + str(c2) + "\n" + str(c3) + "\n" + str(c4)

if __name__ == "__main__":

    #leemos
    '''no hay lectura son valores fijos'''
    ancho = int(17)
    alto = float(12.0)

    #proceso
    c1 = calculo1(ancho)
    c2 = calculo2(ancho)
    c3 = calculo3(alto)
    c4 = calculo4()
    mensaje_salida = mensajeSalida3(c1,c2,c3,c4)

    #devolvemos
    print(mensaje_salida)