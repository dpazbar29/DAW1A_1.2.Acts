#2.12 Pida el peso en kg y la altura en m y calcula el indice de masa corporal devolviendolo

def indiceMasa(peso:float,altura:float) -> float:
    '''calculo del indice de masa corporal'''

    return round((peso/pow(altura,2)),2)

def mensajeSalida12(imc:float) -> str:

    return "Tu IMC es: " + str(imc)


if __name__ == "__main__":

    #leemos
    peso = float(input("Introduce tu peso en kg: ")) 
    altura = float(input("Introduce tu altura en m: "))

    #proceso
    imc = indiceMasa(peso,altura)
    mensaje_salida = mensajeSalida12(imc)

    #devolvemos
    print(mensaje_salida)