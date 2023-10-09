#Ejercicio 2.5 Aplica el tipo de IVA y calcula el importe final


def calculoIva(importe:float,iva:float) -> float:
    
    return importe * iva

def mensajeSalida5(importe_final:float) -> str:

    return "El importe final es: "+ str(importe_final)

if  __name__ == "__main__":

    #leemos
    importe = float(input("Introduzca el importe: "))
    iva = float(input("Introduzca el porcentaje del IVA(general:1.21)(reducido:1.10)(superreducido:1.04): "))

    #procesar
    importe_final = calculoIva(importe,iva)
    mensaje_salida = mensajeSalida5(importe_final)

    #devolvemos
    print(mensaje_salida)