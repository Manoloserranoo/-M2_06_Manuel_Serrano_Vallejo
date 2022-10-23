#Ejercicio1:Usamos el import.math para disponer del número pi,definimos una función area_circulo que almacenará la fórmula del área del circulo,creamos una variable radio que nos pida el radio de la circunferencia y llamamos a la función area_circulo para que calcule el área con el radio dado.

import math 

def area_circulo(R):
  
  area = round(R*R*math.pi,2)
  return area

radio= float(input("¿Que radio tiene la círculo?"))
a = area_circulo(radio)
print("El área de círculo es =", a)

