#2.20 Pide el numero de telefono con prefijo y extension y devuelvelo sin esto

def filtro(numero_tel):
    '''sacamos el numero de telefono'''

    partes = numero_tel.split("-")

    if len(partes) == 3 and partes[0] == "+34" and len(partes[1]) == 9 and len(partes[2]) == 2:
        
        return partes[1]

def mensajeSalida20(filtrado):
    '''mensaje de vuelta'''

    return "El numero de telefono integro es: " + str(filtrado)


if __name__ == "__main__":

    #leemos
    numero_tel = str(input("Introduzca el número de teléfono con prefijo y extensión con formato +34-XXXXXXXXX-XX: "))

    #proceso
    filtrado = filtro(numero_tel)
    mensaje_salida = mensajeSalida20(filtrado)

    #devolvemos
    print(mensaje_salida)
    