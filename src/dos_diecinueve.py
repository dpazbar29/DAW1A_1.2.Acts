#2.19 pide el nombre de usuario y muestralo en mayusculas y di cuantas letras tiene

def mayusculasUser(username:str) -> str:
    '''devulve el username en mayusculas'''

    return username.upper()


def contarUser(username:str) -> str:
    '''devuelve la longitud del username'''

    return len(username)

def mensajeSalida19(user_m,user_cont):

    return "El usuario " + str(user_m) + " tiene un longitud de " + str(user_cont)


if __name__ == "__main__":

    #leemos
    username = str(input("Introduce el nombre de usuario: "))

    #proceso
    user_m = mayusculasUser(username)
    user_cont = contarUser(username)
    mensaje_salida = mensajeSalida19(user_m,user_cont)

    #devolvemos
    print(mensaje_salida)
