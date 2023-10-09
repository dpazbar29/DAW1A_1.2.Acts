#2.22 Haz un programa que pida una frase y que pida una vocal y hacer que esa vocal en la frase aparezca en mayusculas

def filtro22(frase:str,vocal:str) -> str:

    if len(vocal) == 1 and vocal.islower() and vocal in "aeiuo":
    
        return frase.replace(vocal,vocal.upper())

def mensajeSalida22(frase_mod:str) -> str:

    return "La frase sera: " + frase_mod
if __name__ == "__main__":

    #leemos
    frase = str(input("Introduzca una frase: "))
    vocal = str(input("Introduzca una vocal a capitalizar: "))

    #proceso
    frase_mod = filtro22(frase)
    mensaje_salida = mensajeSalida22(frase_mod)

    #devolvemos
    print(mensaje_salida)