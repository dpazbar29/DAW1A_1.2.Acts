#2.25 Pregunta la fecha de nacimiento(dd/mm/aaaa) y muestra el dia el mes y el año

def filtroDia(fecha_nac):

    comp = fecha_nac.split("/")

    return comp[0] 

def filtroMes(fecha_nac):

    comp = fecha_nac.split("/")

    return comp[1]

def filtroAño(fecha_nac):

    comp = fecha_nac.split("/")

    return comp[2]

def mensajeSalida25(dia,mes,año,fecha_nac):

    if len(dia) == 1 or 2:
        dia = filtroDia(fecha_nac)

    if mes == "01" or "1":
        mes = "Enero"
    elif mes == "02" or "2":
        mes = "Febrero"
    elif mes == "03" or "3":
        mes = "Marzo"
    elif mes == "04" or "4":
        mes = "Abril"
    elif mes == "05" or "5":
        mes = "Mayo"
    elif mes == "06" or "6":
        mes = "Junio"
    elif mes == "07" or "7":
        mes = "Julio"
    elif mes == "08" or "8":
        mes = "Agosto"
    elif mes == "09" or "9":
        mes = "Septiembre"
    elif mes == "10":
        mes = "Octubre"
    elif mes == "11":
        mes = "Noviembre"
    elif mes == "12":
        mes = "Diciembre"
    else:
        None
    
    año = año

    return "Dia: " + str(dia) + "\nMes: " + str(mes) + "\nAño: " + str(año)
 




if __name__ == "__main__":

    #leemos
    fecha_nac = str(input("Introduce la fecha de nacimiento(dd/mm/aaaa): "))

    #proceso
    dia = filtroDia(fecha_nac)
    mes = filtroMes(fecha_nac)
    año = filtroAño(fecha_nac)
    mensaje_salida = mensajeSalida25(dia,mes,año)

    #devolvemos
    print(mensaje_salida)