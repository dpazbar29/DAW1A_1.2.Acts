#2.26 Pregunta los producto de una cesta de compra y dalos por separado


def filtro26(productos:str) -> str:

    lista_productos = productos.split(",")

    return productos.split(",") 

def mensajeSalida26(productos:str,lista:str) -> str:
    for productos in lista:
        print(productos.strip())
    
    return None

if __name__ == "__main__":

    #leemos
    productos = str(input("Ingrese los productos de la cesta: "))

    #proceso
    lista = filtro26(productos)
    mensaje_salida = mensajeSalida26(productos,lista)

    #devolvemos
    print(mensaje_salida)






