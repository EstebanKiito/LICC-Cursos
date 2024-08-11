import re
from .regla_base import Regla


class ReglaClasesMayuscula(Regla):
    """
        Regla que revisa cuando hay clases que no partes con mayúscula
    """
    def __init__(self) -> None:
        super().__init__(
            nombre="Clases deben partir con mayúscula",
            nivel="linea"
        )

    # Sobreescribir el método de la clase abstracta.
    def revisar_regla(self, nombre_archivo, contenido):
        # Debemos generar un patrón con regex.
        # Reglas a seguir:
        # 1. Encontrar el string "class" seguido de un espacio.
        # 2. Este string puede estar indentado, asi que podría haber
        #    una cantidad no nula de espacios antes.
        # 3. Luego, encontrar que el caracter que siga NO sea una mayúscula.

        # COMPLETAR
        pass
