import re
from .regla_base import Regla


class ReglaEspacioDespuesComa(Regla):
    """
        Regla que revisa cuando hay comas
        que no son seguidas inmediatamente por un espacio.
    """
    def __init__(self) -> None:
        super().__init__(
            nombre="Comas deben ser siempre seguidas por un espacio",
            nivel="linea"
        )

    # Sobreescribir el método de la clase abstracta.
    def revisar_regla(self, nombre_archivo, contenido):
        # Debemos generar un patrón con regex.
        # Reglas a seguir:
        # 1. Encontrar una coma.
        # 2. Luego, encontrar que el caracter que siga NO sea un espacio.
        # 3. (Difícil) Tratemos de excluir los strings

        #COMPLETAR
        pass
