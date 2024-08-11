"""
Hecho con "amor" por los profe

En el siguiente código se solucionará un problema en un tablero aplicando recursión.

El problema es de un laberinto. Tendremos tableros como el siguiente:

tablero = [
        ["-", "N", "-", "-"],
        ["-", "N", "-", "-"],
        ["-", "N", "-", "-"],
        ["-", "N", "-", "-"],
    ]

Donde indicaremos una posición inicial (fila_inicio, columna_inicio)
y una posición final (fila_fin, columna_fin).

El problema buscará la ruta para llegar desde el inicio a el final.
Y retornará la posicición de dicha ruta.
"""


# Función que verifica si llegamos al caso base recursivo.
# En este caso, que la posición de inicio sea igual a la final
def es_caso_base(inicio, fin):
    # Caso base --> llegamos a la meta
    return inicio == fin


# Función que verifica que la posición indicada es válida para el tablero.
# En este caso, que no se salga del tablero y no sea una posición ya visitada.
def es_valida(tablero, posicion, ruta_actual):
    # Nos salimos del tablero en fila
    if posicion[0] < 0 or posicion[0] >= len(tablero):
        return False

    # Nos salimos del tablero en columna
    if posicion[1] < 0 or posicion[1] >= len(tablero[0]):
        return False

    # Es una pared
    if tablero[posicion[0]][posicion[1]] == "N":
        return False

    # No haber pasado por dicha celda antes
    if posicion in ruta_actual:
        return False

    # Cumple lo esperado, así que la nueva celda es visitable
    return True


# Esta es nuestra función recursiva que recibe el tablero, una posición de inicio,
# una posición de fin y el camino_actual. En la primera ejecución el camino está solo
# con la posición de inicio, pero luego se va llenando con la ruta que estamos probando
# hasta llegar al final.
def obtener_camino(tablero, inicio, fin, camino_actual):
    # Verificar caso base
    if es_caso_base(inicio, fin):
        return camino_actual

    # Posibles jugadas. Moverme en las 4 direcciones posibles
    direcciones = [
        # Fila, Columna
        [-1, 0],  # Arriba
        [0, 1],  # Derecha
        [1, 0],  # Abajo
        [0, -1],  # Izquierda
    ]
    # Probamos cada una de las direcciones
    for direccion in direcciones:
        # Calculamos nuestra nueva posición en función de nuestra posición
        # de inicio y la dirección que queremos probar.
        nueva_pos = [inicio[0] + direccion[0], inicio[1] + direccion[1]]

        # Si es válida la nueva posición, usamos recursión para
        # simular que estamos en esa posición y seguir adelante.
        if es_valida(tablero, nueva_pos, camino_actual):
            # Actualizamos nuestro "origen" a la nueva posición
            # y buscamos una solución desde ese nuevo punto
            # llamando nuevamente a nuestra función
            solucion = obtener_camino(
                tablero, nueva_pos, fin, camino_actual + [nueva_pos]
            )

            # Encontró el camino, retorno esa solución
            if solucion != []:
                return solucion

    # No encontró nada, no es solución... retorno vacío
    return []


if __name__ == "__main__":
    # 'N' = Pared;  '-' = celda vacía

    # Caso 1: desde [0, 0] hasta [0, 3]
    tablero = [
        ["-", "-", "-", "-"],
        ["-", "N", "-", "-"],
        ["-", "N", "-", "-"],
        ["-", "-", "-", "-"],
    ]

    intento = obtener_camino(tablero, inicio=[0, 0], fin=[0, 3], camino_actual=[[0, 0]])
    print(intento)  # Hay solución

    # Caso 2: desde [0, 0] hasta [3, 3] (de una esquina a otra)
    tablero = [
        ["-", "-", "-", "-"],
        ["N", "N", "-", "-"],
        ["-", "N", "-", "-"],
        ["-", "-", "-", "-"],
    ]

    intento = obtener_camino(tablero, inicio=[0, 0], fin=[3, 3], camino_actual=[[0, 0]])
    print(intento)  # Hay solución

    # Caso 3: desde [0, 0] hasta [0, 3] pero hay una pared en la mitad
    tablero = [
        ["-", "N", "-", "-"],
        ["-", "N", "-", "-"],
        ["-", "N", "-", "-"],
        ["-", "N", "-", "-"],
    ]

    intento = obtener_camino(tablero, inicio=[0, 0], fin=[0, 3], camino_actual=[[0, 0]])
    print(intento)  # No hay solución
