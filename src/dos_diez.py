#2.10 Haz un programa que realize la operacion ((3+2)/2*5)^2

def operacion():
    
    return float(pow((5/10),2))

def mensajeSalida10(op:float) ->  str:

    return "El resultado de ((3+2)/2*5)^2 es: " + str(op)

if __name__ ==  "__main__":

    #leemos
    '''No hay nada a leer,ya que se muestra el cálculo de una operación'''

    #proceso
    op = operacion()
    mensaje_salida = mensajeSalida10(op)

    #devolvemos
    print(mensaje_salida)
