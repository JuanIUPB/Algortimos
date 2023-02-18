""" Bowser ha raptado de nuevo a la princesa Peach y Mario irá a su rescate; sin
embargo, el camino no será fácil, él tendrá que recorrer un camino de N
posiciones, y tendrá la opción de moverse M veces saltando varias casillas.
En el trayecto al encontrar a Wario lo hará retroceder 3 casillas, Donkey Kong lo
hará retroceder 5 casillas y un Hongo lo harán retroceder 1 casilla. También podrá
encontrarse con la súper Estrella que le servirá como escudo para impedir que sus
enemigos lo hagan retroceder. Este poder lo podrá usar solo por el siguiente
movimiento.
Ayuda a Mario a saber si puede rescatar a Peach teniendo en cuenta esa cantidad
de movimientos en los que avanza y retrocede. De ser así imprimir el mensaje "LA
PRINCESA PEACH ESTA A SALVO", sino imprimir el mensaje "BOWSER SE
QUEDARA CON LA PRINCESA PEACH".
Input Format
En la primera línea se leerán dos variables enteras N y M que corresponden a la
cantidad de casillas que deberá recorrer Mario para llegar donde la princesa
Peach y la cantidad de movimientos que tendrá Mario, respectivamente.
Seguido de esto debes ingresar los N[i] espacios del camino, donde se lee W, H,
D o E que significan los enemigos de Mario: Wario, Hongo y Donkey Kong, y la
súper estrella que le da poder a Mario, respectivamente. Una L corresponde a un
espacio vacío en el camino.
Por último, leerás los M[i] movimientos con la cantidad de casillas que puede saltar
nuestro personaje separados por un espacio.
Constraints
2 ≤ N ≤ 30
1 ≤ M ≤ 10
N[i] = W, H, D, E, L
1 ≤ M[i] ≤ 6
Output Format
Si Mario puede alcanzar a rescatar a la princesa antes de que se acaben sus
movimientos, imprimir: "LA PRINCESA PEACH ESTA A SALVO", sino imprimir
"BOWSER SE QUEDARA CON LA PRINCESA PEACH".
Sample Input 0
10 4
W L E H H D L L H L
2 2 3 5
Sample Output 0

LA PRINCESA PEACH ESTA A SALVO
Explanation 0
En el primer movimiento Mario cae en un espacio libre (L), por lo que no afecta en
nada su recorrido. En el segundo movimiento avanza hasta una casilla donde hay
un hongo (H), por lo que le hace retroceder una casilla, sin embargo, al devolverse
se encuentra con la estrella (E) que le da super poderes. En el tercer movimiento
avanza 3 casillas, y se encuentra con Donkey Kong (D), pero Mario tiene la
estrella, por lo que no retrocederá 5 casillas. En el último movimiento avanza 5
casillas y logra terminar el camino rescatando así a la Princesa Peach. Por tal
motivo se imprime el mensaje "LA PRINCESA PEACH ESTA A SALVO". Tenga en
cuenta que Mario estará al inicio y Peach estará al final de todos los movimientos.
Sample Input 1
8 3
L L W E L H D L
2 3 2
Sample Output 1
BOWSER SE QUEDARA CON LA PRINCESA PEACH
Explanation 1
En el primer movimiento Mario cae en un espacio libre (L), por lo que no afecta en
nada su recorrido. En el segundo movimiento avanza 3 casillas y también cae en
un espacio libre (L). En el tercer movimiento avanza 2 casillas y se topa con
Donkey Kong que le hace retroceder 5 casillas y cae en un espacio libre, sin
embargo no tiene más movimientos, por lo que no podrá rescatar a Peach y se
muestra en pantalla "BOWSER SE QUEDARA CON LA PRINCESA PEACH".
Tenga en cuenta que Mario estará al inicio y Peach estará al final de todos los
movimientos. """
n, m = map(int, input().split())
posiciones=list(map(str, input().split()))
posiciones.append('G')
movimientos=list(map(int, input().split()))
vecContador=[]
contador=0

for i in range(len(movimientos)):
    contador+=movimientos[i]
    vecContador.append(contador)
    if (posiciones[contador-1]== "W"):
        estrella= (contador-1)-movimientos[i]
        if (posiciones[estrella] == "E"):pass
        else:
            contador-=3
    elif (posiciones[contador-1]== "D"):
        estrella= (contador-1)-movimientos[i]
        if (posiciones[estrella] == "E"):
            pass
        else:
            contador-=5
    elif (posiciones[contador-1]== "H"):
        estrella= (contador-1)-movimientos[i]
        if (posiciones[estrella] == "E"):
            pass
        else:
            contador-=1
    elif (posiciones[contador-1]== "L"):
        estrella= (contador-1)-movimientos[i]
        if (posiciones[estrella] == "E"):
            pass
        else:
            contador=contador
    else:
        pass

if posiciones[contador-1] == "G":
    print("LA PRINCESA PEACH ESTA A SALVO")
else:
    print("BOWSER SE QUEDARA CON LA PRINCESA PEACH")