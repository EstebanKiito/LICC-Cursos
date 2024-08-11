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
        # COMPLETAR
        pass

    # Generamos una tabla para las reglas a nivel línea.
    # Tiene una columna de archivo, una con la línea con el error
    # y otra con el detalle del problema.
    def imprimir_resumen_nivel_linea(self):
        # COMPLETAR
        pass

    # Imprimimos los encabezados del reporte
    # Usando carácteres especiales para el formato
    def imprimir_resumen(self):
        # COMPLETAR
        print(self.faltas) # Esto es muy peeeeeenca
