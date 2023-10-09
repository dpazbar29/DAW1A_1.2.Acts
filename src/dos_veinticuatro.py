#2.24 Pide el precio de un producto y muestra el numero de euros y el de centimos

def euros(precio:float) -> int:

    return int(precio)

def centimos(precio:float,eur:int) -> int:

    return int((precio - eur) * 100)

def mensajeSalida24(eur,cent):

    return "Euros: " + str(eur) + "\nCentimos: " + str(cent)

if __name__ == "__main__":

    #leemos
    precio = float(input("Por favor, introduzca el precio del producto en euros(2 decimales): "))

    #proceso
    eur = euros(precio)
    cent = centimos(precio,eur)
    mensaje_salida = mensajeSalida24(eur,cent)

    #devolvemos
    print(mensaje_salida)
