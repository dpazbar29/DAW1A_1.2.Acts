#2.7 Calcula la suma de tres números 


def suma3 (a:float, b:float, c:float) -> float:

    return a + b + c

def mensajeSalida7(resultado):

    return "El resultado de la suma es: " + str(resultado)

if __name__ == "__main__":

    #leemos
    a  = float(input("Introduce el primero número: "))
    b  = float(input("Introduce el segundo número: "))
    c  = float(input("Introduce el tercer número: "))

    #procesar
    resultado = suma3(a,b,c)
    mensaje_salida = mensajeSalida7(resultado)

    #devolvemos
    print(mensaje_salida)