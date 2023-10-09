#2.23 pide correo electronico y cambia el dominio por @ceu.es

def filtro23(correo:str) -> str:
    '''fraccionamos el correo para obtener la parte buena'''

    partes = correo.split("@")

    return partes[0]

def mensajeSalida23(filtrado:str) -> str:

    return "Su nuevo correo es: " + str(filtrado) + "@ceu.es"


if __name__ == "__main__": 

    #leemos
    correo = str(input("Introduzca su correo electronico: "))

    #proceso
    filtrado = filtro23(correo)
    mensaje_salida = mensajeSalida23(filtrado)

    #devolvemos
    print(mensaje_salida)