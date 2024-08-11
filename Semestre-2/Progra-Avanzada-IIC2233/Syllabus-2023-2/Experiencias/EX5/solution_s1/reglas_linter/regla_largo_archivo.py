from .regla_base import Regla


class ReglaLargoArchivo(Regla):
    """
    Regla que revisa cuantas líneas hay en el archivo
    y si sobrepasa un máximo definido, lanza alerta.
    Si la última es un salto de línea, debemos sumar una al total.
    """

    def __init__(self, maximo_lineas) -> None:
        super().__init__(
            nombre=f"Archivos no pueden superar las {maximo_lineas} líneas",
            nivel="archivo",
        )
        self.maximo_lineas = maximo_lineas

    # Sobreescribir el método de la clase abstracta.
    def revisar_regla(self, nombre_archivo, contenido):
        cantidad_lineas = len(contenido)
        # Si la ultima linea tiene un salto de linea
        # Sumamos uno, ya que el cursor estará una línea bajo esa
        extra_cursor = int(contenido[-1][-1] == "\n")
        lineas_totales = cantidad_lineas + extra_cursor

        # Si hay más líneas que el máximo, lanzo una sola alerta para
        # todo el archivo
        if lineas_totales > self.maximo_lineas:
            self.total_faltas += 1
            self.faltas.append(
                {
                    "archivo": nombre_archivo,
                    "detalle": f"Archivo tiene {lineas_totales} líneas",
                }
            )
