import unittest
import yolanda
import re


# Clase que ejecuta los tests
class RegexTests(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        """
        Levanta una instancia de yolanda para probar las RegEx
        En particular se encarga de comprobar las variables:
        - regex_validador_fechas
        - regex_extractor_signos
        """
        super().__init__(*args, **kwargs)
        self.yolanda = yolanda.Yolanda('', '')

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    ##############################
    #      Validador fechas      #
    ##############################

    def test_validar_fechas_validas(self):
        """
        Todos los elementos de la lista de casos_validos abajo
        son textos que deberían ser capturados por la
        RegEx `regex_validador_fechas`
        """
        casos_validos = [
            "07\tde AgosTo de 95",
            "18 de abril de\n2018",
            "30 de JUNIO\tde 2023",
            "8 de ctbr de 01",
            "14 de carzo de 2010",
            "11 de\tnoviembre de 22",
            "46 de ABRIL de 1999",
        ]

        for i, texto in enumerate(casos_validos):
            with self.subTest(msg=texto):
                respuesta = re.match(self.yolanda.regex_validador_fechas, texto)
                self.assertIsInstance(respuesta, re.Match)
                self.assertEqual(respuesta.group(0), texto)

    def test_validar_fechas_invalidas(self):
        """
        Ninguno de los elementos de la lista de casos_invalidos abajo
        son textos que deberían ser capturados por la
        RegEx `regex_validador_fechas`
        """
        casos_invalidos = [
            "007 de agosto de 1995",
            "11 de noviembre de 022",
            "0 de sept de 20220",
            "18 de abril de 2118",
            "30 de junIO de 1823",
            "8, octubre de 2001",
            "14/marzo/2010",
            "6 de 07 de 1999",
        ]

        for i, texto in enumerate(casos_invalidos):
            with self.subTest(msg=texto):
                respuesta = re.search(self.yolanda.regex_validador_fechas, texto)
                self.assertEqual(respuesta, None)

    #######################################
    #      Verificar extractor signo      #
    #######################################
    def test_extraer_signo_valido(self):
        """
        Todos los elementos de la lista de casos_validos abajo
        son textos que deberían ser capturados por la
        RegEx `regex_extractor_signo`
        """
        casos_validos = [
            "Los   capricornianos pueden   dormir la mejor siesta del semestre.",
            "Las\tSAGITARIANAS\t\n\tpueden vivir el mejor día de su vida.",
            "Las\nacuarianas pueden volver a escuchar la mejor canción de su vida.",
            "Los    escorpianos pueden escuchar música con las aquarianas.",
            "Las liBRianas pueden ser libres por 1 día.",
            "Los cncrianos    pueden ver su serie favorita en la noche.",
            "Las pisqianas pueden    comer su poste favorito mañana.",
        ]
        signos_casos = [
            "capricornianos",
            "SAGITARIANAS",
            "acuarianas",
            "escorpianos",
            "liBRianas",
            "cncrianos",
            "pisqianas",
        ]

        for i, texto in enumerate(casos_validos):
            with self.subTest(msg=texto):
                respuesta = re.search(self.yolanda.regex_extractor_signo, texto)
                self.assertIsInstance(respuesta, re.Match)
                signo = respuesta.group(1)
                self.assertEqual(signo, signos_casos[i])

    def test_extraer_signo_invalido(self):
        """
        Ninguno de los elementos de la lista de casos_invalidos abajo
        son textos que deberían ser capturados por la
        RegEx `regex_extractor_signo`
        """
        casos_invalidos = [
            "Los_arianos pueden   dormir la mejor siesta del semestre.",                # No hay espacio entre Los y signo
            "Las pisqianas_pueden    comer su poste favorito mañana.",                  # No hay espacio entre signo y pueden
            "Lis   tiirinis  pueden   vivir el mejor día de su vida.",                  # Lis no es Las o Los
            "los\tacuarianas\npueden volver a escuchar la mejor canción de su vida.",   # Los no parte con mayúscula
            "Los escorpio pueden escuchar música con las aquarianas.",                  # Signo no está en plural
            "Las liBRianas serán libres por 1 día.",                                    # Falta pueden después del signo
            "Los cncrianos    pueden ver su serie favorita en la noche",                # Falta el punto al final
        ]

        for i, texto in enumerate(casos_invalidos):
            with self.subTest(msg=texto):
                respuesta = re.search(self.yolanda.regex_extractor_signo, texto)
                self.assertEqual(respuesta, None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
