#EJERCICIO 2.1

#Escribe un programa que pida el nombre del usuario y que salude

#Escribe tu nombre: Juan
#Hola, Juan

def saludo(nombre:str) -> str:
    '''función que da el nombre'''
    return nombre

def mensaje_salida(nombre: float) -> str:
    '''Devuelve el mensaje para mostrar en consola'''
    return "Hola, " +  str(nombre)


if __name__ == "__main__":

    # leemos
    nombre = input("Introduzca su nombre: ")

    # procesamos
    salida = mensaje_salida(nombre)
    # mostramos
    print(salida)