#Ejercicio 2.4 introduce temperatura en celsius devuelve farenheit

def conversor(temperatura:float) -> float:
   '''función calculo de farenheits'''
   return((temperatura * 1.8) + 32)

def mensajeSalida4(farenheit:float) -> str:
   '''Devuelve el mensaje para mostrar en consola'''

   return "La temperatura en F es: " +  str(farenheit)

if __name__ == "__main__":

   # leemos
   temperatura = float(input("Introduzca la temperatura en celsius: "))

   # procesamos
   farenheit = conversor(temperatura)
   mensaje_salida = mensajeSalida4(farenheit)
   
   #mostramos
   print(mensaje_salida)
   