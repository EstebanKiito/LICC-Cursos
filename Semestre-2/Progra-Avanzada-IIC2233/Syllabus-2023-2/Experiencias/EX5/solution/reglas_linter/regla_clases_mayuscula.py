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

    def revisar_regla(self, nombre_archivo, contenido):
        # Debemos generar un patrón con regex.
        # Reglas a seguir:
        # 1. Encontrar el string "class" seguido de un espacio.
        # 2. Este string puede estar indentado, asi que podría haber
        #    una cantidad no nula de espacios antes.
        # 3. Luego, encontrar que el caracter que siga NO sea una mayúscula.
        patron = r"^\s*class\s+[^A-Z]"

        # Aplico el patrón a cada linea del archivo
        for n_linea, linea in enumerate(contenido):
            match = re.findall(patron, linea)
            if match:
                self.total_faltas += 1
                self.faltas.append({
                    "archivo": nombre_archivo,
                    "linea": n_linea + 1,
                    "detalle": (
                        "La linea tiene una clase que no parte con mayúscula"
                    )
                })
