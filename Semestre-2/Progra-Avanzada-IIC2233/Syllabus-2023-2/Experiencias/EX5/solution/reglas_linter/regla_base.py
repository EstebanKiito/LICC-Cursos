from abc import ABC, abstractmethod
from .parametros_estilo import NEGRITA_INICIO, SUBRAYADO_INICIO, FIN


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
        columna_archivo = f"{10 * ' '}ARCHIVO{10 * ' '}"
        columna_detalles = f"{30 * ' '}DETALLE{30 * ' '}"
        encabezado = f"|{columna_archivo}|{columna_detalles}|"
        print(
            f"{NEGRITA_INICIO}{'-' * len(encabezado)}{FIN}"
            "\n"
            f"{NEGRITA_INICIO}{encabezado}{FIN}"
            "\n"
            f"{NEGRITA_INICIO}{'-' * len(encabezado)}{FIN}"
        )
        for falta in self.faltas:
            espaciado_archivo = len(columna_archivo)

            espaciado_detalles = len(columna_detalles)

            print(
                f"|{falta['archivo']: ^{espaciado_archivo}}|"
                f"{falta['detalle']: ^{espaciado_detalles}}|"
                "\n"
                f"{NEGRITA_INICIO}{'-' * len(encabezado)}{FIN}"
            )

    # Generamos una tabla para las reglas a nivel línea.
    # Tiene una columna de archivo, una con la línea con el error
    # y otra con el detalle del problema.
    def imprimir_resumen_nivel_linea(self):
        columna_archivo = f"{10 * ' '}ARCHIVO{10 * ' '}"
        columna_linea = "LINEA"
        columna_detalles = f"{30 * ' '}DETALLE{30 * ' '}"
        encabezado = f"|{columna_archivo}|{columna_linea}|{columna_detalles}|"

        print(
            f"{NEGRITA_INICIO}{'-' * len(encabezado)}{FIN}"
            "\n"
            f"{NEGRITA_INICIO}{encabezado}{FIN}"
            "\n"
            f"{NEGRITA_INICIO}{'-' * len(encabezado)}{FIN}"
        )
        for falta in self.faltas:
            espaciado_archivo = len(columna_archivo)
            espaciado_linea = len(columna_linea)
            espaciado_detalles = len(columna_detalles)

            print(
                f"|{falta['archivo']: ^{espaciado_archivo}}|"
                f"{falta['linea']: ^{espaciado_linea}}|"
                f"{falta['detalle']: ^{espaciado_detalles}}|"
                "\n"
                f"{NEGRITA_INICIO}{'-' * len(encabezado)}{FIN}"
            )

    # Imprimimos los encabezados del reporte
    # Usando carácteres especiales para el formato
    def imprimir_resumen(self):
        print(
            f"{SUBRAYADO_INICIO}Reporte de faltas de estilo{FIN}"
            "\n\n"
            f"{NEGRITA_INICIO}Regla analizada:{FIN} {self.nombre}"
            "\n"
            f"{NEGRITA_INICIO}Faltas encontradas en archivo:"
            f"{FIN} {self.total_faltas}"
            "\n"
        )

        if not self.total_faltas:
            return
        if self.nivel == "archivo":
            self.imprimir_resumen_nivel_archivo()
        elif self.nivel == "linea":
            self.imprimir_resumen_nivel_linea()
        print()
