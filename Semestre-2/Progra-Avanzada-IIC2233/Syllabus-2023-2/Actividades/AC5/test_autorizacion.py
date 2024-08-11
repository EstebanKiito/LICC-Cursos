from functools import wraps
import signal
import platform
import unittest
import yolanda
import api


"""
Código del TimeoutError extraido y adaptado de
https://github.com/pnpnpn/timeout-decorator/tree/master
"""


class TimeoutError(AssertionError):

    """
    Error cuando el test toma más del tiempo esperado.
    """

    def __init__(self, value="Timed Out"):
        self.value = value

    def __str__(self):
        return repr(self.value)


def timeout(seconds=None):
    """
    Manejo del timeout (límite de tiempo para la función decorada)
    """
    def decorate(function):
        def handler(signum, frame):
            raise TimeoutError("Timeout")

        @wraps(function)
        def new_function(*args, **kwargs):
            new_seconds = kwargs.pop("timeout", seconds)
            if new_seconds:
                old = signal.signal(signal.SIGALRM, handler)
                signal.setitimer(signal.ITIMER_REAL, new_seconds)

            if not seconds:
                return function(*args, **kwargs)

            try:
                return function(*args, **kwargs)
            finally:
                if new_seconds:
                    signal.setitimer(signal.ITIMER_REAL, 0)
                    signal.signal(signal.SIGALRM, old)

        if platform.system().lower() == "windows":
            return function
        return new_function

    return decorate


N_SECOND = 1


# Clase que ejecuta los tests
class YolandaWebsServiceTestWithAutorization(unittest.TestCase):
    """
    Levanta un servidor para probar los tests.
    En particular se encarga de comprobar las funciones:
    - agregar_horoscopo
    - actualizar_horoscopo
    - eliminar_signo
    """

    host = "localhost"
    port = 4444
    database = {
        "acuario": "Hoy será un hermoso día",
        "leo": "No salgas de casa... te lo recomiendo",
        "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
    }
    servidor = api.Server(host, port, database, mode=2)
    yolanda = yolanda.Yolanda(host, port)
    servidor.start()

    def setUp(self) -> None:
        """
        Reinicia la base de datos antes de cada test
        """
        self.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        self.servidor.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    #####################
    # Agregar horoscopo #
    #####################
    @timeout(N_SECOND)
    def test_agregar_horoscopo_no_autorizado(self):
        """
        Se comprueba que envía el mensaje pedido
        cuando el error de la API es 401 (no autorizado)
        """
        respuesta = self.yolanda.agregar_horoscopo("leo", "grande messi", "FAIL")
        self.assertEqual(respuesta, "Agregar horóscopo no autorizado")

    @timeout(N_SECOND)
    def test_agregar_horoscopo_signo_ya_existe(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el signo ya existía en
        la base de datos.
        """
        respuesta = self.yolanda.agregar_horoscopo(
            "leo", "grande messi", "morenoiic2233"
        )
        self.assertEqual(respuesta, "El signo ya existe, no puedes modificarlo")

    @timeout(N_SECOND)
    def test_agregar_horoscopo_signo_mensaje_muy_corto(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el mensaje a colocar es demasiado corto.
        """
        respuesta = self.yolanda.agregar_horoscopo("leo", "a", "morenoiic2233")
        self.assertEqual(respuesta, "El mensaje debe tener más de 4 caracteres")

    @timeout(N_SECOND)
    def test_agregar_horoscopo_ok_verificar_respuesta(self):
        """
        Se comprueba que envia el mensaje pedido cuando
        la request de la API fue exitosa (200)
        """
        mensaje = "grande messi"
        respuesta = self.yolanda.agregar_horoscopo(
            "Sagitario", mensaje, "morenoiic2233"
        )
        self.assertEqual(respuesta, "La base de YolandAPI ha sido actualizada")

    @timeout(N_SECOND)
    def test_agregar_horoscopo_ok_verificar_base_datos(self):
        """
        Se comprueba que tras realizar una request exitosa a la api,
        el mensaje almacenado en la base de datos haya sido el enviado.
        """
        mensaje = "grande messi"
        self.yolanda.agregar_horoscopo("Sagitario", mensaje, "morenoiic2233")
        self.assertIn("Sagitario", self.servidor.database)
        self.assertEqual(mensaje, self.servidor.database["Sagitario"])

    ########################
    # Actualizar horoscopo #
    ########################
    @timeout(N_SECOND)
    def test_actualizar_horoscopo_no_autorizado(self):
        """
        Se comprueba que envía el mensaje pedido
        cuando el error de la API es 401 (no autorizado)
        """
        respuesta = self.yolanda.actualizar_horoscopo("leo", "grande messi", "FAIL")
        self.assertEqual(respuesta, "Editar horóscopo no autorizado")

    @timeout(N_SECOND)
    def test_actualizar_horoscopo_signo_no_existe(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el signo a enviar no existe en la base de datos.
        """
        respuesta = self.yolanda.actualizar_horoscopo(
            "messi", "grande messi", "morenoiic2233"
        )
        self.assertEqual(respuesta, "El signo no existe")

    @timeout(N_SECOND)
    def test_actualizar_horoscopo_signo_mensaje_muy_corto(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el mensaje a colocar es demasiado corto.
        """
        respuesta = self.yolanda.actualizar_horoscopo("leo", "a", "morenoiic2233")
        self.assertEqual(respuesta, "El mensaje debe tener más de 4 caracteres")

    @timeout(N_SECOND)
    def test_actualizar_horoscopo_ok_verificar_respuesta(self):
        """
        Se comprueba que envia el mensaje pedido cuando
        la request de la API fue exitosa (200)
        """
        mensaje = "grande messi"
        respuesta = self.yolanda.actualizar_horoscopo("leo", mensaje, "morenoiic2233")
        self.assertEqual(respuesta, "La base de YolandAPI ha sido actualizada")

    @timeout(N_SECOND)
    def test_actualizar_horoscopo_ok_verificar_base_datos(self):
        """
        Se comprueba que tras realizar una request exitosa a la api,
        el mensaje almacenado en la base de datos haya sido el enviado.
        """
        mensaje = "grande messi"
        self.yolanda.actualizar_horoscopo("leo", mensaje, "morenoiic2233")
        self.assertEqual(mensaje, self.servidor.database["leo"])

    ##################
    # Eliminar signo #
    ##################
    @timeout(N_SECOND)
    def test_eliminar_signo_no_autorizado(self):
        """
        Se comprueba que envía el mensaje pedido
        cuando el error de la API es 401 (no autorizado)
        """
        respuesta = self.yolanda.eliminar_signo("leo", "FAIL")
        self.assertEqual(respuesta, "Eliminar signo no autorizado")

    @timeout(N_SECOND)
    def test_eliminar_signo_signo_no_existe(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el signo a borrar no existe en la base de datos.
        """
        respuesta = self.yolanda.eliminar_signo("messi", "morenoiic2233")
        self.assertEqual(respuesta, "El signo no existe")

    @timeout(N_SECOND)
    def test_eliminar_signo_ok_verificar_respuesta(self):
        """
        Se comprueba que envia el mensaje pedido cuando
        la request de la API fue exitosa (200)
        """
        respuesta = self.yolanda.eliminar_signo("leo", "morenoiic2233")
        self.assertEqual(respuesta, "La base de YolandAPI ha sido actualizada")

    @timeout(N_SECOND)
    def test_eliminar_signo_ok_verificar_base_datos(self):
        """
        Se comprueba que tras realizar una request exitosa a la api,
        el signo ya no se encuentre en la base de datos.
        """
        self.yolanda.eliminar_signo("leo", "morenoiic2233")
        self.assertNotIn("leo", self.servidor.database)


if __name__ == "__main__":
    unittest.main(verbosity=2)
