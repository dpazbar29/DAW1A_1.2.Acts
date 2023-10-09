#2.21 Pide una frase que sea devuelta al revés

def darVuelta(frase:str) -> str:
    '''Es “cortar” la cadena pero sin especificar inicio ni fin, solo especificando el step; de esta manera avanzamos de -1 en -1;'''
    
    return frase[::-1]

def mensajeSalida21(frase_invertida:str) -> str:
    '''definimos el mensaje a devolver'''
    
    return "La frase invertida es: " + str(frase_invertida)

if __name__ == "__main__":

    #leemos
    frase = str(input("Introduzca una frase: "))

    #proceso
    frase_invertida = darVuelta(frase)
    mensaje_salida = mensajeSalida21(frase_invertida)

    #devolvemos
    print(mensaje_salida)