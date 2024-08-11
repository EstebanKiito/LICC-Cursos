from abc import ABC, abstractmethod
from .parametros_estilo import NEGRITA_INICIO, SUBRAYADO_INICIO, FIN

MAGENTA = "\033[;35m"
# https://gist.github.com/kamito/704813
# https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html


class Regla(ABC):
    """
    Clase abstracta que define una regla y sus atributos/métodos base
    """

    # Necesitamos el nombre de la regla, y registro de las faltas.
    # Ademas de saber su nivel: es una regla a nivel de archivo o de línea
    def __init__(self, nombre, nivel) -> None:
        self.nombre = nombre
        self.total_faltas = 0
        self.faltas = []
        self.nivel = nivel

    # Es abstracto ya que cada regla debe definir
    # qué revisa de forma personalizada
    @abstractmethod
    def revisar_regla(self, nombre_archivo, contenido):
        pass

    # Reiniciamos los contadores de faltas
    def reiniciar_faltas(self):
        self.total_faltas = 0
        self.faltas = []

    # Generamos una tabla para las reglas a nivel archivo.
    # Tiene una columna de archivo y otra con el detalle del problema.
    def imprimir_resumen_nivel_archivo(self):
        # COMPLETAR
        nombre_largo = 30
        detalle_largo = 50

        print(
            f"|{NEGRITA_INICIO}{'-'*(nombre_largo + detalle_largo + 1)}{FIN}|\n"
            + f"|{'nombre': ^{nombre_largo}}|{'detalle': ^{detalle_largo}}|\n"
            + f"|{NEGRITA_INICIO}{'-'*(nombre_largo + detalle_largo + 1)}{FIN}|"
        )

        for x in self.faltas:
            archivo = x["archivo"]
            detalle = x["detalle"]
            texto = f"{archivo: ^{nombre_largo}}|{detalle: ^{detalle_largo}}"
            print(f"|{MAGENTA}{NEGRITA_INICIO}{texto}{FIN}|")

        print(f"|{NEGRITA_INICIO}{'-'*(nombre_largo + detalle_largo + 1)}{FIN}|\n")

    # Generamos una tabla para las reglas a nivel línea.
    # Tiene una columna de archivo, una con la línea con el error
    # y otra con el detalle del problema.
    def imprimir_resumen_nivel_linea(self):
        # COMPLETAR
        nombre_largo = 30
        linea_largo = 5
        detalle_largo = 50

        total = nombre_largo + detalle_largo + linea_largo + 2

        print(
            f"""|{NEGRITA_INICIO}{'-'*(total)}{FIN}|
|{'nombre': ^{nombre_largo}}|{'#': ^{linea_largo}}|{'detalle': ^{detalle_largo}}|
|{NEGRITA_INICIO}{'-'*(total)}{FIN}|"""
        )

        for x in self.faltas:
            linea = x["linea"]
            archivo = x["archivo"]
            detalle = x["detalle"]
            texto = f"{archivo: ^{nombre_largo}}|{linea: ^{linea_largo}}|{detalle: ^{detalle_largo}}"
            print(f"|{MAGENTA}{NEGRITA_INICIO}{texto}{FIN}|")

        print(f"|{NEGRITA_INICIO}{'-'*(total)}{FIN}|\n")

    # Imprimimos los encabezados del reporte
    # Usando caracteres especiales para el formato
    def imprimir_resumen(self):
        print(f"Hola, fallaste {len(self.faltas)} veces.\n")

        if self.nivel == "archivo":
            self.imprimir_resumen_nivel_archivo()
        else:  # nivel == "linea"
            self.imprimir_resumen_nivel_linea()
