#Definimos la función lee_numero que almacena la acción de pedir un número,y la utilizamos para conseguir los tres números que nos piden,finalmente definimos la función mayor la cual compara estos numeros y luego imprimimos la función.
def lee_numero():
  num=(input("Digame un número:"))
 
  return num

num1=lee_numero()
num2=lee_numero()
num3=lee_numero()

def mayor():
  if num1 > num2 and num1 > num3:
      return("El número mayor es",num1)
  elif num2 > num3:
      return("El número mayor es",num2)
  else:
      return("El número mayor es",num3)
print(mayor())

