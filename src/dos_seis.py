#2.6 Pide el importe final y calcula el importe sin iva

def importeSinIva(importe_final:float) -> float:

    return importe_final - ((importe_final * 10)/100)

def mensajeSalida6(importe_sin_iva:float) -> str:

    return "El importe sin IVA es: " + str(importe_sin_iva)


if __name__ == "__main__":

    #leemos
    importe_final = float(input("Introduce el importe final: "))

    #procesamos
    importe_sin_iva = importeSinIva(importe_final)
    mensaje_salida = mensajeSalida6(importe_sin_iva)

    #devolvemos
    print(mensaje_salida)