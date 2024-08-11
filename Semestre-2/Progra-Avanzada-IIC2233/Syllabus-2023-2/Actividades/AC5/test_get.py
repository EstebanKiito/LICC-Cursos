import unittest
import yolanda
import api
from datetime import date


# Clase que ejecuta los tests
class YolandaWebsServiceTestGet(unittest.TestCase):
    """
    Levanta un servidor para probar los tests.
    En particular se encarga de comprobar las funciones:
    - saludar
    - verificar_horoscopo
    - dar_horoscopo
    - dar_horoscopo_aleatorio
    """

    host = "localhost"
    port = 4444
    database = {
        "acuario": "Hoy será un hermoso día",
        "leo": "No salgas de casa.... te lo recomiendo",
        "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
    }
    servidor = api.Server(host, port, database, mode=2)
    yolanda = yolanda.Yolanda(host, port)
    servidor.start()

    def setUp(self) -> None:
        """
        Reinicia la base de datos antes de cada test
        """
        self.servidor.mode = 2
        self.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        self.servidor.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    #####################
    #      Saludar      #
    #####################

    def test_saludar_mode_1_verificar_todo(self):
        """
        Revisa que el método saludar retorne las respuestas correctas
        en el formato correcto.
        """
        self.servidor.mode = 1
        respuesta = self.yolanda.saludar()
        today = date.today()
        resultado = f"Hoy es {today} y es un hermoso día para recibir un horóscopo"

        self.assertIn("status-code", respuesta)
        self.assertIn("saludo", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["saludo"], resultado)

    def test_saludar_mode_2_verificar_todo(self):
        """
        Revisa que el método saludar retorne las respuestas correctas
        en el formato correcto.
        """
        self.servidor.mode = 2
        respuesta = self.yolanda.saludar()
        today = date.today()
        resultado = f"Hoy es {today} y me da gusto escribir horóscopos"

        self.assertIn("status-code", respuesta)
        self.assertIn("saludo", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["saludo"], resultado)

    #####################
    #  Verificar horóscopo  #
    #####################

    def test_verificar_horoscopo_tipo_respuesta(self):
        """
        Verifica que el método retorne un booleano.
        """
        respuesta = self.yolanda.verificar_horoscopo("piscis")
        self.assertIsInstance(respuesta, bool)

    def test_verificar_horoscopo_si_existe(self):
        """
        Verifica que el método retorne True para signos
        presentes en la base de datos.
        """
        respuesta = self.yolanda.verificar_horoscopo("piscis")
        self.assertEqual(respuesta, True)

    def test_verificar_horoscopo_no_existe(self):
        """
        Verifica que el método retorne False para signos
        no presentes en la base de datos.
        """
        respuesta = self.yolanda.verificar_horoscopo("UWU")
        self.assertEqual(respuesta, False)

    #####################
    #   Dar horóscopo   #
    #####################

    def test_dar_horoscopo_verificar_keys(self):
        """
        Verifica que el método retorne un diccionario con
        la estructura pedida
        """
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)

    def test_dar_horoscopo_existe_verificar_status_code(self):
        """
        Verifica que el método retorne el código correcto
        cuando el signo existe en la base de datos.
        """
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["status-code"], 200)

    def test_dar_horoscopo_existe_verificar_mensaje(self):
        """
        Verifica que el método retorne el mensaje correcto
        cuando el signo existe en la base de datos.
        """
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database["piscis"])

    def test_dar_horoscopo_no_existe_verificar_todo(self):
        """
        Verifica que el método retorne el código y mensaje correcto
        cuando el signo no existe en la base de datos.
        """
        respuesta = self.yolanda.dar_horoscopo("UWU")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["status-code"], 400)
        self.assertEqual(respuesta["mensaje"], "El signo no existe")

    ###########################
    # Dar horóscopo aleatorio #
    ###########################

    def test_dar_horoscopo_aleatorio_mode_1(self):
        """
        Verifica que el método retorne un diccionario,
        cuyo mensaje corresponda a uno de los signos de la
        base de datos
        """
        self.servidor.mode = 1
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        signo = list(self.database.keys())[0]
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database[signo])

    def test_dar_horoscopo_aleatorio_mode_2(self):
        """
        Verifica que el método retorne un diccionario,
        cuyo mensaje corresponda a uno de los signos de la
        base de datos
        """
        self.servidor.mode = 2
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        signo = list(self.database.keys())[-1]
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database[signo])

    def test_dar_horoscopo_aleatorio_mode_3(self):
        """
        Verifica que el método falle en ciertos casos,
        dando el mensaje y error correcto.
        """
        self.servidor.mode = 3
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["status-code"], 500)
        self.assertEqual(respuesta["mensaje"], "ups, no pude")


if __name__ == "__main__":
    unittest.main(verbosity=2)
