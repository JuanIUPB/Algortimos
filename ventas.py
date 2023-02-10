""" Elaborar un programa el cual le diga a cada usuario cuanto tendra que pagar por concepto de la compra de N articulos. Sabiendo que para esto se va a generar un descuento SI la compra es menor de 100 mil tendra un descuento de 5%, SI la compra esta entre 100 mil y 250 mil tendra descuento del 7%, SI la compra es mayor a 250 mil y menor a 600 mil tendra 18% de descuento, en caso contario tendra un descuento del 25%.
NOTA: EL gerente desea conocer la venta del bien y el descuento se hace antes del IVA y el IVA del 16%.
"""

#FUNCIONES
def usuarios(m):
  total=0
  pagar=0
  for i in range(m):
    n=int(input("Digite por favor la cantidad de articulos: "))
    pagar=Ciclointerno(n)
    print("El valor a pagar es $",pagar)
    total += pagar
  print("El valor de las ventas fue de $",total)

  return pagar

def Ciclointerno(n):
  j=0
  pagar=0
  while(j<n):
    valor=float(input("Digite por favor el valor del artículo: "))
    pagar += valor
    j+=1
  pagar=Condicion(pagar)
  return pagar

def Condicion(pagar):
  if(pagar < 100000):
    pagar=(pagar*0.95*1.16)
  elif(pagar <  250001):
    pagar=(pagar*0.93*1.16)
  elif(pagar < 600000):
    pagar=(pagar*0.82*1.16)
  else:
    pagar=(pagar*0.75*1.16)
  return pagar

#CODIGO
m=int(input("Digite por favor la cantidad de usuarios: "))
total=usuarios(m)