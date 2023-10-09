#2.8 Suma usando 2 variables

def suma2(suma:float)  -> float:
    
    return suma

def mensajeSalida8(resultado:float) -> str:

    return "La suma es: " + str(resultado)

if __name__ == "__main__":

    #leemos
    suma = float(input("Elije el primer número: ")) + float(input("elige el segundo número: ")) + float(input("Elige el tercer número: "))

    #proceso
    resultado = suma2(suma)
    mensaje_salida = mensajeSalida8(resultado)

    #devolvemos
    print(mensaje_salida)

#TEST NO COMPLETADO