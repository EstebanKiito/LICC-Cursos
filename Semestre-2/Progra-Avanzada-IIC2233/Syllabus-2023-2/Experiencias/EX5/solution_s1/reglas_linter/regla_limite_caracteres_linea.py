from .regla_base import Regla


class ReglaLimiteCaracteresLinea(Regla):
    """
    Regla que revisa cuantos carácteres hay en una línea.
    Si sobrepasa un máximo definido al instancias la regla, lanza alerta.
    """

    def __init__(self, maximo_caracteres) -> None:
        super().__init__(
            nombre=(f"Líneas no pueden superar los {maximo_caracteres} carácteres"),
            nivel="linea",
        )
        self.maximo_caracteres = maximo_caracteres

    # Sobreescribir el método de la clase abstracta.
    def revisar_regla(self, nombre_archivo, contenido):
        # COMPLETAR
        indice = 1
        for linea in contenido:
            # Otra opción es usar enumerate
            if len(linea) > self.maximo_caracteres:
                self.total_faltas += 1
                self.faltas.append(
                    {
                        "archivo": nombre_archivo,
                        "linea": indice,
                        "detalle": f"Linea muy larga: {len(linea)}",
                    }
                )
            indice += 1
