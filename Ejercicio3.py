#Definimos la función imc que almacenará la fórmula del índice de masa corporal,luego pedimos por teclado tanto la altura como el peso y ,mediante comparaciones conseguimos que nos diga si esta en el peso correcto.
def imc(peso,altura):

  imc = round(peso /(altura*altura),2)

  return imc

altura = float(input("¿Cuál es tu altura en metros?"))
peso = float(input("¿Cuál es tu peso en kilogramos?"))
i = imc(peso,altura)
print("Tu imc es=",imc(peso,altura))
if imc(peso,altura) < 18.50 :
  print("Bajo peso")
elif imc(peso,altura) > 18.50  and imc(peso,altura) < 25.00:
  print("Peso normal")
elif imc(peso,altura) > 25.00 and imc(peso,altura) < 30.00:
  print("Sobre peso")
elif imc(peso,altura) >= 30.00 :
  print("Obesidad")



