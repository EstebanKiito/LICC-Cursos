from .regla_base import Regla


class ReglaLimiteCaracteresLinea(Regla):
    """
        Regla que revisa cuantos carácteres hay en una línea.
        Si sobrepasa un máximo definido al instancias la regla, lanza alerta.
    """
    def __init__(self, maximo_caracteres) -> None:
        super().__init__(
            nombre=(
                f"Líneas no pueden superar los {maximo_caracteres} carácteres"
            ),
            nivel="linea"
        )
        self.maximo_caracteres = maximo_caracteres

    # Sobreescribir el método de la clase abstracta.
    def revisar_regla(self, nombre_archivo, contenido):
        # Iteramos sobre las lineas del contenido
        for n_linea, linea in enumerate(contenido):
            # Si la ultima es un salto de línea, la ignoramos
            # (¿Por qué no usamos .strip()?)
            if linea[-1] == "\n":
                linea = linea[:-1]

            # Si el largo sobrepasa el máximo,
            # lo agregamos a la lista de alertas
            if len(linea) > self.maximo_caracteres:
                self.total_faltas += 1
                self.faltas.append({
                    "archivo": nombre_archivo,
                    "linea": n_linea + 1,
                    "detalle": f"Linea tiene {len(linea)} carácteres"
                })
