#2.17 Pide un nombre de usuario y un numero entero y ,¡muestra el nombre tantas veces como el entero
"""

"""

def impresionUsuario(username):
    '''bucle for que repite el nombre el numero de veces querido'''

    return username


if __name__ == "__main__":

    #leemos
    username = str(input("Introduzca un nombre de usuario: "))
    entero = int(input("Introduzca el número de veces a imprimir: "))

    #proceso
    resultado = impresionUsuario(username)

    #devolvemos
    for i in range(entero):
        print(resultado)