from threading import Event
from io import StringIO
from unittest.mock import patch
import unittest

from main import Jugador, Bandera


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


class VerificarJugador(unittest.TestCase):
    def setUp(self) -> None:
        self.bandera = Bandera()
        lock_bandera = FakeLock()
        lock_carrera = FakeLock()
        senal_inicio = Event()
        senal_fin = Event()

        # Instancia los corredores y la carrera
        self.j1 = Jugador(
            "Jose", self.bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera
        )
        self.j2 = Jugador(
            "Mati", self.bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera
        )
        self.j3 = Jugador(
            "Ariel", self.bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera
        )

        self.j1.agregar_rival(self.j2)
        self.j1.agregar_rival(self.j3)

        Jugador.TIEMPO_ESPERA = 0
        Jugador.DISTANCIA_AVANZAR = 10
        Jugador.PORCENTAJE_MIN = 100
        Jugador.PORCENTAJE_MAX = 100
        Jugador.PROBABILIDAD_ROBAR = 1

        self.calls = 0

    def test_corredor_valor_daemon(self):
        """
        Se verifica que el programa espere a los threads antes de finalizar
        """
        self.assertFalse(self.j1.daemon)
        self.assertFalse(self.j2.daemon)
        self.assertFalse(self.j3.daemon)

    def test_perder_bandera_perdida(self):
        """
        Se verifica el valor de "tiene_bandera" cuando se pierde la bandera
        """
        self.j1.tiene_bandera = True
        self.j1.perder_bandera()
        self.assertFalse(self.j1.tiene_bandera)

    def test_capturar_bandera_rivales(self):
        """
        Se verifica el valor de "tiene_bandera" de los rivales cuando se captura la bandera
        """
        self.j2.tiene_bandera = True
        self.j3.tiene_bandera = True
        self.j1.capturar_bandera()
        self.assertFalse(self.j2.tiene_bandera)
        self.assertFalse(self.j3.tiene_bandera)

    def test_capturar_bandera_captura(self):
        """
        Se verifica el valor de "tiene_bandera" cuando se captura la bandera
        """
        self.assertFalse(self.j1.tiene_bandera)
        self.j1.capturar_bandera()
        self.assertTrue(self.j1.tiene_bandera)

    def test_capturar_bandera_actualizacion_bandera(self):
        """
        Se verifica que bandera actualice sus atributos cuando es capturada
        """
        self.assertIsNone(self.j1.bandera.nombre_dueño)
        self.j1.capturar_bandera()
        self.assertEqual(self.j1.bandera.nombre_dueño, self.j1.name)

    def test_intentar_capturar_bandera_blocking(self):
        """
        Se verifica que los jugadores no se queden esperando a que se libere el lock
        """
        self.assertTrue(self.j1.lock_bandera.blocking)
        self.j1.intentar_capturar_bandera()
        self.assertFalse(self.j1.lock_bandera.blocking)

    def test_intentar_capturar_bandera_llama_captura(self):
        """
        Se verifica que el jugador use el método capturar_bandera cuando su intento es exitoso
        """
        with patch("main.Jugador.capturar_bandera") as mock:
            self.j1.intentar_capturar_bandera()
            mock.assert_called()

    def test_intentar_capturar_bandera_sin_release(self):
        """
        Se verifica que nadie libere el lock excepto quien capturó la bandera
        """
        self.j1.tiene_bandera = False
        self.j1.lock_bandera.acquire()
        self.j2.intentar_capturar_bandera()
        self.assertEqual(self.j2.lock_bandera.releases, 0)

    def test_intentar_capturar_bandera_release(self):
        """
        Se verifica que solo quien obtubo el lock sea quien lo libere el lock
        """
        self.j1.intentar_capturar_bandera()
        self.assertNotEqual(self.j1.lock_bandera.releases, 0)

    def test_intentar_capturar_bandera_release(self):
        """
        Se verifica que si se obtiene el lock, pero bandera tiene dueño, no se capture la bandera
        """
        self.bandera.nombre_dueño = "OTRO"
        with patch("main.Jugador.capturar_bandera") as mock:
            self.j1.intentar_capturar_bandera()
            mock.assert_not_called()

    def test_intentar_capturar_bandera_release_BONUS(self):
        """
        Se verifica que si se obtiene el lock, 
        pero bandera tiene dueño, se libere igual el lock
        """
        self.bandera.nombre_dueño = "OTRO"
        with patch("main.Jugador.capturar_bandera"):
            self.j1.intentar_capturar_bandera()
            self.assertNotEqual(self.j1.lock_bandera.releases, 0)

    def test_intentar_robar_bandera_retorno_exitoso(self):
        """
        Se verifica el retorno de intentar_robar_bandera cuando es exitoso
        """
        self.assertEqual(self.j1.PROBABILIDAD_ROBAR, 1)
        respuesta = self.j1.intentar_robar_bandera()
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_intentar_robar_bandera_resultado_fallido(self):
        """
        Se verifica el retorno de intentar_robar_bandera cuando es fallido
        """
        self.j1.PROBABILIDAD_ROBAR = -1
        respuesta = self.j1.intentar_robar_bandera()
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_intentar_robar_bandera_lock_acquire(self):
        """
        Se verifica que solo 1 jugador pueda robar la bandera a la vez
        """
        self.assertFalse(self.j1.lock_bandera.accessed)
        self.j1.intentar_robar_bandera()
        self.assertTrue(self.j1.lock_bandera.accessed)

    def test_intentar_robar_bandera_lock_release(self):
        """
        Se verifica que otro jugador pueda robar la bandera solo cuando el primero ya la robó
        """
        self.assertEqual(self.j1.lock_bandera.releases, 0)
        self.j1.intentar_robar_bandera()
        self.assertNotEqual(self.j1.lock_bandera.releases, 0)

    def test_intentar_robar_bandera_llama_captura(self):
        """
        Se verifica el uso del método "capturar_bandera" cuando se roba la bandera
        """
        self.j1.tiene_bandera = True
        with patch("main.Jugador.capturar_bandera") as mock:
            self.j1.intentar_robar_bandera()
            mock.assert_called_once()

    def test_correr_segunda_mitad_llama_avanzar(self):
        """
        Se verifica que el jugador avance en la segunda mitad de la carrera
        """
        with patch("main.Jugador.avanzar") as mock:
            self.j1.correr_segunda_mitad()
            mock.assert_called_once()

    def test_correr_segunda_mitad_llama_sleep(self):
        """
        Se verifica que el jugador espere entre una ejecución y otra
        """
        with patch("time.sleep") as mock:
            self.j1.correr_segunda_mitad()
            mock.assert_called_once()

    def test_correr_segunda_mitad_lock_acquire(self):
        """
        Se verifica que solo 1 jugador puede revisar el estado de la carrera a la vez
        """
        self.assertFalse(self.j1.lock_carrera.accessed)
        self.j1.correr_segunda_mitad()
        self.assertTrue(self.j1.lock_carrera.accessed)

    def test_correr_segunda_mitad_lock_releases(self):
        """
        Se verifica que otro jugador pueda revisar el estado de la carrera
        solo cuando el primero ya terminó
        """
        self.assertEqual(self.j1.lock_carrera.releases, 0)
        self.j1.correr_segunda_mitad()
        self.assertNotEqual(self.j1.lock_carrera.releases, 0)

    def test_correr_segunda_mitad_carrera_perdida_return(self):
        """
        Se verifica el resultado de correr_segunda_mitad cuando el jugador pierde
        """
        self.j1.senal_fin.set()
        resultado = self.j1.correr_segunda_mitad()
        self.assertIsInstance(resultado, bool)
        self.assertFalse(resultado)

    def test_correr_segunda_mitad_carrera_perdida_correr(self):
        """
        Se verifica que el jugador deje de correr cuando este pierde
        """
        self.j1.senal_fin.set()
        self.j1.correr_segunda_mitad()
        self.assertFalse(self.j1._correr)

    def test_correr_segunda_mitad_carrera_ganada_return(self):
        """
        Se verifica el resultado de correr_segunda_mitad cuando el jugador gana
        """
        self.j1.posicion = 100
        self.j1.tiene_bandera = True
        resultado = self.j1.correr_segunda_mitad()
        self.assertTrue(resultado)

    def test_correr_segunda_mitad_carrera_ganada_senal(self):
        """
        Se comprueba que el jugador revise si la carrera ya terminó durante la segunda mitad
        """
        self.j1.posicion = 100
        self.j1.tiene_bandera = True
        self.j1.correr_segunda_mitad()
        self.assertTrue(self.j1.senal_fin.is_set())

    def test_correr_segunda_mitad_carrera_ganada_correr(self):
        """
        Se verifica que el jugador deje de correr cuando este gana
        """
        self.j1.posicion = 100
        self.j1.tiene_bandera = True
        self.j1.correr_segunda_mitad()
        self.assertFalse(self.j1._correr)

    def test_correr_segunda_mitad_carrera_intentar_robar_bandera(self):
        """
        Se verifica que el jugador intente robar la bandera en la segunda mitad de la carrera
        """
        self.assertFalse(self.j1.tiene_bandera)
        with patch("main.Jugador.intentar_robar_bandera") as mock:
            self.j1.correr_segunda_mitad()
            mock.assert_called_once()

    def test_run_espera_senal_inicio(self):
        """
        Se comprueba que los jugadores esperan a que empiece la carrera antes de correr
        """

        def correr(*args):
            self.j1._correr = False
            self.calls += 1

        self.j1.posicion = 51
        with patch("threading.Event.wait") as mock:
            with patch("main.Jugador.correr_primera_mitad"):
                with patch("main.Jugador.correr_segunda_mitad", correr):
                    self.j1.run()
                    mock.assert_called()


if __name__ == "__main__":
    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
