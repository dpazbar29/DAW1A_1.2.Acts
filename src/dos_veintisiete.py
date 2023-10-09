#2.27

def calculoCoste(precio_unitario,unidades):

    return round(precio_unitario * unidades,2)


def cadenaFinal(nombre_producto,precio_unitario,unidades,coste_total):

    return "{} - {:0>8.2f} - {:0>3} - {:0>8.2f}".format(nombre_producto,precio_unitario,unidades,coste_total)


def mensajeSalida27(cadena_final):

    return "Resultado final: " + str(cadena_final)


if __name__ == "__main__":

    #leemos
    nombre_producto = input("Introduce el nombre del producto: ")
    precio_unitario = float(input("Introduce el precio del producto: "))
    unidades = int(input("Introduce el número de unidades: "))

    #proceso
    coste_total = calculoCoste(precio_unitario,unidades)
    cadena_final = cadenaFinal(nombre_producto,precio_unitario,unidades,coste_total)
    mensaje_salida = mensajeSalida27(cadena_final)

    #devolvemos
    print(mensaje_salida)




# Formatear la cadena de salida

# Mostrar la cadena formateada
