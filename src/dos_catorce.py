#2.14 Calcula el peso del paquete de muñecas y payasos

"""
payasos = input("Número payasos: ")
muñecas = input("Número muñecas: ")
"""

def calculadoraPesoPaquete(payasos:int,muñecas:int) -> int:
    '''calcula el peso del paquete a enviar'''

    return float(((payasos*112)+(muñecas*75))/1000)

def mensajeSalida14(peso_paquete:int) -> str:
    '''devuelta del mensaje con la información'''

    return "El peso en kilogramos del paquete es: " + str(peso_paquete)


if __name__ == "__main__":

    #leemos
    payasos = int(input("Número payasos: "))
    muñecas = int(input("Número muñecas: "))

    #proceso
    peso_paquete = calculadoraPesoPaquete(payasos,muñecas)
    mensaje_salida = mensajeSalida14(peso_paquete)

    #devolvemos
    print(mensaje_salida)