""" Elaborar un programa el cual le diga a cada usuario cual sera su nota definitiva en Herramientas de programacion 2 sabiendo que para esto el docente saca 5 notas. Se desea que almecene la nota definitiva de cada estudiante en un vector llamado notas y el nombre de cada estudiante en la misma posicion de su nota """

def Llenar(usuarios):
  notas=[]
  nombre=list(map(str, input("digite por favor el nombre de los estudiantes: ").split()))
  for i in range(usuarios):
    print("Notas de ",nombre[i])
    nf=NotaFinal()
    notas.append(nf)
  Reverse(notas, nombre)

def NotaFinal():
  nf=0
  j=0
  while(j<5):
    nota=float(input("Digite por favor la nota: "))
    nf+=nota
    j+=1
  return nf/5

def Reverse(notas, nombres):
  for i in range(len(notas)-1):
    for j in range(len(notas)-1):
      if notas[j] < notas[j+1]:
        aux=notas[j]
        notas[j]=notas[j+1]
        notas[j+1]=aux
        auxnom=nombres[j]
        nombres[j]=nombres[j+1]
        nombres[j+1]=auxnom
  print(nombres)
  print(notas)
  
#Llamar las funciones
usuarios=int(input("ingrese el numero de usuarios: "))
Llenar(usuarios)