def imprimir_tablero(tablero: list):
    filas = len(tablero)
    columnas = len(tablero[0])
    tablero = [[str(x) for x in y] for y in tablero]
    tablero_largo = [[len(x) for x in y] for y in tablero]
    max_largo = max([max(x) for x in tablero_largo]) + 2
    tablero_ajustado = [[f"{' '*(max_largo - len(x))}{x}" for x in y] for y in tablero]

    columnas_ = " " * max_largo
    for indice in range(columnas):
        indice = str(indice)
        columnas_ += f"{' '*(max_largo - len(indice))}{indice}"

    print(columnas_)
    for indice in range(filas):
        indice = str(indice)
        fila = f"{' '*(max_largo - len(indice))}{indice}"

        fila += " " + "".join(tablero_ajustado[int(indice)])
        print(fila)
    print()


if __name__ == "__main__":
    # Ejemplo 1
    tablero = [["V2", "--", "PP", "--", "H2"], ["H3", "--", "--", "PP", "R11"]]
    imprimir_tablero(tablero)

    # Ejemplo 2
    tablero2 = [
        ["V2", "--", "PP", "--"],
        ["V2", "--", "PP", "--"],
        ["H3", "--", "H3", "PP"],
        ["R3", "--", "--", "PP"],
        ["H3", "R2", "--", "PP"],
    ]
    imprimir_tablero(tablero2)
