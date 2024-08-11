from threading import Event
from io import StringIO
from unittest.mock import patch
import unittest

from main import Carrera, Jugador, Bandera


class FakeLock:
    def __init__(self) -> None:
        self._locked = False
        self.accessed = False
        self.blocking = True
        self.releases = 0

    def acquire(self, blocking=True):
        self.blocking = blocking
        if not self._locked:
            self.accessed = True
            self._locked = True
            return True

        if self._locked:
            return False

    def release(self):
        self.releases += 1
        if self._locked:
            self._locked = False
        return RuntimeError("release unlocked lock")

    def locked(self):
        return self._locked

    def __enter__(self, *args, **kwargs):
        self.acquire()
        return args, kwargs

    def __exit__(self, *args, **kwargs):
        self.release()
        return args, kwargs


class VerificarCarrera(unittest.TestCase):
    def setUp(self) -> None:
        bandera = Bandera()
        lock_bandera = FakeLock()
        lock_carrera = FakeLock()
        senal_inicio = Event()
        senal_fin = Event()

        # Instancia los corredores y la carrera
        self.j1 = Jugador(
            "Jose", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera
        )
        self.j2 = Jugador(
            "Mati", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera
        )
        self.j3 = Jugador(
            "Ariel", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera
        )

        self.j1.agregar_rival(self.j2)
        self.j1.agregar_rival(self.j3)

        Jugador.TIEMPO_ESPERA = 0
        Jugador.PORCENTAJE_MIN = 100
        Jugador.PORCENTAJE_MAX = 100
        Jugador.PROBABILIDAD_ROBAR = 1

        self.carrera = Carrera(self.j1, self.j2, self.j3,
                               senal_inicio, senal_fin)

    def test_carrera_valor_daemon(self):
        """
        Se verifica que el programa espere al thread antes de finalizar
        """
        self.assertFalse(self.carrera.daemon)

    @patch("threading.Thread.join")
    def test_run_inicia_threads(self, new_join):
        """
        Se verifica la inicialización de los 3 threads.
        """
        with patch("threading.Thread.start") as mock:
            self.carrera.run()
            self.assertEqual(mock.call_count, 3)

    @patch("threading.Thread.join")
    @patch("threading.Thread.start")
    def test_run_senal_inicio(self, new_start, new_join):
        """
        Se verifica el uso de Eventos para avisar el inicio de la carrera.
        """
        with patch("threading.Event.set") as mock:
            self.carrera.run()
            mock.assert_called()
    
    @patch("threading.Thread.join")
    @patch("threading.Thread.start")
    def test_run_senal_inicio_fue_seteada_BONUS(self, new_start, new_join):
        """
        Se verifica que la señal de inicio fue la seteada y no otra
        """
        self.carrera.run()
        self.assertTrue(self.carrera.senal_inicio.is_set())

    @patch("threading.Thread.start")
    def test_run_espera_jugadores(self, new_start):
        """
        Se verifica el uso de join en la carrera.
        """
        with patch("threading.Thread.join") as mock:
            self.carrera.run()
            self.assertEqual(mock.call_count, 3)


if __name__ == "__main__":
    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
