#2.13 Pide dos enteros y realiza su división mostrando por pantalla su cociente y resto

def cocienteDiv(n1:int,n2:int) -> int:
    '''calcula el cociente de una division y muestralo'''

    return n1//n2

def restoDiv(n1:int,n2:int) ->  int:
    '''calcula el resto de una division y muestralo'''

    return n1%n2

def mensajeSalida13(n1:int,n2:int,resto:int,cociente:int) ->str:

    return "La división de "+str(n1)+" y "+str(n2)+", tiene de resto "+str(resto)+" y de cociente "+str(cociente)

if __name__ == "__main__":

    #leemos
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))

    #proceso
    cociente = cocienteDiv(n1,n2)
    resto  = restoDiv(n1,n2)
    mensaje_salida = mensajeSalida13(n1,n2,resto,cociente)

    #devolvemos
    print(mensaje_salida)