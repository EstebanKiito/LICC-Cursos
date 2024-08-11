from random import random, randint
from threading import Event, Lock, Thread
import time


# No modificar
class Bandera:

    def __init__(self) -> None:
        self.nombre_dueño = None

    def actualizar_dueño(self, nombre_jugador: str) -> None:
        self.nombre_dueño = nombre_jugador


# Completar
class Jugador(Thread):

    TIEMPO_ESPERA = 0.2  # Tiempo entre avances del jugador
    PORCENTAJE_MIN = 50  # Mínimo avance del jugador
    PORCENTAJE_MAX = 100  # Máximo avance del jugador
    PROBABILIDAD_ROBAR = 0.3  # Probabilidad de robar la bandera
    DISTANCIA_AVANZAR = 10  # Distancia a avanzar

    def __init__(
        self,
        nombre: str,
        bandera: Bandera,
        lock_bandera: Lock,
        senal_inicio: Event,
        senal_fin: Event,
        lock_carrera: Lock,
    ) -> None:
        super().__init__(name=nombre)
        # Completar
        self.daemon = "COMPLETAR"

        # No modificar el resto de los atributos
        self.bandera = bandera
        self.senal_inicio = senal_inicio
        self.senal_fin = senal_fin
        self.lock_bandera = lock_bandera
        self.lock_carrera = lock_carrera

        self.rivales = list()
        self.tiene_bandera = False
        self.puntaje = 0
        self._posicion = 0
        self._correr = True

    @property
    def posicion(self) -> float:
        return self._posicion

    @posicion.setter
    def posicion(self, nueva_posicion: int) -> None:
        # La posicion no puede aumentar más allá de la meta
        self._posicion = min(nueva_posicion, 100)

    @property
    def dist_avance(self) -> float:
        # El jugador reduce su velocidad si lleva la bandera
        if self.tiene_bandera:
            return Jugador.DISTANCIA_AVANZAR * 0.5
        return Jugador.DISTANCIA_AVANZAR

    def agregar_rival(self, rival: "Jugador") -> None:
        self.rivales.append(rival)

    def avanzar(self) -> None:
        # Se mueve una cantidad aleatoria dependiente de la distancia de avance
        cantidad_avanzar = randint(self.PORCENTAJE_MIN, self.PORCENTAJE_MAX) / 100
        self.posicion += self.dist_avance * cantidad_avanzar
        # Luego de avanzar imprime su posición
        print(f"{self.name}: Avancé a {self.posicion:.2f}")

    def perder_bandera(self) -> None:
        # Completar
        print(f"{self.name}: Perdí la bandera :(")

    def capturar_bandera(self) -> None:
        # Completar
        pass

    def intentar_capturar_bandera(self) -> None:
        # Completar

        if self.tiene_bandera:
            print(f"{self.name}: ¡Capturé la bandera!")

    def intentar_robar_bandera(self) -> bool:
        # Completar
        # PROBABILIDAD_ROBAR de robar la bandera
        if random() < self.PROBABILIDAD_ROBAR:
            return "COMPLETAR"
        else:
            return "COMPLETAR"

    def correr_primera_mitad(self):
        self.avanzar()
        time.sleep(Jugador.TIEMPO_ESPERA)

    def correr_segunda_mitad(self) -> bool:
        # Completar
        pass

    def run(self) -> None:
        # Completar con la primera parte de este método

        # No modificar lo siguiente
        while self.posicion < 50:
            self.correr_primera_mitad()

        self.intentar_capturar_bandera()

        while self._correr:
            self.correr_segunda_mitad()


# Completar
class Carrera(Thread):
    def __init__(
        self,
        juga_1: Jugador,
        juga_2: Jugador,
        juga_3: Jugador,
        senal_inicio: Event,
        senal_fin: Event,
    ) -> None:
        super().__init__()
        # Completar
        self.daemon = "COMPLETAR"

        # No modificar el resto de los atributos

        # Referencias a las señales propias de la carrera
        self.senal_inicio = senal_inicio
        self.senal_fin = senal_fin

        # Guarda los jugadores y los asigna como rivales
        self.jugador_1 = juga_1
        self.jugador_2 = juga_2
        self.jugador_3 = juga_3
        self.jugadores = [self.jugador_1, self.jugador_2, self.jugador_3]

        juga_1.agregar_rival(juga_2)
        juga_1.agregar_rival(juga_3)
        juga_2.agregar_rival(juga_1)
        juga_2.agregar_rival(juga_3)
        juga_3.agregar_rival(juga_1)
        juga_3.agregar_rival(juga_2)

    def run(self) -> None:
        # Completar
        pass

    # No modificar
    def entregar_ganador(self) -> None:
        # Código que encuentra e imprime el ganador.
        jugadores = self.jugadores
        for jugador in jugadores:
            if jugador.tiene_bandera:
                jugador.puntaje += 5
            if jugador.posicion >= 100:
                jugador.puntaje += 5
            print(f"{jugador.name}: {jugador.puntaje}, {jugador.posicion}")
        jugadores.sort(key=lambda j: j.puntaje, reverse=True)

        print(
            f"\n¡¡{jugadores[0].name} ha ganado la carrera con {jugadores[0].puntaje} puntos!!"
        )
        if jugadores[2].puntaje != jugadores[1].puntaje:
            print(
                f"{jugadores[1].name} quedó en segundo lugar con {jugadores[1].puntaje} puntos"
            )
            print(f"Más suerte para la próxima {jugadores[2].name}")
        else:
            msg = "{0} y {1} empataron con {2} puntos"
            print(
                msg.format(jugadores[1].name,
                           jugadores[2].name, jugadores[1].puntaje)
            )


if __name__ == "__main__":
    # Instancia una bandera y las señales. No modificar nada de esta parte
    bandera = Bandera()
    lock_bandera = Lock()
    lock_carrera = Lock()
    senal_inicio = Event()
    senal_fin = Event()

    # Instancia los jugadores y la carrera
    j1 = Jugador("Zelda", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera)
    j2 = Jugador("Kirby", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera)
    j3 = Jugador("Conan", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera)
    carrera = Carrera(j1, j2, j3, senal_inicio, senal_fin)

    # Inicia la carrera y pausa el main thread hasta que termine
    carrera.start()
    carrera.join()

    # Obtiene e imprimer al ganador
    carrera.entregar_ganador()
