class Tablero:
    def __init__(self, tablero: list) -> None:
        # filas         #columnas
        self.dimensiones = [len(tablero), len(tablero[0])]
        self.tablero = tablero

    # TODO: completar esta property
    def desglose(self) -> list:
        return None

    # TODO: completar esta property
    def peones_invalidos(self) -> int:
        return None

    # TODO: completar esta property
    def piezas_explosivas_invalidas(self) -> int:
        return None

    # TODO: completar esta property
    def tablero_transformado(self) -> list:
        return None

    # TODO: Completar este método
    def celdas_afectadas(self, fila: int, columna: int) -> int:
        return None

    # TODO: Completar este método
    def limpiar(self) -> int:
        return None

    # TODO: Completar este método
    def reemplazar(self, nombre_nuevo_tablero: str) -> bool:
        return None

    # TODO: Completar este método
    def solucionar(self) -> list:
        return None
