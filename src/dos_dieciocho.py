#2.18 pide el nombre e imprimelo 3 veces,una en mayusculas otra en minisculas y una con la primera de nombre y apellidos en mayuscula

def mayusculas(nombre:str) -> str:
    '''nombre en mayusculas'''

    return nombre.upper()


def minusculas(nombre:str) -> str:
    '''nombre en minusculas'''

    return nombre.lower()


def reglamentario(nombre:str) -> str:
    '''nombre escrito correctamente'''

    return nombre.title()

def mensajeSalida18(mayus,minus,regl):
    '''mensaje a devolver'''

    return "El nombre en mayusculas: " + str(mayus) + "\nEl nombre en minusculas: " + str(minus) + "\nEl nombre bien escrito: " + str(regl)

if __name__ == "__main__":

    #leemos
    nombre = str(input("Escriba su nombre completo: "))

    #proceso
    mayus = mayusculas(nombre)
    minus = minusculas(nombre)
    regl = reglamentario(nombre)
    mensaje_salida = mensajeSalida18(mayus,minus,regl)

    #devolvemos
    print(mensaje_salida)