#2.16 Pide el numero de barras no frescas vendidas,el descuento hecho a las no frescas y el coste final de las barras no frescas

PRECIO_PAN = 3.49

def descuento(barras_nf:int) -> float:
    '''calculo del descuente que se realiza'''
    
    return round(0.6 * (barras_nf * PRECIO_PAN),2)

def costeBarras(barras_nf:int,desc:float) -> str:
    '''aplicacion del descuento y muestra del precio final de las barras con descuento'''

    return round((barras_nf * PRECIO_PAN) - desc,2)

def mensajeSalida16(precio_barras:str):
    '''muestra el numero de barras nf vendidas'''

    return "El precio final es: " + str(precio_barras)

if __name__  == "__main__":

    #leemos
    barras_nf = int(input("Ingresa el número de barras no frescas vendidas: "))

    #proceso
    desc = descuento(barras_nf)
    precio_barras = str(costeBarras(barras_nf,desc))
    mensaje_salida = mensajeSalida16(precio_barras)

    #devolvemos
    print(mensaje_salida)

