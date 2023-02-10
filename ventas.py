""" Elaborar un programa el cual le diga a cada usuario cuanto tendra que pagar por concepto de la compra de N articulos. Sabiendo que para esto se va a generar un descuento SI la compra es menor de 100 mil tendra un descuento de 5%, SI la compra esta entre 100 mil y 250 mil tendra descuento del 7%, SI la compra es mayor a 250 mil y menor a 600 mil tendra 18% de descuento, en caso contario tendra un descuento del 25%.
NOTA: EL gerente desea conocer la venta del bien y el descuento se hace antes del IVA y el IVA del 16%.
"""

#OPERACIONES

    #Saca descuento del 5% al precio total 
def descuentoDel_5(pagar):
    pagar = (pagar*0.95*1.16)
    return pagar

    #saca descuento del 7%
def descuentoDel_7(pagar):
    pagar = (pagar*0.93*1.16)
    return pagar  

    #saca descuento del 18%
def descuentoDel_18(pagar):
    pagar = (pagar*0.82*1.16)
    return pagar  

    #saca descuento del 25%
def descuentoDel_25(pagar):
    pagar = (pagar*0.75*1.16)
    return pagar  


#CODIGO
total=0
m=int(input("Digite por favor la cantidad de usuarios: "))
for i in range(m):
  n=int(input("Digite por favor la cantidad de articulos: "))
  pagar=0
  j=0
  while(j<n):
    valor=float(input("Digite por favor el valor del artículo: "))
    pagar +=valor
    j+=1
  if(pagar < 100000):
    pagar=descuentoDel_5(pagar)
  elif(pagar <  250001):
    pagar=descuentoDel_7(pagar)
  elif(pagar < 600000):
    pagar=descuentoDel_18(pagar)
  else:
    pagar=descuentoDel_25(pagar)
  print("El valor a pagar es $",pagar)
  total+=pagar
print("El valor de las ventas fue de $",total)