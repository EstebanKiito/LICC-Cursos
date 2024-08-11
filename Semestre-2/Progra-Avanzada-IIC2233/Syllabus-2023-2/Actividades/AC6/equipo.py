from collections import defaultdict, deque


class Jugador:
    def __init__(self, nombre: str, velocidad: int) -> None:
        self.nombre = nombre
        self.velocidad = velocidad

    def __repr__(self) -> None:
        return f'Jugador: {self.nombre}, Velocidad: {self.velocidad}'


class Equipo:
    def __init__(self) -> None:
        self.jugadores = dict()
        self.dict_adyacencia = defaultdict(set)

    def agregar_jugador(self, id_jugador: int, jugador: Jugador) -> bool:
        '''Agrega un nuevo jugador al equipo.'''
        # Completar
        return "COMPLETAR"

    def agregar_vecinos(self, id_jugador: int, vecinos: list[int]) -> int:
        '''Agrega una lista de vecinos a un jugador.'''
        # Completar
        return "COMPLETAR"

    def peor_amigo(self, id_jugador: int) -> Jugador:
        '''Retorna al vecino con la velocidad menos similar.'''
        # Completar
        return "COMPLETAR"

    def mejor_compañero(self, id_jugador: int) -> Jugador:
        '''Retorna al compañero de equipo con la menor diferencia de velocidad.'''
        # Completar
        return "COMPLETAR"

    def mejor_conocido(self, id_jugador: int) -> Jugador:
        '''Retorna al conocido con la menor diferencia de velocidad.'''
        # Completar
        return "COMPLETAR"

    def distancia(self, id_jugador_1: int, id_jugador_2: int) -> int:
        '''Retorna el tamaño del camino más corto entre los jugadores.'''
        # Completar
        return "COMPLETAR"


if __name__ == '__main__':
    equipo = Equipo()
    jugadores = {
        0: Jugador('Ana', 1),
        1: Jugador('Antonio', 3),
        2: Jugador('Alfredo', 6),
        3: Jugador('Ariel', 10)
    }
    adyacencia = {
        0: [1],
        1: [0, 2],
        2: [1],
    }
    for idj, jugador in jugadores.items():
        equipo.agregar_jugador(id_jugador=idj, jugador=jugador)
    for idj, vecinos in adyacencia.items():
        equipo.agregar_vecinos(id_jugador=idj, vecinos=vecinos)

    print(f'El peor amigo de Antonio es {equipo.peor_amigo(1)}') 
    print(f'El mejor compañero de Ana es {equipo.mejor_compañero(0)}')
    print(f'El mejor conocido de Alfredo es {equipo.mejor_conocido(2)}')
    print(f'La distancia entre Alfredo y Ana es {equipo.distancia(2, 0)}')
    print(f'La distancia entre Antonio y Ariel es {equipo.distancia(1, 3)}')
    print(f'La distancia entre Antonio y Amalia es {equipo.distancia(1, 5)}')
