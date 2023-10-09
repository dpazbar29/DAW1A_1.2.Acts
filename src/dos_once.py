#2.11 Pide un número positivo y entero que luego sume su sucesión hasta 1 y muestra el resultado final

def pedir(n:int) -> int:

    if n <= 0:
        n = input("El número ha de ser positivo: ")
    else:
        suma = 0
        #realización suma
        for i in range(1,n+1):
            suma += i 
    
    return suma

def mensajeSalida11(suma:int,n:int) -> str:

    return "La suma de los numeros desde 1 hasta " + str(n) + " es " + str(suma)


if __name__ == "__main__":

    #leer
    n = int(input("Introduzca el número: "))

    #proceso
    if n <= 0:
        n = input("Ha de ser positivo: ")
    else:
        suma = 0
        for i in range(1,n+1):
            suma += i
    mensaje_salida = mensajeSalida11(suma)


    #devolvemos
    print(mensaje_salida)