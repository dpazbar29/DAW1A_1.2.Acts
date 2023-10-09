#pedir horas trabajo y precio
#P1.2(2.2) 


def horas_trabajo(horas: int,coste:int) -> int:
    '''Funcion que calcula el coste'''
    return horas * coste

def mensaje_salida2(costeHora: float) -> str:
    '''Devuelve el mensaje para mostrar en consola'''
    return "Cobra: " +  str(costeHora)

if __name__ == "__main__":

    # leemos
    horas = int(input("¿Cuántas horas trabajas?: "))
    coste = int(input("¿Cuánto cobras por hora?: "))

    # procesamos
    costeHora = horas_trabajo(horas,coste)
    mensajeSalida = mensaje_salida2(costeHora)

    # mostramos
    print(mensajeSalida)
