""" Según la definición de Wikipedia, el balón de oro es un premio otorgado
anualmente por la revista francesa especializada en fútbol: France Football, se
considera el mayor honor individual a nivel futbolístico. Para elegir a los 3 mejores
futbolistas cada año, N cantidad de periodistas votan por el mejor y se realiza su
conteo exacto; pero cada vez tarda más tiempo y se hace más complejo hacerlo.
Por lo tanto, se puso como reto de programación simular este proceso leyendo el
voto de cada periodista y sacando el informe final.
Se muestra un primer informe con los nombres y porcentajes obtenidos por todos
los jugadores ordenados de mayor a menor junto con los rótulos Balon de oro para
el primer puesto, Balon de plata para el segundo puesto y Balon de bronce para el
tercer puesto. Los demás puestos, sólo llevarán el nombre y el porcentaje.
Input Format
La primera línea lee una variable entera N, que corresponden al número de
periodistas que votarán para elegir al balón de oro. Luego, en N líneas, aparecen
la lectura de todos los nombres de los jugadores registrados por los periodistas.
Constraints
6 ≤ N ≤ 100
Output Format
Se muestra un primer informe con los nombres y porcentajes obtenidos (usar 2
decimales en la precisión) por cada jugador ordenados de mayor a menor junto
con los rótulos Balon de oro, para el primer puesto, Balon de plata para el segundo
puesto y Balon de bronce para el tercer puesto. Ver ejemplo para entender mejor
el reto a resolver. En todos los casos siempre habrá jugadores para los 3 primeros
puestos y se garantizan que no hay casos de prueba repetidos.
Sample Input 0
6
Leo Messi
Leo Messi
Robert Lewandowski
Robert Lewandowski
Leo Messi
Kylian Mbappe
Sample Output 0
Leo Messi 50.00% Balon de oro
Robert Lewandowski 33.33% Balon de plata
Kylian Mbappe 16.67% Balon de bronce """
n=int(input())
jugadores=[]
porcentajes=[]
for i in range(n):
  voto=str(input(""))
  jugadores.append(voto)
for i in range(n):
  rep=jugadores.count(jugadores[i])
  porcentaje=(rep*100)/n
  porcentajes.append(porcentaje)

#Creando dos vectores nuevos en los que no se repitan los jugadores y los porcentajes
jugadoresGanadores = []
for i in jugadores:
  if i not in jugadoresGanadores:
    jugadoresGanadores.append(i)
porcentajesGanadores = [] 
for i in porcentajes:
  if i not in porcentajesGanadores:
    porcentajesGanadores.append(i)

#Aplicar metodo burbuja para ordenar de mayor a menor los porcentajes y asi mismo los jugadores correspondientes a cada porcentaje
for i in range(len(porcentajesGanadores)-1):
  for j in range(len(porcentajesGanadores)-1):
    if porcentajesGanadores[j] < porcentajesGanadores[j+1]:
      aux=porcentajesGanadores[j]
      porcentajesGanadores[j] = porcentajesGanadores[j+1]
      porcentajesGanadores[j+1] = aux
      auxjug=jugadoresGanadores[j]
      jugadoresGanadores[j] = jugadoresGanadores[j+1]
      jugadoresGanadores[j+1] = auxjug

#Imprimir los jugadores
print("")
balon=['Balon de oro', 'Balon de plata', 'Balon de bronce']
if (len(jugadoresGanadores)>2):
  print(f"{jugadoresGanadores[0]} {round(porcentajesGanadores[0])}% {balon[0]}")
  print(f"{jugadoresGanadores[1]} {round(porcentajesGanadores[1])}% {balon[1]}")
  print(f"{jugadoresGanadores[2]} {round(porcentajesGanadores[2])}% {balon[2]}")
  for i in range(3,len(jugadoresGanadores)):
    print(f"{jugadoresGanadores[i]} {round(porcentajesGanadores[i])}%")
