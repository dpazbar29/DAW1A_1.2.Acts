def suma1(n1:float,n2:float,n3:float) -> float:
    '''funcion suma'''
    return n1 + n2 + n3

def mensajeSalida9(suma:float) -> str:
    '''funcion devulve resultado de suma'''
    return "La suma es: " + str(suma)


if __name__ == "__main__":

    #leer
    suma =  float(input("Intruduce el primer número: ")) + float(input("Intruduce el segundo número: ")) + float(input("Intruduce el tercer número: "))

    #proceso
    mensaje_salida = mensajeSalida9(suma)

    #resultado
    print(mensajeSalida9(suma))


